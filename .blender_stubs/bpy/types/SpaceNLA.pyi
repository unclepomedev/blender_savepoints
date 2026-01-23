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
from .DopeSheet import DopeSheet
class SpaceNLA(Space):
    type: str
    show_locked_time: bool
    show_region_header: bool
    show_region_footer: bool
    show_region_channels: bool
    show_region_ui: bool
    show_region_hud: bool
    show_seconds: bool
    show_strip_curves: bool
    show_local_markers: bool
    show_markers: bool
    use_realtime_update: bool
    dopesheet: 'DopeSheet'