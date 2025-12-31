# SPDX-License-Identifier: GPL-3.0-or-later

import os
import sys

import bpy


def setup_vse_scene(input_dir, fps):
    """
    Creates a VSE scene with images from input_dir and configures Color Management smart logic.
    """
    if not os.path.exists(input_dir):
        print(f"Error: Input directory not found: {input_dir}")
        return None

    # 1. Collect image files
    valid_exts = {'.png', '.jpg', '.jpeg', '.exr', '.tif', '.tiff', '.webp', '.tga', '.bmp'}
    files = [
        f for f in os.listdir(input_dir)
        if os.path.splitext(f)[1].lower() in valid_exts
    ]
    files.sort()

    if not files:
        print("Error: No images found in directory.")
        return None

    # Identify file type for Color Management logic
    first_file_path = os.path.join(input_dir, files[0])
    first_ext = os.path.splitext(first_file_path)[1].lower()
    is_linear_format = (first_ext == '.exr')

    scene = bpy.context.scene

    # 2. VSE Setup
    if not scene.sequence_editor:
        scene.sequence_editor_create()

    seq = scene.sequence_editor

    if hasattr(seq, "strips"):
        strips_collection = seq.strips
    else:
        strips_collection = seq.sequences

    # Clear existing strips
    for s in strips_collection:
        strips_collection.remove(s)

    try:
        strip = strips_collection.new_image(
            name="Timelapse_Strip",
            filepath=first_file_path,
            channel=1,
            frame_start=1
        )

        for f_name in files[1:]:
            strip.elements.append(f_name)

        strip.frame_final_duration = len(files)

        # 3. Scene Configuration
        scene.frame_start = 1
        scene.frame_end = len(files)
        scene.render.fps = fps

        # Resolution handling
        try:
            tmp_img = bpy.data.images.load(first_file_path)
            scene.render.resolution_x = tmp_img.size[0]
            scene.render.resolution_y = tmp_img.size[1]
            bpy.data.images.remove(tmp_img)
        except Exception as e:
            print(f"Warning: Could not detect resolution. Using default. Error: {e}")

        # 4. Smart Color Management
        if hasattr(scene.view_settings, "view_transform"):
            if is_linear_format:
                print(
                    f"Input is {first_ext} (Linear). Keeping current View Transform: {scene.view_settings.view_transform}")
            else:
                print(f"Input is {first_ext} (Display Referred). Forcing View Transform to 'Standard'.")
                scene.view_settings.view_transform = 'Standard'
                if hasattr(scene.view_settings, "look"):
                    scene.view_settings.look = 'None'

        return scene

    except Exception as e:
        print(f"Error creating VSE strip: {e}")
        return None


def run_timelapse_render(input_dir, output_filepath, fps):
    print("Starting Timelapse Render...")
    print(f"Input: {input_dir}")
    print(f"Output: {output_filepath}")
    print(f"FPS: {fps}")

    scene = setup_vse_scene(input_dir, fps)
    if not scene:
        sys.exit(1)

    # Output settings
    scene.render.filepath = output_filepath

    try:
        img_settings = scene.render.image_settings
        if bpy.app.version >= (5, 0) and hasattr(img_settings, "media_type"):
            img_settings.media_type = 'VIDEO'
    except Exception as e:
        print(f"Info: Blender 5.0+ media_type check skipped: {e}")

    scene.render.image_settings.file_format = 'FFMPEG'
    scene.render.image_settings.color_mode = 'RGB'

    scene.render.ffmpeg.format = 'MPEG4'
    scene.render.ffmpeg.codec = 'H264'
    scene.render.ffmpeg.constant_rate_factor = 'HIGH'
    scene.render.ffmpeg.audio_codec = 'NONE'

    print("Rendering animation...")

    try:
        bpy.ops.render.render(animation=True)
        print("Timelapse Render Finished Successfully.")
    except Exception as e:
        print(f"Render Failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    try:
        argv = sys.argv
        if "--" in argv:
            args = argv[argv.index("--") + 1:]
            if len(args) >= 2:
                in_dir = args[0]
                out_path = args[1]
                try:
                    fps_val = int(args[2]) if len(args) > 2 else 24
                except ValueError:
                    fps_val = 24

                run_timelapse_render(in_dir, out_path, fps_val)
            else:
                print("Worker Error: Missing required arguments.")
                sys.exit(1)
        else:
            print("Worker Error: No arguments separator '--' found.")
            sys.exit(1)
    except Exception as e:
        print(f"Worker Global Error: {e}")
        sys.exit(1)
