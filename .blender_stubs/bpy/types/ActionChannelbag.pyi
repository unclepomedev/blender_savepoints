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
from .ActionGroup import ActionGroup
from .ActionSlot import ActionSlot
from .FCurve import FCurve
class ActionChannelbag(bpy_struct):
    slot_handle: int
    slot: 'ActionSlot'
    fcurves: bpy_prop_collection['FCurve']
    groups: bpy_prop_collection['ActionGroup']