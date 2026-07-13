# SPDX-License-Identifier: GPL-3.0-or-later
# pyright: reportOptionalMemberAccess=false

import bpy
from pathlib import Path

from .i18n import TranslatedOperatorMixin, iface, report as rpt
from .properties import draw_property_with_help
from .translations import TRANSLATION_CONTEXT
from .services.asset_path import unmap_snapshot_paths
from .services.backup import create_backup, HistoryDirectoryUnavailableError
from .services.fork import make_all_local_and_clear_assets
from .services.manifest import initialize_history_for_path
from .services.storage import (
    get_parent_path_from_snapshot,
    get_fork_target_path,
    SNAPSHOT_EXT,
)
from .ui_utils import force_redraw_areas


class SAVEPOINTS_OT_restore(TranslatedOperatorMixin, bpy.types.Operator):
    """Restore this snapshot to the parent file, overwriting it."""

    bl_idname = "savepoints.restore"
    bl_label = "Save as Parent"
    bl_options = {"REGISTER", "UNDO"}
    translation_description = (
        "Replace the parent file with this snapshot after creating a backup"
    )

    def invoke(self, context, event):
        return context.window_manager.invoke_confirm(self, event)

    def execute(self, context):
        original_path_str = get_parent_path_from_snapshot(bpy.data.filepath)

        if not original_path_str:
            self.report(
                {"ERROR"},
                rpt("Could not determine parent file path. Are you in a snapshot?"),
            )
            return {"CANCELLED"}

        original_path = Path(original_path_str)

        if original_path.exists():
            try:
                backup_path = create_backup(original_path)
                self.report(
                    {"INFO"},
                    rpt("Backup created: {name}").format(name=backup_path.name),
                )
            except HistoryDirectoryUnavailableError:
                self.report(
                    {"WARNING"},
                    rpt("Could not create backup: history directory unavailable."),
                )
            except Exception as e:
                self.report({"ERROR"}, rpt("Backup failed: {error}").format(error=e))
                return {"CANCELLED"}
        else:
            self.report({"WARNING"}, rpt("Original file not found. Creating new one."))

        try:
            bpy.ops.wm.save_as_mainfile(filepath=str(original_path))
            self.report({"INFO"}, rpt("Restored to parent file successfully."))
        except Exception as e:
            self.report({"ERROR"}, rpt("Failed to save: {error}").format(error=e))
            return {"CANCELLED"}

        # Force redraw to remove HUD
        force_redraw_areas(context)

        return {"FINISHED"}


class SAVEPOINTS_OT_open_parent(TranslatedOperatorMixin, bpy.types.Operator):
    """Return to the parent file without saving current snapshot as parent."""

    bl_idname = "savepoints.open_parent"
    bl_label = "Return to Parent"
    bl_options = {"REGISTER", "UNDO"}
    translation_description = "Return to the parent file without applying this snapshot"

    def execute(self, _context):
        parent_path_str = get_parent_path_from_snapshot(bpy.data.filepath)

        if not parent_path_str:
            self.report(
                {"ERROR"},
                rpt("Could not determine parent file path. Are you in a snapshot?"),
            )
            return {"CANCELLED"}

        parent_path = Path(parent_path_str)

        if not parent_path.exists():
            self.report(
                {"ERROR"},
                rpt("Parent file not found: {path}").format(path=parent_path),
            )
            return {"CANCELLED"}

        # Note: In UI, this might prompt to save changes if modified.
        bpy.ops.wm.open_mainfile(filepath=str(parent_path))
        return {"FINISHED"}


class SAVEPOINTS_OT_fork_version(TranslatedOperatorMixin, bpy.types.Operator):
    """Save the current snapshot as a new project file"""

    bl_idname = "savepoints.fork_version"
    bl_label = "Fork (Save as New)"
    bl_options = {"REGISTER", "UNDO"}
    translation_description = "Save this snapshot as a new independent project"

    unbind_linked_assets: bpy.props.BoolProperty(
        name="Detach from Library (Make Local & Clear Assets)",
        description="",
        default=False,
        translation_context=TRANSLATION_CONTEXT,
    )

    def invoke(self, context, _event):
        return context.window_manager.invoke_props_dialog(self)

    def draw(self, _context):
        layout = self.layout
        draw_property_with_help(
            layout,
            self,
            "unbind_linked_assets",
            text=iface("Detach from Library (Make Local & Clear Assets)"),
            message="Converts linked data to local and clears asset tags to prevent Asset Browser duplication. Creates a fully independent file (may increase file size).",
        )

    def execute(self, context):
        if not bpy.data.filepath:
            return {"CANCELLED"}

        source_path = Path(bpy.data.filepath)

        # Determine the target path
        try:
            target_path = get_fork_target_path(source_path)
        except Exception as e:
            self.report(
                {"ERROR"}, rpt("Could not determine paths: {error}").format(error=e)
            )
            return {"CANCELLED"}

        if source_path == target_path:
            self.report({"ERROR"}, rpt("Source and target paths are identical."))
            return {"CANCELLED"}

        # Ensure history directory is created for the new file
        try:
            initialize_history_for_path(target_path)
        except Exception as e:
            self.report(
                {"WARNING"}, rpt("History creation failed: {error}").format(error=e)
            )

        try:
            bpy.ops.wm.save_as_mainfile(filepath=str(target_path))

            needs_save = False

            if self.unbind_linked_assets:
                changed, cleared_count = make_all_local_and_clear_assets()
                if changed:
                    self.report(
                        {"INFO"},
                        rpt(
                            "Forked: Detached from library (Cleared {count} asset marks)."
                        ).format(count=cleared_count),
                    )
                    needs_save = True
                else:
                    self.report(
                        {"INFO"}, rpt("Forked: No linked assets required unbinding.")
                    )

            if unmap_snapshot_paths():
                self.report({"INFO"}, rpt("Fixed relative paths for forked project."))
                needs_save = True

            if needs_save:
                bpy.ops.wm.save_mainfile()

        except Exception as e:
            self.report({"ERROR"}, rpt("Failed to fork file: {error}").format(error=e))
            return {"CANCELLED"}

        self.report({"INFO"}, rpt("Forked to {name}").format(name=target_path.name))

        # Force redraw to remove HUD
        force_redraw_areas(context)

        return {"FINISHED"}


class SAVEPOINTS_OT_guard_save(TranslatedOperatorMixin, bpy.types.Operator):
    """Intercept Ctrl+S to prevent saving over snapshots."""

    bl_idname = "savepoints.guard_save"
    bl_label = "Guard Save"
    bl_options = {"INTERNAL"}
    translation_description = (
        "Prevent accidental overwriting while reviewing a snapshot"
    )

    def execute(self, context):
        filepath = bpy.data.filepath
        if filepath and filepath.lower().endswith(SNAPSHOT_EXT):
            msg = rpt("Snapshot Mode (Review Mode): Please use Fork or Save as Parent.")
            self.report({"WARNING"}, msg)

            if not bpy.app.background:

                def draw_popup(self_, _context):
                    layout = self_.layout
                    layout.label(text=iface("Snapshot Mode (Review Mode)"))
                    layout.label(text=iface("Please use 'Fork' or 'Save as Parent'."))

                context.window_manager.popup_menu(
                    draw_popup, title=iface("Save Prevented"), icon="ERROR"
                )

            return {"CANCELLED"}

        try:
            return bpy.ops.wm.save_mainfile("INVOKE_DEFAULT")
        except RuntimeError:
            # Can happen if cancelled or other internal issues, usually safe to ignore in wrapper
            return {"CANCELLED"}
