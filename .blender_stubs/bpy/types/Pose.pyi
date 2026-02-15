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
from .AnimViz import AnimViz
from .IKParam import IKParam
from .PoseBone import PoseBone
class Pose(bpy_struct):
    @property
    def bones(self) -> Annotated[bpy_prop_collection['PoseBone'], "is_animatable=False"]:
        """Individual pose bones for the armature"""
        ...
    ik_solver: Literal['LEGACY', 'ITASC']
    """Selection of IK solver for IK chain"""
    @property
    def ik_param(self) -> Annotated[Optional['IKParam'], "is_animatable=False"]:
        """Parameters for IK solver"""
        ...
    use_mirror_x: bool
    """Apply changes to matching bone on opposite side of X-Axis"""
    use_mirror_relative: bool
    """Apply relative transformations in X-mirror mode (not supported with Auto IK)"""
    use_auto_ik: bool
    """Add temporary IK constraints while grabbing bones in Pose Mode"""
    @property
    def animation_visualization(self) -> Annotated['AnimViz', "is_animatable=False"]:
        """Animation data for this data-block"""
        ...
    def apply_pose_from_action(self, *args, **kwargs) -> Any: ...
    def blend_pose_from_action(self, *args, **kwargs) -> Any: ...
    def backup_create(self, *args, **kwargs) -> Any: ...
    def backup_restore(self, *args, **kwargs) -> Any: ...
    def backup_clear(self, *args, **kwargs) -> Any: ...