# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/gpu.texture.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated


def from_image(*args, **kwargs) -> Any:
    """.. function:: from_image(image)

   Get GPUTexture corresponding to an Image data-block. The GPUTexture memory is shared with Blender.
   Note: Colors read from the texture will be in scene linear color space and have premultiplied or straight alpha matching the image alpha mode.

   :arg image: The Image data-block.
   :type image: :class:`bpy.types.Image`
   :return: The GPUTexture used by the image.
   :rtype: :class:`gpu.types.GPUTexture`


    Online Documentation:
    https://docs.blender.org/api/current/gpu.texture.html"""
    ...
