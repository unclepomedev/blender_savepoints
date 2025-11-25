# SPDX-License-Identifier: GPL-3.0-or-later

import datetime
import json
import os
import shutil

import bpy
import bpy.utils.previews

preview_collections = {}


def register_previews():
    pcoll = bpy.utils.previews.new()
    preview_collections["main"] = pcoll


def unregister_previews():
    for pcoll in preview_collections.values():
        bpy.utils.previews.remove(pcoll)
    preview_collections.clear()


def get_project_path():
    return bpy.data.filepath


def get_history_dir():
    blend_path = get_project_path()
    if not blend_path:
        return None
    filename = os.path.basename(blend_path)
    name_without_ext = os.path.splitext(filename)[0]
    return os.path.join(os.path.dirname(blend_path), f".{name_without_ext}_history")


def get_manifest_path():
    history_dir = get_history_dir()
    if history_dir:
        return os.path.join(history_dir, "manifest.json")
    return None


def load_manifest():
    path = get_manifest_path()
    if path and os.path.exists(path):
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading manifest: {e}")
    return {"parent_file": get_project_path(), "versions": []}


def save_manifest(data):
    path = get_manifest_path()
    if path:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)


def format_file_size(size_in_bytes):
    try:
        size = float(size_in_bytes)
    except (ValueError, TypeError):
        return "0 B"

    for unit in ['B', 'KB', 'MB', 'GB']:
        if size < 1024.0:
            if unit == 'B':
                return f"{int(size)} {unit}"
            return f"{size:.1f} {unit}"
        size /= 1024.0
    return f"{size:.1f} TB"


def sync_history_to_props(context):
    """Read manifest and update the scene property group."""
    data = load_manifest()
    settings = context.scene.savepoints_settings
    settings.versions.clear()

    # Update Previews
    pcoll = preview_collections.get("main")
    if pcoll is not None:
        pcoll.clear()

    history_dir = get_history_dir()

    for v_data in data.get("versions", []):
        item = settings.versions.add()
        item.version_id = v_data.get("id", "")
        item.timestamp = v_data.get("timestamp", "")
        item.note = v_data.get("note", "")
        item.thumbnail_rel_path = v_data.get("thumbnail", "")
        item.blend_rel_path = v_data.get("blend", "")
        item.object_count = v_data.get("object_count", 0)
        
        fsize = v_data.get("file_size", 0)
        item.file_size_display = format_file_size(fsize)

        _load_item_preview(pcoll, history_dir, item)

    # If we have versions and no active index, set to 0
    if len(settings.versions) > 0 and settings.active_version_index < 0:
        settings.active_version_index = 0


def _load_item_preview(pcoll, history_dir, item):
    if pcoll is not None and history_dir and item.thumbnail_rel_path:
        full_path = os.path.join(history_dir, item.thumbnail_rel_path)
        if os.path.exists(full_path):
            try:
                pcoll.load(item.version_id, full_path, 'IMAGE')
            except Exception as e:
                print(f"Failed to load preview for {item.version_id}: {e}")


def get_next_version_id(versions):
    """Determine the next version ID string (e.g., v005)."""
    max_id = 0
    for v in versions:
        vid = v.get("id", "")
        num = _extract_version_number(vid)
        if num > max_id:
            max_id = num
    new_id_num = max_id + 1
    return f"v{new_id_num:03d}"


def _extract_version_number(vid):
    if vid.startswith("v"):
        try:
            return int(vid[1:])
        except:
            pass
    return -1


def capture_thumbnail(context, thumb_path):
    """Capture the current viewport as a thumbnail."""
    render = context.scene.render
    old_filepath = render.filepath

    try:
        render.filepath = thumb_path
        # OpenGL render of viewport
        if context.window_manager.windows:
            bpy.ops.render.opengl(write_still=True)
        else:
            pass
    except Exception as e:
        print(f"Thumbnail generation failed: {e}")
    finally:
        render.filepath = old_filepath


def add_version_to_manifest(manifest, version_id, note, thumb_rel, blend_rel, object_count=0, file_size=0):
    """Add a new version entry to the manifest and save it."""
    now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_version = {
        "id": version_id,
        "timestamp": now_str,
        "note": note,
        "thumbnail": thumb_rel,
        "blend": blend_rel,
        "object_count": object_count,
        "file_size": file_size
    }
    versions = manifest.get("versions", [])
    versions.append(new_version)
    manifest["versions"] = versions
    save_manifest(manifest)


def delete_version_by_id(version_id):
    manifest = load_manifest()
    versions = manifest.get("versions", [])

    target_v = None
    for v in versions:
        if v.get("id") == version_id:
            target_v = v
            break

    if target_v:
        history_dir = get_history_dir()
        if target_v.get('blend'):
            v_folder = os.path.dirname(os.path.join(history_dir, target_v['blend']))
            # Security check: ensure we are deleting inside history dir
            if history_dir and os.path.abspath(history_dir) in os.path.abspath(v_folder):
                shutil.rmtree(v_folder, ignore_errors=True)

        versions.remove(target_v)
        manifest["versions"] = versions
        save_manifest(manifest)
