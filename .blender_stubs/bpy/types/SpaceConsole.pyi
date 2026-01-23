# Blender Probe Generated Stub for Blender 5.1.0 Alpha
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .Space import Space
from .ConsoleLine import ConsoleLine
class SpaceConsole(Space):
    type: str
    show_locked_time: bool
    show_region_header: bool
    font_size: int
    select_start: int
    select_end: int
    prompt: str
    language: str
    history: bpy_prop_collection['ConsoleLine']
    scrollback: bpy_prop_collection['ConsoleLine']