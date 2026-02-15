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
from .Action import Action
from .ActionSlot import ActionSlot
from .FCurve import FCurve
from .FModifier import FModifier
from .NlaStripFCurves import NlaStripFCurves
class NlaStrip(bpy_struct):
    name: Annotated[str, "is_animatable=False"]
    @property
    def type(self) -> Literal['CLIP', 'TRANSITION', 'META', 'SOUND']:
        """Type of NLA Strip"""
        ...
    extrapolation: Literal['NOTHING', 'HOLD', 'HOLD_FORWARD']
    """Action to take for gaps past the strip extents"""
    blend_type: Literal['REPLACE', 'COMBINE', 'ADD', 'SUBTRACT', 'MULTIPLY']
    """Method used for combining strip's result with accumulated result"""
    frame_start: Annotated[float, "subtype='TIME'", "unit='TIME'", "step=10.0", "precision=3"]
    frame_end: Annotated[float, "subtype='TIME'", "unit='TIME'", "step=10.0", "precision=3"]
    frame_start_raw: Annotated[float, "subtype='TIME'", "unit='TIME'", "step=10.0", "precision=3"]
    """Same as frame_start, except that any value can be set, including ones that create an invalid state"""
    frame_end_raw: Annotated[float, "subtype='TIME'", "unit='TIME'", "step=10.0", "precision=3"]
    """Same as frame_end, except that any value can be set, including ones that create an invalid state"""
    frame_start_ui: Annotated[float, "subtype='TIME'", "unit='TIME'", "step=10.0", "precision=3"]
    """Start frame of the NLA strip. Note: changing this value also updates the value of the strip's end frame. If only the start frame should be changed, see the "frame_start" property instead."""
    frame_end_ui: Annotated[float, "subtype='TIME'", "unit='TIME'", "step=10.0", "precision=3"]
    """End frame of the NLA strip. Note: changing this value also updates the value of the strip's repeats or its action's end frame. If only the end frame should be changed, see the "frame_end" property instead."""
    blend_in: Annotated[float, "step=10.0", "precision=3"]
    """Number of frames at start of strip to fade in influence"""
    blend_out: Annotated[float, "step=10.0", "precision=3"]
    use_auto_blend: bool
    """Number of frames for Blending In/Out is automatically determined from overlapping strips"""
    action: Annotated[Optional['Action'], "is_animatable=False"]
    """Action referenced by this strip"""
    action_slot_handle: Annotated[int, "step=1"]
    """A number that identifies which sub-set of the Action is considered to be for this NLA strip"""
    last_slot_identifier: Annotated[str, "is_animatable=False"]
    """The identifier of the most recently assigned action slot. The slot identifies which sub-set of the Action is considered to be for this strip, and its identifier is used to find the right slot when assigning an Action."""
    action_slot: Annotated[Optional['ActionSlot'], "is_animatable=False"]
    """The slot identifies which sub-set of the Action is considered to be for this strip, and its name is used to find the right slot when assigning another Action"""
    @property
    def action_suitable_slots(self) -> Annotated[bpy_prop_collection['ActionSlot'], "is_animatable=False"]:
        """The list of action slots suitable for this NLA strip"""
        ...
    action_frame_start: Annotated[float, "subtype='TIME'", "unit='TIME'", "step=10.0", "precision=3"]
    """First frame from action to use"""
    action_frame_end: Annotated[float, "subtype='TIME'", "unit='TIME'", "step=10.0", "precision=3"]
    """Last frame from action to use"""
    repeat: Annotated[float, "step=10.0", "precision=3"]
    """Number of times to repeat the action range"""
    scale: Annotated[float, "step=10.0", "precision=3"]
    """Scaling factor for action"""
    @property
    def fcurves(self) -> Annotated['NlaStripFCurves', "is_animatable=False"]:
        """F-Curves for controlling the strip's influence and timing"""
        ...
    @property
    def modifiers(self) -> Annotated[bpy_prop_collection['FModifier'], "is_animatable=False"]:
        """Modifiers affecting all the F-Curves in the referenced Action"""
        ...
    @property
    def strips(self) -> Annotated[bpy_prop_collection['NlaStrip'], "is_animatable=False"]:
        """NLA Strips that this strip acts as a container for (if it is of type Meta)"""
        ...
    influence: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Amount the strip contributes to the current result"""
    strip_time: Annotated[float, "subtype='TIME'", "unit='TIME'", "step=10.0", "precision=3"]
    """Frame of referenced Action to evaluate"""
    use_animated_influence: bool
    """Influence setting is controlled by an F-Curve rather than automatically determined"""
    use_animated_time: bool
    """Strip time is controlled by an F-Curve rather than automatically determined"""
    use_animated_time_cyclic: bool
    """Cycle the animated time within the action start and end"""
    @property
    def active(self) -> bool:
        """NLA Strip is active"""
        ...
    select: bool
    """NLA Strip is selected"""
    mute: bool
    """Disable NLA Strip evaluation"""
    use_reverse: bool
    """NLA Strip is played back in reverse order (only when timing is automatically determined)"""
    use_sync_length: bool
    """Update range of frames referenced from action after tweaking strip and its keyframes"""