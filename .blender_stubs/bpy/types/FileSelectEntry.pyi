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
from .AssetMetaData import AssetMetaData
class FileSelectEntry(bpy_struct):
    @property
    def name(self) -> Annotated[str, "subtype='FILE_NAME'", "is_animatable=False"]:
        ...
    @property
    def relative_path(self) -> Annotated[str, "subtype='FILE_PATH'", "is_animatable=False"]:
        """Path relative to the directory currently displayed in the File Browser (includes the file name)"""
        ...
    @property
    def preview_icon_id(self) -> Annotated[int, "step=1"]:
        """Unique integer identifying the preview of this file as an icon (zero means invalid)"""
        ...
    @property
    def asset_data(self) -> Annotated[Optional['AssetMetaData'], "is_animatable=False"]:
        """Asset data, valid if the file represents an asset"""
        ...