# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.FreestyleSettings.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .FreestyleLineSet import FreestyleLineSet
from .FreestyleModuleSettings import FreestyleModuleSettings
from .FreestyleModules import FreestyleModules
from .Linesets import Linesets
from .bpy_prop_collection import bpy_prop_collection

class FreestyleSettings(bpy_struct):

    @property
    def modules(self) -> Annotated['FreestyleModules', "is_animatable=False"]:
        """A list of style modules (to be applied from top to bottom)"""
        ...
    @property
    def mode(self) -> Literal['SCRIPT', 'EDITOR']:
        """Select the Freestyle control mode"""
        ...
    @mode.setter
    def mode(self, value: Literal['SCRIPT', 'EDITOR']) -> None:
        ...
    @property
    def use_culling(self) -> bool:
        """If enabled, out-of-view edges are ignored"""
        ...
    @use_culling.setter
    def use_culling(self, value: bool) -> None:
        ...
    @property
    def use_suggestive_contours(self) -> bool:
        """Enable suggestive contours"""
        ...
    @use_suggestive_contours.setter
    def use_suggestive_contours(self, value: bool) -> None:
        ...
    @property
    def use_ridges_and_valleys(self) -> bool:
        """Enable ridges and valleys"""
        ...
    @use_ridges_and_valleys.setter
    def use_ridges_and_valleys(self, value: bool) -> None:
        ...
    @property
    def use_material_boundaries(self) -> bool:
        """Enable material boundaries"""
        ...
    @use_material_boundaries.setter
    def use_material_boundaries(self, value: bool) -> None:
        ...
    @property
    def use_smoothness(self) -> bool:
        """Take face smoothness into account in view map calculation"""
        ...
    @use_smoothness.setter
    def use_smoothness(self, value: bool) -> None:
        ...
    @property
    def use_view_map_cache(self) -> bool:
        """Keep the computed view map and avoid recalculating it if mesh geometry is unchanged"""
        ...
    @use_view_map_cache.setter
    def use_view_map_cache(self, value: bool) -> None:
        ...
    @property
    def as_render_pass(self) -> bool:
        """Renders Freestyle output to a separate pass instead of overlaying it on the Combined pass"""
        ...
    @as_render_pass.setter
    def as_render_pass(self, value: bool) -> None:
        ...
    @property
    def sphere_radius(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Sphere radius for computing curvatures"""
        ...
    @sphere_radius.setter
    def sphere_radius(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def kr_derivative_epsilon(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Kr derivative epsilon for computing suggestive contours"""
        ...
    @kr_derivative_epsilon.setter
    def kr_derivative_epsilon(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def crease_angle(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]:
        """Angular threshold for detecting crease edges"""
        ...
    @crease_angle.setter
    def crease_angle(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def linesets(self) -> Annotated['Linesets', "is_animatable=False"]:

        ...