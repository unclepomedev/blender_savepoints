# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
class SpaceDopeSheetOverlay(bpy_struct):
    show_overlays: bool
    """Display overlays"""
    show_scene_strip_range: bool
    """When using scene time synchronization in the sequence editor, display the range of the current scene strip"""