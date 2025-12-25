def extract_render_settings(context):
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
    }

    if render.engine == 'CYCLES':
        settings["samples"] = scene.cycles.samples
    elif render.engine in ['BLENDER_EEVEE', 'BLENDER_EEVEE_NEXT']:
        settings["samples"] = scene.eevee.taa_render_samples

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
    render = scene.render

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
        scene.eevee.taa_render_samples = settings["samples"]

    # 4. Apply Scene Context
    scene.frame_current = settings.get("frame_current", 1)

    world_name = settings.get("world_name")
    if world_name and world_name in bpy.data.worlds:
        scene.world = bpy.data.worlds[world_name]

    cam_matrix = settings.get("camera_matrix_world")
    if cam_matrix and scene.camera:
        scene.camera.matrix_world = Matrix(cam_matrix)

    # 5. Execute
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
        else:
            print("Worker Error: No arguments separator '--' found.")
    except Exception as e:
        print(f"Worker Global Error: {e}")
        sys.exit(1)
"""
