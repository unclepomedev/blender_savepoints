# SPDX-License-Identifier: GPL-3.0-or-later

import blf
import bpy
import gpu
from gpu_extras.batch import batch_for_shader

from .services.storage import get_parent_path_from_snapshot

_draw_handler = None
_shader = None


def get_shader():
    global _shader
    if _shader:
        return _shader

    try:
        _shader = gpu.shader.from_builtin("2D_UNIFORM_COLOR")
    except Exception:
        try:
            _shader = gpu.shader.from_builtin("UNIFORM_COLOR")
        except Exception:
            pass
    return _shader


class HUDManager:
    def __init__(self, context):
        self.context = context
        self.scene = getattr(context, "scene", None)
        self.settings = getattr(self.scene, "savepoints_settings", None)

    def should_draw(self):
        if (
            not self.context
            or not self.context.area
            or self.context.area.type != "VIEW_3D"
        ):
            return False

        if not self.context.blend_data or not self.context.blend_data.filepath:
            return False

        return True

    def get_content(self):
        filepath = self.context.blend_data.filepath
        parent_path = get_parent_path_from_snapshot(filepath)

        show_warning = self.settings and self.settings.show_autosave_warning

        if parent_path:
            return "SNAPSHOT MODE (REVIEW MODE)", (1.0, 0.3, 0.3, 1.0)  # Red

        if show_warning and self.settings:
            return (
                self.settings.autosave_warning_message,
                (1.0, 0.6, 0.0, 1.0),
            )  # Orange

        return None

    @staticmethod
    def draw_text(region, text_content, base_color, ui_scale):
        width = region.width
        height = region.height

        font_id = 0
        font_size = int(20 * ui_scale)
        padding = int(60 * ui_scale)

        try:
            blf.size(font_id, font_size)
            blf.color(font_id, *base_color)

            blf.enable(font_id, blf.SHADOW)
            blf.shadow(font_id, 3, 0.0, 0.0, 0.0, 1.0)

            text_width, text_height = blf.dimensions(font_id, text_content)

            positions = [
                (padding, padding),  # Bottom Left
                (padding, height - padding - text_height),  # Top Left
                (
                    width - padding - text_width,
                    height - padding - text_height,
                ),  # Top Right
                (width - padding - text_width, padding),  # Bottom Right
            ]

            for x, y in positions:
                blf.position(font_id, x, y, 0)
                blf.draw(font_id, text_content)

            blf.disable(font_id, blf.SHADOW)
        except Exception:
            pass

    @staticmethod
    def draw_border(region, base_color, ui_scale):
        width = region.width
        height = region.height

        shader = get_shader()
        if not shader:
            return

        coords = [
            (0, 0),
            (width, 0),
            (width, 0),
            (width, height),
            (width, height),
            (0, height),
            (0, height),
            (0, 0),
        ]

        try:
            batch = batch_for_shader(shader, "LINES", {"pos": coords})
        except Exception:
            return

        try:
            gpu.state.blend_set("ALPHA")
            gpu.state.line_width_set(4.0 * ui_scale)
            shader.bind()
            shader.uniform_float(
                "color", (base_color[0], base_color[1], base_color[2], 0.5)
            )
            batch.draw(shader)
        except Exception:
            pass
        finally:
            # Restore state
            try:
                gpu.state.line_width_set(1.0)
                gpu.state.blend_set("NONE")
            except Exception:
                pass

    def draw(self):
        if not self.should_draw():
            return

        content = self.get_content()
        if not content:
            return

        text_content, base_color = content

        region = self.context.region
        if not region:
            return

        ui_scale = self.context.preferences.system.ui_scale

        self.draw_text(region, text_content, base_color, ui_scale)
        self.draw_border(region, base_color, ui_scale)


def draw_hud():
    manager = HUDManager(bpy.context)
    manager.draw()


def register_draw_handler():
    global _draw_handler
    if _draw_handler is None:
        _draw_handler = bpy.types.SpaceView3D.draw_handler_add(
            draw_hud, (), "WINDOW", "POST_PIXEL"
        )


def unregister_draw_handler():
    global _draw_handler
    if _draw_handler is not None:
        bpy.types.SpaceView3D.draw_handler_remove(_draw_handler, "WINDOW")
        _draw_handler = None
