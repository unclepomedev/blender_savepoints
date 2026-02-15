# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.RenderLayer.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .RenderPass import RenderPass
from .RenderPasses import RenderPasses
from .bpy_prop_collection import bpy_prop_collection

class RenderLayer(bpy_struct):

    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:
        """View layer name"""
        ...
    @property
    def use_solid(self) -> bool:
        """Render Solid faces in this Layer"""
        ...
    @property
    def use_sky(self) -> bool:
        """Render Sky in this Layer"""
        ...
    @property
    def use_ao(self) -> bool:
        """Render Ambient Occlusion in this Layer"""
        ...
    @property
    def use_strand(self) -> bool:
        """Render Strands in this Layer"""
        ...
    @property
    def use_volumes(self) -> bool:
        """Render volumes in this Layer"""
        ...
    @property
    def use_motion_blur(self) -> bool:
        """Render motion blur in this Layer, if enabled in the scene"""
        ...
    @property
    def use_grease_pencil(self) -> bool:
        """Render Grease Pencil on this layer"""
        ...
    @property
    def use_pass_combined(self) -> bool:
        """Deliver full combined RGBA buffer"""
        ...
    @property
    def use_pass_z(self) -> bool:
        """Deliver depth values pass"""
        ...
    @property
    def use_pass_vector(self) -> bool:
        """Deliver speed vector pass"""
        ...
    @property
    def use_pass_position(self) -> bool:
        """Deliver position pass"""
        ...
    @property
    def use_pass_normal(self) -> bool:
        """Deliver normal pass"""
        ...
    @property
    def use_pass_uv(self) -> bool:
        """Deliver texture UV pass"""
        ...
    @property
    def use_pass_mist(self) -> bool:
        """Deliver mist factor pass (0.0 to 1.0)"""
        ...
    @property
    def use_pass_object_index(self) -> bool:
        """Deliver object index pass"""
        ...
    @property
    def use_pass_material_index(self) -> bool:
        """Deliver material index pass"""
        ...
    @property
    def use_pass_shadow(self) -> bool:
        """Deliver shadow pass"""
        ...
    @property
    def use_pass_ambient_occlusion(self) -> bool:
        """Deliver Ambient Occlusion pass"""
        ...
    @property
    def use_pass_emit(self) -> bool:
        """Deliver emission pass"""
        ...
    @property
    def use_pass_environment(self) -> bool:
        """Deliver environment lighting pass"""
        ...
    @property
    def use_pass_diffuse_direct(self) -> bool:
        """Deliver diffuse direct pass"""
        ...
    @property
    def use_pass_diffuse_indirect(self) -> bool:
        """Deliver diffuse indirect pass"""
        ...
    @property
    def use_pass_diffuse_color(self) -> bool:
        """Deliver diffuse color pass"""
        ...
    @property
    def use_pass_glossy_direct(self) -> bool:
        """Deliver glossy direct pass"""
        ...
    @property
    def use_pass_glossy_indirect(self) -> bool:
        """Deliver glossy indirect pass"""
        ...
    @property
    def use_pass_glossy_color(self) -> bool:
        """Deliver glossy color pass"""
        ...
    @property
    def use_pass_transmission_direct(self) -> bool:
        """Deliver transmission direct pass"""
        ...
    @property
    def use_pass_transmission_indirect(self) -> bool:
        """Deliver transmission indirect pass"""
        ...
    @property
    def use_pass_transmission_color(self) -> bool:
        """Deliver transmission color pass"""
        ...
    @property
    def use_pass_subsurface_direct(self) -> bool:
        """Deliver subsurface direct pass"""
        ...
    @property
    def use_pass_subsurface_indirect(self) -> bool:
        """Deliver subsurface indirect pass"""
        ...
    @property
    def use_pass_subsurface_color(self) -> bool:
        """Deliver subsurface color pass"""
        ...
    @property
    def passes(self) -> Annotated['RenderPasses', "is_animatable=False"]:

        ...
    def load_from_file(self, *args, **kwargs) -> Any: ...