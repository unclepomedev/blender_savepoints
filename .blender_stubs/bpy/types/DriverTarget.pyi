# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.DriverTarget.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .ID import ID

class DriverTarget(bpy_struct):

    @property
    def id(self) -> Annotated[Optional['ID'], "is_animatable=False"]:
        """ID-block that the specific property used can be found from (id_type property must be set first)"""
        ...
    @id.setter
    def id(self, value: Annotated[Optional['ID'], "is_animatable=False"]):
        ...
    @property
    def id_type(self) -> Literal['ACTION', 'ARMATURE', 'BRUSH', 'CACHEFILE', 'CAMERA', 'COLLECTION', 'CURVE', 'CURVES', 'FONT', 'GREASEPENCIL', 'GREASEPENCIL_V3', 'IMAGE', 'KEY', 'LATTICE', 'LIBRARY', 'LIGHT', 'LIGHT_PROBE', 'LINESTYLE', 'MASK', 'MATERIAL', 'MESH', 'META', 'MOVIECLIP', 'NODETREE', 'OBJECT', 'PAINTCURVE', 'PALETTE', 'PARTICLE', 'POINTCLOUD', 'SCENE', 'SCREEN', 'SOUND', 'SPEAKER', 'TEXT', 'TEXTURE', 'VOLUME', 'WINDOWMANAGER', 'WORKSPACE', 'WORLD']:
        """Type of ID-block that can be used"""
        ...
    @id_type.setter
    def id_type(self, value: Literal['ACTION', 'ARMATURE', 'BRUSH', 'CACHEFILE', 'CAMERA', 'COLLECTION', 'CURVE', 'CURVES', 'FONT', 'GREASEPENCIL', 'GREASEPENCIL_V3', 'IMAGE', 'KEY', 'LATTICE', 'LIBRARY', 'LIGHT', 'LIGHT_PROBE', 'LINESTYLE', 'MASK', 'MATERIAL', 'MESH', 'META', 'MOVIECLIP', 'NODETREE', 'OBJECT', 'PAINTCURVE', 'PALETTE', 'PARTICLE', 'POINTCLOUD', 'SCENE', 'SCREEN', 'SOUND', 'SPEAKER', 'TEXT', 'TEXTURE', 'VOLUME', 'WINDOWMANAGER', 'WORKSPACE', 'WORLD']):
        ...
    @property
    def data_path(self) -> Annotated[str, "is_animatable=False"]:
        """RNA Path (from ID-block) to property used"""
        ...
    @data_path.setter
    def data_path(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def bone_target(self) -> Annotated[str, "is_animatable=False"]:
        """Name of PoseBone to use as target"""
        ...
    @bone_target.setter
    def bone_target(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def transform_type(self) -> Literal['LOC_X', 'LOC_Y', 'LOC_Z', 'ROT_X', 'ROT_Y', 'ROT_Z', 'ROT_W', 'SCALE_X', 'SCALE_Y', 'SCALE_Z', 'SCALE_AVG']:
        """Driver variable type"""
        ...
    @transform_type.setter
    def transform_type(self, value: Literal['LOC_X', 'LOC_Y', 'LOC_Z', 'ROT_X', 'ROT_Y', 'ROT_Z', 'ROT_W', 'SCALE_X', 'SCALE_Y', 'SCALE_Z', 'SCALE_AVG']):
        ...
    @property
    def rotation_mode(self) -> Literal['AUTO', 'XYZ', 'XZY', 'YXZ', 'YZX', 'ZXY', 'ZYX', 'QUATERNION', 'SWING_TWIST_X', 'SWING_TWIST_Y', 'SWING_TWIST_Z']:
        """Mode for calculating rotation channel values"""
        ...
    @rotation_mode.setter
    def rotation_mode(self, value: Literal['AUTO', 'XYZ', 'XZY', 'YXZ', 'YZX', 'ZXY', 'ZYX', 'QUATERNION', 'SWING_TWIST_X', 'SWING_TWIST_Y', 'SWING_TWIST_Z']):
        ...
    @property
    def transform_space(self) -> Literal['WORLD_SPACE', 'TRANSFORM_SPACE', 'LOCAL_SPACE']:
        """Space in which transforms are used"""
        ...
    @transform_space.setter
    def transform_space(self, value: Literal['WORLD_SPACE', 'TRANSFORM_SPACE', 'LOCAL_SPACE']):
        ...
    @property
    def context_property(self) -> Literal['ACTIVE_SCENE', 'ACTIVE_VIEW_LAYER']:
        """Type of a context-dependent data-block to access property from"""
        ...
    @context_property.setter
    def context_property(self, value: Literal['ACTIVE_SCENE', 'ACTIVE_VIEW_LAYER']):
        ...
    @property
    def use_fallback_value(self) -> bool:
        """Use the fallback value if the data path cannot be resolved, instead of failing to evaluate the driver"""
        ...
    @use_fallback_value.setter
    def use_fallback_value(self, value: bool):
        ...
    @property
    def fallback_value(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """The value to use if the data path cannot be resolved"""
        ...
    @fallback_value.setter
    def fallback_value(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def is_fallback_used(self) -> bool:
        """Indicates that the most recent variable evaluation used the fallback value"""
        ...