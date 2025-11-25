# SPDX-License-Identifier: GPL-3.0-or-later

import datetime
import json
import os

import bpy


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


def sync_history_to_props(context):
    """Read manifest and update the scene property group."""
    data = load_manifest()
    settings = context.scene.savepoints_settings
    settings.versions.clear()

    for v_data in data.get("versions", []):
        item = settings.versions.add()
        item.version_id = v_data.get("id", "")
        item.timestamp = v_data.get("timestamp", "")
        item.note = v_data.get("note", "")
        item.thumbnail_rel_path = v_data.get("thumbnail", "")
        item.blend_rel_path = v_data.get("blend", "")

    # If we have versions and no active index, set to 0
    if len(settings.versions) > 0 and settings.active_version_index < 0:
        settings.active_version_index = 0


def get_next_version_id(versions):
    """Determine the next version ID string (e.g., v005)."""
    max_id = 0
    for v in versions:
        vid = v.get("id", "")
        if vid.startswith("v"):
            try:
                num = int(vid[1:])
                if num > max_id:
                    max_id = num
            except:
                pass
    new_id_num = max_id + 1
    return f"v{new_id_num:03d}"


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


def add_version_to_manifest(manifest, version_id, note, thumb_rel, blend_rel):
    """Add a new version entry to the manifest and save it."""
    now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_version = {
        "id": version_id,
        "timestamp": now_str,
        "note": note,
        "thumbnail": thumb_rel,
        "blend": blend_rel
    }
    versions = manifest.get("versions", [])
    versions.append(new_version)
    manifest["versions"] = versions
    save_manifest(manifest)
