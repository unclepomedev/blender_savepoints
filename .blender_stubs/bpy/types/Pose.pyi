# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.Pose.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .AnimViz import AnimViz
from .IKParam import IKParam
from .PoseBone import PoseBone
from .bpy_prop_collection import bpy_prop_collection

class Pose(bpy_struct):

    @property
    def bones(self) -> Annotated[bpy_prop_collection['PoseBone'], "is_animatable=False"]:
        """Individual pose bones for the armature"""
        ...
    @property
    def ik_solver(self) -> Literal['LEGACY', 'ITASC']:
        """Selection of IK solver for IK chain"""
        ...
    @ik_solver.setter
    def ik_solver(self, value: Literal['LEGACY', 'ITASC']) -> None:
        ...
    @property
    def ik_param(self) -> Annotated[Optional['IKParam'], "is_animatable=False"]:
        """Parameters for IK solver"""
        ...
    @property
    def use_mirror_x(self) -> bool:
        """Apply changes to matching bone on opposite side of X-Axis"""
        ...
    @use_mirror_x.setter
    def use_mirror_x(self, value: bool) -> None:
        ...
    @property
    def use_mirror_relative(self) -> bool:
        """Apply relative transformations in X-mirror mode (not supported with Auto IK)"""
        ...
    @use_mirror_relative.setter
    def use_mirror_relative(self, value: bool) -> None:
        ...
    @property
    def use_auto_ik(self) -> bool:
        """Add temporary IK constraints while grabbing bones in Pose Mode"""
        ...
    @use_auto_ik.setter
    def use_auto_ik(self, value: bool) -> None:
        ...
    @property
    def animation_visualization(self) -> Annotated['AnimViz', "is_animatable=False"]:
        """Animation data for this data-block"""
        ...
    def apply_pose_from_action(self, *args, **kwargs) -> Any: ...
    def blend_pose_from_action(self, *args, **kwargs) -> Any: ...
    def backup_create(self, *args, **kwargs) -> Any: ...
    def backup_restore(self, *args, **kwargs) -> Any: ...
    def backup_clear(self, *args, **kwargs) -> Any: ...