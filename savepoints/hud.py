# SPDX-License-Identifier: GPL-3.0-or-later

import blf
import bpy
import gpu
from gpu_extras.batch import batch_for_shader

from . import core

_draw_handler = None


def draw_hud():
    context = bpy.context
    if not context or not context.area or context.area.type != "VIEW_3D":
        return

    if not context.blend_data or not context.blend_data.filepath:
        return

    parent_path = core.get_parent_path_from_snapshot(context.blend_data.filepath)
    if not parent_path:
        return

    ui_scale = context.preferences.system.ui_scale

    region = context.region
    if not region:
        return

    width = region.width
    height = region.height

    # --- Draw Text ---
    font_id = 0
    font_size = int(20 * ui_scale)
    padding = int(20 * ui_scale)

    blf.size(font_id, font_size)
    blf.color(font_id, 1.0, 0.3, 0.3, 1.0)  # red

    blf.enable(font_id, blf.SHADOW)
    blf.shadow(font_id, 3, 0.0, 0.0, 0.0, 1.0)

    text = "SNAPSHOT MODE (READ ONLY)"
    text_width, text_height = blf.dimensions(font_id, text)

    positions = [
        (padding, padding),  # Bottom Left
        (padding, height - padding - text_height),  # Top Left
        (width - padding - text_width, height - padding - text_height),  # Top Right
        (width - padding - text_width, padding)  # Bottom Right
    ]

    for x, y in positions:
        blf.position(font_id, x, y, 0)
        blf.draw(font_id, text)

    blf.disable(font_id, blf.SHADOW)

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
        gpu.state.line_width_set(4.0 * ui_scale)
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
