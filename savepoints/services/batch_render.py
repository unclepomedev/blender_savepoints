import datetime
import os
import bpy


def get_batch_render_output_dir(base_path="//", dry_run=False):
    """
    Generates the output directory path for batch rendering.
    Format: renders_batch/{blend_name}_{timestamp}
    """
    abs_base = bpy.path.abspath(base_path)
    if bpy.data.filepath:
        blend_name = os.path.splitext(os.path.basename(bpy.data.filepath))[0]
    else:
        blend_name = "untitled"

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    
    if dry_run:
        folder_name = f"{blend_name}_{timestamp}_dryrun"
    else:
        folder_name = f"{blend_name}_{timestamp}"

    return os.path.join(abs_base, "renders_batch", folder_name)


def extract_render_settings(context, dry_run=False):
    scene = context.scene
    render = scene.render
    camera = scene.camera

    settings = {
        "resolution_x": render.resolution_x,
        "resolution_y": render.resolution_y,
        "resolution_percentage": render.resolution_percentage,
        "engine": render.engine,
        "frame_current": scene.frame_current,
        "camera_matrix_world": [list(row) for row in camera.matrix_world] if camera else [],
        "world_name": scene.world.name if scene.world else None,
        "active_view_layer": context.view_layer.name,  # For ViewLayer syncing
        "main_blend_path": bpy.data.filepath,  # For appending assets
        "output_format_override": scene.savepoints_settings.batch_output_format,
        "current_scene_format": render.image_settings.file_format,
    }

    if render.engine == 'CYCLES':
        settings["samples"] = scene.cycles.samples
    elif render.engine in ['BLENDER_EEVEE', 'BLENDER_EEVEE_NEXT']:
        settings["samples"] = scene.eevee.taa_render_samples

    if dry_run:
        settings["output_format_override"] = "JPEG"
        settings["resolution_percentage"] = 25
        settings["samples"] = 1
        settings["jpeg_quality"] = 70

    return settings


def get_worker_script_content():
    """
    Returns the python script content for the worker process.
    Includes GPU activation logic for --factory-startup mode.
    """
    return """
import bpy
import json
import sys
import os
from mathutils import Matrix

def enable_gpu():
    try:
        preferences = bpy.context.preferences
        cycles_prefs = preferences.addons['cycles'].preferences
        device_types = ['METAL', 'OPTIX', 'CUDA', 'HIP', 'ONEAPI']

        for dtype in device_types:
            try:
                cycles_prefs.compute_device_type = dtype
                cycles_prefs.get_devices()
                active_devices = []
                for device in cycles_prefs.devices:
                    device.use = True
                    active_devices.append(device.name)

                if active_devices:
                    print(f"Worker: Activated GPU ({dtype}): {active_devices}")
                    return True
            except Exception:
                continue
        print("Worker: No compatible GPU found or failed to activate. Using CPU.")
        return False
    except Exception as e:
        print(f"Worker: GPU setup warning: {e}")
        return False

def run_render(json_path, output_dir, file_prefix):
    # 1. Load Settings
    with open(json_path, 'r') as f:
        settings = json.load(f)

    scene = bpy.context.scene
    context = bpy.context
    render = scene.render

    # 2. Setup GPU
    if settings.get("engine") == 'CYCLES':
        enable_gpu()

    # 3. Apply Render Settings
    render.resolution_x = settings.get("resolution_x", 1920)
    render.resolution_y = settings.get("resolution_y", 1080)
    render.resolution_percentage = settings.get("resolution_percentage", 100)
    render.engine = settings.get("engine", 'CYCLES')

    fmt_override = settings.get("output_format_override", "SCENE")
    if fmt_override == 'PNG':
        render.image_settings.file_format = 'PNG'
    elif fmt_override == 'JPEG':
        render.image_settings.file_format = 'JPEG'
        quality = settings.get("jpeg_quality")
        if quality:
            render.image_settings.quality = quality
    elif fmt_override == 'SCENE':
        current_fmt = settings.get("current_scene_format")
        if current_fmt:
            render.image_settings.file_format = current_fmt

    render.filepath = os.path.join(output_dir, file_prefix)

    if render.engine == 'CYCLES' and "samples" in settings:
        scene.cycles.samples = settings["samples"]
    elif render.engine in ['BLENDER_EEVEE', 'BLENDER_EEVEE_NEXT'] and "samples" in settings:
        scene.eevee.taa_render_samples = settings["samples"]

    # 4. Apply Scene Context (World & ViewLayer)
    world_name = settings.get("world_name")
    main_blend_path = settings.get("main_blend_path")

    if world_name:
        # If world is missing locally, try to append from main file
        if world_name not in bpy.data.worlds and main_blend_path and os.path.exists(main_blend_path):
            print(f"Worker: World '{world_name}' missing locally. Appending from main file...")
            try:
                with bpy.data.libraries.load(main_blend_path, link=False) as (data_from, data_to):
                    if world_name in data_from.worlds:
                        data_to.worlds = [world_name]
            except Exception as e:
                print(f"Worker Warning: Failed to append world: {e}")

        # Set the world if it exists now
        if world_name in bpy.data.worlds:
            scene.world = bpy.data.worlds[world_name]

    # Prevents compositor black screens by matching the ViewLayer name
    target_layer_name = settings.get("active_view_layer", "View Layer")
    current_layer = context.view_layer

    if current_layer.name != target_layer_name:
        # If the target name is already taken by another (inactive) layer, rename it out of the way
        if target_layer_name in scene.view_layers:
            scene.view_layers[target_layer_name].name = f"{target_layer_name}_backup"

        print(f"Worker: Renaming active ViewLayer '{current_layer.name}' -> '{target_layer_name}'")
        current_layer.name = target_layer_name

    # 5. Camera & Execution
    scene.frame_current = settings.get("frame_current", 1)
    cam_matrix = settings.get("camera_matrix_world")

    if cam_matrix:
        if not scene.camera:
            print("Worker: No camera found. Creating a fallback camera.")
            cam_data = bpy.data.cameras.new("BatchRenderCam")
            cam_obj = bpy.data.objects.new("BatchRenderCam", cam_data)
            scene.collection.objects.link(cam_obj)
            scene.camera = cam_obj

        scene.camera.matrix_world = Matrix(cam_matrix)

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
"""


def create_error_log_text_block(version_id, log_path):
    """
    Reads a log file and creates/updates a Blender Text Block.
    Returns the text block object. On failure, the block contains an error message.
    """
    text_name = f"Log_{version_id}"

    if text_name in bpy.data.texts:
        bpy.data.texts.remove(bpy.data.texts[text_name])

    new_text = bpy.data.texts.new(name=text_name)

    if not os.path.exists(log_path):
        new_text.write(f"Error: Log file not found at {log_path}")
        return new_text

    try:
        with open(log_path, 'r', encoding='utf-8', errors='replace') as f:
            log_content = f.read()
            header = f"# SavePoints Batch Render Log\n# Version: {version_id}\n# Path: {log_path}\n{'=' * 40}\n\n"
            new_text.write(header + log_content)
    except Exception as e:
        new_text.write(f"Failed to read log file: {e}")

    return new_text