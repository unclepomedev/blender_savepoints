# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
from .Operator import Operator
from .Scene import Scene
from .Screen import Screen
from .Stereo3dDisplay import Stereo3dDisplay
from .ViewLayer import ViewLayer
from .WorkSpace import WorkSpace
class Window(bpy_struct):
    parent: 'Window'
    scene: 'Scene'
    workspace: 'WorkSpace'
    screen: 'Screen'
    view_layer: 'ViewLayer'
    x: int
    y: int
    width: int
    height: int
    stereo_3d_display: 'Stereo3dDisplay'
    support_hdr_color: bool
    modal_operators: bpy_prop_collection['Operator']
    def cursor_warp(self, *args, **kwargs) -> Any: ...
    def cursor_set(self, *args, **kwargs) -> Any: ...
    def cursor_modal_set(self, *args, **kwargs) -> Any: ...
    def cursor_modal_restore(self, *args, **kwargs) -> Any: ...
    def event_simulate(self, *args, **kwargs) -> Any: ...