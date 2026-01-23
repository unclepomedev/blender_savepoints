"""
Online Documentation:
https://docs.blender.org/api/current/imbuf.types.html
"""

# Blender Probe Generated Stub for Blender 5.1.0 Alpha
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


import sys
import typing
from typing import Any, Union, Callable, Iterator

class ImBuf:
    """
    Online Documentation:
    https://docs.blender.org/api/current/imbuf.types.html
    """
    def __init__(self, /, *args, **kwargs) -> Any: ...
    channels: Any
    def copy(*args, **kwargs) -> Any: ...
    def crop(*args, **kwargs) -> Any: ...
    filepath: Any
    def free(*args, **kwargs) -> Any: ...
    planes: Any
    ppm: Any
    def resize(*args, **kwargs) -> Any: ...
    size: Any
