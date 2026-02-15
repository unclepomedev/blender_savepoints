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
from .SpaceDopeSheetOverlay import SpaceDopeSheetOverlay
class SpaceDopeSheetEditor(Space):
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
    mode: Literal['DOPESHEET', 'ACTION', 'SHAPEKEY', 'GPENCIL', 'MASK', 'CACHEFILE', 'TIMELINE']
    """Editing context being displayed"""
    ui_mode: Literal['DOPESHEET', 'ACTION', 'SHAPEKEY', 'GPENCIL', 'MASK', 'CACHEFILE']
    """Editing context being displayed"""
    show_seconds: bool
    """Show timing as a timecode instead of frames"""
    show_sliders: bool
    """Show sliders beside F-Curve channels"""
    show_pose_markers: bool
    """Show markers belonging to the active action instead of Scene markers (Action and Shape Key Editors only)"""
    show_interpolation: bool
    """Display keyframe handle types and non-Bézier interpolation modes"""
    show_extremes: bool
    """Mark keyframes where the key value flow changes direction, based on comparison with adjacent keys"""
    show_markers: bool
    """If any exists, show markers in a separate row at the bottom of the editor"""
    use_auto_merge_keyframes: bool
    """Automatically merge nearby keyframes"""
    use_realtime_update: bool
    """When transforming keyframes, changes to the animation data are flushed to other views"""
    use_marker_sync: bool
    """Sync Markers with keyframe edits"""
    @property
    def dopesheet(self) -> Annotated[Optional['DopeSheet'], "is_animatable=False"]:
        """Settings for filtering animation data"""
        ...
    show_cache: bool
    """Show the status of cached frames in the timeline"""
    cache_softbody: bool
    """Show the active object's softbody point cache"""
    cache_particles: bool
    """Show the active object's particle point cache"""
    cache_cloth: bool
    """Show the active object's cloth point cache"""
    cache_smoke: bool
    """Show the active object's smoke cache"""
    cache_simulation_nodes: bool
    """Show the active object's simulation nodes cache and bake data"""
    cache_dynamicpaint: bool
    """Show the active object's Dynamic Paint cache"""
    cache_rigidbody: bool
    """Show the active object's Rigid Body cache"""
    @property
    def overlays(self) -> Annotated['SpaceDopeSheetOverlay', "is_animatable=False"]:
        """Settings for display of overlays"""
        ...