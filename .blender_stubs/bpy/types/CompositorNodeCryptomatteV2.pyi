# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated
from .bpy_prop_collection import bpy_prop_collection

from .CompositorNode import CompositorNode
from .CryptomatteEntry import CryptomatteEntry
from .Image import Image
from .Node import Node
from .NodeInputs import NodeInputs
from .NodeLink import NodeLink
from .NodeOutputs import NodeOutputs
from .NodeSocket import NodeSocket
from .Scene import Scene
class CompositorNodeCryptomatteV2(CompositorNode):
    @property
    def type(self) -> Annotated[str, "is_animatable=False"]:
        """Legacy unique node type identifier, redundant with bl_idname property"""
        ...
    location: Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]
    """Location of the node within its parent frame"""
    location_absolute: Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]
    """Location of the node in the entire canvas"""
    width: Annotated[float, "subtype='XYZ'", "step=10.0", "precision=3"]
    """Width of the node"""
    height: Annotated[float, "subtype='XYZ'", "step=10.0", "precision=3"]
    """Height of the node"""
    @property
    def dimensions(self) -> Annotated[list[float], "subtype='XYZ_LENGTH'", "unit='LENGTH'", "step=10.0", "precision=3"]:
        """Absolute bounding box dimensions of the node"""
        ...
    name: Annotated[str, "is_animatable=False"]
    """Unique node identifier"""
    label: Annotated[str, "is_animatable=False"]
    """Optional custom node label"""
    @property
    def inputs(self) -> Annotated['NodeInputs', "is_animatable=False"]:
        ...
    @property
    def outputs(self) -> Annotated['NodeOutputs', "is_animatable=False"]:
        ...
    @property
    def internal_links(self) -> Annotated[bpy_prop_collection['NodeLink'], "is_animatable=False"]:
        """Internal input-to-output connections for muting"""
        ...
    parent: Annotated[Optional['Node'], "is_animatable=False"]
    """Parent this node is attached to"""
    warning_propagation: Literal['ALL', 'NONE', 'ERRORS', 'ERRORS_AND_WARNINGS']
    """The kinds of messages that should be propagated from this node to the parent group node"""
    use_custom_color: Annotated[bool, "is_animatable=False"]
    """Use custom color for the node"""
    color: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    """Custom color of the node body"""
    @property
    def color_tag(self) -> Literal['NONE', 'ATTRIBUTE', 'COLOR', 'CONVERTER', 'DISTORT', 'FILTER', 'GEOMETRY', 'INPUT', 'MATTE', 'OUTPUT', 'SCRIPT', 'SHADER', 'TEXTURE', 'VECTOR', 'PATTERN', 'INTERFACE', 'GROUP']:
        """Node header color tag"""
        ...
    select: bool
    """Node selection state"""
    show_options: bool
    show_preview: bool
    hide: bool
    mute: Annotated[bool, "is_animatable=False"]
    show_texture: bool
    """Display node in viewport textured shading mode"""
    bl_idname: Annotated[str, "is_animatable=False"]
    bl_label: Annotated[str, "is_animatable=False"]
    """The node label"""
    bl_description: Annotated[str, "subtype='TRANSLATION'", "unit='LENGTH'", "is_animatable=False"]
    bl_icon: str
    """The node icon"""
    @property
    def bl_static_type(self) -> Annotated[str, "is_animatable=False"]:
        """Legacy unique node type identifier, redundant with bl_idname property"""
        ...
    bl_width_default: Annotated[float, "subtype='UNSIGNED'", "step=10.0", "precision=3"]
    bl_width_min: Annotated[float, "subtype='UNSIGNED'", "step=10.0", "precision=3"]
    bl_width_max: Annotated[float, "subtype='UNSIGNED'", "step=10.0", "precision=3"]
    bl_height_default: Annotated[float, "subtype='UNSIGNED'", "step=10.0", "precision=3"]
    bl_height_min: Annotated[float, "subtype='UNSIGNED'", "step=10.0", "precision=3"]
    bl_height_max: Annotated[float, "subtype='UNSIGNED'", "step=10.0", "precision=3"]
    source: Literal['RENDER', 'IMAGE']
    """Where the Cryptomatte passes are loaded from"""
    scene: Annotated[Optional['Scene'], "is_animatable=False"]
    image: Annotated[Optional['Image'], "is_animatable=False"]
    matte_id: Annotated[str, "is_animatable=False"]
    """List of object and material crypto IDs to include in matte"""
    add: Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]
    """Add object or material to matte, by picking a color from the Pick output"""
    remove: Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]
    """Remove object or material from matte, by picking a color from the Pick output"""
    layer_name: Literal['CryptoObject', 'CryptoMaterial', 'CryptoAsset']
    """What Cryptomatte layer is used"""
    @property
    def entries(self) -> Annotated[bpy_prop_collection['CryptomatteEntry'], "is_animatable=False"]:
        ...
    frame_duration: Annotated[int, "step=1"]
    """Number of images of a movie to use"""
    frame_start: Annotated[int, "step=1"]
    """Global starting frame of the movie/sequence, assuming first picture has a #1"""
    frame_offset: Annotated[int, "step=1"]
    """Offset the number of the frame to use in the animation"""
    use_cyclic: bool
    """Cycle the images in the movie"""
    use_auto_refresh: bool
    """Always refresh image on frame changes"""
    layer: Literal['PLACEHOLDER']
    @property
    def has_layers(self) -> bool:
        """True if this image has any named layer"""
        ...
    view: Literal['ALL']
    @property
    def has_views(self) -> bool:
        """True if this image has multiple views"""
        ...
    def bl_system_properties_get(self, *args, **kwargs) -> Any: ...
    def socket_value_update(self, *args, **kwargs) -> Any: ...
    def is_registered_node_type(self, *args, **kwargs) -> Any: ...
    def poll(self, *args, **kwargs) -> Any: ...
    def poll_instance(self, *args, **kwargs) -> Any: ...
    def update(self, *args, **kwargs) -> Any: ...
    def insert_link(self, *args, **kwargs) -> Any: ...
    def init(self, *args, **kwargs) -> Any: ...
    def copy(self, *args, **kwargs) -> Any: ...
    def free(self, *args, **kwargs) -> Any: ...
    def draw_buttons(self, *args, **kwargs) -> Any: ...
    def draw_buttons_ext(self, *args, **kwargs) -> Any: ...
    def draw_label(self, *args, **kwargs) -> Any: ...
    def debug_zone_body_lazy_function_graph(self, *args, **kwargs) -> Any: ...
    def debug_zone_lazy_function_graph(self, *args, **kwargs) -> Any: ...
    def poll(self, *args, **kwargs) -> Any: ...
    def poll_instance(self, *args, **kwargs) -> Any: ...
    def update(self, *args, **kwargs) -> Any: ...
    def draw_buttons(self, *args, **kwargs) -> Any: ...
    def draw_buttons_ext(self, *args, **kwargs) -> Any: ...
    def tag_need_exec(self, *args, **kwargs) -> Any: ...
    def is_registered_node_type(self, *args, **kwargs) -> Any: ...
    def input_template(self, *args, **kwargs) -> Any: ...
    def output_template(self, *args, **kwargs) -> Any: ...