# Blender Probe Generated Stub for Blender 5.1.0 Alpha
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .SpreadsheetTableID import SpreadsheetTableID
from .ViewerPath import ViewerPath
class SpreadsheetTableIDGeometry(SpreadsheetTableID):
    type: str
    object_eval_state: str
    geometry_component_type: str
    attribute_domain: str
    geometry_item_type: str
    viewer_path: 'ViewerPath'
    layer_index: int