# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.NodesModifier.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .Modifier import Modifier
from .NodeTree import NodeTree
from .NodesModifierBake import NodesModifierBake
from .NodesModifierBakes import NodesModifierBakes
from .NodesModifierPanel import NodesModifierPanel
from .NodesModifierPanels import NodesModifierPanels
from .NodesModifierWarning import NodesModifierWarning
from .bpy_prop_collection import bpy_prop_collection

class NodesModifier(Modifier):

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
    def node_group(self) -> Annotated[Optional['NodeTree'], "is_animatable=False"]:
        """Node group that controls what this modifier does"""
        ...
    @node_group.setter
    def node_group(self, value: Annotated[Optional['NodeTree'], "is_animatable=False"]):
        ...
    @property
    def bake_directory(self) -> Annotated[str, "subtype='DIR_PATH'", "is_animatable=False"]:
        """Location on disk where the bake data is stored"""
        ...
    @bake_directory.setter
    def bake_directory(self, value: Annotated[str, "subtype='DIR_PATH'", "is_animatable=False"]):
        ...
    @property
    def bake_target(self) -> Literal['PACKED', 'DISK']:
        """Where to store the baked data"""
        ...
    @bake_target.setter
    def bake_target(self, value: Literal['PACKED', 'DISK']):
        ...
    @property
    def bakes(self) -> Annotated['NodesModifierBakes', "is_animatable=False"]:

        ...
    @property
    def panels(self) -> Annotated['NodesModifierPanels', "is_animatable=False"]:

        ...
    @property
    def show_group_selector(self) -> bool:

        ...
    @show_group_selector.setter
    def show_group_selector(self, value: bool):
        ...
    @property
    def show_manage_panel(self) -> bool:

        ...
    @show_manage_panel.setter
    def show_manage_panel(self, value: bool):
        ...
    @property
    def node_warnings(self) -> Annotated[bpy_prop_collection['NodesModifierWarning'], "is_animatable=False"]:

        ...
    @property
    def open_output_attributes_panel(self) -> bool:

        ...
    @open_output_attributes_panel.setter
    def open_output_attributes_panel(self, value: bool):
        ...
    @property
    def open_manage_panel(self) -> bool:

        ...
    @open_manage_panel.setter
    def open_manage_panel(self, value: bool):
        ...
    @property
    def open_bake_panel(self) -> bool:

        ...
    @open_bake_panel.setter
    def open_bake_panel(self, value: bool):
        ...
    @property
    def open_named_attributes_panel(self) -> bool:

        ...
    @open_named_attributes_panel.setter
    def open_named_attributes_panel(self, value: bool):
        ...
    @property
    def open_bake_data_blocks_panel(self) -> bool:

        ...
    @open_bake_data_blocks_panel.setter
    def open_bake_data_blocks_panel(self, value: bool):
        ...
    @property
    def open_warnings_panel(self) -> bool:

        ...
    @open_warnings_panel.setter
    def open_warnings_panel(self, value: bool):
        ...
    def bl_system_properties_get(self, *args, **kwargs) -> Any: ...