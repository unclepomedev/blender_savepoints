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
from .ID import ID
class KeyingSetPath(bpy_struct):
    id: Annotated[Optional['ID'], "is_animatable=False"]
    """ID-Block that keyframes for Keying Set should be added to (for Absolute Keying Sets only)"""
    id_type: Literal['ACTION', 'ARMATURE', 'BRUSH', 'CACHEFILE', 'CAMERA', 'COLLECTION', 'CURVE', 'CURVES', 'FONT', 'GREASEPENCIL', 'GREASEPENCIL_V3', 'IMAGE', 'KEY', 'LATTICE', 'LIBRARY', 'LIGHT', 'LIGHT_PROBE', 'LINESTYLE', 'MASK', 'MATERIAL', 'MESH', 'META', 'MOVIECLIP', 'NODETREE', 'OBJECT', 'PAINTCURVE', 'PALETTE', 'PARTICLE', 'POINTCLOUD', 'SCENE', 'SCREEN', 'SOUND', 'SPEAKER', 'TEXT', 'TEXTURE', 'VOLUME', 'WINDOWMANAGER', 'WORKSPACE', 'WORLD']
    """Type of ID-block that can be used"""
    group: Annotated[str, "is_animatable=False"]
    """Name of Action Group to assign setting(s) for this path to"""
    group_method: Literal['NAMED', 'NONE', 'KEYINGSET']
    """Method used to define which Group-name to use"""
    data_path: Annotated[str, "is_animatable=False"]
    """Path to property setting"""
    array_index: Annotated[int, "step=1"]
    """Index to the specific setting if applicable"""
    use_entire_array: bool
    """When an 'array/vector' type is chosen (Location, Rotation, Color, etc.), entire array is to be used"""
    use_insertkey_override_needed: bool
    """Override default setting to only insert keyframes where they're needed in the relevant F-Curves"""
    use_insertkey_override_visual: bool
    """Override default setting to insert keyframes based on 'visual transforms'"""
    use_insertkey_needed: bool
    """Only insert keyframes where they're needed in the relevant F-Curves"""
    use_insertkey_visual: bool
    """Insert keyframes based on 'visual transforms'"""