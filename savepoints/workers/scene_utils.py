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
    if cam_matrix:
        if not scene.camera:
            print("Worker: No camera found. Creating a fallback camera.")
            cam_data = bpy.data.cameras.new("BatchRenderCam")
            cam_obj = bpy.data.objects.new("BatchRenderCam", cam_data)
            scene.collection.objects.link(cam_obj)
            scene.camera = cam_obj

        scene.camera.matrix_world = Matrix(cam_matrix)
