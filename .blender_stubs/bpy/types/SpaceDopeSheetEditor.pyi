# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.SpaceDopeSheetEditor.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .Space import Space
from .DopeSheet import DopeSheet
from .SpaceDopeSheetOverlay import SpaceDopeSheetOverlay

class SpaceDopeSheetEditor(Space):

    @property
    def type(self) -> Literal['EMPTY', 'VIEW_3D', 'IMAGE_EDITOR', 'NODE_EDITOR', 'SEQUENCE_EDITOR', 'CLIP_EDITOR', 'DOPESHEET_EDITOR', 'GRAPH_EDITOR', 'NLA_EDITOR', 'TEXT_EDITOR', 'CONSOLE', 'INFO', 'TOPBAR', 'STATUSBAR', 'OUTLINER', 'PROPERTIES', 'FILE_BROWSER', 'SPREADSHEET', 'PREFERENCES']:
        """Space data type"""
        ...
    @property
    def show_locked_time(self) -> bool:
        """Synchronize the visible timeline range with other time-based editors"""
        ...
    @show_locked_time.setter
    def show_locked_time(self, value: bool):
        ...
    @property
    def show_region_header(self) -> bool:

        ...
    @show_region_header.setter
    def show_region_header(self, value: bool):
        ...
    @property
    def show_region_footer(self) -> bool:

        ...
    @show_region_footer.setter
    def show_region_footer(self, value: bool):
        ...
    @property
    def show_region_channels(self) -> bool:

        ...
    @show_region_channels.setter
    def show_region_channels(self, value: bool):
        ...
    @property
    def show_region_ui(self) -> bool:

        ...
    @show_region_ui.setter
    def show_region_ui(self, value: bool):
        ...
    @property
    def show_region_hud(self) -> bool:

        ...
    @show_region_hud.setter
    def show_region_hud(self, value: bool):
        ...
    @property
    def mode(self) -> Literal['DOPESHEET', 'ACTION', 'SHAPEKEY', 'GPENCIL', 'MASK', 'CACHEFILE', 'TIMELINE']:
        """Editing context being displayed"""
        ...
    @mode.setter
    def mode(self, value: Literal['DOPESHEET', 'ACTION', 'SHAPEKEY', 'GPENCIL', 'MASK', 'CACHEFILE', 'TIMELINE']):
        ...
    @property
    def ui_mode(self) -> Literal['DOPESHEET', 'ACTION', 'SHAPEKEY', 'GPENCIL', 'MASK', 'CACHEFILE']:
        """Editing context being displayed"""
        ...
    @ui_mode.setter
    def ui_mode(self, value: Literal['DOPESHEET', 'ACTION', 'SHAPEKEY', 'GPENCIL', 'MASK', 'CACHEFILE']):
        ...
    @property
    def show_seconds(self) -> bool:
        """Show timing as a timecode instead of frames"""
        ...
    @show_seconds.setter
    def show_seconds(self, value: bool):
        ...
    @property
    def show_sliders(self) -> bool:
        """Show sliders beside F-Curve channels"""
        ...
    @show_sliders.setter
    def show_sliders(self, value: bool):
        ...
    @property
    def show_pose_markers(self) -> bool:
        """Show markers belonging to the active action instead of Scene markers (Action and Shape Key Editors only)"""
        ...
    @show_pose_markers.setter
    def show_pose_markers(self, value: bool):
        ...
    @property
    def show_interpolation(self) -> bool:
        """Display keyframe handle types and non-Bézier interpolation modes"""
        ...
    @show_interpolation.setter
    def show_interpolation(self, value: bool):
        ...
    @property
    def show_extremes(self) -> bool:
        """Mark keyframes where the key value flow changes direction, based on comparison with adjacent keys"""
        ...
    @show_extremes.setter
    def show_extremes(self, value: bool):
        ...
    @property
    def show_markers(self) -> bool:
        """If any exists, show markers in a separate row at the bottom of the editor"""
        ...
    @show_markers.setter
    def show_markers(self, value: bool):
        ...
    @property
    def use_auto_merge_keyframes(self) -> bool:
        """Automatically merge nearby keyframes"""
        ...
    @use_auto_merge_keyframes.setter
    def use_auto_merge_keyframes(self, value: bool):
        ...
    @property
    def use_realtime_update(self) -> bool:
        """When transforming keyframes, changes to the animation data are flushed to other views"""
        ...
    @use_realtime_update.setter
    def use_realtime_update(self, value: bool):
        ...
    @property
    def use_marker_sync(self) -> bool:
        """Sync Markers with keyframe edits"""
        ...
    @use_marker_sync.setter
    def use_marker_sync(self, value: bool):
        ...
    @property
    def dopesheet(self) -> Annotated[Optional['DopeSheet'], "is_animatable=False"]:
        """Settings for filtering animation data"""
        ...
    @property
    def show_cache(self) -> bool:
        """Show the status of cached frames in the timeline"""
        ...
    @show_cache.setter
    def show_cache(self, value: bool):
        ...
    @property
    def cache_softbody(self) -> bool:
        """Show the active object's softbody point cache"""
        ...
    @cache_softbody.setter
    def cache_softbody(self, value: bool):
        ...
    @property
    def cache_particles(self) -> bool:
        """Show the active object's particle point cache"""
        ...
    @cache_particles.setter
    def cache_particles(self, value: bool):
        ...
    @property
    def cache_cloth(self) -> bool:
        """Show the active object's cloth point cache"""
        ...
    @cache_cloth.setter
    def cache_cloth(self, value: bool):
        ...
    @property
    def cache_smoke(self) -> bool:
        """Show the active object's smoke cache"""
        ...
    @cache_smoke.setter
    def cache_smoke(self, value: bool):
        ...
    @property
    def cache_simulation_nodes(self) -> bool:
        """Show the active object's simulation nodes cache and bake data"""
        ...
    @cache_simulation_nodes.setter
    def cache_simulation_nodes(self, value: bool):
        ...
    @property
    def cache_dynamicpaint(self) -> bool:
        """Show the active object's Dynamic Paint cache"""
        ...
    @cache_dynamicpaint.setter
    def cache_dynamicpaint(self, value: bool):
        ...
    @property
    def cache_rigidbody(self) -> bool:
        """Show the active object's Rigid Body cache"""
        ...
    @cache_rigidbody.setter
    def cache_rigidbody(self, value: bool):
        ...
    @property
    def overlays(self) -> Annotated['SpaceDopeSheetOverlay', "is_animatable=False"]:
        """Settings for display of overlays"""
        ...