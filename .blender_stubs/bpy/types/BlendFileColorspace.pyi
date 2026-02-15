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
class BlendFileColorspace(bpy_struct):
    @property
    def working_space(self) -> Literal['Linear Rec.709', 'Linear Rec.2020', 'ACEScg']:
        """Color space used for all scene linear colors in this file, and for compositing, shader and geometry nodes processing"""
        ...
    @property
    def working_space_interop_id(self) -> Annotated[str, "is_animatable=False"]:
        """Unique identifier for common color spaces, as defined by the Color Interop Forum. May be empty if there is no interop ID for the working space. Common values are lin_rec709_scene, lin_rec2020_scene and lin_ap1_scene (for ACEScg)"""
        ...
    @property
    def is_missing_opencolorio_config(self) -> bool:
        """A color space, view or display was not found, which likely means the OpenColorIO config used to create this blend file is missing"""
        ...