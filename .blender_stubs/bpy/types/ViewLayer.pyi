# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
from .AOV import AOV
from .Depsgraph import Depsgraph
from .FreestyleSettings import FreestyleSettings
from .LayerCollection import LayerCollection
from .Lightgroup import Lightgroup
from .Material import Material
from .Object import Object
from .ViewLayerEEVEE import ViewLayerEEVEE
from .World import World
class ViewLayer(bpy_struct):
    name: str
    material_override: 'Material'
    world_override: 'World'
    samples: int
    pass_alpha_threshold: float
    eevee: 'ViewLayerEEVEE'
    aovs: bpy_prop_collection['AOV']
    active_aov: 'AOV'
    active_aov_index: int
    lightgroups: bpy_prop_collection['Lightgroup']
    active_lightgroup: 'Lightgroup'
    active_lightgroup_index: int
    use_pass_cryptomatte_object: bool
    use_pass_cryptomatte_material: bool
    use_pass_cryptomatte_asset: bool
    pass_cryptomatte_depth: int
    use_pass_cryptomatte_accurate: bool
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
    layer_collection: 'LayerCollection'
    active_layer_collection: 'LayerCollection'
    objects: bpy_prop_collection['Object']
    use: bool
    has_export_collections: bool
    use_freestyle: bool
    freestyle_settings: 'FreestyleSettings'
    use_pass_grease_pencil: bool
    depsgraph: 'Depsgraph'
    cycles: 'CyclesRenderLayerSettings'
    def bl_system_properties_get(self, *args, **kwargs) -> Any: ...
    def update_render_passes(self, *args, **kwargs) -> Any: ...
    def update(self, *args, **kwargs) -> Any: ...