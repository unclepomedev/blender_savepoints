# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.SpreadsheetTableIDGeometry.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .SpreadsheetTableID import SpreadsheetTableID
from .ViewerPath import ViewerPath

class SpreadsheetTableIDGeometry(SpreadsheetTableID):

    @property
    def type(self) -> Literal['GEOMETRY']:
        """The type of the table identifier"""
        ...
    @property
    def object_eval_state(self) -> Literal['EVALUATED', 'ORIGINAL', 'VIEWER_NODE']:

        ...
    @property
    def geometry_component_type(self) -> Literal['MESH', 'POINTCLOUD', 'CURVE', 'INSTANCES', 'GREASEPENCIL']:
        """Part of the geometry to display data from"""
        ...
    @property
    def attribute_domain(self) -> Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER']:
        """Attribute domain to display"""
        ...
    @property
    def viewer_path(self) -> Annotated[Optional['ViewerPath'], "is_animatable=False"]:
        """Path to the data that is displayed"""
        ...
    @property
    def layer_index(self) -> Annotated[int, "step=1"]:
        """Index of the Grease Pencil layer"""
        ...