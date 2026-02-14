# SPDX-License-Identifier: GPL-3.0-or-later

import json
import os
import sys

import bpy

# Add current directory to sys.path to allow importing sibling modules
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

import gpu_utils  # noqa: E402
import render_config  # noqa: E402
import scene_utils  # noqa: E402


def _verify_output(output_dir: str, file_prefix: str) -> bool:
    if not os.path.exists(output_dir):
        return False
    return any(f.startswith(file_prefix) for f in os.listdir(output_dir))


def _execute_render_task(scene, output_dir, file_prefix):
    """
    Executes the render operation and verifies the output.
    Attempts fallback save if write_still fails.
    """
    render = scene.render

    print(f"Rendering frame {scene.frame_current} to {render.filepath}...")

    if scene.camera:
        print(f"Active Camera: {scene.camera.name}")
    else:
        print("Error: No Active Camera!")

    try:
        bpy.ops.render.render(write_still=True)
        print("Render Finished Successfully.")
    except Exception as ex:
        raise RuntimeError(f"Render operation failed: {ex}")

    # Verification 1
    if _verify_output(output_dir, file_prefix):
        return

    print("Warning: write_still=True didn't produce file. Attempting manual save...")

    # Fallback Save
    ext = render.file_extension
    if not ext:
        fmt = render.image_settings.file_format
        if fmt == "PNG":
            ext = ".png"
        elif "EXR" in fmt:
            ext = ".exr"
        elif fmt == "JPEG":
            ext = ".jpg"
        elif fmt == "TIFF":
            ext = ".tif"
        elif fmt in ["TARGA", "TARGA_RAW"]:
            ext = ".tga"
        elif fmt == "BMP":
            ext = ".bmp"
        elif fmt == "WEBP":
            ext = ".webp"
        else:
            ext = ".png"
            print(
                f"Worker Warning: Could not determine extension for format '{fmt}'. Defaulting to .png"
            )

    target_path = os.path.join(output_dir, f"{file_prefix}{ext}")
    try:
        bpy.data.images["Render Result"].save_render(filepath=target_path)
        print(f"Manual save attempted to {target_path}")
    except Exception as ex:
        print(f"Worker Error: Manual save failed: {ex}")

    # Verification 2
    if not _verify_output(output_dir, file_prefix):
        files = os.listdir(output_dir) if os.path.exists(output_dir) else []
        raise FileNotFoundError(
            f"Worker Error: Rendered file not found! Expected file starting with '{file_prefix}' in {output_dir}\n"
            f"Debug: Existing files: {files}"
        )


def run_render(json_path: str, output_dir: str, file_prefix: str):
    # Settings
    with open(json_path, "r") as f:
        settings = json.load(f)
    scene = bpy.context.scene
    render = scene.render
    render_config.apply_image_settings(render, settings)

    # Setup GPU
    if settings.get("engine") == "CYCLES":
        # Respect user choice for CPU
        device_pref = settings.get("cycles_device", "GPU")
        if device_pref != "CPU":
            gpu_utils.enable_gpu()
        else:
            print("Worker: cycles_device is CPU. Skipping GPU setup.")

    # Apply Render Config / Scene Context (World & ViewLayer)
    render_config.apply_render_settings(scene, render, settings)
    render.filepath = os.path.join(output_dir, file_prefix)
    scene_utils.setup_world(scene, settings)
    scene_utils.setup_view_layer(scene, settings)

    # Camera & Execution
    scene.frame_current = settings.get("frame_current", 1)
    scene_utils.setup_camera(scene, settings)
    scene_utils.setup_view_settings(scene, settings)

    render_config.sanitize_render_settings(scene)
    _execute_render_task(scene, output_dir, file_prefix)


if __name__ == "__main__":
    try:
        argv = sys.argv
        if "--" in argv:
            args = argv[argv.index("--") + 1 :]
            if len(args) >= 3:
                run_render(args[0], args[1], args[2])
            else:
                print("Worker Error: Missing arguments.")
                sys.exit(1)
        else:
            print("Worker Error: No arguments separator '--' found.")
            sys.exit(1)
    except Exception as e:
        print(f"Worker Global Error: {e}")
        sys.exit(1)
