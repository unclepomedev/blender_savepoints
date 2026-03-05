# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.ThemeInfo.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .ThemeSpaceGeneric import ThemeSpaceGeneric

class ThemeInfo(bpy_struct):

    @property
    def space(self) -> Annotated['ThemeSpaceGeneric', "is_animatable=False"]:
        """Settings for space"""
        ...
    @property
    def info_selected(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:
        """Background color of selected line"""
        ...
    @info_selected.setter
    def info_selected(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def info_selected_text(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:
        """Text color of selected line"""
        ...
    @info_selected_text.setter
    def info_selected_text(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def info_error_text(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:
        """Foreground color of Error icon"""
        ...
    @info_error_text.setter
    def info_error_text(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def info_warning_text(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:
        """Foreground color of Warning icon"""
        ...
    @info_warning_text.setter
    def info_warning_text(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def info_info_text(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:
        """Foreground color of Info icon"""
        ...
    @info_info_text.setter
    def info_info_text(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def info_debug(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:
        """Background color of Debug icon"""
        ...
    @info_debug.setter
    def info_debug(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def info_debug_text(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:
        """Foreground color of Debug icon"""
        ...
    @info_debug_text.setter
    def info_debug_text(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def info_property(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:
        """Background color of Property icon"""
        ...
    @info_property.setter
    def info_property(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def info_property_text(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:
        """Foreground color of Property icon"""
        ...
    @info_property_text.setter
    def info_property_text(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def info_operator(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:
        """Background color of Operator icon"""
        ...
    @info_operator.setter
    def info_operator(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def info_operator_text(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:
        """Foreground color of Operator icon"""
        ...
    @info_operator_text.setter
    def info_operator_text(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]) -> None:
        ...