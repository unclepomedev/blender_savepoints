# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.TransformConstraint.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .Constraint import Constraint
from .Object import Object

class TransformConstraint(Constraint):

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
    """Target object"""
    subtarget: Annotated[str, "is_animatable=False"]
    """Armature bone, mesh or lattice vertex group, ..."""
    map_from: Literal['LOCATION', 'ROTATION', 'SCALE']
    """The transformation type to use from the target"""
    map_to: Literal['LOCATION', 'ROTATION', 'SCALE']
    """The transformation type to affect on the constrained object"""
    map_to_x_from: Literal['X', 'Y', 'Z']
    """The source axis constrained object's X axis uses"""
    map_to_y_from: Literal['X', 'Y', 'Z']
    """The source axis constrained object's Y axis uses"""
    map_to_z_from: Literal['X', 'Y', 'Z']
    """The source axis constrained object's Z axis uses"""
    use_motion_extrapolate: bool
    """Extrapolate ranges"""
    from_rotation_mode: Literal['AUTO', 'XYZ', 'XZY', 'YXZ', 'YZX', 'ZXY', 'ZYX', 'QUATERNION', 'SWING_TWIST_X', 'SWING_TWIST_Y', 'SWING_TWIST_Z']
    """Specify the type of rotation channels to use"""
    to_euler_order: Literal['AUTO', 'XYZ', 'XZY', 'YXZ', 'YZX', 'ZXY', 'ZYX']
    """Explicitly specify the output euler rotation order"""
    from_min_x: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]
    """Bottom range of X axis source motion"""
    from_min_y: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]
    """Bottom range of Y axis source motion"""
    from_min_z: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]
    """Bottom range of Z axis source motion"""
    from_max_x: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]
    """Top range of X axis source motion"""
    from_max_y: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]
    """Top range of Y axis source motion"""
    from_max_z: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]
    """Top range of Z axis source motion"""
    to_min_x: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]
    """Bottom range of X axis destination motion"""
    to_min_y: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]
    """Bottom range of Y axis destination motion"""
    to_min_z: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]
    """Bottom range of Z axis destination motion"""
    to_max_x: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]
    """Top range of X axis destination motion"""
    to_max_y: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]
    """Top range of Y axis destination motion"""
    to_max_z: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]
    """Top range of Z axis destination motion"""
    mix_mode: Literal['REPLACE', 'ADD']
    """Specify how to combine the new location with original"""
    from_min_x_rot: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]
    """Bottom range of X axis source motion"""
    from_min_y_rot: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]
    """Bottom range of Y axis source motion"""
    from_min_z_rot: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]
    """Bottom range of Z axis source motion"""
    from_max_x_rot: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]
    """Top range of X axis source motion"""
    from_max_y_rot: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]
    """Top range of Y axis source motion"""
    from_max_z_rot: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]
    """Top range of Z axis source motion"""
    to_min_x_rot: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]
    """Bottom range of X axis destination motion"""
    to_min_y_rot: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]
    """Bottom range of Y axis destination motion"""
    to_min_z_rot: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]
    """Bottom range of Z axis destination motion"""
    to_max_x_rot: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]
    """Top range of X axis destination motion"""
    to_max_y_rot: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]
    """Top range of Y axis destination motion"""
    to_max_z_rot: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]
    """Top range of Z axis destination motion"""
    mix_mode_rot: Literal['REPLACE', 'ADD', 'BEFORE', 'AFTER']
    """Specify how to combine the new rotation with original"""
    from_min_x_scale: Annotated[float, "step=10.0", "precision=3"]
    """Bottom range of X axis source motion"""
    from_min_y_scale: Annotated[float, "step=10.0", "precision=3"]
    """Bottom range of Y axis source motion"""
    from_min_z_scale: Annotated[float, "step=10.0", "precision=3"]
    """Bottom range of Z axis source motion"""
    from_max_x_scale: Annotated[float, "step=10.0", "precision=3"]
    """Top range of X axis source motion"""
    from_max_y_scale: Annotated[float, "step=10.0", "precision=3"]
    """Top range of Y axis source motion"""
    from_max_z_scale: Annotated[float, "step=10.0", "precision=3"]
    """Top range of Z axis source motion"""
    to_min_x_scale: Annotated[float, "step=10.0", "precision=3"]
    """Bottom range of X axis destination motion"""
    to_min_y_scale: Annotated[float, "step=10.0", "precision=3"]
    """Bottom range of Y axis destination motion"""
    to_min_z_scale: Annotated[float, "step=10.0", "precision=3"]
    """Bottom range of Z axis destination motion"""
    to_max_x_scale: Annotated[float, "step=10.0", "precision=3"]
    """Top range of X axis destination motion"""
    to_max_y_scale: Annotated[float, "step=10.0", "precision=3"]
    """Top range of Y axis destination motion"""
    to_max_z_scale: Annotated[float, "step=10.0", "precision=3"]
    """Top range of Z axis destination motion"""
    mix_mode_scale: Literal['REPLACE', 'MULTIPLY']
    """Specify how to combine the new scale with original"""