import shutil
import sys
import traceback
import zipfile
from pathlib import Path

import bpy

# Add project root to sys.path
ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT))

import savepoints


def setup_test_env():
    test_dir = ROOT / "test_e2e_zip"
    if test_dir.exists():
        shutil.rmtree(test_dir)
    test_dir.mkdir()
    return test_dir


def cleanup_test_env(test_dir):
    if test_dir.exists():
        shutil.rmtree(test_dir)


def main():
    print("Starting Export Zip Test...")
    test_dir = setup_test_env()
    blend_file_path = test_dir / "test_project_zip.blend"

    try:
        # 1. Save initial project file
        print(f"Saving initial project to {blend_file_path}")
        bpy.ops.wm.save_as_mainfile(filepath=str(blend_file_path))

        # 2. Register Addon
        print("Registering savepoints addon...")
        savepoints.register()

        # 3. Create some history (Version 1)
        print("Creating history...")
        bpy.ops.mesh.primitive_cube_add()
        bpy.ops.savepoints.commit('EXEC_DEFAULT', note="V1")

        # 4. Create Version 2
        bpy.ops.mesh.primitive_uv_sphere_add()
        bpy.ops.savepoints.commit('EXEC_DEFAULT', note="V2")

        history_dir = test_dir / ".test_project_zip_history"
        if not history_dir.exists():
            raise RuntimeError("History dir setup failed")

        # 5. Export ZIP
        print("Testing Export Zip...")
        output_zip_path = test_dir / "export.zip"

        # Pass filepath explicitly for headless execution
        res = bpy.ops.savepoints.export_project_zip('EXEC_DEFAULT', filepath=str(output_zip_path))

        if "FINISHED" not in res:
            raise RuntimeError(f"Export zip failed with result: {res}")

        if not output_zip_path.exists():
            raise RuntimeError("Zip file was not created")

        # 6. Verify Zip Content
        print("Verifying Zip content...")
        with zipfile.ZipFile(output_zip_path, 'r') as zf:
            file_list = zf.namelist()
            print("Files in zip:", file_list)

            # Check main blend file
            if "test_project_zip.blend" not in file_list:
                raise RuntimeError("Main blend file missing in zip")

            # Check history structure
            # Should have .test_project_zip_history/manifest.json
            # Note: The operator uses arcname relative to project parent.
            # Project parent contains: test_project_zip.blend and .test_project_zip_history
            # So paths in zip should be: test_project_zip.blend, .test_project_zip_history/...

            expected_manifest = ".test_project_zip_history/manifest.json"
            if expected_manifest not in file_list:
                raise RuntimeError(f"Manifest missing in zip: {expected_manifest}")

            # Check versions
            # .test_project_zip_history/v001/snapshot.blend_snapshot
            if not any("v001/snapshot.blend_snapshot" in f for f in file_list):
                raise RuntimeError("Version 1 snapshot missing in zip")
            if not any("v002/snapshot.blend_snapshot" in f for f in file_list):
                raise RuntimeError("Version 2 snapshot missing in zip")

            # Check compression
            info = zf.getinfo("test_project_zip.blend")
            if info.compress_type != zipfile.ZIP_STORED:
                print(f"Warning: Compression type is {info.compress_type}, expected STORED (0)")
                raise RuntimeError(f"Compression is not ZIP_STORED. Got: {info.compress_type}")

        print("Export Zip Verification: OK")
        print("ALL TESTS PASSED")

    except Exception:
        traceback.print_exc()
        sys.exit(1)
    finally:
        try:
            savepoints.unregister()
        except:
            pass
        cleanup_test_env(test_dir)


if __name__ == "__main__":
    main()
