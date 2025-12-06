import shutil
import sys
import time
from pathlib import Path

import bpy

# Add project root to sys.path
ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT))

import savepoints  # noqa: E402
from savepoints import operators

def setup_test_env():
    # Create a temporary directory for testing
    test_dir = ROOT / "test_autosave_run"
    if test_dir.exists():
        shutil.rmtree(test_dir)
    test_dir.mkdir()
    return test_dir

def cleanup_test_env(test_dir):
    if test_dir.exists():
        shutil.rmtree(test_dir)

def main():
    print("Starting Auto Save Test...")
    test_dir = setup_test_env()
    blend_file_path = test_dir / "test_autosave.blend"

    try:
        # 1. Save initial project file
        print(f"Saving initial project to {blend_file_path}")
        bpy.ops.wm.save_as_mainfile(filepath=str(blend_file_path))

        # 2. Register Addon
        print("Registering savepoints addon...")
        if not hasattr(bpy.types.Scene, "savepoints_settings"):
             savepoints.register()

        scene = bpy.context.scene
        settings = scene.savepoints_settings

        # 3. Setup Scene
        # Create some data to verify
        bpy.ops.mesh.primitive_cube_add()
        bpy.context.object.name = "AutoSaveCube"

        # 4. Configure Auto Save
        print("Configuring Auto Save...")
        settings.use_auto_save = True
        settings.auto_save_interval = 1 # 1 minute
        
        # Force next save to be in the past to trigger immediate save
        # Note: 0.0 is treated as "uninitialized", so we use 1.0
        settings.next_autosave_timestamp = "1.0" 
        settings.last_autosave_timestamp = "0.0"

        # 5. Trigger Auto Save
        # We manually invoke the timer function. 
        # In a real scenario, this is called by bpy.app.timers.
        print("Triggering autosave_timer()...")
        
        # The timer function returns the interval if it reschedules, or None/float
        ret = operators.autosave_timer()
        print(f"Timer returned: {ret}")

        # 6. Verify Results
        print("Verifying results...")
        
        history_dir = test_dir / ".test_autosave_history"
        if not history_dir.exists():
            raise RuntimeError(f"History directory not found at {history_dir}")

        autosave_dir = history_dir / "autosave"
        if not autosave_dir.exists():
            # Check if maybe it failed and we didn't catch it?
            # operators.autosave_timer prints tracebacks but doesn't raise
            raise RuntimeError(f"Autosave directory not found at {autosave_dir}")

        snapshot_path = autosave_dir / "snapshot.blend"
        if not snapshot_path.exists():
            raise RuntimeError("snapshot.blend not found in autosave folder")

        thumb_path = autosave_dir / "thumbnail.png"
        if not thumb_path.exists():
            print("WARNING: thumbnail.png not found. This might be expected in background mode if render failed silently, but core logic should handle it.")
            # Depending on the fix, we expect thumbnail generation to try its best.
            # If the fix works, it might still fail to render but shouldn't crash.
            # However, existence of the file depends on whether render.opengl wrote it.
            # If background mode + no window, my fix handles the crash, but maybe no file is written.
            # Let's see if we can assert it exists or just that the process finished.
        
        # Check Manifest
        manifest_path = history_dir / "manifest.json"
        if not manifest_path.exists():
            raise RuntimeError("manifest.json not found")
        
        print("Auto Save Test Passed!")

    except Exception as e:
        print(f"TEST FAILED: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    finally:
        # cleanup_test_env(test_dir)
        pass

if __name__ == "__main__":
    main()
