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
from .NlaStrip import NlaStrip
class NlaTrack(bpy_struct):
    strips: bpy_prop_collection['NlaStrip']
    is_override_data: bool
    name: str
    active: bool
    is_solo: bool
    select: bool
    mute: bool
    lock: bool