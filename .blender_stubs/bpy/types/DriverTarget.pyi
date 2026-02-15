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

    id: Annotated[Optional['ID'], "is_animatable=False"]
    """ID-block that the specific property used can be found from (id_type property must be set first)"""
    id_type: Literal['ACTION', 'ARMATURE', 'BRUSH', 'CACHEFILE', 'CAMERA', 'COLLECTION', 'CURVE', 'CURVES', 'FONT', 'GREASEPENCIL', 'GREASEPENCIL_V3', 'IMAGE', 'KEY', 'LATTICE', 'LIBRARY', 'LIGHT', 'LIGHT_PROBE', 'LINESTYLE', 'MASK', 'MATERIAL', 'MESH', 'META', 'MOVIECLIP', 'NODETREE', 'OBJECT', 'PAINTCURVE', 'PALETTE', 'PARTICLE', 'POINTCLOUD', 'SCENE', 'SCREEN', 'SOUND', 'SPEAKER', 'TEXT', 'TEXTURE', 'VOLUME', 'WINDOWMANAGER', 'WORKSPACE', 'WORLD']
    """Type of ID-block that can be used"""
    data_path: Annotated[str, "is_animatable=False"]
    """RNA Path (from ID-block) to property used"""
    bone_target: Annotated[str, "is_animatable=False"]
    """Name of PoseBone to use as target"""
    transform_type: Literal['LOC_X', 'LOC_Y', 'LOC_Z', 'ROT_X', 'ROT_Y', 'ROT_Z', 'ROT_W', 'SCALE_X', 'SCALE_Y', 'SCALE_Z', 'SCALE_AVG']
    """Driver variable type"""
    rotation_mode: Literal['AUTO', 'XYZ', 'XZY', 'YXZ', 'YZX', 'ZXY', 'ZYX', 'QUATERNION', 'SWING_TWIST_X', 'SWING_TWIST_Y', 'SWING_TWIST_Z']
    """Mode for calculating rotation channel values"""
    transform_space: Literal['WORLD_SPACE', 'TRANSFORM_SPACE', 'LOCAL_SPACE']
    """Space in which transforms are used"""
    context_property: Literal['ACTIVE_SCENE', 'ACTIVE_VIEW_LAYER']
    """Type of a context-dependent data-block to access property from"""
    use_fallback_value: bool
    """Use the fallback value if the data path cannot be resolved, instead of failing to evaluate the driver"""
    fallback_value: Annotated[float, "step=10.0", "precision=3"]
    """The value to use if the data path cannot be resolved"""
    @property
    def is_fallback_used(self) -> bool:
        """Indicates that the most recent variable evaluation used the fallback value"""
        ...