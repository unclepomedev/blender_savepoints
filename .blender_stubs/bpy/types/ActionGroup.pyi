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
from .FCurve import FCurve
from .ThemeBoneColorSet import ThemeBoneColorSet
class ActionGroup(bpy_struct):
    name: str
    channels: bpy_prop_collection['FCurve']
    select: bool
    lock: bool
    mute: bool
    show_expanded: bool
    show_expanded_graph: bool
    use_pin: bool
    color_set: str
    is_custom_color_set: bool
    colors: 'ThemeBoneColorSet'