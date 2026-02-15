# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.SplineIKConstraint.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .Constraint import Constraint
from .Object import Object

class SplineIKConstraint(Constraint):

    name: Annotated[str, "is_animatable=False"]
    """Constraint name"""
    @property
    def type(self) -> Literal['CAMERA_SOLVER', 'FOLLOW_TRACK', 'OBJECT_SOLVER', 'COPY_LOCATION', 'COPY_ROTATION', 'COPY_SCALE', 'COPY_TRANSFORMS', 'LIMIT_DISTANCE', 'LIMIT_LOCATION', 'LIMIT_ROTATION', 'LIMIT_SCALE', 'MAINTAIN_VOLUME', 'TRANSFORM', 'TRANSFORM_CACHE', 'CLAMP_TO', 'DAMPED_TRACK', 'IK', 'LOCKED_TRACK', 'SPLINE_IK', 'STRETCH_TO', 'TRACK_TO', 'ACTION', 'ARMATURE', 'CHILD_OF', 'FLOOR', 'FOLLOW_PATH', 'GEOMETRY_ATTRIBUTE', 'PIVOT', 'SHRINKWRAP']:

        ...
    @property
    def is_override_data(self) -> bool:
        """In a local override object, whether this constraint comes from the linked reference object, or is local to the override"""
        ...
    owner_space: Literal['WORLD', 'CUSTOM', 'POSE', 'LOCAL_WITH_PARENT', 'LOCAL']
    """Space that owner is evaluated in"""
    target_space: Literal['WORLD', 'CUSTOM', 'POSE', 'LOCAL_WITH_PARENT', 'LOCAL', 'LOCAL_OWNER_ORIENT']
    """Space that target is evaluated in"""
    space_object: Annotated[Optional['Object'], "is_animatable=False"]
    """Object for Custom Space"""
    space_subtarget: Annotated[str, "is_animatable=False"]
    """Armature bone, mesh or lattice vertex group, ..."""
    mute: bool
    """Enable/Disable Constraint"""
    enabled: bool
    """Use the results of this constraint"""
    show_expanded: bool
    """Constraint's panel is expanded in UI"""
    @property
    def is_valid(self) -> bool:
        """Constraint has valid settings and can be evaluated"""
        ...
    active: bool
    """Constraint is the one being edited"""
    influence: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Amount of influence constraint will have on the final solution"""
    @property
    def error_location(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Amount of residual error in Blender space unit for constraints that work on position"""
        ...
    @property
    def error_rotation(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Amount of residual error in radians for constraints that work on orientation"""
        ...
    target: Annotated[Optional['Object'], "is_animatable=False"]
    """Curve that controls this relationship"""
    chain_count: Annotated[int, "step=1", "is_animatable=False"]
    """How many bones are included in the chain"""
    joint_bindings: Annotated[list[float], "subtype='FACTOR'", "step=10.0", "precision=3"]
    """(EXPERIENCED USERS ONLY) The relative positions of the joints along the chain, as percentages"""
    use_chain_offset: bool
    """Offset the entire chain relative to the root joint"""
    use_even_divisions: bool
    """Ignore the relative lengths of the bones when fitting to the curve"""
    use_curve_radius: bool
    """Average radius of the endpoints is used to tweak the X and Z Scaling of the bones, on top of XZ Scale mode"""
    xz_scale_mode: Literal['NONE', 'BONE_ORIGINAL', 'INVERSE_PRESERVE', 'VOLUME_PRESERVE']
    """Method used for determining the scaling of the X and Z axes of the bones"""
    y_scale_mode: Literal['NONE', 'FIT_CURVE', 'BONE_ORIGINAL']
    """Method used for determining the scaling of the Y axis of the bones, on top of the shape and scaling of the curve itself"""
    use_original_scale: bool
    """Apply volume preservation over the original scaling"""
    bulge: Annotated[float, "step=10.0", "precision=3"]
    """Factor between volume variation and stretching"""
    use_bulge_min: bool
    """Use lower limit for volume variation"""
    use_bulge_max: bool
    """Use upper limit for volume variation"""
    bulge_min: Annotated[float, "step=10.0", "precision=3"]
    """Minimum volume stretching factor"""
    bulge_max: Annotated[float, "step=10.0", "precision=3"]
    """Maximum volume stretching factor"""
    bulge_smooth: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Strength of volume stretching clamping"""