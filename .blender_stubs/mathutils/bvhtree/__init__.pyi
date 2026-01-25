"""
Online Documentation:
https://docs.blender.org/api/current/mathutils.bvhtree.html
"""

# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


import sys
import typing
from typing import Any, Union, Callable, Iterator

class BVHTree:
    """
    Online Documentation:
    https://docs.blender.org/api/current/mathutils.bvhtree.html
    """
    def FromBMesh(*args, **kwargs) -> Any: ...
    def FromObject(*args, **kwargs) -> Any: ...
    def FromPolygons(*args, **kwargs) -> Any: ...
    def __init__(self, /, *args, **kwargs) -> Any: ...
    def find_nearest(*args, **kwargs) -> Any: ...
    def find_nearest_range(*args, **kwargs) -> Any: ...
    def overlap(*args, **kwargs) -> Any: ...
    def ray_cast(*args, **kwargs) -> Any: ...
