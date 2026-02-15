# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated
from .bpy_prop_collection import bpy_prop_collection

from .ViewerPathElem import ViewerPathElem
from .NodeTree import NodeTree
class EvaluateClosureNodeViewerPathElem(ViewerPathElem):
    @property
    def type(self) -> Literal['ID', 'MODIFIER', 'GROUP_NODE', 'SIMULATION_ZONE', 'VIEWER_NODE', 'REPEAT_ZONE', 'FOREACH_GEOMETRY_ELEMENT_ZONE', 'EVALUATE_CLOSURE']:
        """Type of the path element"""
        ...
    @property
    def ui_name(self) -> Annotated[str, "is_animatable=False"]:
        """Name that can be displayed in the UI for this element"""
        ...
    evaluate_node_id: Annotated[int, "step=1"]
    source_output_node_id: Annotated[int, "step=1"]
    @property
    def source_node_tree(self) -> Annotated[Optional['NodeTree'], "is_animatable=False"]:
        ...