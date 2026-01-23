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
from .XrActionMapItem import XrActionMapItem
class XrActionMap(bpy_struct):
    name: str
    actionmap_items: bpy_prop_collection['XrActionMapItem']
    selected_item: int