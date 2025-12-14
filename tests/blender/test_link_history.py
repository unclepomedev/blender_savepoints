import json
import shutil
import sys
import traceback
from pathlib import Path

import bpy

# Add project root to sys.path
ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT))

import savepoints


def setup_test_env():
    test_dir = ROOT / "test_link_history_env"
    if test_dir.exists():
        shutil.rmtree(test_dir)
    test_dir.mkdir()
    return test_dir


def main():
    print("Starting Link History Test...")
    test_dir = setup_test_env()

    try:
        # 1. Save main project
        project_path = test_dir / "my_project.blend"
        print(f"Saving project to {project_path}")
        bpy.ops.wm.save_as_mainfile(filepath=str(project_path))

        # 2. Register addon
        savepoints.register()

        # 3. Create an orphaned history folder
        orphan_dir = test_dir / "some_random_backup_folder"
        orphan_dir.mkdir()

        # Add manifest
        manifest_data = {
            "parent_file": "unknown",
            "versions": [
                {"id": "v001", "note": "Old version"}
            ]
        }
        with open(orphan_dir / "manifest.json", "w") as f:
            json.dump(manifest_data, f)

        # Verify pre-conditions
        history_dir = test_dir / ".my_project_history"
        if history_dir.exists():
            raise RuntimeError("History dir should not exist yet")

        # 4. Run Link History Operator
        print(f"Linking from: {orphan_dir}")

        # We pass both filepath and directory to be safe, as ImportHelper logic relies on them.
        # Logic in operator: checks filepath, checks if it is manifest, checks if dir.
        res = bpy.ops.savepoints.link_history('EXEC_DEFAULT', filepath=str(orphan_dir), directory=str(orphan_dir))

        if "FINISHED" not in res:
            raise RuntimeError(f"Operator failed: {res}")

        # 5. Verify
        if not history_dir.exists():
            raise RuntimeError(f"History dir was not created at {history_dir}")

        if orphan_dir.exists():
            raise RuntimeError("Orphan dir was not removed/moved")

        if not (history_dir / "manifest.json").exists():
            raise RuntimeError("Manifest not found in new history dir")

        print("Link History Verification: OK")

    except Exception:
        traceback.print_exc()
        sys.exit(1)
    finally:
        # Clean up
        try:
            savepoints.unregister()
        except Exception:
            pass
        if test_dir.exists():
            shutil.rmtree(test_dir)


if __name__ == "__main__":
    main()
