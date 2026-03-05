# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.DataTransferModifier.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .Modifier import Modifier
from .Object import Object

class DataTransferModifier(Modifier):

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
    def object(self) -> Annotated[Optional['Object'], "is_animatable=False"]:
        """Object to transfer data from"""
        ...
    @object.setter
    def object(self, value: Annotated[Optional['Object'], "is_animatable=False"]):
        ...
    @property
    def use_object_transform(self) -> bool:
        """Evaluate source and destination meshes in global space"""
        ...
    @use_object_transform.setter
    def use_object_transform(self, value: bool):
        ...
    @property
    def use_vert_data(self) -> bool:
        """Enable vertex data transfer"""
        ...
    @use_vert_data.setter
    def use_vert_data(self, value: bool):
        ...
    @property
    def use_edge_data(self) -> bool:
        """Enable edge data transfer"""
        ...
    @use_edge_data.setter
    def use_edge_data(self, value: bool):
        ...
    @property
    def use_loop_data(self) -> bool:
        """Enable face corner data transfer"""
        ...
    @use_loop_data.setter
    def use_loop_data(self, value: bool):
        ...
    @property
    def use_poly_data(self) -> bool:
        """Enable face data transfer"""
        ...
    @use_poly_data.setter
    def use_poly_data(self, value: bool):
        ...
    @property
    def data_types_verts(self) -> set[str]:
        """Which vertex data layers to transfer"""
        ...
    @data_types_verts.setter
    def data_types_verts(self, value: set[str]):
        ...
    @property
    def data_types_edges(self) -> set[str]:
        """Which edge data layers to transfer"""
        ...
    @data_types_edges.setter
    def data_types_edges(self, value: set[str]):
        ...
    @property
    def data_types_loops(self) -> set[str]:
        """Which face corner data layers to transfer"""
        ...
    @data_types_loops.setter
    def data_types_loops(self, value: set[str]):
        ...
    @property
    def data_types_polys(self) -> set[str]:
        """Which face data layers to transfer"""
        ...
    @data_types_polys.setter
    def data_types_polys(self, value: set[str]):
        ...
    @property
    def vert_mapping(self) -> Literal['TOPOLOGY', 'NEAREST', 'EDGE_NEAREST', 'EDGEINTERP_NEAREST', 'POLY_NEAREST', 'POLYINTERP_NEAREST', 'POLYINTERP_VNORPROJ']:
        """Method used to map source vertices to destination ones"""
        ...
    @vert_mapping.setter
    def vert_mapping(self, value: Literal['TOPOLOGY', 'NEAREST', 'EDGE_NEAREST', 'EDGEINTERP_NEAREST', 'POLY_NEAREST', 'POLYINTERP_NEAREST', 'POLYINTERP_VNORPROJ']):
        ...
    @property
    def edge_mapping(self) -> Literal['TOPOLOGY', 'VERT_NEAREST', 'NEAREST', 'POLY_NEAREST', 'EDGEINTERP_VNORPROJ']:
        """Method used to map source edges to destination ones"""
        ...
    @edge_mapping.setter
    def edge_mapping(self, value: Literal['TOPOLOGY', 'VERT_NEAREST', 'NEAREST', 'POLY_NEAREST', 'EDGEINTERP_VNORPROJ']):
        ...
    @property
    def loop_mapping(self) -> Literal['TOPOLOGY', 'NEAREST_NORMAL', 'NEAREST_POLYNOR', 'NEAREST_POLY', 'POLYINTERP_NEAREST', 'POLYINTERP_LNORPROJ']:
        """Method used to map source faces' corners to destination ones"""
        ...
    @loop_mapping.setter
    def loop_mapping(self, value: Literal['TOPOLOGY', 'NEAREST_NORMAL', 'NEAREST_POLYNOR', 'NEAREST_POLY', 'POLYINTERP_NEAREST', 'POLYINTERP_LNORPROJ']):
        ...
    @property
    def poly_mapping(self) -> Literal['TOPOLOGY', 'NEAREST', 'NORMAL', 'POLYINTERP_PNORPROJ']:
        """Method used to map source faces to destination ones"""
        ...
    @poly_mapping.setter
    def poly_mapping(self, value: Literal['TOPOLOGY', 'NEAREST', 'NORMAL', 'POLYINTERP_PNORPROJ']):
        ...
    @property
    def use_max_distance(self) -> bool:
        """Source elements must be closer than given distance from destination one"""
        ...
    @use_max_distance.setter
    def use_max_distance(self, value: bool):
        ...
    @property
    def max_distance(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=1.0", "precision=3"]:
        """Maximum allowed distance between source and destination element, for non-topology mappings"""
        ...
    @max_distance.setter
    def max_distance(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=1.0", "precision=3"]):
        ...
    @property
    def ray_radius(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=1.0", "precision=3"]:
        """'Width' of rays (especially useful when raycasting against vertices or edges)"""
        ...
    @ray_radius.setter
    def ray_radius(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=1.0", "precision=3"]):
        ...
    @property
    def islands_precision(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=1.0", "precision=3"]:
        """Factor controlling precision of islands handling (typically, 0.1 should be enough, higher values can make things really slow)"""
        ...
    @islands_precision.setter
    def islands_precision(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=1.0", "precision=3"]):
        ...
    @property
    def layers_vgroup_select_src(self) -> Literal['ACTIVE', 'ALL', 'BONE_SELECT', 'BONE_DEFORM']:
        """Which layers to transfer, in case of multi-layers types"""
        ...
    @layers_vgroup_select_src.setter
    def layers_vgroup_select_src(self, value: Literal['ACTIVE', 'ALL', 'BONE_SELECT', 'BONE_DEFORM']):
        ...
    @property
    def layers_vcol_vert_select_src(self) -> Literal['ACTIVE', 'ALL', 'BONE_SELECT', 'BONE_DEFORM']:
        """Which layers to transfer, in case of multi-layers types"""
        ...
    @layers_vcol_vert_select_src.setter
    def layers_vcol_vert_select_src(self, value: Literal['ACTIVE', 'ALL', 'BONE_SELECT', 'BONE_DEFORM']):
        ...
    @property
    def layers_vcol_loop_select_src(self) -> Literal['ACTIVE', 'ALL', 'BONE_SELECT', 'BONE_DEFORM']:
        """Which layers to transfer, in case of multi-layers types"""
        ...
    @layers_vcol_loop_select_src.setter
    def layers_vcol_loop_select_src(self, value: Literal['ACTIVE', 'ALL', 'BONE_SELECT', 'BONE_DEFORM']):
        ...
    @property
    def layers_uv_select_src(self) -> Literal['ACTIVE', 'ALL', 'BONE_SELECT', 'BONE_DEFORM']:
        """Which layers to transfer, in case of multi-layers types"""
        ...
    @layers_uv_select_src.setter
    def layers_uv_select_src(self, value: Literal['ACTIVE', 'ALL', 'BONE_SELECT', 'BONE_DEFORM']):
        ...
    @property
    def layers_vgroup_select_dst(self) -> Literal['ACTIVE', 'NAME', 'INDEX']:
        """How to match source and destination layers"""
        ...
    @layers_vgroup_select_dst.setter
    def layers_vgroup_select_dst(self, value: Literal['ACTIVE', 'NAME', 'INDEX']):
        ...
    @property
    def layers_vcol_vert_select_dst(self) -> Literal['ACTIVE', 'NAME', 'INDEX']:
        """How to match source and destination layers"""
        ...
    @layers_vcol_vert_select_dst.setter
    def layers_vcol_vert_select_dst(self, value: Literal['ACTIVE', 'NAME', 'INDEX']):
        ...
    @property
    def layers_vcol_loop_select_dst(self) -> Literal['ACTIVE', 'NAME', 'INDEX']:
        """How to match source and destination layers"""
        ...
    @layers_vcol_loop_select_dst.setter
    def layers_vcol_loop_select_dst(self, value: Literal['ACTIVE', 'NAME', 'INDEX']):
        ...
    @property
    def layers_uv_select_dst(self) -> Literal['ACTIVE', 'NAME', 'INDEX']:
        """How to match source and destination layers"""
        ...
    @layers_uv_select_dst.setter
    def layers_uv_select_dst(self, value: Literal['ACTIVE', 'NAME', 'INDEX']):
        ...
    @property
    def mix_mode(self) -> Literal['REPLACE', 'ABOVE_THRESHOLD', 'BELOW_THRESHOLD', 'MIX', 'ADD', 'SUB', 'MUL']:
        """How to affect destination elements with source values"""
        ...
    @mix_mode.setter
    def mix_mode(self, value: Literal['REPLACE', 'ABOVE_THRESHOLD', 'BELOW_THRESHOLD', 'MIX', 'ADD', 'SUB', 'MUL']):
        ...
    @property
    def mix_factor(self) -> Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=3"]:
        """Factor to use when applying data to destination (exact behavior depends on mix mode, multiplied with weights from vertex group when defined)"""
        ...
    @mix_factor.setter
    def mix_factor(self, value: Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=3"]):
        ...
    @property
    def vertex_group(self) -> Annotated[str, "is_animatable=False"]:
        """Vertex group name for selecting the affected areas"""
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