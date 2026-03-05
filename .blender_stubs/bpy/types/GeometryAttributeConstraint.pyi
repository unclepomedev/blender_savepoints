# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.GeometryAttributeConstraint.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .Constraint import Constraint
from .Object import Object

class GeometryAttributeConstraint(Constraint):

    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:
        """Constraint name"""
        ...
    @name.setter
    def name(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def type(self) -> Literal['CAMERA_SOLVER', 'FOLLOW_TRACK', 'OBJECT_SOLVER', 'COPY_LOCATION', 'COPY_ROTATION', 'COPY_SCALE', 'COPY_TRANSFORMS', 'LIMIT_DISTANCE', 'LIMIT_LOCATION', 'LIMIT_ROTATION', 'LIMIT_SCALE', 'MAINTAIN_VOLUME', 'TRANSFORM', 'TRANSFORM_CACHE', 'CLAMP_TO', 'DAMPED_TRACK', 'IK', 'LOCKED_TRACK', 'SPLINE_IK', 'STRETCH_TO', 'TRACK_TO', 'ACTION', 'ARMATURE', 'CHILD_OF', 'FLOOR', 'FOLLOW_PATH', 'GEOMETRY_ATTRIBUTE', 'PIVOT', 'SHRINKWRAP']:

        ...
    @property
    def is_override_data(self) -> bool:
        """In a local override object, whether this constraint comes from the linked reference object, or is local to the override"""
        ...
    @property
    def owner_space(self) -> Literal['WORLD', 'CUSTOM', 'POSE', 'LOCAL_WITH_PARENT', 'LOCAL']:
        """Space that owner is evaluated in"""
        ...
    @owner_space.setter
    def owner_space(self, value: Literal['WORLD', 'CUSTOM', 'POSE', 'LOCAL_WITH_PARENT', 'LOCAL']):
        ...
    @property
    def target_space(self) -> Literal['WORLD', 'CUSTOM', 'POSE', 'LOCAL_WITH_PARENT', 'LOCAL', 'LOCAL_OWNER_ORIENT']:
        """Space that target is evaluated in"""
        ...
    @target_space.setter
    def target_space(self, value: Literal['WORLD', 'CUSTOM', 'POSE', 'LOCAL_WITH_PARENT', 'LOCAL', 'LOCAL_OWNER_ORIENT']):
        ...
    @property
    def space_object(self) -> Annotated[Optional['Object'], "is_animatable=False"]:
        """Object for Custom Space"""
        ...
    @space_object.setter
    def space_object(self, value: Annotated[Optional['Object'], "is_animatable=False"]):
        ...
    @property
    def space_subtarget(self) -> Annotated[str, "is_animatable=False"]:
        """Armature bone, mesh or lattice vertex group, ..."""
        ...
    @space_subtarget.setter
    def space_subtarget(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def mute(self) -> bool:
        """Enable/Disable Constraint"""
        ...
    @mute.setter
    def mute(self, value: bool):
        ...
    @property
    def enabled(self) -> bool:
        """Use the results of this constraint"""
        ...
    @enabled.setter
    def enabled(self, value: bool):
        ...
    @property
    def show_expanded(self) -> bool:
        """Constraint's panel is expanded in UI"""
        ...
    @show_expanded.setter
    def show_expanded(self, value: bool):
        ...
    @property
    def is_valid(self) -> bool:
        """Constraint has valid settings and can be evaluated"""
        ...
    @property
    def active(self) -> bool:
        """Constraint is the one being edited"""
        ...
    @active.setter
    def active(self, value: bool):
        ...
    @property
    def influence(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Amount of influence constraint will have on the final solution"""
        ...
    @influence.setter
    def influence(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def error_location(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Amount of residual error in Blender space unit for constraints that work on position"""
        ...
    @property
    def error_rotation(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Amount of residual error in radians for constraints that work on orientation"""
        ...
    @property
    def target(self) -> Annotated[Optional['Object'], "is_animatable=False"]:
        """Target geometry object"""
        ...
    @target.setter
    def target(self, value: Annotated[Optional['Object'], "is_animatable=False"]):
        ...
    @property
    def attribute_name(self) -> Annotated[str, "is_animatable=False"]:
        """Name of the attribute to retrieve the transform from"""
        ...
    @attribute_name.setter
    def attribute_name(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def domain(self) -> Literal['POINT', 'EDGE', 'FACE', 'FACE_CORNER', 'CURVE', 'INSTANCE']:
        """Attribute domain"""
        ...
    @domain.setter
    def domain(self, value: Literal['POINT', 'EDGE', 'FACE', 'FACE_CORNER', 'CURVE', 'INSTANCE']):
        ...
    @property
    def apply_target_transform(self) -> bool:
        """Apply the target object's world transform on top of the attribute's transform"""
        ...
    @apply_target_transform.setter
    def apply_target_transform(self, value: bool):
        ...
    @property
    def data_type(self) -> Literal['VECTOR', 'QUATERNION', 'FLOAT4X4']:
        """Select data type of attribute"""
        ...
    @data_type.setter
    def data_type(self, value: Literal['VECTOR', 'QUATERNION', 'FLOAT4X4']):
        ...
    @property
    def sample_index(self) -> Annotated[int, "step=1"]:
        """Sample Index"""
        ...
    @sample_index.setter
    def sample_index(self, value: Annotated[int, "step=1"]):
        ...
    @property
    def mix_loc(self) -> bool:
        """Mix Location"""
        ...
    @mix_loc.setter
    def mix_loc(self, value: bool):
        ...
    @property
    def mix_rot(self) -> bool:
        """Mix Rotation"""
        ...
    @mix_rot.setter
    def mix_rot(self, value: bool):
        ...
    @property
    def mix_scl(self) -> bool:
        """Mix Scale"""
        ...
    @mix_scl.setter
    def mix_scl(self, value: bool):
        ...
    @property
    def mix_mode(self) -> Literal['REPLACE', 'BEFORE_FULL', 'BEFORE_SPLIT', 'AFTER_FULL', 'AFTER_SPLIT']:
        """Specify how the copied and existing transformations are combined"""
        ...
    @mix_mode.setter
    def mix_mode(self, value: Literal['REPLACE', 'BEFORE_FULL', 'BEFORE_SPLIT', 'AFTER_FULL', 'AFTER_SPLIT']):
        ...