# SPDX-License-Identifier: GPL-3.0-or-later

import json
from functools import lru_cache
from pathlib import Path

import bpy

from .storage import get_history_dir, ensure_directory

OBJECT_DATA_SUFFIX = "_objects.json"


def _round_float(val):
    return round(float(val), 4)


def _matrix_to_list(matrix):
    # Flatten 4x4 matrix, keep as floats
    return [_round_float(x) for row in matrix for x in row]


def _bbox_to_min_max(bbox):
    # bbox is a list of 8 Vector(3) corners usually.
    # Calculate min and max for each axis to get AABB (2 points, 6 floats)
    xs = [p[0] for p in bbox]
    ys = [p[1] for p in bbox]
    zs = [p[2] for p in bbox]

    # Store as [[min_x, min_y, min_z], [max_x, max_y, max_z]]
    min_pt = [_round_float(min(xs)), _round_float(min(ys)), _round_float(min(zs))]
    max_pt = [_round_float(max(xs)), _round_float(max(ys)), _round_float(max(zs))]
    return [min_pt, max_pt]


def extract_object_data(obj):
    data = {}

    # World Matrix
    data['matrix'] = _matrix_to_list(obj.matrix_world)

    # Bounding Box (Local coordinates -> Reduced to Min/Max)
    if obj.bound_box and len(obj.bound_box) >= 8:
        data['bbox'] = _bbox_to_min_max(obj.bound_box)
    else:
        data['bbox'] = [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]

    # v_count (Mesh only)
    if obj.type == 'MESH' and obj.data:
        data['v_count'] = len(obj.data.vertices)
    else:
        data['v_count'] = 0

    return data


def save_object_data(version_id, objects):
    """
    Saves metadata for the given objects to {version_id}_objects.json inside the version folder.
    """
    history_dir_str = get_history_dir()
    if not history_dir_str:
        return

    if bpy.context.view_layer:
        bpy.context.view_layer.update()
    history_dir = Path(history_dir_str)
    version_dir = history_dir / version_id
    # Ensure directory exists (it should be created by snapshot process, but safety first)
    ensure_directory(version_dir)

    output_path = version_dir / f"{version_id}{OBJECT_DATA_SUFFIX}"

    data_map = {}
    for obj in objects:
        try:
            data_map[obj.name] = extract_object_data(obj)
        except Exception as e:
            print(f"[SavePoints] Error extracting data for {obj.name}: {e}")
            continue

    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            # Use compact separators to save space
            json.dump(data_map, f, separators=(',', ':'))
    except Exception as e:
        print(f"[SavePoints] Failed to save object data: {e}")


@lru_cache(maxsize=128)
def load_object_data(version_id):
    """
    Loads metadata from {version_id}_objects.json.
    Returns a dict: { "ObjectName": {data} }
    """
    history_dir_str = get_history_dir()
    if not history_dir_str:
        return {}

    history_dir = Path(history_dir_str)
    file_path = history_dir / version_id / f"{version_id}{OBJECT_DATA_SUFFIX}"

    if not file_path.exists():
        return {}

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return {}
