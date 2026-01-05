# SPDX-License-Identifier: GPL-3.0-or-later

import os
import sys

import bpy

# Add current directory to sys.path to allow importing sibling modules
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

import render_config  # noqa: E402
import scene_utils  # noqa: E402

FRAMES_PER_IMAGE = 6
VALID_EXTENSIONS = {'.png', '.jpg', '.jpeg', '.exr', '.hdr', '.tif', '.tiff', '.webp', '.tga', '.bmp'}


class TimelapseArgs:
    """Handles command-line argument parsing and validation."""

    def __init__(self, input_dir, output_filepath, fps, burn_in, burn_in_pos):
        self.input_dir = input_dir
        self.output_filepath = output_filepath
        self.fps = fps
        self.burn_in = burn_in
        self.burn_in_pos = burn_in_pos

    @classmethod
    def parse(cls, argv):
        """
        Parses system arguments and returns a TimelapseArgs instance.
        Exits the program if arguments are invalid.
        """
        if "--" not in argv:
            print("Worker Error: No arguments separator '--' found.")
            sys.exit(1)

        args = argv[argv.index("--") + 1:]

        if len(args) < 2:
            print("Worker Error: Missing required arguments.")
            sys.exit(1)

        input_dir = args[0]
        output_filepath = args[1]

        # Parse FPS
        try:
            fps = int(args[2]) if len(args) > 2 else 24
        except ValueError:
            fps = 24

        # Parse Burn-in
        burn_in = False
        if len(args) > 3:
            try:
                burn_in = bool(int(args[3]))
            except Exception:
                pass

        # Parse Burn-in Position
        burn_in_pos = 'BL'
        if len(args) > 4:
            pos = args[4]
            if pos in ['TL', 'TR', 'BL', 'BR']:
                burn_in_pos = pos
            else:
                print(f"Warning: Invalid Burn-in position '{pos}', using default 'BL'.")

        return cls(input_dir, output_filepath, fps, burn_in, burn_in_pos)

    def log_info(self):
        print("Starting Timelapse Render...")
        print(f"Input: {self.input_dir}")
        print(f"Output: {self.output_filepath}")
        print(f"FPS: {self.fps}")
        print(f"Burn-in: {self.burn_in} ({self.burn_in_pos})")


class BurnInGenerator:
    """Handles the creation of burn-in text strips."""

    def __init__(self, scene, strips_collection):
        self.scene = scene
        self.strips = strips_collection
        self.res_y = scene.render.resolution_y

    def generate(self, files, pos):
        """Adds text strips for each frame with the filename."""

        # Calculate layout
        font_size, align_x, align_y, loc_x, loc_y = self._calculate_layout(pos)

        # Add strip for each file
        for i, f_name in enumerate(files):
            self._add_text_strip(i, f_name, font_size, align_x, align_y, loc_x, loc_y)

    def _calculate_layout(self, pos):
        # Dynamic font size (approx 4% of height)
        font_size = int(self.res_y * 0.04)
        if font_size < 12:
            font_size = 12

        margin_x = 0.03
        margin_y = 0.05

        # Defaults
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
            # Defaults are correct
            pass
        elif pos == 'BR':
            align_x = 'RIGHT'
            align_y = 'BOTTOM'
            loc_x = 1.0 - margin_x
            loc_y = margin_y

        return font_size, align_x, align_y, loc_x, loc_y

    def _add_text_strip(self, index, filename, font_size, align_x, align_y, loc_x, loc_y):
        # Prepare text content
        text_content = os.path.splitext(filename)[0]
        if text_content.endswith("_render"):
            text_content = text_content[:-7]

        try:
            start_frame = index * FRAMES_PER_IMAGE + 1

            kwargs = {
                "name": f"Text_{index}",
                "type": 'TEXT',
                "frame_start": start_frame,
                "channel": 2,
            }

            if bpy.app.version < (5, 0):
                kwargs["frame_end"] = start_frame + FRAMES_PER_IMAGE
            else:
                kwargs["length"] = FRAMES_PER_IMAGE

            t_strip = self.strips.new_effect(**kwargs)
            t_strip.frame_final_duration = FRAMES_PER_IMAGE

            t_strip.text = text_content
            t_strip.font_size = font_size
            t_strip.use_shadow = True
            t_strip.shadow_color = (0, 0, 0, 1)
            t_strip.color = (1, 1, 1, 1)

            # Apply alignment
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
            print(f"Warning: Failed to add text strip for frame {index}: {e}")


class SceneBuilder:
    """Manages the VSE scene setup."""

    def __init__(self, args: TimelapseArgs):
        self.args = args
        self.scene = bpy.context.scene
        self.first_image_info = {
            "path": "",
            "resolution_x": 1920,
            "resolution_y": 1080,
            "is_linear": False,
            "ext": ""
        }

    def build(self):
        """Orchestrates the scene building process."""
        if not os.path.exists(self.args.input_dir):
            print(f"Error: Input directory not found: {self.args.input_dir}")
            return None

        files = self._collect_images()
        if not files:
            print("Error: No images found in directory.")
            return None

        # Analyze the first image (Resolution & Color Space detection)
        first_file_path = os.path.join(self.args.input_dir, files[0])
        self._analyze_image(first_file_path)

        # Setup VSE
        strips = self._setup_vse_editor()

        # Add Image Strips
        total_frames = self._add_image_strips(strips, files)

        # Configure Scene (FPS, Duration, Resolution)
        self._configure_scene_properties(total_frames)

        # Color Management
        self._setup_color_management()

        # Burn-in
        if self.args.burn_in:
            print(f"Adding Burn-in text (Pos: {self.args.burn_in_pos})")
            burn_in_gen = BurnInGenerator(self.scene, strips)
            burn_in_gen.generate(files, self.args.burn_in_pos)

        return self.scene

    def _collect_images(self):
        files = [
            f for f in os.listdir(self.args.input_dir)
            if os.path.splitext(f)[1].lower() in VALID_EXTENSIONS
        ]
        files.sort()
        return files

    def _analyze_image(self, filepath):
        """Loads the first image to determine resolution and likely color space."""
        self.first_image_info["path"] = filepath
        self.first_image_info["ext"] = os.path.splitext(filepath)[1].lower()

        try:
            # Load image temporarily
            tmp_img = bpy.data.images.load(filepath)

            # Resolution
            self.first_image_info["resolution_x"] = tmp_img.size[0]
            self.first_image_info["resolution_y"] = tmp_img.size[1]

            # Color Space Heuristics
            # 1. EXR and HDR are inherently Linear (Scene Referred)
            if self.first_image_info["ext"] in {'.exr', '.hdr'}:
                self.first_image_info["is_linear"] = True
            # 2. Check if the image buffer is floating point (e.g. 32bit Float TIFF)
            elif tmp_img.is_float:
                print(f"Info: Image detected as Floating Point ({self.first_image_info['ext']}). Treating as Linear.")
                self.first_image_info["is_linear"] = True
            else:
                self.first_image_info["is_linear"] = False

            # Cleanup
            bpy.data.images.remove(tmp_img)

        except Exception as e:
            print(f"Warning: Failed to analyze image {filepath}. Using defaults. Error: {e}")

    def _setup_vse_editor(self):
        if not self.scene.sequence_editor:
            self.scene.sequence_editor_create()

        seq = self.scene.sequence_editor
        if hasattr(seq, "strips"):
            strips_collection = seq.strips
        else:
            strips_collection = seq.sequences

        for s in strips_collection:
            strips_collection.remove(s)

        return strips_collection

    def _add_image_strips(self, strips, files):
        current_frame = 1
        for i, f_name in enumerate(files):
            f_path = os.path.join(self.args.input_dir, f_name)
            try:
                strip = strips.new_image(
                    name=f"Image_{i}",
                    filepath=f_path,
                    channel=1,
                    frame_start=current_frame
                )
                strip.frame_final_duration = FRAMES_PER_IMAGE
                current_frame += FRAMES_PER_IMAGE
            except Exception as e:
                print(f"Error adding strip for {f_name}: {e}")

        return current_frame

    def _configure_scene_properties(self, end_frame):
        self.scene.frame_start = 1
        self.scene.frame_end = end_frame - 1
        self.scene.render.fps = self.args.fps

        print(f"Timelapse Duration: {self.scene.frame_end} frames")

        # Apply Resolution from analyzed info
        res_settings = {
            "resolution_x": self.first_image_info["resolution_x"],
            "resolution_y": self.first_image_info["resolution_y"],
            "resolution_percentage": 100
        }
        render_config.apply_render_settings(self.scene, self.scene.render, res_settings)

    def _setup_color_management(self):
        if not hasattr(self.scene.view_settings, "view_transform"):
            return

        is_linear = self.first_image_info["is_linear"]
        ext = self.first_image_info["ext"]

        if is_linear:
            print(
                f"Input is {ext} (Linear/Float). Keeping current View Transform: {self.scene.view_settings.view_transform}")
        else:
            print(f"Input is {ext} (Display Referred). Forcing View Transform to 'Standard'.")

            settings = {
                "view_settings": {
                    "view_transform": 'Standard',
                    "look": 'None'
                }
            }
            scene_utils.setup_view_settings(self.scene, settings)


class Renderer:
    """Handles the rendering configuration and execution."""

    def __init__(self, scene, output_filepath):
        self.scene = scene
        self.output_filepath = output_filepath

    def configure(self):
        self.scene.render.filepath = self.output_filepath

        # Blender 5.0+ Media Type
        try:
            img_settings = self.scene.render.image_settings
            if bpy.app.version >= (5, 0) and hasattr(img_settings, "media_type"):
                img_settings.media_type = 'VIDEO'
        except Exception as e:
            print(f"Info: Blender 5.0+ media_type check skipped: {e}")

        # Apply Image Settings
        settings = {
            "image_settings": {
                "file_format": 'FFMPEG',
                "color_mode": 'RGB'
            },
            "ffmpeg": {
                "format": 'MPEG4',
                "codec": 'H264',
                "constant_rate_factor": 'HIGH',
                "audio_codec": 'NONE'
            }
        }

        render_config.apply_image_settings(self.scene.render, settings)
        render_config.apply_ffmpeg_settings(self.scene.render, settings)

    def execute(self):
        print("Rendering animation...")
        try:
            bpy.ops.render.render(animation=True)
            print("Timelapse Render Finished Successfully.")
        except Exception as e:
            print(f"Render Failed: {e}")
            sys.exit(1)


def main():
    try:
        # 1. Parse Arguments
        args = TimelapseArgs.parse(sys.argv)
        args.log_info()

        # 2. Build Scene
        builder = SceneBuilder(args)
        scene = builder.build()

        if not scene:
            sys.exit(1)

        # 3. Configure and Render
        renderer = Renderer(scene, args.output_filepath)
        renderer.configure()
        renderer.execute()

    except Exception as e:
        print(f"Worker Global Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
