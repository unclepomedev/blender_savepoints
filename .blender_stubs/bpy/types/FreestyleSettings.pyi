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
from .FreestyleLineSet import FreestyleLineSet
from .FreestyleModuleSettings import FreestyleModuleSettings
from .FreestyleModules import FreestyleModules
from .Linesets import Linesets
class FreestyleSettings(bpy_struct):
    @property
    def modules(self) -> Annotated['FreestyleModules', "is_animatable=False"]:
        """A list of style modules (to be applied from top to bottom)"""
        ...
    mode: Literal['SCRIPT', 'EDITOR']
    """Select the Freestyle control mode"""
    use_culling: bool
    """If enabled, out-of-view edges are ignored"""
    use_suggestive_contours: bool
    """Enable suggestive contours"""
    use_ridges_and_valleys: bool
    """Enable ridges and valleys"""
    use_material_boundaries: bool
    """Enable material boundaries"""
    use_smoothness: bool
    """Take face smoothness into account in view map calculation"""
    use_view_map_cache: bool
    """Keep the computed view map and avoid recalculating it if mesh geometry is unchanged"""
    as_render_pass: bool
    """Renders Freestyle output to a separate pass instead of overlaying it on the Combined pass"""
    sphere_radius: Annotated[float, "step=10.0", "precision=3"]
    """Sphere radius for computing curvatures"""
    kr_derivative_epsilon: Annotated[float, "step=10.0", "precision=3"]
    """Kr derivative epsilon for computing suggestive contours"""
    crease_angle: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]
    """Angular threshold for detecting crease edges"""
    @property
    def linesets(self) -> Annotated['Linesets', "is_animatable=False"]:
        ...