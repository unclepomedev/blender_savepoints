# SPDX-License-Identifier: GPL-3.0-or-later

import os

import bpy
from mathutils import Matrix


def setup_world(scene, settings):
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


def setup_view_layer(scene, settings):
    target_layer_name = settings.get("active_view_layer", "View Layer")
    current_layer = bpy.context.view_layer

    if current_layer.name != target_layer_name:
        if target_layer_name in scene.view_layers:
            scene.view_layers[target_layer_name].name = f"{target_layer_name}_backup"

        print(f"Worker: Renaming active ViewLayer '{current_layer.name}' -> '{target_layer_name}'")
        current_layer.name = target_layer_name


def setup_camera(scene, settings):
    cam_matrix = settings.get("camera_matrix_world")
    cam_data_settings = settings.get("camera_data")
    if cam_matrix:
        if not scene.camera:
            print("Worker: No camera found. Creating a fallback camera.")
            cam_data = bpy.data.cameras.new("BatchRenderCam")
            cam_obj = bpy.data.objects.new("BatchRenderCam", cam_data)
            scene.collection.objects.link(cam_obj)
            scene.camera = cam_obj

        scene.camera.matrix_world = Matrix(cam_matrix)

        if cam_data_settings and scene.camera.data:
            cd = scene.camera.data
            try:
                cd.type = cam_data_settings.get("type", 'PERSP')
                cd.lens = cam_data_settings.get("lens", 50.0)
                cd.ortho_scale = cam_data_settings.get("ortho_scale", 6.0)
                cd.sensor_width = cam_data_settings.get("sensor_width", 36.0)
                cd.sensor_height = cam_data_settings.get("sensor_height", 24.0)
                cd.sensor_fit = cam_data_settings.get("sensor_fit", 'AUTO')
                cd.shift_x = cam_data_settings.get("shift_x", 0.0)
                cd.shift_y = cam_data_settings.get("shift_y", 0.0)
                cd.clip_start = cam_data_settings.get("clip_start", 0.1)
                cd.clip_end = cam_data_settings.get("clip_end", 1000.0)
            except Exception as e:
                print(f"Worker Warning: Failed to apply camera lens settings: {e}")


def setup_view_settings(scene, settings):
    vs_data = settings.get("view_settings")
    if vs_data:
        try:
            scene.view_settings.view_transform = vs_data.get("view_transform", 'AgX')
            scene.view_settings.look = vs_data.get("look", 'None')
            scene.view_settings.exposure = vs_data.get("exposure", 0.0)
            scene.view_settings.gamma = vs_data.get("gamma", 1.0)
        except Exception as e:
            print(f"Worker Warning: Failed to apply view settings: {e}")
