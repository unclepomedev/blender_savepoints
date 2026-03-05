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

    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:
        """Unique name of track"""
        ...
    @name.setter
    def name(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def frames_limit(self) -> Annotated[int, "step=1", "is_animatable=False"]:
        """Every tracking cycle, this number of frames are tracked"""
        ...
    @frames_limit.setter
    def frames_limit(self, value: Annotated[int, "step=1", "is_animatable=False"]) -> None:
        ...
    @property
    def pattern_match(self) -> Annotated[Literal['KEYFRAME', 'PREV_FRAME'], "is_animatable=False"]:
        """Track pattern from given frame when tracking marker to next frame"""
        ...
    @pattern_match.setter
    def pattern_match(self, value: Annotated[Literal['KEYFRAME', 'PREV_FRAME'], "is_animatable=False"]) -> None:
        ...
    @property
    def margin(self) -> Annotated[int, "subtype='PIXEL'", "step=1", "is_animatable=False"]:
        """Distance from image boundary at which marker stops tracking"""
        ...
    @margin.setter
    def margin(self, value: Annotated[int, "subtype='PIXEL'", "step=1", "is_animatable=False"]) -> None:
        ...
    @property
    def motion_model(self) -> Annotated[Literal['Perspective', 'Affine', 'LocRotScale', 'LocScale', 'LocRot', 'Loc'], "is_animatable=False"]:
        """Default motion model to use for tracking"""
        ...
    @motion_model.setter
    def motion_model(self, value: Annotated[Literal['Perspective', 'Affine', 'LocRotScale', 'LocScale', 'LocRot', 'Loc'], "is_animatable=False"]) -> None:
        ...
    @property
    def correlation_min(self) -> Annotated[float, "step=0.05000000074505806", "precision=3", "is_animatable=False"]:
        """Minimal value of correlation between matched pattern and reference that is still treated as successful tracking"""
        ...
    @correlation_min.setter
    def correlation_min(self, value: Annotated[float, "step=0.05000000074505806", "precision=3", "is_animatable=False"]) -> None:
        ...
    @property
    def use_brute(self) -> Annotated[bool, "is_animatable=False"]:
        """Use a brute-force translation only pre-track before refinement"""
        ...
    @use_brute.setter
    def use_brute(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def use_mask(self) -> bool:
        """Use a Grease Pencil data-block as a mask to use only specified areas of pattern when tracking"""
        ...
    @use_mask.setter
    def use_mask(self, value: bool) -> None:
        ...
    @property
    def use_normalization(self) -> Annotated[bool, "is_animatable=False"]:
        """Normalize light intensities while tracking (slower)"""
        ...
    @use_normalization.setter
    def use_normalization(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def markers(self) -> Annotated['MovieTrackingMarkers', "is_animatable=False"]:
        """Collection of markers in track"""
        ...
    @property
    def use_red_channel(self) -> Annotated[bool, "is_animatable=False"]:
        """Use red channel from footage for tracking"""
        ...
    @use_red_channel.setter
    def use_red_channel(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def use_green_channel(self) -> Annotated[bool, "is_animatable=False"]:
        """Use green channel from footage for tracking"""
        ...
    @use_green_channel.setter
    def use_green_channel(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def use_blue_channel(self) -> Annotated[bool, "is_animatable=False"]:
        """Use blue channel from footage for tracking"""
        ...
    @use_blue_channel.setter
    def use_blue_channel(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def use_grayscale_preview(self) -> Annotated[bool, "is_animatable=False"]:
        """Display what the tracking algorithm sees in the preview"""
        ...
    @use_grayscale_preview.setter
    def use_grayscale_preview(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def use_alpha_preview(self) -> Annotated[bool, "is_animatable=False"]:
        """Apply track's mask on displaying preview"""
        ...
    @use_alpha_preview.setter
    def use_alpha_preview(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def has_bundle(self) -> bool:
        """True if track has a valid bundle"""
        ...
    @property
    def bundle(self) -> Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=1.0", "precision=5"]:
        """Position of bundle reconstructed from this track"""
        ...
    @property
    def hide(self) -> Annotated[bool, "is_animatable=False"]:
        """Track is hidden"""
        ...
    @hide.setter
    def hide(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def select(self) -> bool:
        """Track is selected"""
        ...
    @select.setter
    def select(self, value: bool) -> None:
        ...
    @property
    def select_anchor(self) -> bool:
        """Track's anchor point is selected"""
        ...
    @select_anchor.setter
    def select_anchor(self, value: bool) -> None:
        ...
    @property
    def select_pattern(self) -> bool:
        """Track's pattern area is selected"""
        ...
    @select_pattern.setter
    def select_pattern(self, value: bool) -> None:
        ...
    @property
    def select_search(self) -> bool:
        """Track's search area is selected"""
        ...
    @select_search.setter
    def select_search(self, value: bool) -> None:
        ...
    @property
    def lock(self) -> Annotated[bool, "is_animatable=False"]:
        """Track is locked and all changes to it are disabled"""
        ...
    @lock.setter
    def lock(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def use_custom_color(self) -> Annotated[bool, "is_animatable=False"]:
        """Use custom color instead of theme-defined"""
        ...
    @use_custom_color.setter
    def use_custom_color(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def color(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:
        """Color of the track in the Movie Clip Editor and the 3D viewport after a solve"""
        ...
    @color.setter
    def color(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def average_error(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Average error of re-projection"""
        ...
    @property
    def annotation(self) -> Annotated[Optional['Annotation'], "is_animatable=False"]:
        """Annotation data for this track"""
        ...
    @annotation.setter
    def annotation(self, value: Annotated[Optional['Annotation'], "is_animatable=False"]) -> None:
        ...
    @property
    def weight(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Influence of this track on a final solution"""
        ...
    @weight.setter
    def weight(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def weight_stab(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Influence of this track on 2D stabilization"""
        ...
    @weight_stab.setter
    def weight_stab(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def offset(self) -> Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=1.0", "precision=5"]:
        """Offset of track from the parenting point"""
        ...
    @offset.setter
    def offset(self, value: Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=1.0", "precision=5"]) -> None:
        ...