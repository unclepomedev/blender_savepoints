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

    info: Annotated[str, "is_animatable=False"]
    """Layer name"""
    @property
    def frames(self) -> Annotated['AnnotationFrames', "is_animatable=False"]:
        """Sketches for this layer on different frames"""
        ...
    @property
    def active_frame(self) -> Annotated[Optional['AnnotationFrame'], "is_animatable=False"]:
        """Frame currently being displayed for this layer"""
        ...
    annotation_opacity: Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]
    """Annotation Layer Opacity"""
    color: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3", "is_animatable=False"]
    """Color for all strokes in this layer"""
    thickness: Annotated[int, "subtype='PIXEL'", "step=1", "is_animatable=False"]
    """Thickness of annotation strokes"""
    use_annotation_onion_skinning: Annotated[bool, "is_animatable=False"]
    """Display annotation onion skins before and after the current frame"""
    annotation_onion_before_range: Annotated[int, "step=1", "is_animatable=False"]
    """Maximum number of frames to show before current frame"""
    annotation_onion_after_range: Annotated[int, "step=1", "is_animatable=False"]
    """Maximum number of frames to show after current frame"""
    annotation_onion_before_color: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3", "is_animatable=False"]
    """Base color for ghosts before the active frame"""
    annotation_onion_after_color: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3", "is_animatable=False"]
    """Base color for ghosts after the active frame"""
    annotation_onion_use_custom_color: Annotated[bool, "is_animatable=False"]
    """Use custom colors for onion skinning instead of the theme"""
    annotation_hide: Annotated[bool, "is_animatable=False"]
    """Set annotation Visibility"""
    lock: bool
    """Protect layer from further editing and/or frame changes"""
    lock_frame: Annotated[bool, "is_animatable=False"]
    """Lock current frame displayed by layer"""
    @property
    def is_ruler(self) -> bool:
        """This is a special ruler layer"""
        ...
    select: bool
    """Layer is selected for editing in the Dope Sheet"""
    show_in_front: bool
    """Make the layer display in front of objects"""