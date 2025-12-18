# SPDX-License-Identifier: GPL-3.0-or-later
import os
import shutil
from pathlib import Path

import bpy

from .asset_path import unmap_snapshot_paths
from .path_utils import get_safe_version_dir
from .snapshot import get_snapshot_file_path
from .storage import (
    RESCUE_TEMP_FILENAME, get_history_dir
)


def cleanup_rescue_temp_files() -> int:
    """
    Remove any lingering rescue temporary files from all version directories.

    Returns:
        int: The number of files removed.
    """
    history_dir_str = get_history_dir()
    if not history_dir_str:
        return 0

    history_dir = Path(history_dir_str)
    if not history_dir.exists():
        return 0

    count = 0
    # Iterate over all subdirectories (versions)
    for version_dir in history_dir.iterdir():
        if version_dir.is_dir():
            temp_file = version_dir / RESCUE_TEMP_FILENAME
            if temp_file.exists():
                try:
                    temp_file.unlink()
                    count += 1
                except Exception as e:
                    print(f"[SavePoints] Failed to remove temp file {temp_file}: {e}")

    if count > 0:
        print(f"[SavePoints] Cleaned up {count} rescue temporary file(s).")

    return count


def prepare_rescue_file(version_id: str) -> Path:
    version_dir = get_safe_version_dir(version_id, must_exist=True)
    snapshot_path = get_snapshot_file_path(version_dir)
    temp_blend_path = version_dir / RESCUE_TEMP_FILENAME

    try:
        shutil.copy2(str(snapshot_path), str(temp_blend_path))
        print(f"[SavePoints] Created temp file for rescue: {temp_blend_path}")
    except Exception as e:
        if temp_blend_path.exists():
            try:
                os.remove(temp_blend_path)
            except OSError:
                pass
        raise IOError(f"Failed to create temp file: {e}") from e

    return temp_blend_path


class RescuePostHandler:
    def __init__(self, temp_path: Path, initial_obj_count: int):
        self.temp_path = temp_path
        self.initial_obj_count = initial_obj_count

    def __call__(self, scene):
        try:
            current_obj_count = len(bpy.data.objects)
            paths_fixed = False

            try:
                paths_fixed = unmap_snapshot_paths()
            except Exception as e:
                print(f"[SavePoints] Error fixing paths after rescue: {e}")

            has_changes = (current_obj_count != self.initial_obj_count) or paths_fixed

            if has_changes:
                print("[SavePoints] Rescue successful: Changes detected.")
            else:
                pass

        except Exception as e:
            print(f"[SavePoints] Handler Error: {e}")
        finally:
            self._cleanup()

    def _cleanup(self):
        if self in bpy.app.handlers.depsgraph_update_post:
            bpy.app.handlers.depsgraph_update_post.remove(self)

        if self.temp_path.exists():
            try:
                os.remove(self.temp_path)
                print(f"[SavePoints] Removed temp file: {self.temp_path}")
            except Exception as e:
                print(f"[SavePoints] Error removing temp file: {e}")
