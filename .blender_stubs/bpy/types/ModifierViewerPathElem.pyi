# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.ModifierViewerPathElem.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .ViewerPathElem import ViewerPathElem

class ModifierViewerPathElem(ViewerPathElem):

    @property
    def type(self) -> Literal['ID', 'MODIFIER', 'GROUP_NODE', 'SIMULATION_ZONE', 'VIEWER_NODE', 'REPEAT_ZONE', 'FOREACH_GEOMETRY_ELEMENT_ZONE', 'EVALUATE_CLOSURE']:
        """Type of the path element"""
        ...
    @property
    def ui_name(self) -> Annotated[str, "is_animatable=False"]:
        """Name that can be displayed in the UI for this element"""
        ...
    @property
    def modifier_uid(self) -> Annotated[int, "step=1"]:
        """The persistent UID of the modifier"""
        ...
    @modifier_uid.setter
    def modifier_uid(self, value: Annotated[int, "step=1"]) -> None:
        ...