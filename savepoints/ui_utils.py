# SPDX-License-Identifier: GPL-3.0-or-later

import os
from typing import Any

import bpy
import bpy.utils.previews

from . import core

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
    data = core.load_manifest(create_if_missing=False)
    settings = context.scene.savepoints_settings
    settings.versions.clear()

    # Update Previews
    pcoll = preview_collections.get("main")
    if pcoll is not None:
        pcoll.clear()

    history_dir = core.get_history_dir()

    versions = data.get("versions", [])
    # Sort: Normal versions first (by ID), autosave last
    versions.sort(key=lambda v: (1 if v.get("id") == "autosave" else 0, v.get("id", "")))

    for v_data in versions:
        item = settings.versions.add()
        item.version_id = v_data.get("id", "")
        item.timestamp = v_data.get("timestamp", "")
        item.note = v_data.get("note", "")
        item.thumbnail_rel_path = core.from_posix_path(v_data.get("thumbnail", ""))
        item.blend_rel_path = core.from_posix_path(v_data.get("blend", ""))
        item.object_count = v_data.get("object_count", 0)
        item.is_protected = v_data.get("is_protected", False)
        item.tag = v_data.get("tag", "NONE")

        fsize = v_data.get("file_size", 0)
        item.file_size_display = core.format_file_size(fsize)

        _load_item_preview(pcoll, history_dir, item)

    # If we have versions and no active index, set to 0
    if len(settings.versions) > 0 and settings.active_version_index < 0:
        settings.active_version_index = 0


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
