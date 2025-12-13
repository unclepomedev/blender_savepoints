import shutil
import sys
import os
import json
import traceback
from pathlib import Path

import bpy

# Add project root to sys.path
ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT))

import savepoints  # noqa: E402
from savepoints.core import get_parent_path_from_snapshot


def setup_test_env():
    # Create a temporary directory for testing
    test_dir = ROOT / "test_e2e_compat"
    if test_dir.exists():
        shutil.rmtree(test_dir)
    test_dir.mkdir()
    return test_dir


def cleanup_test_env(test_dir):
    if test_dir.exists():
        shutil.rmtree(test_dir)


def create_manual_history(test_dir, blend_file_path):
    """
    Manually create a history structure with mixed extensions.
    v001 -> snapshot.blend (Old format)
    v002 -> snapshot.blend_snapshot (New format)
    """
    history_dir = test_dir / ".compat_project_history"
    history_dir.mkdir()

    # Create v001 (Old format: .blend)
    v001_dir = history_dir / "v001"
    v001_dir.mkdir()
    shutil.copy2(blend_file_path, v001_dir / "snapshot.blend")

    # Create v002 (New format: .blend_snapshot)
    v002_dir = history_dir / "v002"
    v002_dir.mkdir()
    shutil.copy2(blend_file_path, v002_dir / "snapshot.blend_snapshot")

    # Create manifest.json
    manifest = {
        "parent_file": str(blend_file_path),
        "versions": [
            {
                "id": "v001",
                "note": "Old Format",
                "timestamp": "1234567890",
                "thumbnail": "v001/thumbnail.png",
                "blend": "v001/snapshot.blend",
                "object_count": 1,
                "file_size": 1024
            },
            {
                "id": "v002",
                "note": "New Format",
                "timestamp": "1234567891",
                "thumbnail": "v002/thumbnail.png",
                "blend": "v002/snapshot.blend_snapshot",
                "object_count": 1,
                "file_size": 1024
            }
        ]
    }

    with open(history_dir / "manifest.json", "w") as f:
        json.dump(manifest, f, indent=4)


def main() -> None:
    print("Starting Extension Compatibility Test...")
    test_dir = setup_test_env()
    blend_file_path = test_dir / "compat_project.blend"

    try:
        # 1. Save initial project file
        print(f"Saving initial project to {blend_file_path}")
        bpy.ops.wm.save_as_mainfile(filepath=str(blend_file_path))

        # 2. Register Addon
        print("Registering savepoints addon...")
        savepoints.register()

        # 3. Create Manual History (Mixed extensions)
        print("Creating manual history with mixed extensions...")
        create_manual_history(test_dir, blend_file_path)

        # Refresh to load manifest
        bpy.ops.savepoints.refresh()

        # Verify settings loaded
        settings = bpy.context.scene.savepoints_settings
        if len(settings.versions) != 2:
            raise RuntimeError(f"Expected 2 versions, found {len(settings.versions)}")

        # 4. Test Checkout Old Format (.blend)
        print("Testing Checkout v001 (.blend)...")
        settings.active_version_index = 0  # v001

        bpy.ops.savepoints.checkout()

        current_path = Path(bpy.data.filepath)
        print(f"Current path after checkout: {current_path}")

        if current_path.name != "snapshot.blend":
            raise RuntimeError(f"Failed to checkout old format. Expected snapshot.blend, got {current_path.name}")

        parent_path = get_parent_path_from_snapshot(bpy.data.filepath)
        if not parent_path:
            raise RuntimeError("Snapshot mode not detected for .blend file")
        if Path(parent_path) != blend_file_path:
            raise RuntimeError(f"Incorrect parent path detected: {parent_path}")

        print("v001 (.blend) Verification: OK")

        # 5. Return to Parent (to be clean, though checkout handles switching)
        print("Returning to parent...")
        bpy.ops.savepoints.open_parent()
        if Path(bpy.data.filepath) != blend_file_path:
            raise RuntimeError("Failed to return to parent file")

        # 6. Test Checkout New Format (.blend_snapshot)
        print("Testing Checkout v002 (.blend_snapshot)...")
        # Need to refresh or ensure index is correct. 
        # When opening parent, settings might be reset if not persistent, but here it's same session.
        # But wait, open_mainfile resets bpy.context.scene.
        # So we need to re-find the index.

        # Reloading parent file re-initializes the addon properties if registered?
        # Addon is registered globally. Scene properties are stored in file.
        # Since we just opened the parent file (which we saved at start), 
        # it doesn't have the history loaded in properties yet (unless we saved it after refresh).
        # But `savepoints` operators load manifest on demand or refresh.
        # We need to call refresh again after opening parent.

        bpy.ops.savepoints.refresh()
        settings = bpy.context.scene.savepoints_settings
        settings.active_version_index = 1  # v002

        bpy.ops.savepoints.checkout()

        current_path = Path(bpy.data.filepath)
        print(f"Current path after checkout: {current_path}")

        if current_path.name != "snapshot.blend_snapshot":
            raise RuntimeError(
                f"Failed to checkout new format. Expected snapshot.blend_snapshot, got {current_path.name}")

        parent_path = get_parent_path_from_snapshot(bpy.data.filepath)
        if not parent_path:
            raise RuntimeError("Snapshot mode not detected for .blend_snapshot file")

        print("v002 (.blend_snapshot) Verification: OK")

        print("ALL COMPATIBILITY TESTS PASSED")

    except Exception:
        traceback.print_exc()
        sys.exit(1)
    finally:
        print("Cleaning up...")
        try:
            savepoints.unregister()
        except Exception:
            pass
        cleanup_test_env(test_dir)


if __name__ == "__main__":
    main()
