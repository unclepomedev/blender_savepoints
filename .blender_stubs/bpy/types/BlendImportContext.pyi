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
from .BlendImportContextItem import BlendImportContextItem
from .BlendImportContextItems import BlendImportContextItems
class BlendImportContext(bpy_struct):
    @property
    def import_items(self) -> Annotated['BlendImportContextItems', "is_animatable=False"]:
        ...
    @property
    def options(self) -> set[str]:
        """Options for this blendfile import operation"""
        ...
    @property
    def process_stage(self) -> Literal['INIT', 'DONE']:
        """Current stage of the import process"""
        ...