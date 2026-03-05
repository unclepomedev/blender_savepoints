# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.CompositorNodeCryptomatteV2.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .CompositorNode import CompositorNode
from .CryptomatteEntry import CryptomatteEntry
from .Image import Image
from .Node import Node
from .NodeInputs import NodeInputs
from .NodeLink import NodeLink
from .NodeOutputs import NodeOutputs
from .NodeSocket import NodeSocket
from .Scene import Scene
from .bpy_prop_collection import bpy_prop_collection

class CompositorNodeCryptomatteV2(CompositorNode):

    @property
    def type(self) -> Annotated[str, "is_animatable=False"]:
        """Legacy unique node type identifier, redundant with bl_idname property"""
        ...
    @property
    def location(self) -> Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]:
        """Location of the node within its parent frame"""
        ...
    @location.setter
    def location(self, value: Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def location_absolute(self) -> Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]:
        """Location of the node in the entire canvas"""
        ...
    @location_absolute.setter
    def location_absolute(self, value: Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def width(self) -> Annotated[float, "subtype='XYZ'", "step=10.0", "precision=3"]:
        """Width of the node"""
        ...
    @width.setter
    def width(self, value: Annotated[float, "subtype='XYZ'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def height(self) -> Annotated[float, "subtype='XYZ'", "step=10.0", "precision=3"]:
        """Height of the node"""
        ...
    @height.setter
    def height(self, value: Annotated[float, "subtype='XYZ'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def dimensions(self) -> Annotated[list[float], "subtype='XYZ_LENGTH'", "unit='LENGTH'", "step=10.0", "precision=3"]:
        """Absolute bounding box dimensions of the node"""
        ...
    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:
        """Unique node identifier"""
        ...
    @name.setter
    def name(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def label(self) -> Annotated[str, "is_animatable=False"]:
        """Optional custom node label"""
        ...
    @label.setter
    def label(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
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
    @property
    def parent(self) -> Annotated[Optional['Node'], "is_animatable=False"]:
        """Parent this node is attached to"""
        ...
    @parent.setter
    def parent(self, value: Annotated[Optional['Node'], "is_animatable=False"]) -> None:
        ...
    @property
    def warning_propagation(self) -> Literal['ALL', 'NONE', 'ERRORS', 'ERRORS_AND_WARNINGS']:
        """The kinds of messages that should be propagated from this node to the parent group node"""
        ...
    @warning_propagation.setter
    def warning_propagation(self, value: Literal['ALL', 'NONE', 'ERRORS', 'ERRORS_AND_WARNINGS']) -> None:
        ...
    @property
    def use_custom_color(self) -> Annotated[bool, "is_animatable=False"]:
        """Use custom color for the node"""
        ...
    @use_custom_color.setter
    def use_custom_color(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def color(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:
        """Custom color of the node body"""
        ...
    @color.setter
    def color(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def color_tag(self) -> Literal['NONE', 'ATTRIBUTE', 'COLOR', 'CONVERTER', 'DISTORT', 'FILTER', 'GEOMETRY', 'INPUT', 'MATTE', 'OUTPUT', 'SCRIPT', 'SHADER', 'TEXTURE', 'VECTOR', 'PATTERN', 'INTERFACE', 'GROUP']:
        """Node header color tag"""
        ...
    @property
    def select(self) -> bool:
        """Node selection state"""
        ...
    @select.setter
    def select(self, value: bool) -> None:
        ...
    @property
    def show_options(self) -> bool:

        ...
    @show_options.setter
    def show_options(self, value: bool) -> None:
        ...
    @property
    def show_preview(self) -> bool:

        ...
    @show_preview.setter
    def show_preview(self, value: bool) -> None:
        ...
    @property
    def hide(self) -> bool:

        ...
    @hide.setter
    def hide(self, value: bool) -> None:
        ...
    @property
    def mute(self) -> Annotated[bool, "is_animatable=False"]:

        ...
    @mute.setter
    def mute(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def show_texture(self) -> bool:
        """Display node in viewport textured shading mode"""
        ...
    @show_texture.setter
    def show_texture(self, value: bool) -> None:
        ...
    bl_idname: Annotated[str, "is_animatable=False"]
    bl_label: Annotated[str, "is_animatable=False"]
    """The node label"""
    bl_description: Annotated[str, "subtype='TRANSLATION'", "unit='LENGTH'", "is_animatable=False"]
    bl_icon: str
    """The node icon"""
    bl_static_type: Annotated[str, "is_animatable=False"]
    """Legacy unique node type identifier, redundant with bl_idname property"""
    bl_width_default: Annotated[float, "subtype='UNSIGNED'", "step=10.0", "precision=3"]
    bl_width_min: Annotated[float, "subtype='UNSIGNED'", "step=10.0", "precision=3"]
    bl_width_max: Annotated[float, "subtype='UNSIGNED'", "step=10.0", "precision=3"]
    bl_height_default: Annotated[float, "subtype='UNSIGNED'", "step=10.0", "precision=3"]
    bl_height_min: Annotated[float, "subtype='UNSIGNED'", "step=10.0", "precision=3"]
    bl_height_max: Annotated[float, "subtype='UNSIGNED'", "step=10.0", "precision=3"]
    @property
    def source(self) -> Literal['RENDER', 'IMAGE']:
        """Where the Cryptomatte passes are loaded from"""
        ...
    @source.setter
    def source(self, value: Literal['RENDER', 'IMAGE']) -> None:
        ...
    @property
    def scene(self) -> Annotated[Optional['Scene'], "is_animatable=False"]:

        ...
    @scene.setter
    def scene(self, value: Annotated[Optional['Scene'], "is_animatable=False"]) -> None:
        ...
    @property
    def image(self) -> Annotated[Optional['Image'], "is_animatable=False"]:

        ...
    @image.setter
    def image(self, value: Annotated[Optional['Image'], "is_animatable=False"]) -> None:
        ...
    @property
    def matte_id(self) -> Annotated[str, "is_animatable=False"]:
        """List of object and material crypto IDs to include in matte"""
        ...
    @matte_id.setter
    def matte_id(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def add(self) -> Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]:
        """Add object or material to matte, by picking a color from the Pick output"""
        ...
    @add.setter
    def add(self, value: Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def remove(self) -> Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]:
        """Remove object or material from matte, by picking a color from the Pick output"""
        ...
    @remove.setter
    def remove(self, value: Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def layer_name(self) -> Literal['CryptoObject', 'CryptoMaterial', 'CryptoAsset']:
        """What Cryptomatte layer is used"""
        ...
    @layer_name.setter
    def layer_name(self, value: Literal['CryptoObject', 'CryptoMaterial', 'CryptoAsset']) -> None:
        ...
    @property
    def entries(self) -> Annotated[bpy_prop_collection['CryptomatteEntry'], "is_animatable=False"]:

        ...
    @property
    def frame_duration(self) -> Annotated[int, "step=1"]:
        """Number of images of a movie to use"""
        ...
    @frame_duration.setter
    def frame_duration(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def frame_start(self) -> Annotated[int, "step=1"]:
        """Global starting frame of the movie/sequence, assuming first picture has a #1"""
        ...
    @frame_start.setter
    def frame_start(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def frame_offset(self) -> Annotated[int, "step=1"]:
        """Offset the number of the frame to use in the animation"""
        ...
    @frame_offset.setter
    def frame_offset(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def use_cyclic(self) -> bool:
        """Cycle the images in the movie"""
        ...
    @use_cyclic.setter
    def use_cyclic(self, value: bool) -> None:
        ...
    @property
    def use_auto_refresh(self) -> bool:
        """Always refresh image on frame changes"""
        ...
    @use_auto_refresh.setter
    def use_auto_refresh(self, value: bool) -> None:
        ...
    @property
    def layer(self) -> Literal['PLACEHOLDER']:

        ...
    @layer.setter
    def layer(self, value: Literal['PLACEHOLDER']) -> None:
        ...
    @property
    def has_layers(self) -> bool:
        """True if this image has any named layer"""
        ...
    @property
    def view(self) -> Literal['ALL']:

        ...
    @view.setter
    def view(self, value: Literal['ALL']) -> None:
        ...
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