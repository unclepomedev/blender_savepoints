# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/imbuf.types.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated


class ImBuf:
    """
    Online Documentation:
    https://docs.blender.org/api/current/imbuf.types.html"""
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
