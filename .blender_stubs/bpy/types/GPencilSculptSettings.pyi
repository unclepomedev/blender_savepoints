# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.GPencilSculptSettings.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .CurveMapping import CurveMapping
from .GPencilSculptGuide import GPencilSculptGuide

class GPencilSculptSettings(bpy_struct):

    @property
    def guide(self) -> Annotated[Optional['GPencilSculptGuide'], "is_animatable=False"]:

        ...
    use_multiframe_falloff: Annotated[bool, "is_animatable=False"]
    """Use falloff effect when edit in multiframe mode to compute brush effect by frame"""
    use_thickness_curve: Annotated[bool, "is_animatable=False"]
    """Use curve to define primitive stroke thickness"""
    use_scale_thickness: Annotated[bool, "is_animatable=False"]
    """Scale the stroke thickness when transforming strokes"""
    use_automasking_stroke: Annotated[bool, "is_animatable=False"]
    """Affect only strokes below the cursor"""
    use_automasking_layer_stroke: Annotated[bool, "is_animatable=False"]
    """Affect only strokes below the cursor"""
    use_automasking_material_stroke: Annotated[bool, "is_animatable=False"]
    """Affect only strokes below the cursor"""
    use_automasking_layer_active: Annotated[bool, "is_animatable=False"]
    """Affect only the Active Layer"""
    use_automasking_material_active: Annotated[bool, "is_animatable=False"]
    """Affect only the Active Material"""
    @property
    def multiframe_falloff_curve(self) -> Annotated[Optional['CurveMapping'], "is_animatable=False"]:
        """Custom curve to control falloff of brush effect by Grease Pencil frames"""
        ...
    @property
    def thickness_primitive_curve(self) -> Annotated[Optional['CurveMapping'], "is_animatable=False"]:
        """Custom curve to control primitive thickness"""
        ...
    lock_axis: Annotated[Literal['VIEW', 'AXIS_Y', 'AXIS_X', 'AXIS_Z', 'CURSOR'], "is_animatable=False"]

    intersection_threshold: Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]
    """Threshold for stroke intersections"""