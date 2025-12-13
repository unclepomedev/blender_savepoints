import shutil
import sys
import time
import traceback
from pathlib import Path

import bpy

# Add project root to sys.path
ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT))

import savepoints  # noqa: E402
from savepoints.core import load_manifest


def setup_test_env():
    # Create a temporary directory for testing
    test_dir = ROOT / "test_render_autosave_run"
    if test_dir.exists():
        shutil.rmtree(test_dir)
    test_dir.mkdir()
    return test_dir


def cleanup_test_env(test_dir):
    if test_dir.exists():
        shutil.rmtree(test_dir)


def main() -> None:
    print("Starting Render Autosave Test...")
    test_dir = setup_test_env()
    blend_file_path = test_dir / "test_project.blend"

    try:
        # 1. Setup Project
        print(f"Saving initial project to {blend_file_path}")
        bpy.ops.wm.save_as_mainfile(filepath=str(blend_file_path))

        print("Registering savepoints addon...")
        savepoints.register()

        # Enable Autosave and set interval
        settings = bpy.context.scene.savepoints_settings
        settings.use_auto_save = True
        settings.auto_save_interval = 1  # 1 min

        # Helper to force autosave condition
        def make_autosave_due():
            # Set timestamp to 2 minutes ago
            settings.last_autosave_timestamp = str(time.time() - 120)

        # 2. Test: Autosave blocked during render
        print("Test 1: Autosave blocked during render")

        # Trigger render init
        print(" Simonulating Render Init...")
        savepoints.operators.render_init_handler(bpy.context.scene)

        # Verify global flag (optional, but good for debug)
        if not savepoints.operators._is_rendering:
            raise RuntimeError("_is_rendering flag not set after render_init_handler")

        # Force due
        make_autosave_due()

        # Run timer manually
        savepoints.operators.autosave_timer()

        # Verify NO autosave happened
        # Check manifest for "autosave" id
        manifest = load_manifest()
        versions = manifest.get("versions", [])
        autosaves = [v for v in versions if v["id"] == "autosave"]

        if autosaves:
            raise RuntimeError("Autosave occurred during rendering! (Should be blocked)")

        print(" -> Passed: No autosave during render.")

        # 3. Test: Autosave works after render complete
        print("Test 2: Autosave works after render complete")

        # Trigger render complete
        print(" Simulating Render Complete...")
        savepoints.operators.render_complete_handler(bpy.context.scene)

        if savepoints.operators._is_rendering:
            raise RuntimeError("_is_rendering flag still set after render_complete_handler")

        # Run timer manually (still due because previous one was skipped)
        # Note: autosave_timer logic: if blocked, it returns but doesn't update timestamp.
        # So it should still be due. But let's be sure.
        make_autosave_due()

        savepoints.operators.autosave_timer()

        # Verify autosave happened
        manifest = load_manifest()
        versions = manifest.get("versions", [])
        autosaves = [v for v in versions if v["id"] == "autosave"]

        if not autosaves:
            raise RuntimeError("Autosave did NOT occur after rendering finished!")

        print(" -> Passed: Autosave occurred after render.")

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
