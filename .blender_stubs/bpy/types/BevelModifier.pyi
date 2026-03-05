# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.BevelModifier.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .Modifier import Modifier
from .CurveProfile import CurveProfile

class BevelModifier(Modifier):

    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:
        """Modifier name"""
        ...
    @name.setter
    def name(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def type(self) -> Literal['GREASE_PENCIL_VERTEX_WEIGHT_PROXIMITY', 'DATA_TRANSFER', 'MESH_CACHE', 'MESH_SEQUENCE_CACHE', 'NORMAL_EDIT', 'WEIGHTED_NORMAL', 'UV_PROJECT', 'UV_WARP', 'VERTEX_WEIGHT_EDIT', 'VERTEX_WEIGHT_MIX', 'VERTEX_WEIGHT_PROXIMITY', 'GREASE_PENCIL_COLOR', 'GREASE_PENCIL_TINT', 'GREASE_PENCIL_OPACITY', 'GREASE_PENCIL_VERTEX_WEIGHT_ANGLE', 'GREASE_PENCIL_TIME', 'GREASE_PENCIL_TEXTURE', 'ARRAY', 'BEVEL', 'BOOLEAN', 'BUILD', 'DECIMATE', 'EDGE_SPLIT', 'NODES', 'MASK', 'MIRROR', 'MESH_TO_VOLUME', 'MULTIRES', 'REMESH', 'SCREW', 'SKIN', 'SOLIDIFY', 'SUBSURF', 'TRIANGULATE', 'VOLUME_TO_MESH', 'WELD', 'WIREFRAME', 'GREASE_PENCIL_ARRAY', 'GREASE_PENCIL_BUILD', 'GREASE_PENCIL_LENGTH', 'LINEART', 'GREASE_PENCIL_MIRROR', 'GREASE_PENCIL_MULTIPLY', 'GREASE_PENCIL_SIMPLIFY', 'GREASE_PENCIL_SUBDIV', 'GREASE_PENCIL_ENVELOPE', 'GREASE_PENCIL_OUTLINE', 'ARMATURE', 'CAST', 'CURVE', 'DISPLACE', 'HOOK', 'LAPLACIANDEFORM', 'LATTICE', 'MESH_DEFORM', 'SHRINKWRAP', 'SIMPLE_DEFORM', 'SMOOTH', 'CORRECTIVE_SMOOTH', 'LAPLACIANSMOOTH', 'SURFACE_DEFORM', 'WARP', 'WAVE', 'VOLUME_DISPLACE', 'GREASE_PENCIL_HOOK', 'GREASE_PENCIL_NOISE', 'GREASE_PENCIL_OFFSET', 'GREASE_PENCIL_SMOOTH', 'GREASE_PENCIL_THICKNESS', 'GREASE_PENCIL_LATTICE', 'GREASE_PENCIL_DASH', 'GREASE_PENCIL_ARMATURE', 'GREASE_PENCIL_SHRINKWRAP', 'CLOTH', 'COLLISION', 'DYNAMIC_PAINT', 'EXPLODE', 'FLUID', 'OCEAN', 'PARTICLE_INSTANCE', 'PARTICLE_SYSTEM', 'SOFT_BODY', 'SURFACE']:

        ...
    @property
    def show_viewport(self) -> bool:
        """Display modifier in viewport"""
        ...
    @show_viewport.setter
    def show_viewport(self, value: bool):
        ...
    @property
    def show_render(self) -> bool:
        """Use modifier during render"""
        ...
    @show_render.setter
    def show_render(self, value: bool):
        ...
    @property
    def show_in_editmode(self) -> bool:
        """Display modifier in Edit mode"""
        ...
    @show_in_editmode.setter
    def show_in_editmode(self, value: bool):
        ...
    @property
    def show_on_cage(self) -> bool:
        """Adjust edit cage to modifier result"""
        ...
    @show_on_cage.setter
    def show_on_cage(self, value: bool):
        ...
    @property
    def show_expanded(self) -> bool:
        """Set modifier expanded in the user interface"""
        ...
    @show_expanded.setter
    def show_expanded(self, value: bool):
        ...
    @property
    def is_active(self) -> Annotated[bool, "is_animatable=False"]:
        """The active modifier in the list"""
        ...
    @is_active.setter
    def is_active(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_pin_to_last(self) -> Annotated[bool, "is_animatable=False"]:
        """Keep the modifier at the end of the list"""
        ...
    @use_pin_to_last.setter
    def use_pin_to_last(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def is_override_data(self) -> bool:
        """In a local override object, whether this modifier comes from the linked reference object, or is local to the override"""
        ...
    @property
    def use_apply_on_spline(self) -> bool:
        """Apply this and all preceding deformation modifiers on splines' points rather than on filled curve/surface"""
        ...
    @use_apply_on_spline.setter
    def use_apply_on_spline(self, value: bool):
        ...
    @property
    def execution_time(self) -> Annotated[float, "subtype='TIME_ABSOLUTE'", "unit='TIME_ABSOLUTE'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Time in seconds that the modifier took to evaluate. This is only set on evaluated objects. If multiple modifiers run in parallel, execution time is not a reliable metric."""
        ...
    @property
    def persistent_uid(self) -> Annotated[int, "step=1"]:
        """Uniquely identifies the modifier within the modifier stack that it is part of"""
        ...
    @property
    def width(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.10000000149011612", "precision=4"]:
        """Bevel amount"""
        ...
    @width.setter
    def width(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.10000000149011612", "precision=4"]):
        ...
    @property
    def width_pct(self) -> Annotated[float, "subtype='PERCENTAGE'", "step=5.0", "precision=2"]:
        """Bevel amount for percentage method"""
        ...
    @width_pct.setter
    def width_pct(self, value: Annotated[float, "subtype='PERCENTAGE'", "step=5.0", "precision=2"]):
        ...
    @property
    def segments(self) -> Annotated[int, "step=1"]:
        """Number of segments for round edges/verts"""
        ...
    @segments.setter
    def segments(self, value: Annotated[int, "step=1"]):
        ...
    @property
    def affect(self) -> Literal['VERTICES', 'EDGES']:
        """Affect edges or vertices"""
        ...
    @affect.setter
    def affect(self, value: Literal['VERTICES', 'EDGES']):
        ...
    @property
    def limit_method(self) -> Literal['NONE', 'ANGLE', 'WEIGHT', 'VGROUP']:

        ...
    @limit_method.setter
    def limit_method(self, value: Literal['NONE', 'ANGLE', 'WEIGHT', 'VGROUP']):
        ...
    @property
    def edge_weight(self) -> Annotated[str, "is_animatable=False"]:
        """Attribute name for edge weight"""
        ...
    @edge_weight.setter
    def edge_weight(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def vertex_weight(self) -> Annotated[str, "is_animatable=False"]:
        """Attribute name for vertex weight"""
        ...
    @vertex_weight.setter
    def vertex_weight(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def angle_limit(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=4"]:
        """Angle above which to bevel edges"""
        ...
    @angle_limit.setter
    def angle_limit(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=4"]):
        ...
    @property
    def vertex_group(self) -> Annotated[str, "is_animatable=False"]:
        """Vertex group name"""
        ...
    @vertex_group.setter
    def vertex_group(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def invert_vertex_group(self) -> bool:
        """Invert vertex group influence"""
        ...
    @invert_vertex_group.setter
    def invert_vertex_group(self, value: bool):
        ...
    @property
    def use_clamp_overlap(self) -> bool:
        """Clamp the width to avoid overlap"""
        ...
    @use_clamp_overlap.setter
    def use_clamp_overlap(self, value: bool):
        ...
    @property
    def offset_type(self) -> Literal['OFFSET', 'WIDTH', 'DEPTH', 'PERCENT', 'ABSOLUTE']:
        """What distance Width measures"""
        ...
    @offset_type.setter
    def offset_type(self, value: Literal['OFFSET', 'WIDTH', 'DEPTH', 'PERCENT', 'ABSOLUTE']):
        ...
    @property
    def profile_type(self) -> Literal['SUPERELLIPSE', 'CUSTOM']:
        """The type of shape used to rebuild a beveled section"""
        ...
    @profile_type.setter
    def profile_type(self, value: Literal['SUPERELLIPSE', 'CUSTOM']):
        ...
    @property
    def profile(self) -> Annotated[float, "subtype='FACTOR'", "step=0.05000000074505806", "precision=2"]:
        """The profile shape (0.5 = round)"""
        ...
    @profile.setter
    def profile(self, value: Annotated[float, "subtype='FACTOR'", "step=0.05000000074505806", "precision=2"]):
        ...
    @property
    def material(self) -> Annotated[int, "step=1"]:
        """Material index of generated faces, -1 for automatic"""
        ...
    @material.setter
    def material(self, value: Annotated[int, "step=1"]):
        ...
    @property
    def loop_slide(self) -> bool:
        """Prefer sliding along edges to having even widths"""
        ...
    @loop_slide.setter
    def loop_slide(self, value: bool):
        ...
    @property
    def mark_seam(self) -> bool:
        """Mark Seams along beveled edges"""
        ...
    @mark_seam.setter
    def mark_seam(self, value: bool):
        ...
    @property
    def mark_sharp(self) -> bool:
        """Mark beveled edges as sharp"""
        ...
    @mark_sharp.setter
    def mark_sharp(self, value: bool):
        ...
    @property
    def harden_normals(self) -> bool:
        """Match normals of new faces to adjacent faces"""
        ...
    @harden_normals.setter
    def harden_normals(self, value: bool):
        ...
    @property
    def face_strength_mode(self) -> Literal['FSTR_NONE', 'FSTR_NEW', 'FSTR_AFFECTED', 'FSTR_ALL']:
        """Whether to set face strength, and which faces to set it on"""
        ...
    @face_strength_mode.setter
    def face_strength_mode(self, value: Literal['FSTR_NONE', 'FSTR_NEW', 'FSTR_AFFECTED', 'FSTR_ALL']):
        ...
    @property
    def miter_outer(self) -> Literal['MITER_SHARP', 'MITER_PATCH', 'MITER_ARC']:
        """Pattern to use for outside of miters"""
        ...
    @miter_outer.setter
    def miter_outer(self, value: Literal['MITER_SHARP', 'MITER_PATCH', 'MITER_ARC']):
        ...
    @property
    def miter_inner(self) -> Literal['MITER_SHARP', 'MITER_ARC']:
        """Pattern to use for inside of miters"""
        ...
    @miter_inner.setter
    def miter_inner(self, value: Literal['MITER_SHARP', 'MITER_ARC']):
        ...
    @property
    def spread(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.10000000149011612", "precision=4"]:
        """Spread distance for inner miter arcs"""
        ...
    @spread.setter
    def spread(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.10000000149011612", "precision=4"]):
        ...
    @property
    def custom_profile(self) -> Annotated[Optional['CurveProfile'], "is_animatable=False"]:
        """The path for the custom profile"""
        ...
    @property
    def vmesh_method(self) -> Literal['ADJ', 'CUTOFF']:
        """The method to use to create the mesh at intersections"""
        ...
    @vmesh_method.setter
    def vmesh_method(self, value: Literal['ADJ', 'CUTOFF']):
        ...