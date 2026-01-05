# SPDX-License-Identifier: GPL-3.0-or-later

from .manifest import load_manifest
from .object_data import load_object_data
from .versioning import get_sorted_versions

CHANGE_TYPE_MAJOR = 'MAJOR'
CHANGE_TYPE_MINOR = 'MINOR'
CHANGE_TYPE_MOVED = 'MOVED'
CHANGE_TYPE_CREATED = 'CREATED'
CHANGE_TYPE_RECORD = 'RECORD'


def compare_object_history(obj, include_change_not_detected=False):
    """
    Compares object state efficiently by iterating form Oldest -> Newest (Single Pass).
    If include_unchanged is True, returns all versions where object exists.
    """
    manifest = load_manifest()
    if not manifest:
        return []

    sorted_versions = get_sorted_versions(manifest, newest_first=False)

    history = []
    prev_data = None

    for info in sorted_versions:
        vid = info['id']

        full_data = load_object_data(vid)

        if not full_data or obj.name not in full_data:
            prev_data = None
            continue

        curr_data = full_data[obj.name]

        details = ""
        change_type = CHANGE_TYPE_RECORD

        if prev_data is None:
            change_type = CHANGE_TYPE_CREATED
            details = "Created / First Record"
        else:
            cur_v = curr_data.get('v_count', 0)
            old_v = prev_data.get('v_count', 0)

            if cur_v != old_v:
                change_type = CHANGE_TYPE_MAJOR
                diff = cur_v - old_v
                sign = "+" if diff > 0 else ""
                details = f"{sign}{diff} verts"

            elif curr_data['bbox'] != prev_data['bbox']:
                change_type = CHANGE_TYPE_MINOR
                details = "Shape Modified"

            elif curr_data['matrix'] != prev_data['matrix']:
                change_type = CHANGE_TYPE_MOVED
                details = "Moved / Transformed"

        if change_type != CHANGE_TYPE_RECORD or include_change_not_detected:
            history.append({
                'version_id': vid,
                'change_type': change_type,
                'details': details,
                'note': info.get('note', ''),
                'timestamp': info.get('timestamp', 0)
            })

        prev_data = curr_data

    return list(reversed(history))
