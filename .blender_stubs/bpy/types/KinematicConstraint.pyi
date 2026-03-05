# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.KinematicConstraint.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .Constraint import Constraint
from .Object import Object

class KinematicConstraint(Constraint):

    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:
        """Constraint name"""
        ...
    @name.setter
    def name(self, value: Annotated[str, "is_animatable=False"]) -> None:
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
    def owner_space(self, value: Literal['WORLD', 'CUSTOM', 'POSE', 'LOCAL_WITH_PARENT', 'LOCAL']) -> None:
        ...
    @property
    def target_space(self) -> Literal['WORLD', 'CUSTOM', 'POSE', 'LOCAL_WITH_PARENT', 'LOCAL', 'LOCAL_OWNER_ORIENT']:
        """Space that target is evaluated in"""
        ...
    @target_space.setter
    def target_space(self, value: Literal['WORLD', 'CUSTOM', 'POSE', 'LOCAL_WITH_PARENT', 'LOCAL', 'LOCAL_OWNER_ORIENT']) -> None:
        ...
    @property
    def space_object(self) -> Annotated[Optional['Object'], "is_animatable=False"]:
        """Object for Custom Space"""
        ...
    @space_object.setter
    def space_object(self, value: Annotated[Optional['Object'], "is_animatable=False"]) -> None:
        ...
    @property
    def space_subtarget(self) -> Annotated[str, "is_animatable=False"]:
        """Armature bone, mesh or lattice vertex group, ..."""
        ...
    @space_subtarget.setter
    def space_subtarget(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def mute(self) -> bool:
        """Enable/Disable Constraint"""
        ...
    @mute.setter
    def mute(self, value: bool) -> None:
        ...
    @property
    def enabled(self) -> bool:
        """Use the results of this constraint"""
        ...
    @enabled.setter
    def enabled(self, value: bool) -> None:
        ...
    @property
    def show_expanded(self) -> bool:
        """Constraint's panel is expanded in UI"""
        ...
    @show_expanded.setter
    def show_expanded(self, value: bool) -> None:
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
    def active(self, value: bool) -> None:
        ...
    @property
    def influence(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Amount of influence constraint will have on the final solution"""
        ...
    @influence.setter
    def influence(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
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
        """Target object"""
        ...
    @target.setter
    def target(self, value: Annotated[Optional['Object'], "is_animatable=False"]) -> None:
        ...
    @property
    def subtarget(self) -> Annotated[str, "is_animatable=False"]:
        """Armature bone, mesh or lattice vertex group, ..."""
        ...
    @subtarget.setter
    def subtarget(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def iterations(self) -> Annotated[int, "step=1"]:
        """Maximum number of solving iterations"""
        ...
    @iterations.setter
    def iterations(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def pole_target(self) -> Annotated[Optional['Object'], "is_animatable=False"]:
        """Object for pole rotation"""
        ...
    @pole_target.setter
    def pole_target(self, value: Annotated[Optional['Object'], "is_animatable=False"]) -> None:
        ...
    @property
    def pole_subtarget(self) -> Annotated[str, "is_animatable=False"]:

        ...
    @pole_subtarget.setter
    def pole_subtarget(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def pole_angle(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=4"]:
        """Pole rotation offset"""
        ...
    @pole_angle.setter
    def pole_angle(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=4"]) -> None:
        ...
    @property
    def weight(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """For Tree-IK: Weight of position control for this target"""
        ...
    @weight.setter
    def weight(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def orient_weight(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """For Tree-IK: Weight of orientation control for this target"""
        ...
    @orient_weight.setter
    def orient_weight(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def chain_count(self) -> Annotated[int, "step=1", "is_animatable=False"]:
        """How many bones are included in the IK effect - 0 uses all bones"""
        ...
    @chain_count.setter
    def chain_count(self, value: Annotated[int, "step=1", "is_animatable=False"]) -> None:
        ...
    @property
    def use_tail(self) -> bool:
        """Include bone's tail as last element in chain"""
        ...
    @use_tail.setter
    def use_tail(self, value: bool) -> None:
        ...
    @property
    def reference_axis(self) -> Literal['BONE', 'TARGET']:
        """Constraint axis Lock options relative to Bone or Target reference"""
        ...
    @reference_axis.setter
    def reference_axis(self, value: Literal['BONE', 'TARGET']) -> None:
        ...
    @property
    def use_location(self) -> bool:
        """Chain follows position of target"""
        ...
    @use_location.setter
    def use_location(self, value: bool) -> None:
        ...
    @property
    def lock_location_x(self) -> bool:
        """Constraint position along X axis"""
        ...
    @lock_location_x.setter
    def lock_location_x(self, value: bool) -> None:
        ...
    @property
    def lock_location_y(self) -> bool:
        """Constraint position along Y axis"""
        ...
    @lock_location_y.setter
    def lock_location_y(self, value: bool) -> None:
        ...
    @property
    def lock_location_z(self) -> bool:
        """Constraint position along Z axis"""
        ...
    @lock_location_z.setter
    def lock_location_z(self, value: bool) -> None:
        ...
    @property
    def use_rotation(self) -> bool:
        """Chain follows rotation of target"""
        ...
    @use_rotation.setter
    def use_rotation(self, value: bool) -> None:
        ...
    @property
    def lock_rotation_x(self) -> bool:
        """Constraint rotation along X axis"""
        ...
    @lock_rotation_x.setter
    def lock_rotation_x(self, value: bool) -> None:
        ...
    @property
    def lock_rotation_y(self) -> bool:
        """Constraint rotation along Y axis"""
        ...
    @lock_rotation_y.setter
    def lock_rotation_y(self, value: bool) -> None:
        ...
    @property
    def lock_rotation_z(self) -> bool:
        """Constraint rotation along Z axis"""
        ...
    @lock_rotation_z.setter
    def lock_rotation_z(self, value: bool) -> None:
        ...
    @property
    def use_stretch(self) -> bool:
        """Enable IK Stretching"""
        ...
    @use_stretch.setter
    def use_stretch(self, value: bool) -> None:
        ...
    @property
    def ik_type(self) -> Literal['COPY_POSE', 'DISTANCE']:

        ...
    @ik_type.setter
    def ik_type(self, value: Literal['COPY_POSE', 'DISTANCE']) -> None:
        ...
    @property
    def limit_mode(self) -> Literal['LIMITDIST_INSIDE', 'LIMITDIST_OUTSIDE', 'LIMITDIST_ONSURFACE']:
        """Distances in relation to sphere of influence to allow"""
        ...
    @limit_mode.setter
    def limit_mode(self, value: Literal['LIMITDIST_INSIDE', 'LIMITDIST_OUTSIDE', 'LIMITDIST_ONSURFACE']) -> None:
        ...
    @property
    def distance(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Radius of limiting sphere"""
        ...
    @distance.setter
    def distance(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...