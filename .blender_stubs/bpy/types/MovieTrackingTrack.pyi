# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.MovieTrackingTrack.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .Annotation import Annotation
from .MovieTrackingMarker import MovieTrackingMarker
from .MovieTrackingMarkers import MovieTrackingMarkers
from .bpy_prop_collection import bpy_prop_collection

class MovieTrackingTrack(bpy_struct):

    name: Annotated[str, "is_animatable=False"]
    """Unique name of track"""
    frames_limit: Annotated[int, "step=1", "is_animatable=False"]
    """Every tracking cycle, this number of frames are tracked"""
    pattern_match: Annotated[Literal['KEYFRAME', 'PREV_FRAME'], "is_animatable=False"]
    """Track pattern from given frame when tracking marker to next frame"""
    margin: Annotated[int, "subtype='PIXEL'", "step=1", "is_animatable=False"]
    """Distance from image boundary at which marker stops tracking"""
    motion_model: Annotated[Literal['Perspective', 'Affine', 'LocRotScale', 'LocScale', 'LocRot', 'Loc'], "is_animatable=False"]
    """Default motion model to use for tracking"""
    correlation_min: Annotated[float, "step=0.05000000074505806", "precision=3", "is_animatable=False"]
    """Minimal value of correlation between matched pattern and reference that is still treated as successful tracking"""
    use_brute: Annotated[bool, "is_animatable=False"]
    """Use a brute-force translation only pre-track before refinement"""
    use_mask: bool
    """Use a Grease Pencil data-block as a mask to use only specified areas of pattern when tracking"""
    use_normalization: Annotated[bool, "is_animatable=False"]
    """Normalize light intensities while tracking (slower)"""
    @property
    def markers(self) -> Annotated['MovieTrackingMarkers', "is_animatable=False"]:
        """Collection of markers in track"""
        ...
    use_red_channel: Annotated[bool, "is_animatable=False"]
    """Use red channel from footage for tracking"""
    use_green_channel: Annotated[bool, "is_animatable=False"]
    """Use green channel from footage for tracking"""
    use_blue_channel: Annotated[bool, "is_animatable=False"]
    """Use blue channel from footage for tracking"""
    use_grayscale_preview: Annotated[bool, "is_animatable=False"]
    """Display what the tracking algorithm sees in the preview"""
    use_alpha_preview: Annotated[bool, "is_animatable=False"]
    """Apply track's mask on displaying preview"""
    @property
    def has_bundle(self) -> bool:
        """True if track has a valid bundle"""
        ...
    @property
    def bundle(self) -> Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=1.0", "precision=5"]:
        """Position of bundle reconstructed from this track"""
        ...
    hide: Annotated[bool, "is_animatable=False"]
    """Track is hidden"""
    select: bool
    """Track is selected"""
    select_anchor: bool
    """Track's anchor point is selected"""
    select_pattern: bool
    """Track's pattern area is selected"""
    select_search: bool
    """Track's search area is selected"""
    lock: Annotated[bool, "is_animatable=False"]
    """Track is locked and all changes to it are disabled"""
    use_custom_color: Annotated[bool, "is_animatable=False"]
    """Use custom color instead of theme-defined"""
    color: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    """Color of the track in the Movie Clip Editor and the 3D viewport after a solve"""
    @property
    def average_error(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Average error of re-projection"""
        ...
    annotation: Annotated[Optional['Annotation'], "is_animatable=False"]
    """Annotation data for this track"""
    weight: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Influence of this track on a final solution"""
    weight_stab: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Influence of this track on 2D stabilization"""
    offset: Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=1.0", "precision=5"]
    """Offset of track from the parenting point"""