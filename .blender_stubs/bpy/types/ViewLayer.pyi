# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.ViewLayer.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

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
from .bpy_prop_collection import bpy_prop_collection

class ViewLayer(bpy_struct):

    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:
        """View layer name"""
        ...
    @name.setter
    def name(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def material_override(self) -> Annotated[Optional['Material'], "is_animatable=False"]:
        """Material to override all other materials in this view layer"""
        ...
    @material_override.setter
    def material_override(self, value: Annotated[Optional['Material'], "is_animatable=False"]):
        ...
    @property
    def world_override(self) -> Annotated[Optional['World'], "is_animatable=False"]:
        """Override world in this view layer"""
        ...
    @world_override.setter
    def world_override(self, value: Annotated[Optional['World'], "is_animatable=False"]):
        ...
    @property
    def samples(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Override number of render samples for this view layer, 0 will use the scene setting"""
        ...
    @samples.setter
    def samples(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1"]):
        ...
    @property
    def pass_alpha_threshold(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Z, Index, normal, UV and vector passes are only affected by surfaces with alpha transparency equal to or higher than this threshold"""
        ...
    @pass_alpha_threshold.setter
    def pass_alpha_threshold(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]):
        ...
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
    @property
    def active_aov_index(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Index of active AOV"""
        ...
    @active_aov_index.setter
    def active_aov_index(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1"]):
        ...
    @property
    def lightgroups(self) -> Annotated['Lightgroups', "is_animatable=False"]:

        ...
    @property
    def active_lightgroup(self) -> Annotated[Optional['Lightgroup'], "is_animatable=False"]:
        """Active Lightgroup"""
        ...
    @property
    def active_lightgroup_index(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Index of active lightgroup"""
        ...
    @active_lightgroup_index.setter
    def active_lightgroup_index(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1"]):
        ...
    @property
    def use_pass_cryptomatte_object(self) -> bool:
        """Render cryptomatte object pass, for isolating objects in compositing"""
        ...
    @use_pass_cryptomatte_object.setter
    def use_pass_cryptomatte_object(self, value: bool):
        ...
    @property
    def use_pass_cryptomatte_material(self) -> bool:
        """Render cryptomatte material pass, for isolating materials in compositing"""
        ...
    @use_pass_cryptomatte_material.setter
    def use_pass_cryptomatte_material(self, value: bool):
        ...
    @property
    def use_pass_cryptomatte_asset(self) -> bool:
        """Render cryptomatte asset pass, for isolating groups of objects with the same parent"""
        ...
    @use_pass_cryptomatte_asset.setter
    def use_pass_cryptomatte_asset(self, value: bool):
        ...
    @property
    def pass_cryptomatte_depth(self) -> Annotated[int, "step=2"]:
        """Sets how many unique objects can be distinguished per pixel"""
        ...
    @pass_cryptomatte_depth.setter
    def pass_cryptomatte_depth(self, value: Annotated[int, "step=2"]):
        ...
    @property
    def use_pass_cryptomatte_accurate(self) -> bool:
        """Generate a more accurate cryptomatte pass"""
        ...
    @use_pass_cryptomatte_accurate.setter
    def use_pass_cryptomatte_accurate(self, value: bool):
        ...
    @property
    def use_solid(self) -> bool:
        """Render Solid faces in this Layer"""
        ...
    @use_solid.setter
    def use_solid(self, value: bool):
        ...
    @property
    def use_sky(self) -> bool:
        """Render Sky in this Layer"""
        ...
    @use_sky.setter
    def use_sky(self, value: bool):
        ...
    @property
    def use_ao(self) -> bool:
        """Render Ambient Occlusion in this Layer"""
        ...
    @use_ao.setter
    def use_ao(self, value: bool):
        ...
    @property
    def use_strand(self) -> bool:
        """Render Strands in this Layer"""
        ...
    @use_strand.setter
    def use_strand(self, value: bool):
        ...
    @property
    def use_volumes(self) -> bool:
        """Render volumes in this Layer"""
        ...
    @use_volumes.setter
    def use_volumes(self, value: bool):
        ...
    @property
    def use_motion_blur(self) -> bool:
        """Render motion blur in this Layer, if enabled in the scene"""
        ...
    @use_motion_blur.setter
    def use_motion_blur(self, value: bool):
        ...
    @property
    def use_grease_pencil(self) -> bool:
        """Render Grease Pencil on this layer"""
        ...
    @use_grease_pencil.setter
    def use_grease_pencil(self, value: bool):
        ...
    @property
    def use_pass_combined(self) -> bool:
        """Deliver full combined RGBA buffer"""
        ...
    @use_pass_combined.setter
    def use_pass_combined(self, value: bool):
        ...
    @property
    def use_pass_z(self) -> bool:
        """Deliver depth values pass"""
        ...
    @use_pass_z.setter
    def use_pass_z(self, value: bool):
        ...
    @property
    def use_pass_vector(self) -> bool:
        """Deliver speed vector pass"""
        ...
    @use_pass_vector.setter
    def use_pass_vector(self, value: bool):
        ...
    @property
    def use_pass_position(self) -> bool:
        """Deliver position pass"""
        ...
    @use_pass_position.setter
    def use_pass_position(self, value: bool):
        ...
    @property
    def use_pass_normal(self) -> bool:
        """Deliver normal pass"""
        ...
    @use_pass_normal.setter
    def use_pass_normal(self, value: bool):
        ...
    @property
    def use_pass_uv(self) -> bool:
        """Deliver texture UV pass"""
        ...
    @use_pass_uv.setter
    def use_pass_uv(self, value: bool):
        ...
    @property
    def use_pass_mist(self) -> bool:
        """Deliver mist factor pass (0.0 to 1.0)"""
        ...
    @use_pass_mist.setter
    def use_pass_mist(self, value: bool):
        ...
    @property
    def use_pass_object_index(self) -> bool:
        """Deliver object index pass"""
        ...
    @use_pass_object_index.setter
    def use_pass_object_index(self, value: bool):
        ...
    @property
    def use_pass_material_index(self) -> bool:
        """Deliver material index pass"""
        ...
    @use_pass_material_index.setter
    def use_pass_material_index(self, value: bool):
        ...
    @property
    def use_pass_shadow(self) -> bool:
        """Deliver shadow pass"""
        ...
    @use_pass_shadow.setter
    def use_pass_shadow(self, value: bool):
        ...
    @property
    def use_pass_ambient_occlusion(self) -> bool:
        """Deliver Ambient Occlusion pass"""
        ...
    @use_pass_ambient_occlusion.setter
    def use_pass_ambient_occlusion(self, value: bool):
        ...
    @property
    def use_pass_emit(self) -> bool:
        """Deliver emission pass"""
        ...
    @use_pass_emit.setter
    def use_pass_emit(self, value: bool):
        ...
    @property
    def use_pass_environment(self) -> bool:
        """Deliver environment lighting pass"""
        ...
    @use_pass_environment.setter
    def use_pass_environment(self, value: bool):
        ...
    @property
    def use_pass_diffuse_direct(self) -> bool:
        """Deliver diffuse direct pass"""
        ...
    @use_pass_diffuse_direct.setter
    def use_pass_diffuse_direct(self, value: bool):
        ...
    @property
    def use_pass_diffuse_indirect(self) -> bool:
        """Deliver diffuse indirect pass"""
        ...
    @use_pass_diffuse_indirect.setter
    def use_pass_diffuse_indirect(self, value: bool):
        ...
    @property
    def use_pass_diffuse_color(self) -> bool:
        """Deliver diffuse color pass"""
        ...
    @use_pass_diffuse_color.setter
    def use_pass_diffuse_color(self, value: bool):
        ...
    @property
    def use_pass_glossy_direct(self) -> bool:
        """Deliver glossy direct pass"""
        ...
    @use_pass_glossy_direct.setter
    def use_pass_glossy_direct(self, value: bool):
        ...
    @property
    def use_pass_glossy_indirect(self) -> bool:
        """Deliver glossy indirect pass"""
        ...
    @use_pass_glossy_indirect.setter
    def use_pass_glossy_indirect(self, value: bool):
        ...
    @property
    def use_pass_glossy_color(self) -> bool:
        """Deliver glossy color pass"""
        ...
    @use_pass_glossy_color.setter
    def use_pass_glossy_color(self, value: bool):
        ...
    @property
    def use_pass_transmission_direct(self) -> bool:
        """Deliver transmission direct pass"""
        ...
    @use_pass_transmission_direct.setter
    def use_pass_transmission_direct(self, value: bool):
        ...
    @property
    def use_pass_transmission_indirect(self) -> bool:
        """Deliver transmission indirect pass"""
        ...
    @use_pass_transmission_indirect.setter
    def use_pass_transmission_indirect(self, value: bool):
        ...
    @property
    def use_pass_transmission_color(self) -> bool:
        """Deliver transmission color pass"""
        ...
    @use_pass_transmission_color.setter
    def use_pass_transmission_color(self, value: bool):
        ...
    @property
    def use_pass_subsurface_direct(self) -> bool:
        """Deliver subsurface direct pass"""
        ...
    @use_pass_subsurface_direct.setter
    def use_pass_subsurface_direct(self, value: bool):
        ...
    @property
    def use_pass_subsurface_indirect(self) -> bool:
        """Deliver subsurface indirect pass"""
        ...
    @use_pass_subsurface_indirect.setter
    def use_pass_subsurface_indirect(self, value: bool):
        ...
    @property
    def use_pass_subsurface_color(self) -> bool:
        """Deliver subsurface color pass"""
        ...
    @use_pass_subsurface_color.setter
    def use_pass_subsurface_color(self, value: bool):
        ...
    @property
    def layer_collection(self) -> Annotated['LayerCollection', "is_animatable=False"]:
        """Root of collections hierarchy of this view layer, its 'collection' pointer property is the same as the scene's master collection"""
        ...
    @property
    def active_layer_collection(self) -> Annotated['LayerCollection', "is_animatable=False"]:
        """Active layer collection in this view layer's hierarchy"""
        ...
    @active_layer_collection.setter
    def active_layer_collection(self, value: Annotated['LayerCollection', "is_animatable=False"]):
        ...
    @property
    def objects(self) -> Annotated['LayerObjects', "is_animatable=False"]:
        """All the objects in this layer"""
        ...
    @property
    def use(self) -> bool:
        """Enable or disable rendering of this View Layer"""
        ...
    @use.setter
    def use(self, value: bool):
        ...
    @property
    def has_export_collections(self) -> bool:
        """At least one Collection in this View Layer has an exporter"""
        ...
    @property
    def use_freestyle(self) -> bool:
        """Render stylized strokes in this Layer"""
        ...
    @use_freestyle.setter
    def use_freestyle(self, value: bool):
        ...
    @property
    def freestyle_settings(self) -> Annotated['FreestyleSettings', "is_animatable=False"]:

        ...
    @property
    def use_pass_grease_pencil(self) -> bool:
        """Deliver Grease Pencil render result in a separate pass"""
        ...
    @use_pass_grease_pencil.setter
    def use_pass_grease_pencil(self, value: bool):
        ...
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