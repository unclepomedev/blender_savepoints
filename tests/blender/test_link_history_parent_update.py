import json
import shutil
import sys
from pathlib import Path


# Add project root to sys.path
ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT))

from savepoints.services.linking import link_history

def setup_test_env():
    test_dir = ROOT / "test_link_parent_run"
    if test_dir.exists():
        shutil.rmtree(test_dir)
    test_dir.mkdir()
    return test_dir


def cleanup_test_env(test_dir):
    if test_dir.exists():
        shutil.rmtree(test_dir)


def test_link_history_parent_update():
    print("Starting Link History Parent Update Test...")
    test_dir = setup_test_env()

    # 1. Setup paths
    old_blend_path = test_dir / "old_project.blend"
    new_blend_path = test_dir / "new_project.blend"

    # Fake source history directory
    source_history_name = ".old_project_history"
    source_history_dir = test_dir / source_history_name
    source_history_dir.mkdir()

    # Create manifest with old parent reference
    manifest_path = source_history_dir / "manifest.json"
    manifest_data = {
        "parent_file": str(old_blend_path),
        "versions": []
    }
    with manifest_path.open('w', encoding='utf-8') as f:
        json.dump(manifest_data, f)

    print(f"Created source history at {source_history_dir} with parent_file: {old_blend_path}")

    # 2. Execute Link History
    print("Executing link_history...")
    try:
        new_history_path_str = link_history(source_history_dir, str(new_blend_path))
    except Exception as e:
        raise RuntimeError(f"link_history failed: {e}")

    new_history_path = Path(new_history_path_str)

    if not new_history_path.exists():
        raise RuntimeError("New history directory does not exist")

    # 3. Verify manifest update
    new_manifest_path = new_history_path / "manifest.json"
    with new_manifest_path.open('r', encoding='utf-8') as f:
        new_data = json.load(f)

    actual_parent = new_data.get("parent_file")
    # core.link_history uses Blender's path logic, but here we are testing purely python logic
    # core.to_posix_path might be involved if we implement the fix using it.
    # The fix should probably use core.to_posix_path(blend_filepath)

    # For robust comparison, let's just check if it matches the input string first
    # Or strict path equality

    if actual_parent != str(new_blend_path):
        # Try posix version if simple string fails (in case fix uses posix conversion)
        if actual_parent != Path(new_blend_path).as_posix():
            raise RuntimeError(f"FAILURE: parent_file was not updated. Expected {new_blend_path}, got {actual_parent}")

    print("SUCCESS: parent_file updated correctly.")
    cleanup_test_env(test_dir)


if __name__ == "__main__":
    try:
        test_link_history_parent_update()
    except Exception as e:
        print(f"TEST FAILED: {e}")
        sys.exit(1)
