# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/blf.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated


CLIPPING = 2
MONOCHROME = 128
ROTATION = 1
SHADOW = 4
WORD_WRAP = 64
def aspect(*args, **kwargs) -> Any:
    """.. function:: aspect(fontid, aspect)

   Set the aspect for drawing text.

   :arg fontid: The id of the typeface as returned by :func:`blf.load`, for default font use 0.
   :type fontid: int
   :arg aspect: The aspect ratio for text drawing to use.
   :type aspect: float


    Online Documentation:
    https://docs.blender.org/api/current/blf.html"""
    ...

def bind_imbuf(*args, **kwargs) -> Any:
    """.. method:: bind_imbuf(fontid, image)

   Context manager to draw text into an image buffer instead of the GPU's context.

   :arg fontid: The id of the typeface as returned by :func:`blf.load`, for default font use 0.
   :type fontid: int
   :arg imbuf: The image to draw into.
   :type imbuf: :class:`imbuf.types.ImBuf`
   :return: The BLF ImBuf context manager.
   :rtype: BLFImBufContext


    Online Documentation:
    https://docs.blender.org/api/current/blf.html"""
    ...

def clipping(*args, **kwargs) -> Any:
    """.. function:: clipping(fontid, xmin, ymin, xmax, ymax)

   Set the clipping, enable/disable using CLIPPING.

   :arg fontid: The id of the typeface as returned by :func:`blf.load`, for default font use 0.
   :type fontid: int
   :arg xmin: Clip the drawing area by these bounds.
   :type xmin: float
   :arg ymin: Clip the drawing area by these bounds.
   :type ymin: float
   :arg xmax: Clip the drawing area by these bounds.
   :type xmax: float
   :arg ymax: Clip the drawing area by these bounds.
   :type ymax: float


    Online Documentation:
    https://docs.blender.org/api/current/blf.html"""
    ...

def color(*args, **kwargs) -> Any:
    """.. function:: color(fontid, r, g, b, a)

   Set the color for drawing text.

   :arg fontid: The id of the typeface as returned by :func:`blf.load`, for default font use 0.
   :type fontid: int
   :arg r: red channel 0.0 - 1.0.
   :type r: float
   :arg g: green channel 0.0 - 1.0.
   :type g: float
   :arg b: blue channel 0.0 - 1.0.
   :type b: float
   :arg a: alpha channel 0.0 - 1.0.
   :type a: float


    Online Documentation:
    https://docs.blender.org/api/current/blf.html"""
    ...

def dimensions(*args, **kwargs) -> Any:
    """.. function:: dimensions(fontid, text)

   Return the width and height of the text.

   :arg fontid: The id of the typeface as returned by :func:`blf.load`, for default font use 0.
   :type fontid: int
   :arg text: the text to draw.
   :type text: str
   :return: the width and height of the text.
   :rtype: tuple[float, float]


    Online Documentation:
    https://docs.blender.org/api/current/blf.html"""
    ...

def disable(*args, **kwargs) -> Any:
    """.. function:: disable(fontid, option)

   Disable option.

   :arg fontid: The id of the typeface as returned by :func:`blf.load`, for default font use 0.
   :type fontid: int
   :arg option: One of ROTATION, CLIPPING, SHADOW or KERNING_DEFAULT.
   :type option: int


    Online Documentation:
    https://docs.blender.org/api/current/blf.html"""
    ...

def draw(*args, **kwargs) -> Any:
    """.. function:: draw(fontid, text)

   Draw text in the current context.

   :arg fontid: The id of the typeface as returned by :func:`blf.load`, for default font use 0.
   :type fontid: int
   :arg text: the text to draw.
   :type text: str


    Online Documentation:
    https://docs.blender.org/api/current/blf.html"""
    ...

def draw_buffer(*args, **kwargs) -> Any:
    """.. function:: draw_buffer(fontid, text)

   Draw text into the buffer bound to the fontid.

   :arg fontid: The id of the typeface as returned by :func:`blf.load`, for default font use 0.
   :type fontid: int
   :arg text: the text to draw.
   :type text: str


    Online Documentation:
    https://docs.blender.org/api/current/blf.html"""
    ...

def enable(*args, **kwargs) -> Any:
    """.. function:: enable(fontid, option)

   Enable option.

   :arg fontid: The id of the typeface as returned by :func:`blf.load`, for default font use 0.
   :type fontid: int
   :arg option: One of ROTATION, CLIPPING, SHADOW or KERNING_DEFAULT.
   :type option: int


    Online Documentation:
    https://docs.blender.org/api/current/blf.html"""
    ...

def load(*args, **kwargs) -> Any:
    """.. function:: load(filepath)

   Load a new font.

   :arg filepath: the filepath of the font.
   :type filepath: str | bytes
   :return: the new font's fontid or -1 if there was an error.
   :rtype: int


    Online Documentation:
    https://docs.blender.org/api/current/blf.html"""
    ...

def position(*args, **kwargs) -> Any:
    """.. function:: position(fontid, x, y, z)

   Set the position for drawing text.

   :arg fontid: The id of the typeface as returned by :func:`blf.load`, for default font use 0.
   :type fontid: int
   :arg x: X axis position to draw the text.
   :type x: float
   :arg y: Y axis position to draw the text.
   :type y: float
   :arg z: Z axis position to draw the text.
   :type z: float


    Online Documentation:
    https://docs.blender.org/api/current/blf.html"""
    ...

def rotation(*args, **kwargs) -> Any:
    """.. function:: rotation(fontid, angle)

   Set the text rotation angle, enable/disable using ROTATION.

   :arg fontid: The id of the typeface as returned by :func:`blf.load`, for default font use 0.
   :type fontid: int
   :arg angle: The angle for text drawing to use.
   :type angle: float


    Online Documentation:
    https://docs.blender.org/api/current/blf.html"""
    ...

def shadow(*args, **kwargs) -> Any:
    """.. function:: shadow(fontid, level, r, g, b, a)

   Shadow options, enable/disable using SHADOW .

   :arg fontid: The id of the typeface as returned by :func:`blf.load`, for default font use 0.
   :type fontid: int
   :arg level: The blur level (0, 3, 5) or outline (6).
   :type level: int
   :arg r: Shadow color (red channel 0.0 - 1.0).
   :type r: float
   :arg g: Shadow color (green channel 0.0 - 1.0).
   :type g: float
   :arg b: Shadow color (blue channel 0.0 - 1.0).
   :type b: float
   :arg a: Shadow color (alpha channel 0.0 - 1.0).
   :type a: float


    Online Documentation:
    https://docs.blender.org/api/current/blf.html"""
    ...

def shadow_offset(*args, **kwargs) -> Any:
    """.. function:: shadow_offset(fontid, x, y)

   Set the offset for shadow text.

   :arg fontid: The id of the typeface as returned by :func:`blf.load`, for default font use 0.
   :type fontid: int
   :arg x: Vertical shadow offset value in pixels.
   :type x: float
   :arg y: Horizontal shadow offset value in pixels.
   :type y: float


    Online Documentation:
    https://docs.blender.org/api/current/blf.html"""
    ...

def size(*args, **kwargs) -> Any:
    """.. function:: size(fontid, size)

   Set the size for drawing text.

   :arg fontid: The id of the typeface as returned by :func:`blf.load`, for default font use 0.
   :type fontid: int
   :arg size: Point size of the font.
   :type size: float


    Online Documentation:
    https://docs.blender.org/api/current/blf.html"""
    ...

def unload(*args, **kwargs) -> Any:
    """.. function:: unload(filepath)

   Unload an existing font.

   :arg filepath: the filepath of the font.
   :type filepath: str | bytes


    Online Documentation:
    https://docs.blender.org/api/current/blf.html"""
    ...

def word_wrap(*args, **kwargs) -> Any:
    """.. function:: word_wrap(fontid, wrap_width)

   Set the wrap width, enable/disable using WORD_WRAP.

   :arg fontid: The id of the typeface as returned by :func:`blf.load`, for default font use 0.
   :type fontid: int
   :arg wrap_width: The width (in pixels) to wrap words at.
   :type wrap_width: int


    Online Documentation:
    https://docs.blender.org/api/current/blf.html"""
    ...
