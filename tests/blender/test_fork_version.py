import shutil
import sys
import traceback
from pathlib import Path

import bpy

# Add project root to sys.path
ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT))

import savepoints  # noqa: E402
from savepoints.services.storage import get_parent_path_from_snapshot, load_manifest, get_history_dir


def setup_test_env():
    # Create a temporary directory for testing
    test_dir = ROOT / "test_fork_run"
    if test_dir.exists():
        shutil.rmtree(test_dir)
    test_dir.mkdir()
    return test_dir


def cleanup_test_env(test_dir):
    if test_dir.exists():
        shutil.rmtree(test_dir)


def main() -> None:
    print("Starting Fork Feature Test...")
    test_dir = setup_test_env()

    # Paths
    original_blend_path = test_dir / "original_project.blend"
    forked_blend_path = test_dir / "original_project_v001.blend"

    try:
        # 1. Setup Initial Project
        print(f"Saving initial project to {original_blend_path}")
        bpy.ops.wm.save_as_mainfile(filepath=str(original_blend_path))

        print("Registering savepoints addon...")
        savepoints.register()

        # 2. Create a Version (Commit)
        print("Creating v001...")
        # Add an object to verify content later
        bpy.ops.mesh.primitive_cube_add()
        bpy.context.object.name = "OriginalCube"

        res = bpy.ops.savepoints.commit('EXEC_DEFAULT', note="Base Version")
        if "FINISHED" not in res:
            raise RuntimeError(f"Commit failed: {res}")

        # 3. Checkout (Enter Snapshot Mode)
        print("Checking out v001...")
        bpy.context.scene.savepoints_settings.active_version_index = 0
        res = bpy.ops.savepoints.checkout()
        if "FINISHED" not in res:
            raise RuntimeError(f"Checkout failed: {res}")

        # Verify we are in snapshot mode
        current_path = Path(bpy.data.filepath)
        if current_path.name != "snapshot.blend_snapshot":
            raise RuntimeError(f"Not in snapshot mode: {current_path}")

        # 4. Execute Fork
        print(f"Forking to {forked_blend_path}...")

        # No arguments needed, it should auto-detect everything
        res = bpy.ops.savepoints.fork_version('EXEC_DEFAULT')

        if "FINISHED" not in res:
            raise RuntimeError(f"Fork failed: {res}")

        # 5. Verification
        print("Verifying Fork results...")

        # A. File Existence
        if not forked_blend_path.exists():
            raise RuntimeError("Forked file was not created on disk")

        # B. Context Switch
        # bpy.ops.wm.open_mainfile should have switched the current file
        current_loaded_path = Path(bpy.data.filepath)
        if current_loaded_path != forked_blend_path:
            raise RuntimeError(f"Blender did not switch to forked file. Current: {current_loaded_path}")

        # C. Content Verification
        if "OriginalCube" not in bpy.data.objects:
            raise RuntimeError("Forked file missing objects from snapshot")

        # D. Fresh History Verification
        # The new file will have a history folder created (by the fork operator).
        # But it should be EMPTY (no versions from the original project)
        history_dir = get_history_dir()
        if not history_dir or not Path(history_dir).exists():
            # If it doesn't exist yet, that's fine too, but usually it's created on load.
            pass
        else:
            # If it exists, check manifest
            manifest = load_manifest()
            versions = manifest.get("versions", [])
            if len(versions) > 0:
                raise RuntimeError(
                    f"Forked project history should be empty, but has {len(versions)} versions: {versions}")

            # Also verify parent_file in manifest matches current file
            manifest_parent = manifest.get("parent_file")
            # Normalize paths for comparison
            if Path(manifest_parent).resolve() != forked_blend_path.resolve():
                raise RuntimeError(
                    f"New manifest parent_file mismatch. Expected {forked_blend_path}, got {manifest_parent}")

        # E. Verify we are NOT in snapshot mode anymore
        parent_path = get_parent_path_from_snapshot(bpy.data.filepath)
        if parent_path:
            raise RuntimeError("Forked project should be a normal file, not in snapshot mode")

        print("Fork Test Passed!")

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
