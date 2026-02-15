# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.IDViewerPathElem.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .ViewerPathElem import ViewerPathElem
from .ID import ID

class IDViewerPathElem(ViewerPathElem):

    @property
    def type(self) -> Literal['ID', 'MODIFIER', 'GROUP_NODE', 'SIMULATION_ZONE', 'VIEWER_NODE', 'REPEAT_ZONE', 'FOREACH_GEOMETRY_ELEMENT_ZONE', 'EVALUATE_CLOSURE']:
        """Type of the path element"""
        ...
    @property
    def ui_name(self) -> Annotated[str, "is_animatable=False"]:
        """Name that can be displayed in the UI for this element"""
        ...
    @property
    def id(self) -> Annotated[Optional['ID'], "is_animatable=False"]:

        ...