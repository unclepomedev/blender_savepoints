# Blender Probe Generated Stub for Blender 5.1.0 Alpha
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
class MovieClipProxy(bpy_struct):
    build_25: bool
    build_50: bool
    build_75: bool
    build_100: bool
    build_undistorted_25: bool
    build_undistorted_50: bool
    build_undistorted_75: bool
    build_undistorted_100: bool
    build_record_run: bool
    quality: int
    timecode: str
    directory: str