# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.EditBone.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from ._GenericBone import _GenericBone
from .BoneCollection import BoneCollection
from .BoneColor import BoneColor
from .bpy_prop_collection import bpy_prop_collection

class EditBone(bpy_struct, _GenericBone):

    @property
    def collections(self) -> Annotated[bpy_prop_collection['BoneCollection'], "is_animatable=False"]:
        """Bone Collections that contain this bone"""
        ...
    @property
    def parent(self) -> Annotated[Optional['EditBone'], "is_animatable=False"]:
        """Parent edit bone (in same Armature)"""
        ...
    @parent.setter
    def parent(self, value: Annotated[Optional['EditBone'], "is_animatable=False"]) -> None:
        ...
    @property
    def roll(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=2", "is_animatable=False"]:
        """Bone rotation around head-tail axis"""
        ...
    @roll.setter
    def roll(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=2", "is_animatable=False"]) -> None:
        ...
    @property
    def head(self) -> Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=10.0", "precision=5", "is_animatable=False"]:
        """Location of head end of the bone"""
        ...
    @head.setter
    def head(self, value: Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=10.0", "precision=5", "is_animatable=False"]) -> None:
        ...
    @property
    def tail(self) -> Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=10.0", "precision=5", "is_animatable=False"]:
        """Location of tail end of the bone"""
        ...
    @tail.setter
    def tail(self, value: Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=10.0", "precision=5", "is_animatable=False"]) -> None:
        ...
    @property
    def length(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=1.0", "precision=5", "is_animatable=False"]:
        """Length of the bone. Changing moves the tail end."""
        ...
    @length.setter
    def length(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=1.0", "precision=5", "is_animatable=False"]) -> None:
        ...
    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:

        ...
    @name.setter
    def name(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def color(self) -> Annotated[Optional['BoneColor'], "is_animatable=False"]:

        ...
    @property
    def display_type(self) -> Literal['ARMATURE_DEFINED', 'OCTAHEDRAL', 'STICK', 'BBONE', 'ENVELOPE', 'WIRE']:

        ...
    @display_type.setter
    def display_type(self, value: Literal['ARMATURE_DEFINED', 'OCTAHEDRAL', 'STICK', 'BBONE', 'ENVELOPE', 'WIRE']) -> None:
        ...
    @property
    def use_connect(self) -> bool:
        """When bone has a parent, bone's head is stuck to the parent's tail"""
        ...
    @use_connect.setter
    def use_connect(self, value: bool) -> None:
        ...
    @property
    def use_inherit_rotation(self) -> bool:
        """Bone inherits rotation or scale from parent bone"""
        ...
    @use_inherit_rotation.setter
    def use_inherit_rotation(self, value: bool) -> None:
        ...
    @property
    def use_envelope_multiply(self) -> bool:
        """When deforming bone, multiply effects of Vertex Group weights with Envelope influence"""
        ...
    @use_envelope_multiply.setter
    def use_envelope_multiply(self, value: bool) -> None:
        ...
    @property
    def use_deform(self) -> bool:
        """Enable Bone to deform geometry"""
        ...
    @use_deform.setter
    def use_deform(self, value: bool) -> None:
        ...
    @property
    def inherit_scale(self) -> Literal['FULL', 'FIX_SHEAR', 'ALIGNED', 'AVERAGE', 'NONE', 'NONE_LEGACY']:
        """Specifies how the bone inherits scaling from the parent bone"""
        ...
    @inherit_scale.setter
    def inherit_scale(self, value: Literal['FULL', 'FIX_SHEAR', 'ALIGNED', 'AVERAGE', 'NONE', 'NONE_LEGACY']) -> None:
        ...
    @property
    def use_local_location(self) -> bool:
        """Bone location is set in local space"""
        ...
    @use_local_location.setter
    def use_local_location(self, value: bool) -> None:
        ...
    @property
    def use_relative_parent(self) -> bool:
        """Object children will use relative transform, like deform"""
        ...
    @use_relative_parent.setter
    def use_relative_parent(self, value: bool) -> None:
        ...
    @property
    def show_wire(self) -> bool:
        """Bone is always displayed in wireframe regardless of viewport shading mode (useful for non-obstructive custom bone shapes)"""
        ...
    @show_wire.setter
    def show_wire(self, value: bool) -> None:
        ...
    @property
    def use_cyclic_offset(self) -> bool:
        """When bone does not have a parent, it receives cyclic offset effects (Deprecated)"""
        ...
    @use_cyclic_offset.setter
    def use_cyclic_offset(self, value: bool) -> None:
        ...
    @property
    def hide_select(self) -> bool:
        """Bone is able to be selected"""
        ...
    @hide_select.setter
    def hide_select(self, value: bool) -> None:
        ...
    @property
    def envelope_distance(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]:
        """Bone deformation distance (for Envelope deform only)"""
        ...
    @envelope_distance.setter
    def envelope_distance(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def envelope_weight(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Bone deformation weight (for Envelope deform only)"""
        ...
    @envelope_weight.setter
    def envelope_weight(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def head_radius(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.10000000149011612", "precision=3"]:
        """Radius of head of bone (for Envelope deform only)"""
        ...
    @head_radius.setter
    def head_radius(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.10000000149011612", "precision=3"]) -> None:
        ...
    @property
    def tail_radius(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.10000000149011612", "precision=3"]:
        """Radius of tail of bone (for Envelope deform only)"""
        ...
    @tail_radius.setter
    def tail_radius(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.10000000149011612", "precision=3"]) -> None:
        ...
    @property
    def bbone_segments(self) -> Annotated[int, "step=1"]:
        """Number of subdivisions of bone (for B-Bones only)"""
        ...
    @bbone_segments.setter
    def bbone_segments(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def bbone_mapping_mode(self) -> Annotated[Literal['STRAIGHT', 'CURVED'], "is_animatable=False"]:
        """Selects how the vertices are mapped to B-Bone segments based on their position"""
        ...
    @bbone_mapping_mode.setter
    def bbone_mapping_mode(self, value: Annotated[Literal['STRAIGHT', 'CURVED'], "is_animatable=False"]) -> None:
        ...
    @property
    def bbone_x(self) -> Annotated[float, "step=1.0", "precision=5"]:
        """B-Bone X size"""
        ...
    @bbone_x.setter
    def bbone_x(self, value: Annotated[float, "step=1.0", "precision=5"]) -> None:
        ...
    @property
    def bbone_z(self) -> Annotated[float, "step=1.0", "precision=5"]:
        """B-Bone Z size"""
        ...
    @bbone_z.setter
    def bbone_z(self, value: Annotated[float, "step=1.0", "precision=5"]) -> None:
        ...
    @property
    def bbone_handle_type_start(self) -> Annotated[Literal['AUTO', 'ABSOLUTE', 'RELATIVE', 'TANGENT'], "is_animatable=False"]:
        """Selects how the start handle of the B-Bone is computed"""
        ...
    @bbone_handle_type_start.setter
    def bbone_handle_type_start(self, value: Annotated[Literal['AUTO', 'ABSOLUTE', 'RELATIVE', 'TANGENT'], "is_animatable=False"]) -> None:
        ...
    @property
    def bbone_custom_handle_start(self) -> Annotated[Optional['EditBone'], "is_animatable=False"]:
        """Bone that serves as the start handle for the B-Bone curve"""
        ...
    @bbone_custom_handle_start.setter
    def bbone_custom_handle_start(self, value: Annotated[Optional['EditBone'], "is_animatable=False"]) -> None:
        ...
    @property
    def bbone_handle_use_scale_start(self) -> list[bool]:
        """Multiply B-Bone Scale In channels by the local scale values of the start handle. This is done after the Scale Easing option and isn't affected by it."""
        ...
    @bbone_handle_use_scale_start.setter
    def bbone_handle_use_scale_start(self, value: list[bool]) -> None:
        ...
    @property
    def bbone_handle_use_ease_start(self) -> bool:
        """Multiply the B-Bone Ease In channel by the local Y scale value of the start handle. This is done after the Scale Easing option and isn't affected by it."""
        ...
    @bbone_handle_use_ease_start.setter
    def bbone_handle_use_ease_start(self, value: bool) -> None:
        ...
    @property
    def bbone_handle_type_end(self) -> Annotated[Literal['AUTO', 'ABSOLUTE', 'RELATIVE', 'TANGENT'], "is_animatable=False"]:
        """Selects how the end handle of the B-Bone is computed"""
        ...
    @bbone_handle_type_end.setter
    def bbone_handle_type_end(self, value: Annotated[Literal['AUTO', 'ABSOLUTE', 'RELATIVE', 'TANGENT'], "is_animatable=False"]) -> None:
        ...
    @property
    def bbone_custom_handle_end(self) -> Annotated[Optional['EditBone'], "is_animatable=False"]:
        """Bone that serves as the end handle for the B-Bone curve"""
        ...
    @bbone_custom_handle_end.setter
    def bbone_custom_handle_end(self, value: Annotated[Optional['EditBone'], "is_animatable=False"]) -> None:
        ...
    @property
    def bbone_handle_use_scale_end(self) -> list[bool]:
        """Multiply B-Bone Scale Out channels by the local scale values of the end handle. This is done after the Scale Easing option and isn't affected by it."""
        ...
    @bbone_handle_use_scale_end.setter
    def bbone_handle_use_scale_end(self, value: list[bool]) -> None:
        ...
    @property
    def bbone_handle_use_ease_end(self) -> bool:
        """Multiply the B-Bone Ease Out channel by the local Y scale value of the end handle. This is done after the Scale Easing option and isn't affected by it."""
        ...
    @bbone_handle_use_ease_end.setter
    def bbone_handle_use_ease_end(self, value: bool) -> None:
        ...
    @property
    def bbone_rollin(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=2"]:
        """Roll offset for the start of the B-Bone, adjusts twist"""
        ...
    @bbone_rollin.setter
    def bbone_rollin(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=2"]) -> None:
        ...
    @property
    def bbone_rollout(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=2"]:
        """Roll offset for the end of the B-Bone, adjusts twist"""
        ...
    @bbone_rollout.setter
    def bbone_rollout(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=2"]) -> None:
        ...
    @property
    def use_endroll_as_inroll(self) -> Annotated[bool, "is_animatable=False"]:
        """Add Roll Out of the Start Handle bone to the Roll In value"""
        ...
    @use_endroll_as_inroll.setter
    def use_endroll_as_inroll(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def bbone_curveinx(self) -> Annotated[float, "step=1.0", "precision=5"]:
        """X-axis handle offset for start of the B-Bone's curve, adjusts curvature"""
        ...
    @bbone_curveinx.setter
    def bbone_curveinx(self, value: Annotated[float, "step=1.0", "precision=5"]) -> None:
        ...
    @property
    def bbone_curveinz(self) -> Annotated[float, "step=1.0", "precision=5"]:
        """Z-axis handle offset for start of the B-Bone's curve, adjusts curvature"""
        ...
    @bbone_curveinz.setter
    def bbone_curveinz(self, value: Annotated[float, "step=1.0", "precision=5"]) -> None:
        ...
    @property
    def bbone_curveoutx(self) -> Annotated[float, "step=1.0", "precision=5"]:
        """X-axis handle offset for end of the B-Bone's curve, adjusts curvature"""
        ...
    @bbone_curveoutx.setter
    def bbone_curveoutx(self, value: Annotated[float, "step=1.0", "precision=5"]) -> None:
        ...
    @property
    def bbone_curveoutz(self) -> Annotated[float, "step=1.0", "precision=5"]:
        """Z-axis handle offset for end of the B-Bone's curve, adjusts curvature"""
        ...
    @bbone_curveoutz.setter
    def bbone_curveoutz(self, value: Annotated[float, "step=1.0", "precision=5"]) -> None:
        ...
    @property
    def bbone_easein(self) -> Annotated[float, "step=1.0", "precision=3"]:
        """Length of first Bézier Handle (for B-Bones only)"""
        ...
    @bbone_easein.setter
    def bbone_easein(self, value: Annotated[float, "step=1.0", "precision=3"]) -> None:
        ...
    @property
    def bbone_easeout(self) -> Annotated[float, "step=1.0", "precision=3"]:
        """Length of second Bézier Handle (for B-Bones only)"""
        ...
    @bbone_easeout.setter
    def bbone_easeout(self, value: Annotated[float, "step=1.0", "precision=3"]) -> None:
        ...
    @property
    def use_scale_easing(self) -> bool:
        """Multiply the final easing values by the Scale In/Out Y factors"""
        ...
    @use_scale_easing.setter
    def use_scale_easing(self, value: bool) -> None:
        ...
    @property
    def bbone_scalein(self) -> Annotated[list[float], "subtype='XYZ'", "step=1.0", "precision=3"]:
        """Scale factors for the start of the B-Bone, adjusts thickness (for tapering effects)"""
        ...
    @bbone_scalein.setter
    def bbone_scalein(self, value: Annotated[list[float], "subtype='XYZ'", "step=1.0", "precision=3"]) -> None:
        ...
    @property
    def bbone_scaleout(self) -> Annotated[list[float], "subtype='XYZ'", "step=1.0", "precision=3"]:
        """Scale factors for the end of the B-Bone, adjusts thickness (for tapering effects)"""
        ...
    @bbone_scaleout.setter
    def bbone_scaleout(self, value: Annotated[list[float], "subtype='XYZ'", "step=1.0", "precision=3"]) -> None:
        ...
    @property
    def hide(self) -> Annotated[bool, "is_animatable=False"]:
        """Bone is not visible when in Edit Mode"""
        ...
    @hide.setter
    def hide(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def lock(self) -> Annotated[bool, "is_animatable=False"]:
        """Bone is not able to be transformed when in Edit Mode"""
        ...
    @lock.setter
    def lock(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def select(self) -> Annotated[bool, "is_animatable=False"]:

        ...
    @select.setter
    def select(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def select_head(self) -> Annotated[bool, "is_animatable=False"]:

        ...
    @select_head.setter
    def select_head(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def select_tail(self) -> Annotated[bool, "is_animatable=False"]:

        ...
    @select_tail.setter
    def select_tail(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def matrix(self) -> Annotated[list[float], "subtype='MATRIX'", "step=10.0", "precision=3"]:
        """Matrix combining location and rotation of the bone (head position, direction and roll), in armature space (does not include/support bone's length/size)"""
        ...
    @matrix.setter
    def matrix(self, value: Annotated[list[float], "subtype='MATRIX'", "step=10.0", "precision=3"]) -> None:
        ...
    def bl_system_properties_get(self, *args, **kwargs) -> Any: ...
    def align_roll(self, *args, **kwargs) -> Any: ...