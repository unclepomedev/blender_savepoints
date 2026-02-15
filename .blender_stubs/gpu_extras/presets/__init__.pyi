# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/gpu_extras.presets.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated


def draw_circle_2d(position, color, radius, *, segments=None) -> Any:
    """
    Draw a circle.

    :arg position: 2D position where the circle will be drawn.
    :type position: Sequence[float]
    :arg color: Color of the circle (RGBA).
       To use transparency blend must be set to ``ALPHA``, see: :func:`gpu.state.blend_set`.
    :type color: Sequence[float]
    :arg radius: Radius of the circle.
    :type radius: float
    :arg segments: How many segments will be used to draw the circle.
        Higher values give better results but the drawing will take longer.
        If None or not specified, an automatic value will be calculated.
    :type segments: int | None
    

    Online Documentation:
    https://docs.blender.org/api/current/gpu_extras.presets.html"""
    ...

def draw_texture_2d(texture, position, width, height, is_scene_linear_with_rec709_srgb_target=False) -> Any:
    """
    Draw a 2d texture.

    :arg texture: GPUTexture to draw (e.g. gpu.texture.from_image(image) for :class:`bpy.types.Image`).
    :type texture: :class:`gpu.types.GPUTexture`
    :arg position: Position of the lower left corner.
    :type position: 2D Vector
    :arg width: Width of the image when drawn (not necessarily
        the original width of the texture).
    :type width: float
    :arg height: Height of the image when drawn.
    :type height: float
    :arg is_scene_linear_with_rec709_srgb_target:
        True if the `texture` is stored in scene linear color space and
        the destination framebuffer uses the Rec.709 sRGB color space
        (which is true when drawing textures acquired from :class:`bpy.types.Image` inside a
        'PRE_VIEW', 'POST_VIEW' or 'POST_PIXEL' draw handler).
        Otherwise the color space is assumed to match the one of the framebuffer. (default=False)
    :type is_scene_linear_with_rec709_srgb_target: bool
    

    Online Documentation:
    https://docs.blender.org/api/current/gpu_extras.presets.html"""
    ...
