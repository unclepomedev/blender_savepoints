# Blender Probe Generated Stub for Blender 5.1.0 Alpha
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
from .AnimViz import AnimViz
from .IKParam import IKParam
from .PoseBone import PoseBone
class Pose(bpy_struct):
    bones: bpy_prop_collection['PoseBone']
    ik_solver: str
    ik_param: 'IKParam'
    use_mirror_x: bool
    use_mirror_relative: bool
    use_auto_ik: bool
    animation_visualization: 'AnimViz'
    def apply_pose_from_action(self, *args, **kwargs) -> Any: ...
    def blend_pose_from_action(self, *args, **kwargs) -> Any: ...
    def backup_create(self, *args, **kwargs) -> Any: ...
    def backup_restore(self, *args, **kwargs) -> Any: ...
    def backup_clear(self, *args, **kwargs) -> Any: ...