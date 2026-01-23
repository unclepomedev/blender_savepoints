# SPDX-License-Identifier: GPL-3.0-or-later

import datetime
import os
from typing import Any

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
    img_settings = scene.render.image_settings

    settings: dict[str, Any] = {
        "resolution_x": render.resolution_x,
        "resolution_y": render.resolution_y,
        "resolution_percentage": render.resolution_percentage,
        "engine": render.engine,
        "frame_current": scene.frame_current,
        "camera_matrix_world": [list(row) for row in camera.matrix_world] if camera else [],
        "camera_data": {
            "type": camera.data.type,
            "lens": camera.data.lens,
            "ortho_scale": camera.data.ortho_scale,
            "sensor_width": camera.data.sensor_width,
            "sensor_height": camera.data.sensor_height,
            "sensor_fit": camera.data.sensor_fit,
            "shift_x": camera.data.shift_x,
            "shift_y": camera.data.shift_y,
            "clip_start": camera.data.clip_start,
            "clip_end": camera.data.clip_end,
        } if camera else None,
        "world_name": scene.world.name if scene.world else None,
        "view_settings": {
            "view_transform": scene.view_settings.view_transform,
            "look": scene.view_settings.look,
            "exposure": scene.view_settings.exposure,
            "gamma": scene.view_settings.gamma,
        },
        "active_view_layer": context.view_layer.name,  # For ViewLayer syncing
        "main_blend_path": bpy.data.filepath,  # For appending assets
        "output_format_override": scene.savepoints_settings.batch_output_format,
        "image_settings": {
            "file_format": img_settings.file_format,
            "color_mode": img_settings.color_mode,
            "color_depth": img_settings.color_depth,
            "compression": img_settings.compression,
            "quality": img_settings.quality,
            "exr_codec": img_settings.exr_codec,
        }
    }

    if render.engine == 'CYCLES':
        settings["samples"] = scene.cycles.samples
    elif render.engine in ['BLENDER_EEVEE', 'BLENDER_EEVEE_NEXT']:
        settings["samples"] = getattr(scene.eevee, "taa_render_samples", 64)

    if dry_run:
        settings["output_format_override"] = "JPEG"
        settings["resolution_percentage"] = 25
        settings["samples"] = 1
        settings["jpeg_quality"] = 70
        settings["image_settings"]["quality"] = 70
        settings["image_settings"]["file_format"] = 'JPEG'
        settings["image_settings"]["color_mode"] = 'RGB'

    return settings


def get_worker_script_path():
    """
    Returns the absolute path to the worker script file.
    """
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "workers", "render_worker.py"))


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
