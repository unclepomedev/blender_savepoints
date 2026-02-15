# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/gpu.state.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated


def active_framebuffer_get(*args, **kwargs) -> Any:
    """.. function:: active_framebuffer_get(enable)

   Return the active frame-buffer in context.


    Online Documentation:
    https://docs.blender.org/api/current/gpu.state.html"""
    ...

def blend_get(*args, **kwargs) -> Any:
    """.. function:: blend_get()

    Current blending equation.



    Online Documentation:
    https://docs.blender.org/api/current/gpu.state.html"""
    ...

def blend_set(*args, **kwargs) -> Any:
    """.. function:: blend_set(mode)

   Defines the fixed pipeline blending equation.

   :arg mode: The type of blend mode.

      * ``NONE`` No blending.
      * ``ALPHA`` The original color channels are interpolated according to the alpha value.
      * ``ALPHA_PREMULT`` The original color channels are interpolated according to the alpha value with the new colors pre-multiplied by this value.
      * ``ADDITIVE`` The original color channels are added by the corresponding ones.
      * ``ADDITIVE_PREMULT`` The original color channels are added by the corresponding ones that are pre-multiplied by the alpha value.
      * ``MULTIPLY`` The original color channels are multiplied by the corresponding ones.
      * ``SUBTRACT`` The original color channels are subtracted by the corresponding ones.
      * ``INVERT`` The original color channels are replaced by its complementary color.
   :type mode: str


    Online Documentation:
    https://docs.blender.org/api/current/gpu.state.html"""
    ...

def clip_distances_set(*args, **kwargs) -> Any:
    """.. function:: clip_distances_set(distances_enabled)

   Sets the number of ``gl_ClipDistance`` planes used for clip geometry.

   :arg distances_enabled: Number of clip distances enabled.
   :type distances_enabled: int


    Online Documentation:
    https://docs.blender.org/api/current/gpu.state.html"""
    ...

def color_mask_set(*args, **kwargs) -> Any:
    """.. function:: color_mask_set(r, g, b, a)

   Enable or disable writing of frame buffer color components.

   :arg r, g, b, a: components red, green, blue, and alpha.
   :type r, g, b, a: bool


    Online Documentation:
    https://docs.blender.org/api/current/gpu.state.html"""
    ...

def depth_mask_get(*args, **kwargs) -> Any:
    """.. function:: depth_mask_get()

   Writing status in the depth component.


    Online Documentation:
    https://docs.blender.org/api/current/gpu.state.html"""
    ...

def depth_mask_set(*args, **kwargs) -> Any:
    """.. function:: depth_mask_set(value)

   Write to depth component.

   :arg value: True for writing to the depth component.
   :type near: bool


    Online Documentation:
    https://docs.blender.org/api/current/gpu.state.html"""
    ...

def depth_test_get(*args, **kwargs) -> Any:
    """.. function:: depth_test_get()

    Current depth_test equation.



    Online Documentation:
    https://docs.blender.org/api/current/gpu.state.html"""
    ...

def depth_test_set(*args, **kwargs) -> Any:
    """.. function:: depth_test_set(mode)

   Defines the depth_test equation.

   :arg mode: The depth test equation name.
      Possible values are ``NONE``, ``ALWAYS``, ``LESS``, ``LESS_EQUAL``, ``EQUAL``, ``GREATER`` and ``GREATER_EQUAL``.
   :type mode: str


    Online Documentation:
    https://docs.blender.org/api/current/gpu.state.html"""
    ...

def face_culling_set(*args, **kwargs) -> Any:
    """.. function:: face_culling_set(culling)

   Specify whether none, front-facing or back-facing facets can be culled.

   :arg mode: ``NONE``, ``FRONT`` or ``BACK``.
   :type mode: str


    Online Documentation:
    https://docs.blender.org/api/current/gpu.state.html"""
    ...

def front_facing_set(*args, **kwargs) -> Any:
    """.. function:: front_facing_set(invert)

   Specifies the orientation of front-facing polygons.

   :arg invert: True for clockwise polygons as front-facing.
   :type mode: bool


    Online Documentation:
    https://docs.blender.org/api/current/gpu.state.html"""
    ...

def line_width_get(*args, **kwargs) -> Any:
    """.. function:: line_width_get()

   Current width of rasterized lines.


    Online Documentation:
    https://docs.blender.org/api/current/gpu.state.html"""
    ...

def line_width_set(*args, **kwargs) -> Any:
    """.. function:: line_width_set(width)

   Specify the width of rasterized lines.

   :arg size: New width.
   :type mode: float


    Online Documentation:
    https://docs.blender.org/api/current/gpu.state.html"""
    ...

def point_size_set(*args, **kwargs) -> Any:
    """.. function:: point_size_set(size)

   Specify the diameter of rasterized points.

   :arg size: New diameter.
   :type mode: float


    Online Documentation:
    https://docs.blender.org/api/current/gpu.state.html"""
    ...

def program_point_size_set(*args, **kwargs) -> Any:
    """.. function:: program_point_size_set(enable)

   If enabled, the derived point size is taken from the (potentially clipped) shader builtin gl_PointSize.

   :arg enable: True for shader builtin gl_PointSize.
   :type enable: bool


    Online Documentation:
    https://docs.blender.org/api/current/gpu.state.html"""
    ...

def scissor_get(*args, **kwargs) -> Any:
    """.. function:: scissor_get()

   Retrieve the scissors of the active framebuffer.
   Note: Only valid between 'scissor_set' and a framebuffer rebind.

   :return: The scissor of the active framebuffer as a tuple
        (x, y, xsize, ysize).
        x, y: lower left corner of the scissor rectangle, in pixels.
        xsize, ysize: width and height of the scissor rectangle.
   :rtype: tuple[int, int, int, int]


    Online Documentation:
    https://docs.blender.org/api/current/gpu.state.html"""
    ...

def scissor_set(*args, **kwargs) -> Any:
    """.. function:: scissor_set(x, y, xsize, ysize)

   Specifies the scissor area of the active framebuffer.
   Note: The scissor state is not saved upon framebuffer rebind.

   :arg x, y: lower left corner of the scissor rectangle, in pixels.
   :type x, y: int
   :arg xsize, ysize: width and height of the scissor rectangle.
   :type xsize, ysize: int


    Online Documentation:
    https://docs.blender.org/api/current/gpu.state.html"""
    ...

def scissor_test_set(*args, **kwargs) -> Any:
    """.. function:: scissor_test_set(enable)

   Enable/disable scissor testing on the active framebuffer.

   :arg enable:
        True - enable scissor testing.
        False - disable scissor testing.
   :type enable: bool


    Online Documentation:
    https://docs.blender.org/api/current/gpu.state.html"""
    ...

def viewport_get(*args, **kwargs) -> Any:
    """.. function:: viewport_get()

   Viewport of the active framebuffer.


    Online Documentation:
    https://docs.blender.org/api/current/gpu.state.html"""
    ...

def viewport_set(*args, **kwargs) -> Any:
    """.. function:: viewport_set(x, y, xsize, ysize)

   Specifies the viewport of the active framebuffer.
   Note: The viewport state is not saved upon framebuffer rebind.

   :arg x, y: lower left corner of the viewport_set rectangle, in pixels.
   :type x, y: int
   :arg xsize, ysize: width and height of the viewport_set.
   :type xsize, ysize: int


    Online Documentation:
    https://docs.blender.org/api/current/gpu.state.html"""
    ...
