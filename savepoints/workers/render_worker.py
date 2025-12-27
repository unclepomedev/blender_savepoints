import bpy
import json
import sys
import os
from mathutils import Matrix

def enable_gpu():
    try:
        preferences = bpy.context.preferences
        cycles_addon = preferences.addons.get('cycles')
        if not cycles_addon:
            print("Worker: Cycles addon not found in preferences (Factory Startup?). Skipping GPU.")
            return False

        cycles_prefs = cycles_addon.preferences
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
    render = scene.render

    # A. Apply inherited settings first
    src_img_settings = settings.get("image_settings", {})
    if src_img_settings:
        render.image_settings.file_format = src_img_settings.get("file_format", "PNG")
        render.image_settings.color_mode = src_img_settings.get("color_mode", "RGBA")
        render.image_settings.color_depth = src_img_settings.get("color_depth", "8")
        render.image_settings.compression = src_img_settings.get("compression", 15)
        render.image_settings.quality = src_img_settings.get("quality", 90)
        if "exr_codec" in src_img_settings:
            render.image_settings.exr_codec = src_img_settings["exr_codec"]

    # B. Apply overrides
    fmt_override = settings.get("output_format_override", "SCENE")

    if fmt_override == 'PNG':
        render.image_settings.file_format = 'PNG'
    elif fmt_override == 'JPEG':
        render.image_settings.file_format = 'JPEG'
        render.image_settings.color_mode = 'RGB'

        # Check for overrides (DryRun puts 'jpeg_quality' in root)
        if "jpeg_quality" in settings:
             render.image_settings.quality = settings["jpeg_quality"]
        elif "quality" in src_img_settings:
             render.image_settings.quality = src_img_settings["quality"]

    # 2. Setup GPU
    if settings.get("engine") == 'CYCLES':
        enable_gpu()

    # 3. Apply Render Settings
    render.resolution_x = settings.get("resolution_x", 1920)
    render.resolution_y = settings.get("resolution_y", 1080)
    render.resolution_percentage = settings.get("resolution_percentage", 100)
    render.engine = settings.get("engine", 'CYCLES')

    render.filepath = os.path.join(output_dir, file_prefix)

    if render.engine == 'CYCLES' and "samples" in settings:
        scene.cycles.samples = settings["samples"]
    elif render.engine in ['BLENDER_EEVEE', 'BLENDER_EEVEE_NEXT'] and "samples" in settings:
        if hasattr(scene.eevee, "taa_render_samples"):
            scene.eevee.taa_render_samples = settings["samples"]

    # 4. Apply Scene Context (World & ViewLayer)
    world_name = settings.get("world_name")
    main_blend_path = settings.get("main_blend_path")

    if world_name:
        if world_name not in bpy.data.worlds and main_blend_path and os.path.exists(main_blend_path):
            try:
                with bpy.data.libraries.load(main_blend_path, link=False) as (data_from, data_to):
                    if world_name in data_from.worlds:
                        data_to.worlds = [world_name]
            except Exception as e:
                print(f"Worker Warning: Failed to append world: {e}")

        if world_name in bpy.data.worlds:
            scene.world = bpy.data.worlds[world_name]

    # Prevents compositor black screens by matching the ViewLayer name
    target_layer_name = settings.get("active_view_layer", "View Layer")
    current_layer = bpy.context.view_layer 

    if current_layer.name != target_layer_name:
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
