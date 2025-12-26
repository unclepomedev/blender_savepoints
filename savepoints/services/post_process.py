import os

import bpy


def open_folder_platform_independent(directory_path):
    """
    Opens the directory in the OS default file explorer.
    """
    if not os.path.exists(directory_path):
        return False

    try:
        bpy.ops.wm.path_open(filepath=directory_path)
        return True
    except Exception as e:
        print(f"Failed to open folder: {e}")
        return False


def create_vse_timelapse(directory_path, scene_name_suffix="_Timelapse"):
    """
    Creates a new Scene, imports rendered images into VSE.
    Returns the scene name if successful, None otherwise.
    """
    if not os.path.exists(directory_path):
        return None

    # 1. collect and sort image files
    valid_exts = {'.png', '.jpg', '.jpeg', '.exr', '.tif', '.tiff'}
    files = [
        f for f in os.listdir(directory_path)
        if os.path.splitext(f)[1].lower() in valid_exts
    ]

    files.sort()

    if not files:
        print("No images found to create timelapse.")
        return None

    # 2. get current file name and determine scene name
    base_name = os.path.basename(directory_path)
    scene_name = f"{base_name}{scene_name_suffix}"

    new_scene = bpy.data.scenes.new(name=scene_name)

    # 3. scene setup
    current_scene = bpy.context.scene
    new_scene.render.resolution_x = current_scene.render.resolution_x
    new_scene.render.resolution_y = current_scene.render.resolution_y
    new_scene.render.fps = 24

    # 4. VSE setup
    if not new_scene.sequence_editor:
        new_scene.sequence_editor_create()

    seq = new_scene.sequence_editor

    if hasattr(seq, 'strips'):
        strips_collection = seq.strips
    else:
        strips_collection = seq.sequences

    try:
        first_file_path = os.path.join(directory_path, files[0])

        strip = strips_collection.new_image(
            name="SavePoints_Timelapse",
            filepath=first_file_path,
            channel=1,
            frame_start=1,
        )

        for f_name in files[1:]:
            strip.elements.append(f_name)

        strip.frame_final_duration = len(files)
        new_scene.frame_end = len(files)

        return new_scene.name

    except Exception as e:
        print(f"SavePoints Error creating VSE strip: {e}")
        import traceback
        traceback.print_exc()
        return None
