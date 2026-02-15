# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated
from .bpy_prop_collection import bpy_prop_collection

from .Space import Space
from .DopeSheet import DopeSheet
class SpaceNLA(Space):
    @property
    def type(self) -> Literal['EMPTY', 'VIEW_3D', 'IMAGE_EDITOR', 'NODE_EDITOR', 'SEQUENCE_EDITOR', 'CLIP_EDITOR', 'DOPESHEET_EDITOR', 'GRAPH_EDITOR', 'NLA_EDITOR', 'TEXT_EDITOR', 'CONSOLE', 'INFO', 'TOPBAR', 'STATUSBAR', 'OUTLINER', 'PROPERTIES', 'FILE_BROWSER', 'SPREADSHEET', 'PREFERENCES']:
        """Space data type"""
        ...
    show_locked_time: bool
    """Synchronize the visible timeline range with other time-based editors"""
    show_region_header: bool
    show_region_footer: bool
    show_region_channels: bool
    show_region_ui: bool
    show_region_hud: bool
    show_seconds: bool
    """Show timing as a timecode instead of frames"""
    show_strip_curves: bool
    """Show influence F-Curves on strips"""
    show_local_markers: bool
    """Show action-local markers on the strips, useful when synchronizing timing across strips"""
    show_markers: bool
    """If any exists, show markers in a separate row at the bottom of the editor"""
    use_realtime_update: bool
    """When transforming strips, changes to the animation data are flushed to other views"""
    @property
    def dopesheet(self) -> Annotated[Optional['DopeSheet'], "is_animatable=False"]:
        """Settings for filtering animation data"""
        ...