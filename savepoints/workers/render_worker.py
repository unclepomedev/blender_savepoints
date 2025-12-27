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


def run_render(json_path, output_dir, file_prefix):
    # 1. Load Settings
    with open(json_path, 'r') as f:
        settings = json.load(f)

    scene = bpy.context.scene
    render = scene.render

    # 2. Apply Settings
    render_config.apply_image_settings(render, settings)

    # 3. Setup GPU
    if settings.get("engine") == 'CYCLES':
        gpu_utils.enable_gpu()

    # 4. Apply Render Config
    render_config.apply_render_settings(scene, render, settings)

    render.filepath = os.path.join(output_dir, file_prefix)

    # 5. Apply Scene Context (World & ViewLayer)
    scene_utils.setup_world(scene, settings)
    scene_utils.setup_view_layer(scene, settings)

    # 6. Camera & Execution
    scene.frame_current = settings.get("frame_current", 1)
    scene_utils.setup_camera(scene, settings)

    print(f"Rendering frame {scene.frame_current} to {render.filepath}...")
    try:
        bpy.ops.render.render(write_still=True)
        print("Render Finished Successfully.")
    except Exception as e:
        print(f"Render Failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    try:
        argv = sys.argv
        if "--" in argv:
            args = argv[argv.index("--") + 1:]
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
