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
from .AOV import AOV
from .AOVs import AOVs
from .Depsgraph import Depsgraph
from .FreestyleSettings import FreestyleSettings
from .LayerCollection import LayerCollection
from .LayerObjects import LayerObjects
from .Lightgroup import Lightgroup
from .Lightgroups import Lightgroups
from .Material import Material
from .Object import Object
from .ViewLayerEEVEE import ViewLayerEEVEE
from .World import World
class ViewLayer(bpy_struct):
    name: Annotated[str, "is_animatable=False"]
    """View layer name"""
    material_override: Annotated[Optional['Material'], "is_animatable=False"]
    """Material to override all other materials in this view layer"""
    world_override: Annotated[Optional['World'], "is_animatable=False"]
    """Override world in this view layer"""
    samples: Annotated[int, "subtype='UNSIGNED'", "step=1"]
    """Override number of render samples for this view layer, 0 will use the scene setting"""
    pass_alpha_threshold: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Z, Index, normal, UV and vector passes are only affected by surfaces with alpha transparency equal to or higher than this threshold"""
    @property
    def eevee(self) -> Annotated['ViewLayerEEVEE', "is_animatable=False"]:
        """View layer settings for EEVEE"""
        ...
    @property
    def aovs(self) -> Annotated['AOVs', "is_animatable=False"]:
        ...
    @property
    def active_aov(self) -> Annotated[Optional['AOV'], "is_animatable=False"]:
        """Active AOV"""
        ...
    active_aov_index: Annotated[int, "subtype='UNSIGNED'", "step=1"]
    """Index of active AOV"""
    @property
    def lightgroups(self) -> Annotated['Lightgroups', "is_animatable=False"]:
        ...
    @property
    def active_lightgroup(self) -> Annotated[Optional['Lightgroup'], "is_animatable=False"]:
        """Active Lightgroup"""
        ...
    active_lightgroup_index: Annotated[int, "subtype='UNSIGNED'", "step=1"]
    """Index of active lightgroup"""
    use_pass_cryptomatte_object: bool
    """Render cryptomatte object pass, for isolating objects in compositing"""
    use_pass_cryptomatte_material: bool
    """Render cryptomatte material pass, for isolating materials in compositing"""
    use_pass_cryptomatte_asset: bool
    """Render cryptomatte asset pass, for isolating groups of objects with the same parent"""
    pass_cryptomatte_depth: Annotated[int, "step=2"]
    """Sets how many unique objects can be distinguished per pixel"""
    use_pass_cryptomatte_accurate: bool
    """Generate a more accurate cryptomatte pass"""
    use_solid: bool
    """Render Solid faces in this Layer"""
    use_sky: bool
    """Render Sky in this Layer"""
    use_ao: bool
    """Render Ambient Occlusion in this Layer"""
    use_strand: bool
    """Render Strands in this Layer"""
    use_volumes: bool
    """Render volumes in this Layer"""
    use_motion_blur: bool
    """Render motion blur in this Layer, if enabled in the scene"""
    use_grease_pencil: bool
    """Render Grease Pencil on this layer"""
    use_pass_combined: bool
    """Deliver full combined RGBA buffer"""
    use_pass_z: bool
    """Deliver depth values pass"""
    use_pass_vector: bool
    """Deliver speed vector pass"""
    use_pass_position: bool
    """Deliver position pass"""
    use_pass_normal: bool
    """Deliver normal pass"""
    use_pass_uv: bool
    """Deliver texture UV pass"""
    use_pass_mist: bool
    """Deliver mist factor pass (0.0 to 1.0)"""
    use_pass_object_index: bool
    """Deliver object index pass"""
    use_pass_material_index: bool
    """Deliver material index pass"""
    use_pass_shadow: bool
    """Deliver shadow pass"""
    use_pass_ambient_occlusion: bool
    """Deliver Ambient Occlusion pass"""
    use_pass_emit: bool
    """Deliver emission pass"""
    use_pass_environment: bool
    """Deliver environment lighting pass"""
    use_pass_diffuse_direct: bool
    """Deliver diffuse direct pass"""
    use_pass_diffuse_indirect: bool
    """Deliver diffuse indirect pass"""
    use_pass_diffuse_color: bool
    """Deliver diffuse color pass"""
    use_pass_glossy_direct: bool
    """Deliver glossy direct pass"""
    use_pass_glossy_indirect: bool
    """Deliver glossy indirect pass"""
    use_pass_glossy_color: bool
    """Deliver glossy color pass"""
    use_pass_transmission_direct: bool
    """Deliver transmission direct pass"""
    use_pass_transmission_indirect: bool
    """Deliver transmission indirect pass"""
    use_pass_transmission_color: bool
    """Deliver transmission color pass"""
    use_pass_subsurface_direct: bool
    """Deliver subsurface direct pass"""
    use_pass_subsurface_indirect: bool
    """Deliver subsurface indirect pass"""
    use_pass_subsurface_color: bool
    """Deliver subsurface color pass"""
    @property
    def layer_collection(self) -> Annotated['LayerCollection', "is_animatable=False"]:
        """Root of collections hierarchy of this view layer, its 'collection' pointer property is the same as the scene's master collection"""
        ...
    active_layer_collection: Annotated['LayerCollection', "is_animatable=False"]
    """Active layer collection in this view layer's hierarchy"""
    @property
    def objects(self) -> Annotated['LayerObjects', "is_animatable=False"]:
        """All the objects in this layer"""
        ...
    use: bool
    """Enable or disable rendering of this View Layer"""
    @property
    def has_export_collections(self) -> bool:
        """At least one Collection in this View Layer has an exporter"""
        ...
    use_freestyle: bool
    """Render stylized strokes in this Layer"""
    @property
    def freestyle_settings(self) -> Annotated['FreestyleSettings', "is_animatable=False"]:
        ...
    use_pass_grease_pencil: bool
    """Deliver Grease Pencil render result in a separate pass"""
    @property
    def depsgraph(self) -> Annotated[Optional['Depsgraph'], "is_animatable=False"]:
        """Dependencies in the scene data"""
        ...
    @property
    def cycles(self) -> Annotated[Optional['CyclesRenderLayerSettings'], "is_animatable=False"]:
        """Cycles ViewLayer Settings"""
        ...
    def bl_system_properties_get(self, *args, **kwargs) -> Any: ...
    def update_render_passes(self, *args, **kwargs) -> Any: ...
    def update(self, *args, **kwargs) -> Any: ...