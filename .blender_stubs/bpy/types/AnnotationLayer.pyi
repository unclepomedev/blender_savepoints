# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.AnnotationLayer.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .AnnotationFrame import AnnotationFrame
from .AnnotationFrames import AnnotationFrames
from .bpy_prop_collection import bpy_prop_collection

class AnnotationLayer(bpy_struct):

    @property
    def info(self) -> Annotated[str, "is_animatable=False"]:
        """Layer name"""
        ...
    @info.setter
    def info(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def frames(self) -> Annotated['AnnotationFrames', "is_animatable=False"]:
        """Sketches for this layer on different frames"""
        ...
    @property
    def active_frame(self) -> Annotated[Optional['AnnotationFrame'], "is_animatable=False"]:
        """Frame currently being displayed for this layer"""
        ...
    @property
    def annotation_opacity(self) -> Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]:
        """Annotation Layer Opacity"""
        ...
    @annotation_opacity.setter
    def annotation_opacity(self, value: Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def color(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Color for all strokes in this layer"""
        ...
    @color.setter
    def color(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def thickness(self) -> Annotated[int, "subtype='PIXEL'", "step=1", "is_animatable=False"]:
        """Thickness of annotation strokes"""
        ...
    @thickness.setter
    def thickness(self, value: Annotated[int, "subtype='PIXEL'", "step=1", "is_animatable=False"]):
        ...
    @property
    def use_annotation_onion_skinning(self) -> Annotated[bool, "is_animatable=False"]:
        """Display annotation onion skins before and after the current frame"""
        ...
    @use_annotation_onion_skinning.setter
    def use_annotation_onion_skinning(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def annotation_onion_before_range(self) -> Annotated[int, "step=1", "is_animatable=False"]:
        """Maximum number of frames to show before current frame"""
        ...
    @annotation_onion_before_range.setter
    def annotation_onion_before_range(self, value: Annotated[int, "step=1", "is_animatable=False"]):
        ...
    @property
    def annotation_onion_after_range(self) -> Annotated[int, "step=1", "is_animatable=False"]:
        """Maximum number of frames to show after current frame"""
        ...
    @annotation_onion_after_range.setter
    def annotation_onion_after_range(self, value: Annotated[int, "step=1", "is_animatable=False"]):
        ...
    @property
    def annotation_onion_before_color(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Base color for ghosts before the active frame"""
        ...
    @annotation_onion_before_color.setter
    def annotation_onion_before_color(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def annotation_onion_after_color(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Base color for ghosts after the active frame"""
        ...
    @annotation_onion_after_color.setter
    def annotation_onion_after_color(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def annotation_onion_use_custom_color(self) -> Annotated[bool, "is_animatable=False"]:
        """Use custom colors for onion skinning instead of the theme"""
        ...
    @annotation_onion_use_custom_color.setter
    def annotation_onion_use_custom_color(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def annotation_hide(self) -> Annotated[bool, "is_animatable=False"]:
        """Set annotation Visibility"""
        ...
    @annotation_hide.setter
    def annotation_hide(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def lock(self) -> bool:
        """Protect layer from further editing and/or frame changes"""
        ...
    @lock.setter
    def lock(self, value: bool):
        ...
    @property
    def lock_frame(self) -> Annotated[bool, "is_animatable=False"]:
        """Lock current frame displayed by layer"""
        ...
    @lock_frame.setter
    def lock_frame(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def is_ruler(self) -> bool:
        """This is a special ruler layer"""
        ...
    @property
    def select(self) -> bool:
        """Layer is selected for editing in the Dope Sheet"""
        ...
    @select.setter
    def select(self, value: bool):
        ...
    @property
    def show_in_front(self) -> bool:
        """Make the layer display in front of objects"""
        ...
    @show_in_front.setter
    def show_in_front(self, value: bool):
        ...