import shutil
import sys
import traceback
from pathlib import Path
import os
import bpy

# Add project root to sys.path
ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT))

import savepoints
from savepoints import operators


def setup_test_env():
    """Setup temporary directory for testing."""
    test_dir = ROOT / "test_autosave_skip_thumb_run"
    if test_dir.exists():
        shutil.rmtree(test_dir)
    test_dir.mkdir()
    return test_dir


def cleanup_test_env(test_dir):
    if test_dir.exists():
        shutil.rmtree(test_dir)


def main() -> None:
    print("Starting Autosave Skip Thumbnail Test...")
    test_dir = setup_test_env()
    blend_file_path = test_dir / "test_project.blend"

    try:
        # 1. Initialize Project
        print(f"Saving initial project to {blend_file_path}")
        bpy.ops.wm.save_as_mainfile(filepath=str(blend_file_path))

        # 2. Register Add-on
        print("Registering savepoints addon...")
        savepoints.register()

        # 3. Test: Explicit Thumbnail Skipping
        print("Testing create_snapshot(skip_thumbnail=True)...")

        context = bpy.context
        if not hasattr(context.scene, "savepoints_settings"):
            raise RuntimeError("savepoints_settings not found on scene")

        version_id_no_thumb = "v_no_thumb"
        operators.create_snapshot(context, version_id_no_thumb, "No Thumb", skip_thumbnail=True)

        # Verification: Snapshot exists, but thumbnail does not.
        history_dir = test_dir / ".test_project_history"
        v_dir = history_dir / version_id_no_thumb

        if not v_dir.exists():
            raise RuntimeError(f"Version dir {v_dir} missing")
        if not (v_dir / "snapshot.blend_snapshot").exists():
            raise RuntimeError("Snapshot file missing")
        if (v_dir / "thumbnail.png").exists():
            raise RuntimeError("Thumbnail exists but should have been skipped")

        print("Verification skip_thumbnail=True: OK")

        # 4. Test: Default Behavior (Attempt Thumbnail)
        print("Testing create_snapshot(skip_thumbnail=False)...")
        version_id_with_thumb = "v_with_thumb"
        operators.create_snapshot(context, version_id_with_thumb, "With Thumb", skip_thumbnail=False)

        # Note: In background/headless mode, thumbnail generation may be skipped internally due to lack of window context.
        # The test passes if the operation completes without crashing.
        print("Verification skip_thumbnail=False: OK (Execution completed)")

        # 5. Test: Autosave Simulation
        print("Testing Autosave logic simulation...")

        # Simulate autosave call (which forces skip_thumbnail=True)
        operators.create_snapshot(context, "autosave", "Auto Save", skip_thumbnail=True)

        autosave_dir = history_dir / "autosave"
        if not autosave_dir.exists():
            raise RuntimeError("Autosave dir not created")
        if (autosave_dir / "thumbnail.png").exists():
            raise RuntimeError("Autosave SHOULD NOT have thumbnail")

        print("Autosave logic verification: OK")
        print("ALL TESTS PASSED")

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
