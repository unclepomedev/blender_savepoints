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
from .Object import Object
class BakeSettings(bpy_struct):
    type: str
    cage_object: 'Object'
    filepath: str
    width: int
    height: int
    margin: int
    margin_type: str
    max_ray_distance: float
    cage_extrusion: float
    normal_space: str
    normal_r: str
    normal_g: str
    normal_b: str
    image_settings: 'ImageFormatSettings'
    target: str
    save_mode: str
    view_from: str
    use_selected_to_active: bool
    use_clear: bool
    use_split_materials: bool
    use_automatic_name: bool
    use_cage: bool
    use_pass_emit: bool
    use_pass_direct: bool
    use_pass_indirect: bool
    use_pass_color: bool
    use_pass_diffuse: bool
    use_pass_glossy: bool
    use_pass_transmission: bool
    pass_filter: set[str]
    use_multires: bool
    use_lores_mesh: bool
    displacement_space: str