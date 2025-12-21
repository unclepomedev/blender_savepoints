# SPDX-License-Identifier: GPL-3.0-or-later

import os
from typing import Any

import bpy
import bpy.utils.previews

from .services.manifest import load_manifest
from .services.storage import from_posix_path, format_file_size, get_history_dir
from .services.versioning import get_sorted_versions

preview_collections: dict = {}


def register_previews() -> None:
    """Register custom preview collections."""
    pcoll = bpy.utils.previews.new()
    preview_collections["main"] = pcoll


def unregister_previews() -> None:
    """Unregister custom preview collections."""
    for pcoll in preview_collections.values():
        bpy.utils.previews.remove(pcoll)
    preview_collections.clear()


def _load_item_preview(pcoll: bpy.utils.previews.ImagePreviewCollection, history_dir: str | None, item: Any) -> None:
    if pcoll is not None and history_dir and item.thumbnail_rel_path:
        full_path = os.path.join(history_dir, item.thumbnail_rel_path)
        if os.path.exists(full_path):
            try:
                pcoll.load(item.version_id, full_path, 'IMAGE')
            except Exception as e:
                print(f"Failed to load preview for {item.version_id}: {e}")


def sync_history_to_props(context: bpy.types.Context) -> None:
    """
    Read manifest and update the scene property group.
    
    Args:
        context: Blender context.
    """
    data = load_manifest(create_if_missing=False)
    settings = context.scene.savepoints_settings
    current_selected_id = None
    if len(settings.versions) > 0 and settings.active_version_index >= 0:
        try:
            current_selected_id = settings.versions[settings.active_version_index].version_id
        except IndexError:
            pass

    settings.versions.clear()

    # Update Previews
    pcoll = preview_collections.get("main")
    if pcoll is not None:
        pcoll.clear()

    history_dir = get_history_dir()
    sorted_versions = get_sorted_versions(data, newest_first=True, include_autosave=True)

    new_active_index = 0

    for i, v_data in enumerate(sorted_versions):
        item = settings.versions.add()
        item.version_id = v_data.get("id", "")
        item.timestamp = v_data.get("timestamp", "")
        item.note = v_data.get("note", "")
        item.thumbnail_rel_path = from_posix_path(v_data.get("thumbnail", ""))
        item.blend_rel_path = from_posix_path(v_data.get("blend", ""))
        item.object_count = v_data.get("object_count", 0)
        item.is_protected = v_data.get("is_protected", False)
        item.tag = v_data.get("tag", "NONE")

        fsize = v_data.get("file_size", 0)
        item.file_size_display = format_file_size(fsize)

        if current_selected_id and item.version_id == current_selected_id:
            new_active_index = i

        _load_item_preview(pcoll, history_dir, item)

    # If we have versions and no active index, set to 0
    if len(settings.versions) > 0:
        settings.active_version_index = new_active_index


def force_redraw_areas(context: bpy.types.Context, area_types: set[str] = None) -> None:
    """
    Force redraw of specific area types to update UI/HUD.
    
    Args:
        context: Blender context.
        area_types: Set of area types to redraw (e.g. {'VIEW_3D'}). Defaults to {'VIEW_3D'}.
    """
    if area_types is None:
        area_types = {'VIEW_3D'}

    if not hasattr(context, "window_manager"):
        return

    for window in context.window_manager.windows:
        for area in window.screen.areas:
            if area.type in area_types:
                area.tag_redraw()


def find_3d_view_override(context):
    for window in context.window_manager.windows:
        screen = window.screen
        for area in screen.areas:
            if area.type == 'VIEW_3D':
                for region in area.regions:
                    if region.type == 'WINDOW':
                        return {
                            "window": window,
                            "screen": screen,
                            "area": area,
                            "region": region,
                            "workspace": window.workspace,
                            "scene": window.scene,
                        }
    return None
