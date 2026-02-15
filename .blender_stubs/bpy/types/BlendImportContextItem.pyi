# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.BlendImportContextItem.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .BlendImportContextLibraries import BlendImportContextLibraries
from .BlendImportContextLibrary import BlendImportContextLibrary
from .ID import ID
from .Library import Library
from .bpy_prop_collection import bpy_prop_collection

class BlendImportContextItem(bpy_struct):

    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:
        """ID name of the item"""
        ...
    @property
    def id_type(self) -> Literal['ACTION', 'ARMATURE', 'BRUSH', 'CACHEFILE', 'CAMERA', 'COLLECTION', 'CURVE', 'CURVES', 'FONT', 'GREASEPENCIL', 'GREASEPENCIL_V3', 'IMAGE', 'KEY', 'LATTICE', 'LIBRARY', 'LIGHT', 'LIGHT_PROBE', 'LINESTYLE', 'MASK', 'MATERIAL', 'MESH', 'META', 'MOVIECLIP', 'NODETREE', 'OBJECT', 'PAINTCURVE', 'PALETTE', 'PARTICLE', 'POINTCLOUD', 'SCENE', 'SCREEN', 'SOUND', 'SPEAKER', 'TEXT', 'TEXTURE', 'VOLUME', 'WINDOWMANAGER', 'WORKSPACE', 'WORLD']:
        """ID type of the item"""
        ...
    @property
    def source_libraries(self) -> Annotated['BlendImportContextLibraries', "is_animatable=False"]:
        """List of libraries to search and import that ID from. The ID will be imported from the first file in that list that contains it"""
        ...
    @property
    def append_action(self) -> Literal['UNSET', 'KEEP_LINKED', 'REUSE_LOCAL', 'MAKE_LOCAL', 'COPY_LOCAL']:
        """How this item has been handled by the append operation. Only set if the data has been appended"""
        ...
    @property
    def import_info(self) -> set[str]:
        """Various status info about an item after it has been imported"""
        ...
    @property
    def id(self) -> Annotated[Optional['ID'], "is_animatable=False"]:
        """The imported ID. None until it has been linked or appended. May be the same as ``reusable_local_id`` when appended"""
        ...
    @property
    def source_library(self) -> Annotated[Optional['Library'], "is_animatable=False"]:
        """Library ID representing the blendfile from which the ID was imported. None until the ID has been linked or appended"""
        ...
    @property
    def library_override_id(self) -> Annotated[Optional['ID'], "is_animatable=False"]:
        """The library override of the linked ID. None until it has been created"""
        ...
    @property
    def reusable_local_id(self) -> Annotated[Optional['ID'], "is_animatable=False"]:
        """The already existing local ID that may be reused in append & reuse case. None until it has been found"""
        ...