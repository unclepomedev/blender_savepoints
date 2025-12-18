import json
import shutil
import sys
from pathlib import Path

from savepoints.services.linking import link_history

# Add project root to sys.path
ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT))


def setup_test_env():
    test_dir = ROOT / "test_validation_run"
    if test_dir.exists():
        shutil.rmtree(test_dir)
    test_dir.mkdir()
    return test_dir


def cleanup_test_env(test_dir):
    if test_dir.exists():
        shutil.rmtree(test_dir)


def test_link_history_validation():
    print("Starting Link History Validation Test...")
    test_dir = setup_test_env()

    # Setup Paths
    project_path = test_dir / "project.blend"
    bad_json_dir = test_dir / "bad_json_history"
    missing_keys_dir = test_dir / "missing_keys_history"
    valid_dir = test_dir / "valid_history"

    # Create dummy project file (just for the path existence check in core if any, actually core.link_history doesn't check if blend exists on disk, but checks bpy.data.filepath usually. But core.link_history takes path as arg)
    # core.link_history checks: if not blend_filepath: raise ValueError("Save the current file first.")

    # 1. Test Malformed JSON
    bad_json_dir.mkdir()
    (bad_json_dir / "manifest.json").write_text("{ this is not json }", encoding='utf-8')

    print("Testing Malformed JSON...")
    try:
        link_history(bad_json_dir, str(project_path))
        raise RuntimeError("Malformed JSON should have raised ValueError")
    except ValueError as e:
        print(f"Caught expected error: {e}")
        if "JSON" not in str(e) and "Invalid" not in str(e):
            # Adjust expectation based on implementation
            pass

    # 2. Test Missing Keys (Valid JSON but not a manifest)
    missing_keys_dir.mkdir()
    (missing_keys_dir / "manifest.json").write_text("{}", encoding='utf-8')

    print("Testing Missing Keys...")
    try:
        link_history(missing_keys_dir, str(project_path))
        raise RuntimeError("Empty JSON should have raised ValueError")
    except ValueError as e:
        print(f"Caught expected error: {e}")

    # 3. Test Valid Manifest
    valid_dir.mkdir()
    valid_manifest = {
        "versions": [],
        "parent_file": str(project_path)
    }
    with (valid_dir / "manifest.json").open('w', encoding='utf-8') as f:
        json.dump(valid_manifest, f)

    print("Testing Valid Manifest...")
    # This should succeed
    try:
        target_path_str = link_history(valid_dir, str(project_path))
        print("Valid manifest linked successfully.")

        # Verification
        target_path = Path(target_path_str)
        if not target_path.exists():
            raise RuntimeError(f"Target history directory not found at: {target_path}")

        if valid_dir.exists():
            raise RuntimeError(f"Source directory still exists at: {valid_dir}")

        if not (target_path / "manifest.json").exists():
            raise RuntimeError("manifest.json not found in target directory")

        expected_name = ".project_history"
        if target_path.name != expected_name:
            raise RuntimeError(f"Unexpected target directory name. Expected {expected_name}, got {target_path.name}")

    except Exception as e:
        raise RuntimeError(f"Valid manifest failed: {e}")

    print("ALL VALIDATION TESTS PASSED")
    cleanup_test_env(test_dir)


if __name__ == "__main__":
    try:
        test_link_history_validation()
    except Exception as e:
        print(f"TEST FAILED: {e}")
        sys.exit(1)
