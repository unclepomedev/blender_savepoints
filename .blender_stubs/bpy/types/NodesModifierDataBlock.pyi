# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.NodesModifierDataBlock.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .ID import ID

class NodesModifierDataBlock(bpy_struct):

    @property
    def id_name(self) -> Annotated[str, "is_animatable=False"]:
        """Name that is mapped to the referenced data-block"""
        ...
    @property
    def lib_name(self) -> Annotated[str, "is_animatable=False"]:
        """Used when the data block is not local to the current .blend file but is linked from some library"""
        ...
    @property
    def id(self) -> Annotated[Optional['ID'], "is_animatable=False"]:

        ...
    @id.setter
    def id(self, value: Annotated[Optional['ID'], "is_animatable=False"]) -> None:
        ...
    @property
    def id_type(self) -> Annotated[Literal['ACTION', 'ARMATURE', 'BRUSH', 'CACHEFILE', 'CAMERA', 'COLLECTION', 'CURVE', 'CURVES', 'FONT', 'GREASEPENCIL', 'GREASEPENCIL_V3', 'IMAGE', 'KEY', 'LATTICE', 'LIBRARY', 'LIGHT', 'LIGHT_PROBE', 'LINESTYLE', 'MASK', 'MATERIAL', 'MESH', 'META', 'MOVIECLIP', 'NODETREE', 'OBJECT', 'PAINTCURVE', 'PALETTE', 'PARTICLE', 'POINTCLOUD', 'SCENE', 'SCREEN', 'SOUND', 'SPEAKER', 'TEXT', 'TEXTURE', 'VOLUME', 'WINDOWMANAGER', 'WORKSPACE', 'WORLD'], "is_animatable=False"]:

        ...