# SPDX-License-Identifier: GPL-3.0-or-later

import blf
import bpy
import gpu
from gpu_extras.batch import batch_for_shader

from . import core

_draw_handler = None


def draw_hud():
    try:
        context = bpy.context
    except AttributeError:
        return

    if not context.area or context.area.type != "VIEW_3D":
        return

    try:
        blend_path = context.blend_data.filepath
    except AttributeError:
        return

    if not blend_path:
        return

    parent_path = core.get_parent_path_from_snapshot(blend_path)
    if not parent_path:
        return

    # --- Draw Text ---
    font_id = 0
    blf.size(font_id, 20)
    blf.color(font_id, 1.0, 0.2, 0.2, 1.0)  # Red

    text = "SNAPSHOT MODE (READ ONLY)"
    text_width, text_height = blf.dimensions(font_id, text)

    region = context.region
    if not region:
        return

    width = region.width
    height = region.height
    padding = 20

    # Bottom Left
    blf.position(font_id, padding, padding, 0)
    blf.draw(font_id, text)

    # Top Left
    blf.position(font_id, padding, height - padding - text_height, 0)
    blf.draw(font_id, text)

    # Top Right
    blf.position(font_id, width - padding - text_width, height - padding - text_height, 0)
    blf.draw(font_id, text)

    # Bottom Right
    blf.position(font_id, width - padding - text_width, padding, 0)
    blf.draw(font_id, text)

    # --- Draw Red Border ---
    try:
        try:
            shader = gpu.shader.from_builtin("2D_UNIFORM_COLOR")
        except Exception:
            shader = gpu.shader.from_builtin("UNIFORM_COLOR")
    except Exception:
        # Fallback or skip if shaders are not available
        return

    coords = [
        (0, 0), (width, 0),
        (width, 0), (width, height),
        (width, height), (0, height),
        (0, height), (0, 0)
    ]

    batch = batch_for_shader(shader, "LINES", {"pos": coords})

    try:
        gpu.state.blend_set("ALPHA")
        gpu.state.line_width_set(4.0)
        shader.bind()
        shader.uniform_float("color", (1.0, 0.0, 0.0, 0.5))
        batch.draw(shader)
        gpu.state.line_width_set(1.0)
        gpu.state.blend_set("NONE")
    except Exception:
        # gpu.state might not exist or fail
        pass


def register():
    global _draw_handler
    if _draw_handler is None:
        _draw_handler = bpy.types.SpaceView3D.draw_handler_add(draw_hud, (), "WINDOW", "POST_PIXEL")


def unregister():
    global _draw_handler
    if _draw_handler is not None:
        bpy.types.SpaceView3D.draw_handler_remove(_draw_handler, "WINDOW")
        _draw_handler = None
