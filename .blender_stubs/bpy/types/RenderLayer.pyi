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
from .RenderPass import RenderPass
class RenderLayer(bpy_struct):
    name: str
    use_solid: bool
    use_sky: bool
    use_ao: bool
    use_strand: bool
    use_volumes: bool
    use_motion_blur: bool
    use_grease_pencil: bool
    use_pass_combined: bool
    use_pass_z: bool
    use_pass_vector: bool
    use_pass_position: bool
    use_pass_normal: bool
    use_pass_uv: bool
    use_pass_mist: bool
    use_pass_object_index: bool
    use_pass_material_index: bool
    use_pass_shadow: bool
    use_pass_ambient_occlusion: bool
    use_pass_emit: bool
    use_pass_environment: bool
    use_pass_diffuse_direct: bool
    use_pass_diffuse_indirect: bool
    use_pass_diffuse_color: bool
    use_pass_glossy_direct: bool
    use_pass_glossy_indirect: bool
    use_pass_glossy_color: bool
    use_pass_transmission_direct: bool
    use_pass_transmission_indirect: bool
    use_pass_transmission_color: bool
    use_pass_subsurface_direct: bool
    use_pass_subsurface_indirect: bool
    use_pass_subsurface_color: bool
    passes: bpy_prop_collection['RenderPass']
    def load_from_file(self, *args, **kwargs) -> Any: ...