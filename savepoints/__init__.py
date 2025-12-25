# SPDX-License-Identifier: GPL-3.0-or-later
import sys
import time
import traceback

import bpy
from bpy.app.handlers import persistent

from . import hud
from . import operators
from . import operators_io
from . import properties
from . import ui
from . import ui_utils
from .services.asset_path import remap_snapshot_paths
from .services.autosave import autosave_timer

classes = (
    properties.SavePointsVersion,
    properties.SavePointsSettings,
    operators.SAVEPOINTS_OT_commit,
    operators.SAVEPOINTS_OT_link_history,
    operators.SAVEPOINTS_OT_edit_note,
    operators.SAVEPOINTS_OT_set_tag,
    operators.SAVEPOINTS_OT_rescue_assets,
    operators.SAVEPOINTS_OT_toggle_protection,
    operators.SAVEPOINTS_OT_toggle_ghost,
    operators.SAVEPOINTS_OT_checkout,
    operators.SAVEPOINTS_OT_restore,
    operators.SAVEPOINTS_OT_open_parent,
    operators.SAVEPOINTS_OT_fork_version,
    operators.SAVEPOINTS_OT_delete,
    operators.SAVEPOINTS_OT_refresh,
    operators.SAVEPOINTS_OT_guard_save,
    ui.SAVEPOINTS_MT_tag_menu,
    ui.SAVEPOINTS_UL_version_list,
    ui.SAVEPOINTS_PT_main,
)

addon_keymaps = []


@persistent
def load_handler(dummy):
    """Sync history when file is loaded."""
    max_retries = 10
    execution_state = {"retries": 0}

    def _delayed_sync_history():
        context = bpy.context
        if not context or not context.scene or (not bpy.app.background and not context.view_layer):
            execution_state["retries"] += 1

            if execution_state["retries"] > max_retries:
                print(f"[SavePoints] Warning: History sync timed out after {max_retries} retries.")
                return None

            return 0.05

        try:
            ui_utils.sync_history_to_props(context)

            if hasattr(context.scene, "savepoints_settings"):
                # Reset autosave timer on load so autosave doesn't trigger immediately after opening a file
                context.scene.savepoints_settings.last_autosave_timestamp = str(time.time())
        except Exception:
            print("[SavePoints] Error during delayed sync history on load.")
            traceback.print_exc()

        return None

    bpy.app.timers.register(_delayed_sync_history, first_interval=0.01)


@persistent
def auto_remap_paths_handler(dummy):
    """Handler to automatically remap paths when opening a snapshot."""
    try:
        remap_snapshot_paths(dummy)
    except Exception as e:
        print(f"[SavePoints] Error remapping paths: {e}")


def register():
    ui_utils.register_previews()
    hud.register()
    operators_io.register()
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.savepoints_settings = bpy.props.PointerProperty(type=properties.SavePointsSettings)
    bpy.app.handlers.load_post.append(load_handler)
    bpy.app.handlers.load_post.append(auto_remap_paths_handler)

    if not bpy.app.timers.is_registered(autosave_timer):
        bpy.app.timers.register(autosave_timer, first_interval=10.0, persistent=True)

    # Register Keymaps
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = kc.keymaps.new(name='Window', space_type='EMPTY')
        is_mac = (sys.platform == 'darwin')

        # ---------------------------------------------------------
        # 1. Standard: Ctrl+Alt+S (Mac: Cmd+Alt+S)
        # ---------------------------------------------------------
        kmi1 = km.keymap_items.new(
            "savepoints.commit", 'S', 'PRESS',
            ctrl=(not is_mac), oskey=is_mac, alt=True
        )
        kmi1.properties.force_quick = False
        addon_keymaps.append((km, kmi1))

        # ---------------------------------------------------------
        # 2. Forced Quick: Ctrl+Alt+Shift+S (Mac: Cmd+Alt+Shift+S)
        # ---------------------------------------------------------
        kmi2 = km.keymap_items.new(
            "savepoints.commit", 'S', 'PRESS',
            ctrl=(not is_mac), oskey=is_mac, alt=True, shift=True
        )
        kmi2.properties.force_quick = True
        addon_keymaps.append((km, kmi2))

        # ---------------------------------------------------------
        # 3. Guard Save: Ctrl+S (Mac: Cmd+S) -> Intercept standard save
        # ---------------------------------------------------------
        kmi_guard = km.keymap_items.new(
            "savepoints.guard_save", 'S', 'PRESS',
            ctrl=(not is_mac), oskey=is_mac
        )
        addon_keymaps.append((km, kmi_guard))


def unregister():
    # Unregister Keymaps
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()

    if bpy.app.timers.is_registered(autosave_timer):
        bpy.app.timers.unregister(autosave_timer)

    if load_handler in bpy.app.handlers.load_post:
        bpy.app.handlers.load_post.remove(load_handler)

    if auto_remap_paths_handler in bpy.app.handlers.load_post:
        bpy.app.handlers.load_post.remove(auto_remap_paths_handler)

    ui_utils.unregister_previews()
    hud.unregister()
    operators_io.unregister()
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

    del bpy.types.Scene.savepoints_settings


if __name__ == "__main__":
    register()
