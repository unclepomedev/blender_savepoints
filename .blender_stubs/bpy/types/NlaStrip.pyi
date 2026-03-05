# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.NlaStrip.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .Action import Action
from .ActionSlot import ActionSlot
from .FCurve import FCurve
from .FModifier import FModifier
from .NlaStripFCurves import NlaStripFCurves
from .bpy_prop_collection import bpy_prop_collection

class NlaStrip(bpy_struct):

    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:

        ...
    @name.setter
    def name(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def type(self) -> Literal['CLIP', 'TRANSITION', 'META', 'SOUND']:
        """Type of NLA Strip"""
        ...
    @property
    def extrapolation(self) -> Literal['NOTHING', 'HOLD', 'HOLD_FORWARD']:
        """Action to take for gaps past the strip extents"""
        ...
    @extrapolation.setter
    def extrapolation(self, value: Literal['NOTHING', 'HOLD', 'HOLD_FORWARD']) -> None:
        ...
    @property
    def blend_type(self) -> Literal['REPLACE', 'COMBINE', 'ADD', 'SUBTRACT', 'MULTIPLY']:
        """Method used for combining strip's result with accumulated result"""
        ...
    @blend_type.setter
    def blend_type(self, value: Literal['REPLACE', 'COMBINE', 'ADD', 'SUBTRACT', 'MULTIPLY']) -> None:
        ...
    @property
    def frame_start(self) -> Annotated[float, "subtype='TIME'", "unit='TIME'", "step=10.0", "precision=3"]:

        ...
    @frame_start.setter
    def frame_start(self, value: Annotated[float, "subtype='TIME'", "unit='TIME'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def frame_end(self) -> Annotated[float, "subtype='TIME'", "unit='TIME'", "step=10.0", "precision=3"]:

        ...
    @frame_end.setter
    def frame_end(self, value: Annotated[float, "subtype='TIME'", "unit='TIME'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def frame_start_raw(self) -> Annotated[float, "subtype='TIME'", "unit='TIME'", "step=10.0", "precision=3"]:
        """Same as frame_start, except that any value can be set, including ones that create an invalid state"""
        ...
    @frame_start_raw.setter
    def frame_start_raw(self, value: Annotated[float, "subtype='TIME'", "unit='TIME'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def frame_end_raw(self) -> Annotated[float, "subtype='TIME'", "unit='TIME'", "step=10.0", "precision=3"]:
        """Same as frame_end, except that any value can be set, including ones that create an invalid state"""
        ...
    @frame_end_raw.setter
    def frame_end_raw(self, value: Annotated[float, "subtype='TIME'", "unit='TIME'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def frame_start_ui(self) -> Annotated[float, "subtype='TIME'", "unit='TIME'", "step=10.0", "precision=3"]:
        """Start frame of the NLA strip. Note: changing this value also updates the value of the strip's end frame. If only the start frame should be changed, see the "frame_start" property instead."""
        ...
    @frame_start_ui.setter
    def frame_start_ui(self, value: Annotated[float, "subtype='TIME'", "unit='TIME'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def frame_end_ui(self) -> Annotated[float, "subtype='TIME'", "unit='TIME'", "step=10.0", "precision=3"]:
        """End frame of the NLA strip. Note: changing this value also updates the value of the strip's repeats or its action's end frame. If only the end frame should be changed, see the "frame_end" property instead."""
        ...
    @frame_end_ui.setter
    def frame_end_ui(self, value: Annotated[float, "subtype='TIME'", "unit='TIME'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def blend_in(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Number of frames at start of strip to fade in influence"""
        ...
    @blend_in.setter
    def blend_in(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def blend_out(self) -> Annotated[float, "step=10.0", "precision=3"]:

        ...
    @blend_out.setter
    def blend_out(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def use_auto_blend(self) -> bool:
        """Number of frames for Blending In/Out is automatically determined from overlapping strips"""
        ...
    @use_auto_blend.setter
    def use_auto_blend(self, value: bool) -> None:
        ...
    @property
    def action(self) -> Annotated[Optional['Action'], "is_animatable=False"]:
        """Action referenced by this strip"""
        ...
    @action.setter
    def action(self, value: Annotated[Optional['Action'], "is_animatable=False"]) -> None:
        ...
    @property
    def action_slot_handle(self) -> Annotated[int, "step=1"]:
        """A number that identifies which sub-set of the Action is considered to be for this NLA strip"""
        ...
    @action_slot_handle.setter
    def action_slot_handle(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def last_slot_identifier(self) -> Annotated[str, "is_animatable=False"]:
        """The identifier of the most recently assigned action slot. The slot identifies which sub-set of the Action is considered to be for this strip, and its identifier is used to find the right slot when assigning an Action."""
        ...
    @last_slot_identifier.setter
    def last_slot_identifier(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def action_slot(self) -> Annotated[Optional['ActionSlot'], "is_animatable=False"]:
        """The slot identifies which sub-set of the Action is considered to be for this strip, and its name is used to find the right slot when assigning another Action"""
        ...
    @action_slot.setter
    def action_slot(self, value: Annotated[Optional['ActionSlot'], "is_animatable=False"]) -> None:
        ...
    @property
    def action_suitable_slots(self) -> Annotated[bpy_prop_collection['ActionSlot'], "is_animatable=False"]:
        """The list of action slots suitable for this NLA strip"""
        ...
    @property
    def action_frame_start(self) -> Annotated[float, "subtype='TIME'", "unit='TIME'", "step=10.0", "precision=3"]:
        """First frame from action to use"""
        ...
    @action_frame_start.setter
    def action_frame_start(self, value: Annotated[float, "subtype='TIME'", "unit='TIME'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def action_frame_end(self) -> Annotated[float, "subtype='TIME'", "unit='TIME'", "step=10.0", "precision=3"]:
        """Last frame from action to use"""
        ...
    @action_frame_end.setter
    def action_frame_end(self, value: Annotated[float, "subtype='TIME'", "unit='TIME'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def repeat(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Number of times to repeat the action range"""
        ...
    @repeat.setter
    def repeat(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def scale(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Scaling factor for action"""
        ...
    @scale.setter
    def scale(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
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
    @property
    def influence(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Amount the strip contributes to the current result"""
        ...
    @influence.setter
    def influence(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def strip_time(self) -> Annotated[float, "subtype='TIME'", "unit='TIME'", "step=10.0", "precision=3"]:
        """Frame of referenced Action to evaluate"""
        ...
    @strip_time.setter
    def strip_time(self, value: Annotated[float, "subtype='TIME'", "unit='TIME'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def use_animated_influence(self) -> bool:
        """Influence setting is controlled by an F-Curve rather than automatically determined"""
        ...
    @use_animated_influence.setter
    def use_animated_influence(self, value: bool) -> None:
        ...
    @property
    def use_animated_time(self) -> bool:
        """Strip time is controlled by an F-Curve rather than automatically determined"""
        ...
    @use_animated_time.setter
    def use_animated_time(self, value: bool) -> None:
        ...
    @property
    def use_animated_time_cyclic(self) -> bool:
        """Cycle the animated time within the action start and end"""
        ...
    @use_animated_time_cyclic.setter
    def use_animated_time_cyclic(self, value: bool) -> None:
        ...
    @property
    def active(self) -> bool:
        """NLA Strip is active"""
        ...
    @property
    def select(self) -> bool:
        """NLA Strip is selected"""
        ...
    @select.setter
    def select(self, value: bool) -> None:
        ...
    @property
    def mute(self) -> bool:
        """Disable NLA Strip evaluation"""
        ...
    @mute.setter
    def mute(self, value: bool) -> None:
        ...
    @property
    def use_reverse(self) -> bool:
        """NLA Strip is played back in reverse order (only when timing is automatically determined)"""
        ...
    @use_reverse.setter
    def use_reverse(self, value: bool) -> None:
        ...
    @property
    def use_sync_length(self) -> bool:
        """Update range of frames referenced from action after tweaking strip and its keyframes"""
        ...
    @use_sync_length.setter
    def use_sync_length(self, value: bool) -> None:
        ...