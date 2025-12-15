import shutil
import sys
import traceback
from pathlib import Path

import bpy

# Add project root to sys.path
ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT))

from savepoints import core


def setup_test_env():
    test_dir = ROOT / "test_remap_env"
    if test_dir.exists():
        shutil.rmtree(test_dir)
    test_dir.mkdir()
    return test_dir


def cleanup_test_env(test_dir):
    if test_dir.exists():
        shutil.rmtree(test_dir)


def main():
    print("Starting Remap Snapshot Paths Test...")
    test_dir = setup_test_env()

    # Paths setup
    project_dir = test_dir
    history_dir = project_dir / ".project_history"
    version_dir = history_dir / "v001"
    version_dir.mkdir(parents=True)

    # Create a dummy library file to link against
    lib_dir = project_dir / "Lib"
    lib_dir.mkdir()
    lib_path = lib_dir / "library.blend"

    # Create dummy image file location (file doesn't need to exist for logic test, but path does)
    tex_dir = project_dir / "Textures"
    tex_dir.mkdir()
    img_path = tex_dir / "image.png"

    # Create dummy object to link and save lib
    bpy.ops.wm.read_factory_settings(use_empty=True)
    ob = bpy.data.objects.new("DummyObj", None)
    ob.use_fake_user = True
    bpy.ops.wm.save_as_mainfile(filepath=str(lib_path))

    try:
        # --- Setup Data Blocks ---
        # Start with a clean slate
        bpy.ops.wm.read_factory_settings(use_empty=True)

        # 1. Image
        img = bpy.data.images.new("TestImage", 128, 128)

        # 2. Library
        with bpy.data.libraries.load(str(lib_path), link=True) as (data_from, data_to):
            if "DummyObj" in data_from.objects:
                data_to.objects = ["DummyObj"]

        if not bpy.data.libraries:
            raise RuntimeError(f"Failed to load library. Libs: {list(bpy.data.libraries)}")

        lib = bpy.data.libraries[0]

        # 3. VSE
        scene = bpy.context.scene
        if not scene.sequence_editor:
            scene.sequence_editor_create()

        # Add an image strip
        # Note: new_image requires a file, but we can fake it or use the one we have?
        # Actually it doesn't check existence strictly on creation sometimes, 
        # but let's just make sure we are safe.
        # We'll rely on property setting anyway.
        # We need a valid path for creation usually? 
        # Let's create a dummy file for the strip to be happy.
        with open(img_path, 'wb') as f:
            f.write(b'fake png')

        print(f"DEBUG: SequenceEditor attributes: {dir(scene.sequence_editor)}")
        # Check if sequences exists or if we need to use something else
        if hasattr(scene.sequence_editor, "sequences"):
            seq = scene.sequence_editor.sequences.new_image("TestSeq", str(img_path), channel=1, frame_start=1)
        elif hasattr(scene.sequence_editor, "strips"):
            seq = scene.sequence_editor.strips.new_image("TestSeq", str(img_path), channel=1, frame_start=1)
        else:
            # Fallback for newer API?
            print("WARNING: 'sequences' and 'strips' not found in SequenceEditor.")
            seq = None

        print("\n--- Test 1: Valid Snapshot Remapping ---")
        # 1. Move file to snapshot location
        snapshot_path = version_dir / "snapshot.blend_snapshot"
        bpy.ops.wm.save_as_mainfile(filepath=str(snapshot_path), check_existing=False)

        # 2. Set broken relative paths (simulate they are relative to project root)
        img.filepath = "//Textures/image.png"
        lib.filepath = "//Lib/library.blend"

        # Check what property seq has
        seq_has_filepath = hasattr(seq, "filepath")
        seq_has_directory = hasattr(seq, "directory")

        if seq_has_filepath:
            seq.filepath = "//Textures/image.png"
        elif seq_has_directory:
            seq.directory = "//Textures/"

        # Verify setup
        print(f"Current Filepath: {bpy.data.filepath}")

        # RUN REMAP
        core.remap_snapshot_paths(None)

        # ASSERT
        expected_prefix = "//../../"

        img_path_normalized = img.filepath.replace("\\", "/")
        if not img_path_normalized.startswith(expected_prefix):
            raise RuntimeError(f"Image path not remapped! Got: {img.filepath}")

        lib_path_normalized = lib.filepath.replace("\\", "/")
        if not lib_path_normalized.startswith(expected_prefix):
            raise RuntimeError(f"Library path not remapped! Got: {lib.filepath}")

        if seq:
            if seq_has_filepath:
                seq_path_normalized = seq.filepath.replace("\\", "/")
                if not seq_path_normalized.startswith(expected_prefix):
                    raise RuntimeError(f"Sequence filepath not remapped! Got: {seq.filepath}")
            elif seq_has_directory:
                seq_dir_normalized = seq.directory.replace("\\", "/")
                if not seq_dir_normalized.startswith(expected_prefix):
                    raise RuntimeError(f"Sequence directory not remapped! Got: {seq.directory}")

        print("Test 1 Passed: All paths remapped correctly.")

        print("\n--- Test 2: Double Remapping Prevention ---")
        # Paths are now //../../...
        # Run remap again
        core.remap_snapshot_paths(None)

        img_path_normalized = img.filepath.replace("\\", "/")
        if img_path_normalized.startswith("//../../../../"):
            raise RuntimeError(f"Double remapping detected! Got: {img.filepath}")

        print("Test 2 Passed: Paths remained stable.")

        print("\n--- Test 3: Not a Snapshot (Normal .blend) ---")
        # Move to normal project location
        project_blend = project_dir / "project.blend"
        bpy.ops.wm.save_as_mainfile(filepath=str(project_blend), check_existing=False)

        # Reset paths
        img.filepath = "//Textures/image.png"

        core.remap_snapshot_paths(None)

        if img.filepath != "//Textures/image.png":
            raise RuntimeError(f"Remapped unexpectedly in normal file! Got: {img.filepath}")

        print("Test 3 Passed: Normal file ignored.")

        print("\n--- Test 4: Snapshot outside History folder ---")
        # Move to snapshot outside history
        outside_snapshot = project_dir / "copy.blend_snapshot"
        bpy.ops.wm.save_as_mainfile(filepath=str(outside_snapshot), check_existing=False)

        # Reset paths
        img.filepath = "//Textures/image.png"

        core.remap_snapshot_paths(None)

        if img.filepath != "//Textures/image.png":
            raise RuntimeError(f"Remapped unexpectedly outside history! Got: {img.filepath}")

        print("Test 4 Passed: Snapshot outside history ignored.")

        print("\n--- Test 5: Absolute Paths ---")
        # Move back to valid snapshot location to test exclusion logic
        bpy.ops.wm.save_as_mainfile(filepath=str(snapshot_path), check_existing=False)

        # Set absolute path
        abs_path = str(img_path)
        img.filepath = abs_path

        core.remap_snapshot_paths(None)

        # On Windows/some setups, abs_path format might vary slightly, but checking if it was NOT remapped to relative is key.
        if img.filepath.startswith("//"):
            raise RuntimeError(f"Absolute path was remapped to relative! Got: {img.filepath}")

        print("Test 5 Passed: Absolute path ignored.")

        print("\nALL TESTS PASSED")

    except Exception:
        traceback.print_exc()
        sys.exit(1)
    finally:
        cleanup_test_env(test_dir)


if __name__ == "__main__":
    main()
