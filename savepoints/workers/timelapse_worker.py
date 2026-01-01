# SPDX-License-Identifier: GPL-3.0-or-later

import os
import sys

import bpy


def setup_burn_in(scene, strips, files, pos):
    """
    Adds text strips for each frame with the filename as text.
    """
    res_y = scene.render.resolution_y

    # Dynamic font size (approx 4% of height)
    font_size = int(res_y * 0.04)
    if font_size < 12:
        font_size = 12

    # Relative margins (3% and 5%)
    # Note: Y margin is often visually larger needed to not touch edge
    margin_x = 0.03
    margin_y = 0.05

    # Set alignment and location base
    # location is (x, y) 0.0-1.0
    align_x = 'LEFT'
    align_y = 'BOTTOM'
    loc_x = margin_x
    loc_y = margin_y

    if pos == 'TL':
        align_x = 'LEFT'
        align_y = 'TOP'
        loc_x = margin_x
        loc_y = 1.0 - margin_y
    elif pos == 'TR':
        align_x = 'RIGHT'
        align_y = 'TOP'
        loc_x = 1.0 - margin_x
        loc_y = 1.0 - margin_y
    elif pos == 'BL':
        align_x = 'LEFT'
        align_y = 'BOTTOM'
        loc_x = margin_x
        loc_y = margin_y
    elif pos == 'BR':
        align_x = 'RIGHT'
        align_y = 'BOTTOM'
        loc_x = 1.0 - margin_x
        loc_y = margin_y

    # Add strip for each file
    for i, f_name in enumerate(files):
        # Remove extension and known suffixes like "_render"
        text_content = os.path.splitext(f_name)[0]
        # specific for SavePoints batch render: remove "_render" suffix if present to make it cleaner
        if text_content.endswith("_render"):
            text_content = text_content[:-7]

        try:
            kwargs = {
                "name": f"Text_{i}",
                "type": 'TEXT',
                "frame_start": i + 1,
                "channel": 2,
            }

            if bpy.app.version < (5, 0):
                # Blender 4.x expects frame_end
                kwargs["frame_end"] = i + 2
            else:
                # Blender 5.x expects length
                kwargs["length"] = 1

            t_strip = strips.new_effect(**kwargs)
            t_strip.frame_final_duration = 1

            t_strip.text = text_content
            t_strip.font_size = font_size
            t_strip.use_shadow = True
            t_strip.shadow_color = (0, 0, 0, 1)
            t_strip.color = (1, 1, 1, 1)

            # Apply alignment and position
            # Blender 4.x vs 5.x compatibility (align_x/y -> alignment_x/y)
            if hasattr(t_strip, "align_x"):
                t_strip.align_x = align_x
            elif hasattr(t_strip, "alignment_x"):
                t_strip.alignment_x = align_x

            if hasattr(t_strip, "align_y"):
                t_strip.align_y = align_y
            elif hasattr(t_strip, "alignment_y"):
                t_strip.alignment_y = align_y

            t_strip.location = (loc_x, loc_y)

        except Exception as e:
            print(f"Warning: Failed to add text strip for frame {i}: {e}")


def setup_vse_scene(input_dir, fps, burn_in=False, burn_in_pos='BL'):
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
                try:
                    scene.view_settings.view_transform = 'Standard'
                except TypeError:
                    print(f"Warning: 'Standard' transform not found. Keeping: {scene.view_settings.view_transform}")
                if hasattr(scene.view_settings, "look"):
                    try:
                        scene.view_settings.look = 'None'
                    except (TypeError, ValueError):
                        print("Warning: 'None' look not found.")

        # 5. Burn-in
        if burn_in:
            print(f"Adding Burn-in text (Pos: {burn_in_pos})")
            setup_burn_in(scene, strips_collection, files, burn_in_pos)

        return scene

    except Exception as e:
        print(f"Error creating VSE strip: {e}")
        return None


def run_timelapse_render(input_dir, output_filepath, fps, burn_in=False, burn_in_pos='BL'):
    print("Starting Timelapse Render...")
    print(f"Input: {input_dir}")
    print(f"Output: {output_filepath}")
    print(f"FPS: {fps}")
    print(f"Burn-in: {burn_in} ({burn_in_pos})")

    scene = setup_vse_scene(input_dir, fps, burn_in, burn_in_pos)
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

                burn_in = False
                burn_in_pos = 'BL'

                if len(args) > 3:
                    try:
                        burn_in = bool(int(args[3]))
                    except Exception:
                        pass

                if len(args) > 4:
                    burn_in_pos = args[4]

                run_timelapse_render(in_dir, out_path, fps_val, burn_in, burn_in_pos)
            else:
                print("Worker Error: Missing required arguments.")
                sys.exit(1)
        else:
            print("Worker Error: No arguments separator '--' found.")
            sys.exit(1)
    except Exception as e:
        print(f"Worker Global Error: {e}")
        sys.exit(1)
