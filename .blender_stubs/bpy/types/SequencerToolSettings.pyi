# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
class SequencerToolSettings(bpy_struct):
    fit_method: Annotated[Literal['FIT', 'FILL', 'STRETCH', 'ORIGINAL'], "is_animatable=False"]
    """Scale fit method"""
    snap_to_current_frame: Annotated[bool, "is_animatable=False"]
    """Snap to current frame"""
    snap_to_hold_offset: Annotated[bool, "is_animatable=False"]
    """Snap to strip hold offsets"""
    snap_to_markers: Annotated[bool, "is_animatable=False"]
    """Snap to markers"""
    snap_to_retiming_keys: Annotated[bool, "is_animatable=False"]
    """Snap to retiming keys"""
    snap_to_frame_range: Annotated[bool, "is_animatable=False"]
    """Snap to preview or scene start and end frame"""
    snap_to_borders: Annotated[bool, "is_animatable=False"]
    """Snap to preview borders"""
    snap_to_center: Annotated[bool, "is_animatable=False"]
    """Snap to preview center"""
    snap_to_strips_preview: Annotated[bool, "is_animatable=False"]
    """Snap to borders and origins of deselected, visible strips"""
    snap_ignore_muted: Annotated[bool, "is_animatable=False"]
    """Don't snap to hidden strips"""
    snap_ignore_sound: Annotated[bool, "is_animatable=False"]
    """Don't snap to sound strips"""
    use_snap_current_frame_to_strips: Annotated[bool, "is_animatable=False"]
    """Snap current frame to strip start or end"""
    snap_distance: Annotated[int, "subtype='PIXEL'", "step=1", "is_animatable=False"]
    """Maximum distance for snapping in pixels"""
    overlap_mode: Annotated[Literal['EXPAND', 'OVERWRITE', 'SHUFFLE'], "is_animatable=False"]
    """How to resolve overlap after transformation"""
    pivot_point: Annotated[Literal['CENTER', 'MEDIAN', 'CURSOR', 'INDIVIDUAL_ORIGINS'], "is_animatable=False"]
    """Rotation or scaling pivot point"""