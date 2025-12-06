import shutil
import sys
import traceback
from pathlib import Path

import bpy

# Add project root to sys.path
ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT))

import savepoints  # noqa: E402


def setup_test_env():
    # Create a temporary directory for testing
    test_dir = ROOT / "test_e2e_run"
    if test_dir.exists():
        shutil.rmtree(test_dir)
    test_dir.mkdir()

    return test_dir


def cleanup_test_env(test_dir):
    if test_dir.exists():
        shutil.rmtree(test_dir)


def main() -> None:
    print("Starting E2E Test...")
    test_dir = setup_test_env()
    blend_file_path = test_dir / "test_project.blend"

    try:
        # 1. Save initial project file
        print(f"Saving initial project to {blend_file_path}")
        bpy.ops.wm.save_as_mainfile(filepath=str(blend_file_path))

        # 2. Register Addon
        print("Registering savepoints addon...")
        savepoints.register()

        # Disable autosave to prevent interference during tests
        bpy.context.scene.savepoints_settings.use_auto_save = False

        # 3. Test Commit
        print("Testing Commit...")
        # Create some data to verify later
        bpy.ops.mesh.primitive_cube_add()
        bpy.context.object.name = "TestCube_v1"

        # [Test] Relative Path Setup
        external_file = test_dir / "external.txt"
        external_file.write_text("dummy content")
        txt_block = bpy.data.texts.load(str(external_file), internal=False)
        txt_block.filepath = "//external.txt"  # Force relative
        print(f"Setup text block with path: {txt_block.filepath}")

        # [Test] Verify Fail Fast on Relative Paths (Background Mode)
        if bpy.app.background:
            print("Testing Fail Fast on Relative Paths...")
            try:
                # This should fail now because of relative paths
                bpy.ops.savepoints.commit('EXEC_DEFAULT', note="Should Fail")
                raise RuntimeError("Commit succeeded with relative paths in background mode (Should have failed)")
            except RuntimeError as e:
                print(f"Commit blocked as expected: {e}")
                # Verify the error message contains relevant info (optional but good)
                if "Relative paths detected" not in str(e):
                    print(f"Warning: Unexpected error message: {e}")

            # Flush streams to ensure log ordering
            sys.stdout.flush()
            sys.stderr.flush()

            # Apply Workaround: Make Absolute
            print("Applying workaround: Make Paths Absolute")
            bpy.ops.file.make_paths_absolute()

            # Verify it is absolute now
            if txt_block.filepath.startswith("//"):
                # Fallback if make_paths_absolute didn't work (it relies on file being saved)
                # But we saved 'test_project.blend' at start, so it should work.
                raise RuntimeError(f"Make paths absolute failed: {txt_block.filepath}")

        # EXEC_DEFAULT to bypass invoke_props_dialog
        res = bpy.ops.savepoints.commit('EXEC_DEFAULT', note="First Version")
        if "FINISHED" not in res:
            raise RuntimeError(f"Commit failed with result: {res}")

        # Verify filesystem
        history_dir = test_dir / ".test_project_history"
        if not history_dir.exists():
            raise RuntimeError("History directory not created")

        manifest_path = history_dir / "manifest.json"
        if not manifest_path.exists():
            raise RuntimeError("Manifest not created")

        v001_dir = history_dir / "v001"
        if not v001_dir.exists():
            raise RuntimeError("Version v001 folder not created")

        snapshot_path = v001_dir / "snapshot.blend"
        if not snapshot_path.exists():
            raise RuntimeError("Snapshot file not created")

        # [Test] Verify Undo (Relative Paths preserved in current session)
        if not bpy.app.background:
            if bpy.data.texts["external.txt"].filepath != "//external.txt":
                raise RuntimeError(
                    f"Relative path broken in current session after commit: {bpy.data.texts['external.txt'].filepath}")
        else:
            # In background mode, we explicitly made paths absolute, so we expect absolute path
            if bpy.data.texts["external.txt"].filepath.startswith("//"):
                raise RuntimeError("Expected absolute path in background mode after workaround")

        print("Commit Verification: OK")

        # 4. Test Checkout
        print("Testing Checkout...")
        # Modify current scene so we know if we switched
        bpy.ops.mesh.primitive_uv_sphere_add()
        bpy.context.object.name = "TransientSphere"

        # Set active index to 0 (v001)
        bpy.context.scene.savepoints_settings.active_version_index = 0

        res = bpy.ops.savepoints.checkout()
        if "FINISHED" not in res:
            raise RuntimeError(f"Checkout failed with result: {res}")

        # Verify loaded file
        current_path = Path(bpy.data.filepath)
        if current_path.name != "snapshot.blend":
            raise RuntimeError(f"Checkout did not load snapshot.blend, current: {current_path}")

        # Verify content (should have TestCube_v1, but NOT TransientSphere)
        if "TestCube_v1" not in bpy.data.objects:
            raise RuntimeError("Snapshot does not contain TestCube_v1")
        if "TransientSphere" in bpy.data.objects:
            raise RuntimeError("Snapshot contains TransientSphere (should have been discarded)")

        # [Test] Verify Relative Path Fix in Snapshot
        # In interactive mode, Fix is applied (Undo based).
        # In background mode, we pre-applied absolute paths manually.
        # In both cases, the snapshot should have absolute paths OR correctly remapped relative paths.
        loaded_txt_path = bpy.data.texts["external.txt"].filepath
        print(f"Loaded text path in snapshot: {loaded_txt_path}")

        # Resolve the path relative to the current blend file (snapshot.blend)
        resolved_abs_path = Path(bpy.path.abspath(loaded_txt_path)).resolve()
        expected_abs_path = external_file.resolve()

        print(f"Resolved: {resolved_abs_path}")
        print(f"Expected: {expected_abs_path}")

        if resolved_abs_path != expected_abs_path:
            raise RuntimeError(
                f"Path in snapshot does not point to original file: {loaded_txt_path} (resolved: {resolved_abs_path}) vs {expected_abs_path}")

        # Verify Snapshot Mode
        from savepoints.core import get_parent_path_from_snapshot
        parent_path_detected = get_parent_path_from_snapshot(bpy.data.filepath)

        if not parent_path_detected:
            raise RuntimeError("Snapshot Mode not detected (get_parent_path_from_snapshot returned None)")

        if Path(parent_path_detected) != blend_file_path:
            raise RuntimeError(f"Parent path mismatch: {parent_path_detected} vs {blend_file_path}")

        # Verify Commit Guard (should fail in snapshot mode)
        print("Testing Commit Guard...")
        try:
            bpy.ops.savepoints.commit('EXEC_DEFAULT', note="Illegal Commit")
            raise RuntimeError("Commit should have failed in snapshot mode but succeeded")
        except RuntimeError:
            # Expected failure: poll() failed
            print("Commit blocked as expected.")
        except Exception as e:
            raise RuntimeError(f"Unexpected error during commit guard test: {e}")

        print("Checkout Verification: OK")

        # 5. Test Restore (Save as Parent)
        print("Testing Restore...")

        # Add something new in the snapshot to verify it gets saved to parent
        bpy.ops.mesh.primitive_cone_add()
        bpy.context.object.name = "RestoredCone"

        # EXEC_DEFAULT to bypass confirmation
        res = bpy.ops.savepoints.restore('EXEC_DEFAULT')
        if "FINISHED" not in res:
            raise RuntimeError(f"Restore failed with result: {res}")

        # Verify filepath is back to original
        current_path = Path(bpy.data.filepath)
        if current_path.name != "test_project.blend":
            raise RuntimeError(f"Restore did not switch back to original file, current: {current_path}")

        # Verify content
        if "RestoredCone" not in bpy.data.objects:
            raise RuntimeError("Restored file does not contain the new object added in snapshot")

        # Verify Backup
        backups = list(history_dir.glob("test_project.blend.*.bak"))
        if not backups:
            raise RuntimeError("Backup file was not created in history folder")

        print("Restore Verification: OK")

        # 6. Test Multiple Versions
        print("Testing Multiple Versions...")
        # Create v002
        bpy.ops.mesh.primitive_monkey_add()
        bpy.context.object.name = "Monkey_v2"
        res = bpy.ops.savepoints.commit('EXEC_DEFAULT', note="Second Version")
        if "FINISHED" not in res:
            raise RuntimeError("Failed to commit v002")

        # Verify existence
        v002_dir = history_dir / "v002"
        if not v002_dir.exists():
            raise RuntimeError("v002 folder not created")

        # 7. Test Deletion
        print("Testing Deletion...")
        # Force refresh to ensure UI list is up-to-date
        bpy.ops.savepoints.refresh()

        versions = bpy.context.scene.savepoints_settings.versions
        print(f"Versions before delete: {[v.version_id for v in versions]}")

        if len(versions) != 2:
            raise RuntimeError(f"Expected 2 versions, found {len(versions)}")

        # Find index of v001
        v001_index = -1
        for i, v in enumerate(versions):
            if v.version_id == "v001":
                v001_index = i
                break

        if v001_index == -1:
            raise RuntimeError("v001 not found in versions list")

        # Delete v001
        bpy.context.scene.savepoints_settings.active_version_index = v001_index
        res = bpy.ops.savepoints.delete()
        if "FINISHED" not in res:
            raise RuntimeError("Delete failed")

        # Verify v001 gone
        if v001_dir.exists():
            raise RuntimeError("v001 directory still exists after deletion")

        # Verify manifest updated
        versions = bpy.context.scene.savepoints_settings.versions
        print(f"Versions after delete: {[v.version_id for v in versions]}")

        if len(versions) != 1:
            raise RuntimeError(f"Expected 1 version, found {len(versions)}")

        if versions[0].version_id != "v002":
            raise RuntimeError(f"Expected remaining version to be v002, found {versions[0].version_id}")

        # 8. Test Checkout of remaining version
        print("Testing Checkout of remaining version...")
        bpy.context.scene.savepoints_settings.active_version_index = 0  # v002 is now at index 0
        res = bpy.ops.savepoints.checkout()
        if "FINISHED" not in res:
            raise RuntimeError("Checkout of v002 failed")

        if "Monkey_v2" not in bpy.data.objects:
            raise RuntimeError("Monkey_v2 not found in v002 snapshot")

        print("Multiple Versions & Deletion Verification: OK")

        print("ALL TESTS PASSED")

    except Exception:
        traceback.print_exc()
        sys.exit(1)
    finally:
        print("Cleaning up...")
        # Unregister might fail if register failed half-way, but try anyway
        try:
            savepoints.unregister()
        except Exception:
            pass
        cleanup_test_env(test_dir)


if __name__ == "__main__":
    main()
