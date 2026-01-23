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
from .OperatorProperties import OperatorProperties
class KeyMapItem(bpy_struct):
    idname: str
    name: str
    properties: 'OperatorProperties'
    map_type: str
    type: str
    value: str
    direction: str
    id: int
    any: bool
    shift: int
    ctrl: int
    alt: int
    oskey: int
    hyper: int
    shift_ui: bool
    ctrl_ui: bool
    alt_ui: bool
    oskey_ui: bool
    hyper_ui: bool
    key_modifier: str
    repeat: bool
    show_expanded: bool
    propvalue: str
    active: bool
    is_user_modified: bool
    is_user_defined: bool
    def compare(self, *args, **kwargs) -> Any: ...
    def to_string(self, *args, **kwargs) -> Any: ...