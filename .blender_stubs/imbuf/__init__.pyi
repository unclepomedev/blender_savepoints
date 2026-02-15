# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/imbuf.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated


def load(*args, **kwargs) -> Any:
    """.. function:: load(filepath)

   Load an image from a file.

   :arg filepath: the filepath of the image.
   :type filepath: str | bytes
   :return: the newly loaded image.
   :rtype: :class:`ImBuf`


    Online Documentation:
    https://docs.blender.org/api/current/imbuf.html"""
    ...

def load_from_buffer(*args, **kwargs) -> Any:
    """.. function:: load_from_buffer(buffer)

   Load an image from a buffer.

   :arg buffer: A buffer containing the image data.
   :type buffer: collections.abc.Buffer
   :return: the newly loaded image.
   :rtype: :class:`ImBuf`


    Online Documentation:
    https://docs.blender.org/api/current/imbuf.html"""
    ...

def new(*args, **kwargs) -> Any:
    """.. function:: new(size)

   Load a new image.

   :arg size: The size of the image in pixels.
   :type size: tuple[int, int]
   :return: the newly loaded image.
   :rtype: :class:`ImBuf`


    Online Documentation:
    https://docs.blender.org/api/current/imbuf.html"""
    ...

def write(*args, **kwargs) -> Any:
    """.. function:: write(image, *, filepath=image.filepath)

   Write an image.

   :arg image: the image to write.
   :type image: :class:`ImBuf`
   :arg filepath: Optional filepath of the image (fallback to the images file path).
   :type filepath: str | bytes | None


    Online Documentation:
    https://docs.blender.org/api/current/imbuf.html"""
    ...

from . import types as types
# Documentation: https://docs.blender.org/api/current/imbuf.types.html