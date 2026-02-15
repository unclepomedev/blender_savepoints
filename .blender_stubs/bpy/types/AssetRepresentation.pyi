# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.AssetRepresentation.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .AssetMetaData import AssetMetaData
from .ID import ID

class AssetRepresentation(bpy_struct):

    @property
    def name(self) -> Annotated[str, "subtype='FILE_NAME'", "is_animatable=False"]:

        ...
    @property
    def metadata(self) -> Annotated[Optional['AssetMetaData'], "is_animatable=False"]:
        """Additional information about the asset"""
        ...
    @property
    def id_type(self) -> Annotated[Literal['ACTION', 'ARMATURE', 'BRUSH', 'CACHEFILE', 'CAMERA', 'COLLECTION', 'CURVE', 'CURVES', 'FONT', 'GREASEPENCIL', 'GREASEPENCIL_V3', 'IMAGE', 'KEY', 'LATTICE', 'LIBRARY', 'LIGHT', 'LIGHT_PROBE', 'LINESTYLE', 'MASK', 'MATERIAL', 'MESH', 'META', 'MOVIECLIP', 'NODETREE', 'OBJECT', 'PAINTCURVE', 'PALETTE', 'PARTICLE', 'POINTCLOUD', 'SCENE', 'SCREEN', 'SOUND', 'SPEAKER', 'TEXT', 'TEXTURE', 'VOLUME', 'WINDOWMANAGER', 'WORKSPACE', 'WORLD'], "is_animatable=False"]:
        """The type of the data-block, if the asset represents one ('NONE' otherwise)"""
        ...
    @property
    def local_id(self) -> Annotated[Optional['ID'], "is_animatable=False"]:
        """The local data-block this asset represents; only valid if that is a data-block in this file"""
        ...
    @property
    def full_library_path(self) -> Annotated[str, "subtype='FILE_NAME'", "is_animatable=False"]:
        """Absolute path to the .blend file containing this asset"""
        ...
    @property
    def full_path(self) -> Annotated[str, "subtype='FILE_NAME'", "is_animatable=False"]:
        """Absolute path to the .blend file containing this asset extended with the path of the asset inside the file"""
        ...