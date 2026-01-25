"""
Online Documentation:
https://docs.blender.org/api/current/bpy.utils.previews.html
"""

# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


import sys
import typing
from typing import Any, Union, Callable, Iterator

class ImagePreviewCollection:
    """
    Dictionary-like class of previews.

    This is a subclass of Python's built-in dict type,
    used to store multiple image previews.

    .. note::

        - instance with :mod:`bpy.utils.previews.new`
        - keys must be ``str`` type.
        - values will be :class:`bpy.types.ImagePreview`
    """
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.previews.html
    """
    def __init__(self) -> Any: ...
    def clear(self) -> Any: ...
    def close(self) -> Any: ...
    def copy(*args, **kwargs) -> Any: ...
    def fromkeys(iterable, value=None, /) -> Any: ...
    def get(self, key, default=None, /) -> Any: ...
    def items(*args, **kwargs) -> Any: ...
    def keys(*args, **kwargs) -> Any: ...
    def load(self, name, path, path_type, force_reload=False) -> Any: ...
    def new(self, name) -> Any: ...
    def pop(*args, **kwargs) -> Any: ...
    def popitem(self, /) -> Any: ...
    def setdefault(self, key, default=None, /) -> Any: ...
    def update(*args, **kwargs) -> Any: ...
    def values(*args, **kwargs) -> Any: ...

def new() -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.previews.html
    """
    ...

def remove(pcoll) -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.previews.html
    """
    ...
