# Blender Probe Generated Stub for Blender 5.1.0 Alpha
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
from .ImageFormatSettings import ImageFormatSettings
class NodeCompositorFileOutputItem(bpy_struct):
    name: str
    socket_type: str
    vector_socket_dimensions: int
    color: list[float]
    override_node_format: bool
    save_as_render: bool
    format: 'ImageFormatSettings'