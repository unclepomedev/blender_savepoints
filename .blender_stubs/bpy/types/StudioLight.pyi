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
from .UserSolidLight import UserSolidLight
class StudioLight(bpy_struct):
    @property
    def index(self) -> Annotated[int, "step=1"]:
        ...
    @property
    def is_user_defined(self) -> bool:
        ...
    @property
    def has_specular_highlight_pass(self) -> bool:
        """Studio light image file has separate "diffuse" and "specular" passes"""
        ...
    @property
    def type(self) -> Literal['STUDIO', 'WORLD', 'MATCAP']:
        ...
    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:
        ...
    @property
    def path(self) -> Annotated[str, "subtype='DIR_PATH'", "is_animatable=False"]:
        ...
    @property
    def solid_lights(self) -> Annotated[bpy_prop_collection['UserSolidLight'], "is_animatable=False"]:
        """Lights used to display objects in solid draw mode"""
        ...
    @property
    def light_ambient(self) -> Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]:
        """Color of the ambient light that uniformly lit the scene"""
        ...