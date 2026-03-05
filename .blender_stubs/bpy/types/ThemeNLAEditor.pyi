# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.ThemeNLAEditor.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .ThemeSpaceGeneric import ThemeSpaceGeneric

class ThemeNLAEditor(bpy_struct):

    @property
    def space(self) -> Annotated['ThemeSpaceGeneric', "is_animatable=False"]:
        """Settings for space"""
        ...
    @property
    def grid(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:

        ...
    @grid.setter
    def grid(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]):
        ...
    @property
    def active_action(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:
        """Animation data-block has active action"""
        ...
    @active_action.setter
    def active_action(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]):
        ...
    @property
    def active_action_unset(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:
        """Animation data-block does not have active action"""
        ...
    @active_action_unset.setter
    def active_action_unset(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]):
        ...
    @property
    def strips(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:
        """Unselected Action-Clip Strip"""
        ...
    @strips.setter
    def strips(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]):
        ...
    @property
    def strips_selected(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:
        """Selected Action-Clip Strip"""
        ...
    @strips_selected.setter
    def strips_selected(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]):
        ...
    @property
    def transition_strips(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:
        """Unselected Transition Strip"""
        ...
    @transition_strips.setter
    def transition_strips(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]):
        ...
    @property
    def transition_strips_selected(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:
        """Selected Transition Strip"""
        ...
    @transition_strips_selected.setter
    def transition_strips_selected(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]):
        ...
    @property
    def meta_strips(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:
        """Unselected Meta Strip (for grouping related strips)"""
        ...
    @meta_strips.setter
    def meta_strips(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]):
        ...
    @property
    def meta_strips_selected(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:
        """Selected Meta Strip (for grouping related strips)"""
        ...
    @meta_strips_selected.setter
    def meta_strips_selected(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]):
        ...
    @property
    def sound_strips(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:
        """Unselected Sound Strip (for timing speaker sounds)"""
        ...
    @sound_strips.setter
    def sound_strips(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]):
        ...
    @property
    def sound_strips_selected(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:
        """Selected Sound Strip (for timing speaker sounds)"""
        ...
    @sound_strips_selected.setter
    def sound_strips_selected(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]):
        ...
    @property
    def tweak(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:
        """Color for strip/action being "tweaked" or edited"""
        ...
    @tweak.setter
    def tweak(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]):
        ...
    @property
    def tweak_duplicate(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:
        """Warning/error indicator color for strips referencing the strip being tweaked"""
        ...
    @tweak_duplicate.setter
    def tweak_duplicate(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]):
        ...
    @property
    def keyframe_border(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:
        """Color of keyframe border"""
        ...
    @keyframe_border.setter
    def keyframe_border(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]):
        ...
    @property
    def keyframe_border_selected(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:
        """Color of selected keyframe border"""
        ...
    @keyframe_border_selected.setter
    def keyframe_border_selected(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]):
        ...