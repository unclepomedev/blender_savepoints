# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .Space import Space
class SpacePreferences(Space):
    type: str
    show_locked_time: bool
    show_region_header: bool
    show_region_ui: bool
    filter_type: str
    filter_text: str