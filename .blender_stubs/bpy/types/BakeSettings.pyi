# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.BakeSettings.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .ImageFormatSettings import ImageFormatSettings
from .Object import Object

class BakeSettings(bpy_struct):

    @property
    def type(self) -> Annotated[Literal['NORMALS', 'DISPLACEMENT', 'VECTOR_DISPLACEMENT'], "is_animatable=False"]:
        """Choose shading information to bake into the image"""
        ...
    @type.setter
    def type(self, value: Annotated[Literal['NORMALS', 'DISPLACEMENT', 'VECTOR_DISPLACEMENT'], "is_animatable=False"]):
        ...
    @property
    def cage_object(self) -> Annotated[Optional['Object'], "is_animatable=False"]:
        """Object to use as cage instead of calculating the cage from the active object with cage extrusion"""
        ...
    @cage_object.setter
    def cage_object(self, value: Annotated[Optional['Object'], "is_animatable=False"]):
        ...
    @property
    def filepath(self) -> Annotated[str, "subtype='FILE_PATH'", "is_animatable=False"]:
        """Image filepath to use when saving externally"""
        ...
    @filepath.setter
    def filepath(self, value: Annotated[str, "subtype='FILE_PATH'", "is_animatable=False"]):
        ...
    @property
    def width(self) -> Annotated[int, "subtype='PIXEL'", "step=1", "is_animatable=False"]:
        """Horizontal dimension of the baking map"""
        ...
    @width.setter
    def width(self, value: Annotated[int, "subtype='PIXEL'", "step=1", "is_animatable=False"]):
        ...
    @property
    def height(self) -> Annotated[int, "subtype='PIXEL'", "step=1", "is_animatable=False"]:
        """Vertical dimension of the baking map"""
        ...
    @height.setter
    def height(self, value: Annotated[int, "subtype='PIXEL'", "step=1", "is_animatable=False"]):
        ...
    @property
    def margin(self) -> Annotated[int, "subtype='PIXEL'", "step=1", "is_animatable=False"]:
        """Extends the baked result as a post process filter"""
        ...
    @margin.setter
    def margin(self, value: Annotated[int, "subtype='PIXEL'", "step=1", "is_animatable=False"]):
        ...
    @property
    def margin_type(self) -> Annotated[Literal['ADJACENT_FACES', 'EXTEND'], "is_animatable=False"]:
        """Algorithm to extend the baked result"""
        ...
    @margin_type.setter
    def margin_type(self, value: Annotated[Literal['ADJACENT_FACES', 'EXTEND'], "is_animatable=False"]):
        ...
    @property
    def max_ray_distance(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=1.0", "precision=3", "is_animatable=False"]:
        """The maximum ray distance for matching points between the active and selected objects. If zero, there is no limit."""
        ...
    @max_ray_distance.setter
    def max_ray_distance(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=1.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def cage_extrusion(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=1.0", "precision=3", "is_animatable=False"]:
        """Inflate the active object by the specified distance for baking. This helps matching to points nearer to the outside of the selected object meshes."""
        ...
    @cage_extrusion.setter
    def cage_extrusion(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=1.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def normal_space(self) -> Annotated[Literal['OBJECT', 'TANGENT'], "is_animatable=False"]:
        """Choose normal space for baking"""
        ...
    @normal_space.setter
    def normal_space(self, value: Annotated[Literal['OBJECT', 'TANGENT'], "is_animatable=False"]):
        ...
    @property
    def normal_r(self) -> Annotated[Literal['POS_X', 'POS_Y', 'POS_Z', 'NEG_X', 'NEG_Y', 'NEG_Z'], "is_animatable=False"]:
        """Axis to bake in red channel"""
        ...
    @normal_r.setter
    def normal_r(self, value: Annotated[Literal['POS_X', 'POS_Y', 'POS_Z', 'NEG_X', 'NEG_Y', 'NEG_Z'], "is_animatable=False"]):
        ...
    @property
    def normal_g(self) -> Annotated[Literal['POS_X', 'POS_Y', 'POS_Z', 'NEG_X', 'NEG_Y', 'NEG_Z'], "is_animatable=False"]:
        """Axis to bake in green channel"""
        ...
    @normal_g.setter
    def normal_g(self, value: Annotated[Literal['POS_X', 'POS_Y', 'POS_Z', 'NEG_X', 'NEG_Y', 'NEG_Z'], "is_animatable=False"]):
        ...
    @property
    def normal_b(self) -> Annotated[Literal['POS_X', 'POS_Y', 'POS_Z', 'NEG_X', 'NEG_Y', 'NEG_Z'], "is_animatable=False"]:
        """Axis to bake in blue channel"""
        ...
    @normal_b.setter
    def normal_b(self, value: Annotated[Literal['POS_X', 'POS_Y', 'POS_Z', 'NEG_X', 'NEG_Y', 'NEG_Z'], "is_animatable=False"]):
        ...
    @property
    def image_settings(self) -> Annotated['ImageFormatSettings', "is_animatable=False"]:

        ...
    @property
    def target(self) -> Annotated[Literal['IMAGE_TEXTURES', 'VERTEX_COLORS'], "is_animatable=False"]:
        """Where to output the baked map"""
        ...
    @target.setter
    def target(self, value: Annotated[Literal['IMAGE_TEXTURES', 'VERTEX_COLORS'], "is_animatable=False"]):
        ...
    @property
    def save_mode(self) -> Annotated[Literal['INTERNAL', 'EXTERNAL'], "is_animatable=False"]:
        """Where to save baked image textures"""
        ...
    @save_mode.setter
    def save_mode(self, value: Annotated[Literal['INTERNAL', 'EXTERNAL'], "is_animatable=False"]):
        ...
    @property
    def view_from(self) -> Annotated[Literal['ABOVE_SURFACE', 'ACTIVE_CAMERA'], "is_animatable=False"]:
        """Source of reflection ray directions"""
        ...
    @view_from.setter
    def view_from(self, value: Annotated[Literal['ABOVE_SURFACE', 'ACTIVE_CAMERA'], "is_animatable=False"]):
        ...
    @property
    def use_selected_to_active(self) -> Annotated[bool, "is_animatable=False"]:
        """Bake shading on the surface of selected objects to the active object"""
        ...
    @use_selected_to_active.setter
    def use_selected_to_active(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_clear(self) -> Annotated[bool, "is_animatable=False"]:
        """Clear Images before baking (internal only)"""
        ...
    @use_clear.setter
    def use_clear(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_split_materials(self) -> Annotated[bool, "is_animatable=False"]:
        """Split external images per material (external only)"""
        ...
    @use_split_materials.setter
    def use_split_materials(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_automatic_name(self) -> Annotated[bool, "is_animatable=False"]:
        """Automatically name the output file with the pass type (external only)"""
        ...
    @use_automatic_name.setter
    def use_automatic_name(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_cage(self) -> Annotated[bool, "is_animatable=False"]:
        """Cast rays to active object from a cage"""
        ...
    @use_cage.setter
    def use_cage(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_pass_emit(self) -> Annotated[bool, "is_animatable=False"]:
        """Add emission contribution"""
        ...
    @use_pass_emit.setter
    def use_pass_emit(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_pass_direct(self) -> Annotated[bool, "is_animatable=False"]:
        """Add direct lighting contribution"""
        ...
    @use_pass_direct.setter
    def use_pass_direct(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_pass_indirect(self) -> Annotated[bool, "is_animatable=False"]:
        """Add indirect lighting contribution"""
        ...
    @use_pass_indirect.setter
    def use_pass_indirect(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_pass_color(self) -> Annotated[bool, "is_animatable=False"]:
        """Color the pass"""
        ...
    @use_pass_color.setter
    def use_pass_color(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_pass_diffuse(self) -> Annotated[bool, "is_animatable=False"]:
        """Add diffuse contribution"""
        ...
    @use_pass_diffuse.setter
    def use_pass_diffuse(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_pass_glossy(self) -> Annotated[bool, "is_animatable=False"]:
        """Add glossy contribution"""
        ...
    @use_pass_glossy.setter
    def use_pass_glossy(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_pass_transmission(self) -> Annotated[bool, "is_animatable=False"]:
        """Add transmission contribution"""
        ...
    @use_pass_transmission.setter
    def use_pass_transmission(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def pass_filter(self) -> Annotated[set[str], "is_animatable=False"]:
        """Passes to include in the active baking pass"""
        ...
    @property
    def use_multires(self) -> Annotated[bool, "is_animatable=False"]:
        """Bake directly from multires object"""
        ...
    @use_multires.setter
    def use_multires(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_lores_mesh(self) -> Annotated[bool, "is_animatable=False"]:
        """Calculate heights against unsubdivided low resolution mesh"""
        ...
    @use_lores_mesh.setter
    def use_lores_mesh(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def displacement_space(self) -> Annotated[Literal['OBJECT', 'TANGENT'], "is_animatable=False"]:
        """Choose displacement space for baking"""
        ...
    @displacement_space.setter
    def displacement_space(self, value: Annotated[Literal['OBJECT', 'TANGENT'], "is_animatable=False"]):
        ...