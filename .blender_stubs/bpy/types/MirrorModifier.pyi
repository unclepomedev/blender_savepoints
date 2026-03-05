# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.MirrorModifier.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .Modifier import Modifier
from .Object import Object

class MirrorModifier(Modifier):

    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:
        """Modifier name"""
        ...
    @name.setter
    def name(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def type(self) -> Literal['GREASE_PENCIL_VERTEX_WEIGHT_PROXIMITY', 'DATA_TRANSFER', 'MESH_CACHE', 'MESH_SEQUENCE_CACHE', 'NORMAL_EDIT', 'WEIGHTED_NORMAL', 'UV_PROJECT', 'UV_WARP', 'VERTEX_WEIGHT_EDIT', 'VERTEX_WEIGHT_MIX', 'VERTEX_WEIGHT_PROXIMITY', 'GREASE_PENCIL_COLOR', 'GREASE_PENCIL_TINT', 'GREASE_PENCIL_OPACITY', 'GREASE_PENCIL_VERTEX_WEIGHT_ANGLE', 'GREASE_PENCIL_TIME', 'GREASE_PENCIL_TEXTURE', 'ARRAY', 'BEVEL', 'BOOLEAN', 'BUILD', 'DECIMATE', 'EDGE_SPLIT', 'NODES', 'MASK', 'MIRROR', 'MESH_TO_VOLUME', 'MULTIRES', 'REMESH', 'SCREW', 'SKIN', 'SOLIDIFY', 'SUBSURF', 'TRIANGULATE', 'VOLUME_TO_MESH', 'WELD', 'WIREFRAME', 'GREASE_PENCIL_ARRAY', 'GREASE_PENCIL_BUILD', 'GREASE_PENCIL_LENGTH', 'LINEART', 'GREASE_PENCIL_MIRROR', 'GREASE_PENCIL_MULTIPLY', 'GREASE_PENCIL_SIMPLIFY', 'GREASE_PENCIL_SUBDIV', 'GREASE_PENCIL_ENVELOPE', 'GREASE_PENCIL_OUTLINE', 'ARMATURE', 'CAST', 'CURVE', 'DISPLACE', 'HOOK', 'LAPLACIANDEFORM', 'LATTICE', 'MESH_DEFORM', 'SHRINKWRAP', 'SIMPLE_DEFORM', 'SMOOTH', 'CORRECTIVE_SMOOTH', 'LAPLACIANSMOOTH', 'SURFACE_DEFORM', 'WARP', 'WAVE', 'VOLUME_DISPLACE', 'GREASE_PENCIL_HOOK', 'GREASE_PENCIL_NOISE', 'GREASE_PENCIL_OFFSET', 'GREASE_PENCIL_SMOOTH', 'GREASE_PENCIL_THICKNESS', 'GREASE_PENCIL_LATTICE', 'GREASE_PENCIL_DASH', 'GREASE_PENCIL_ARMATURE', 'GREASE_PENCIL_SHRINKWRAP', 'CLOTH', 'COLLISION', 'DYNAMIC_PAINT', 'EXPLODE', 'FLUID', 'OCEAN', 'PARTICLE_INSTANCE', 'PARTICLE_SYSTEM', 'SOFT_BODY', 'SURFACE']:

        ...
    @property
    def show_viewport(self) -> bool:
        """Display modifier in viewport"""
        ...
    @show_viewport.setter
    def show_viewport(self, value: bool) -> None:
        ...
    @property
    def show_render(self) -> bool:
        """Use modifier during render"""
        ...
    @show_render.setter
    def show_render(self, value: bool) -> None:
        ...
    @property
    def show_in_editmode(self) -> bool:
        """Display modifier in Edit mode"""
        ...
    @show_in_editmode.setter
    def show_in_editmode(self, value: bool) -> None:
        ...
    @property
    def show_on_cage(self) -> bool:
        """Adjust edit cage to modifier result"""
        ...
    @show_on_cage.setter
    def show_on_cage(self, value: bool) -> None:
        ...
    @property
    def show_expanded(self) -> bool:
        """Set modifier expanded in the user interface"""
        ...
    @show_expanded.setter
    def show_expanded(self, value: bool) -> None:
        ...
    @property
    def is_active(self) -> Annotated[bool, "is_animatable=False"]:
        """The active modifier in the list"""
        ...
    @is_active.setter
    def is_active(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def use_pin_to_last(self) -> Annotated[bool, "is_animatable=False"]:
        """Keep the modifier at the end of the list"""
        ...
    @use_pin_to_last.setter
    def use_pin_to_last(self, value: Annotated[bool, "is_animatable=False"]) -> None:
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
    def use_apply_on_spline(self, value: bool) -> None:
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
    def use_axis(self) -> list[bool]:
        """Enable axis mirror"""
        ...
    @use_axis.setter
    def use_axis(self, value: list[bool]) -> None:
        ...
    @property
    def use_bisect_axis(self) -> list[bool]:
        """Cuts the mesh across the mirror plane"""
        ...
    @use_bisect_axis.setter
    def use_bisect_axis(self, value: list[bool]) -> None:
        ...
    @property
    def use_bisect_flip_axis(self) -> list[bool]:
        """Flips the direction of the slice"""
        ...
    @use_bisect_flip_axis.setter
    def use_bisect_flip_axis(self, value: list[bool]) -> None:
        ...
    @property
    def use_clip(self) -> bool:
        """Prevent vertices from going through the mirror during transform"""
        ...
    @use_clip.setter
    def use_clip(self, value: bool) -> None:
        ...
    @property
    def use_mirror_vertex_groups(self) -> bool:
        """Mirror vertex groups (e.g. .R->.L)"""
        ...
    @use_mirror_vertex_groups.setter
    def use_mirror_vertex_groups(self, value: bool) -> None:
        ...
    @property
    def use_mirror_merge(self) -> bool:
        """Merge vertices within the merge threshold"""
        ...
    @use_mirror_merge.setter
    def use_mirror_merge(self, value: bool) -> None:
        ...
    @property
    def use_mirror_u(self) -> bool:
        """Mirror the U texture coordinate around the flip offset point"""
        ...
    @use_mirror_u.setter
    def use_mirror_u(self, value: bool) -> None:
        ...
    @property
    def use_mirror_v(self) -> bool:
        """Mirror the V texture coordinate around the flip offset point"""
        ...
    @use_mirror_v.setter
    def use_mirror_v(self, value: bool) -> None:
        ...
    @property
    def use_mirror_udim(self) -> bool:
        """Mirror the texture coordinate around each tile center"""
        ...
    @use_mirror_udim.setter
    def use_mirror_udim(self, value: bool) -> None:
        ...
    @property
    def mirror_offset_u(self) -> Annotated[float, "subtype='FACTOR'", "step=2.0", "precision=4"]:
        """Amount to offset mirrored UVs flipping point from the 0.5 on the U axis"""
        ...
    @mirror_offset_u.setter
    def mirror_offset_u(self, value: Annotated[float, "subtype='FACTOR'", "step=2.0", "precision=4"]) -> None:
        ...
    @property
    def mirror_offset_v(self) -> Annotated[float, "subtype='FACTOR'", "step=2.0", "precision=4"]:
        """Amount to offset mirrored UVs flipping point from the 0.5 point on the V axis"""
        ...
    @mirror_offset_v.setter
    def mirror_offset_v(self, value: Annotated[float, "subtype='FACTOR'", "step=2.0", "precision=4"]) -> None:
        ...
    @property
    def offset_u(self) -> Annotated[float, "subtype='FACTOR'", "step=2.0", "precision=4"]:
        """Mirrored UV offset on the U axis"""
        ...
    @offset_u.setter
    def offset_u(self, value: Annotated[float, "subtype='FACTOR'", "step=2.0", "precision=4"]) -> None:
        ...
    @property
    def offset_v(self) -> Annotated[float, "subtype='FACTOR'", "step=2.0", "precision=4"]:
        """Mirrored UV offset on the V axis"""
        ...
    @offset_v.setter
    def offset_v(self, value: Annotated[float, "subtype='FACTOR'", "step=2.0", "precision=4"]) -> None:
        ...
    @property
    def merge_threshold(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.009999999776482582", "precision=6"]:
        """Distance within which mirrored vertices are merged"""
        ...
    @merge_threshold.setter
    def merge_threshold(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.009999999776482582", "precision=6"]) -> None:
        ...
    @property
    def bisect_threshold(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.009999999776482582", "precision=6"]:
        """Distance from the bisect plane within which vertices are removed"""
        ...
    @bisect_threshold.setter
    def bisect_threshold(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.009999999776482582", "precision=6"]) -> None:
        ...
    @property
    def mirror_object(self) -> Annotated[Optional['Object'], "is_animatable=False"]:
        """Object to use as mirror"""
        ...
    @mirror_object.setter
    def mirror_object(self, value: Annotated[Optional['Object'], "is_animatable=False"]) -> None:
        ...