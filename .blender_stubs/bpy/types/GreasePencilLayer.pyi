# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.GreasePencilLayer.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .GreasePencilTreeNode import GreasePencilTreeNode
from .GreasePencilFrame import GreasePencilFrame
from .GreasePencilFrames import GreasePencilFrames
from .GreasePencilLayerGroup import GreasePencilLayerGroup
from .GreasePencilLayerMask import GreasePencilLayerMask
from .GreasePencilLayerMasks import GreasePencilLayerMasks
from .Object import Object
from .bpy_prop_collection import bpy_prop_collection

class GreasePencilLayer(GreasePencilTreeNode):

    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:
        """The name of the tree node"""
        ...
    @name.setter
    def name(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def hide(self) -> bool:
        """Set tree node visibility"""
        ...
    @hide.setter
    def hide(self, value: bool) -> None:
        ...
    @property
    def lock(self) -> bool:
        """Protect tree node from editing"""
        ...
    @lock.setter
    def lock(self, value: bool) -> None:
        ...
    @property
    def select(self) -> bool:
        """Tree node is selected"""
        ...
    @select.setter
    def select(self, value: bool) -> None:
        ...
    @property
    def use_onion_skinning(self) -> bool:
        """Display onion skins before and after the current frame"""
        ...
    @use_onion_skinning.setter
    def use_onion_skinning(self, value: bool) -> None:
        ...
    @property
    def use_masks(self) -> bool:
        """The visibility of drawings in this tree node is affected by the layers in the masks list"""
        ...
    @use_masks.setter
    def use_masks(self, value: bool) -> None:
        ...
    @property
    def channel_color(self) -> Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]:
        """Color of the channel in the dope sheet"""
        ...
    @channel_color.setter
    def channel_color(self, value: Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def next_node(self) -> Annotated[Optional['GreasePencilTreeNode'], "is_animatable=False"]:
        """The layer tree node after (i.e. above) this one"""
        ...
    @property
    def prev_node(self) -> Annotated[Optional['GreasePencilTreeNode'], "is_animatable=False"]:
        """The layer tree node before (i.e. below) this one"""
        ...
    @property
    def parent_group(self) -> Annotated[Optional['GreasePencilLayerGroup'], "is_animatable=False"]:
        """The parent group of this layer tree node"""
        ...
    @property
    def frames(self) -> Annotated['GreasePencilFrames', "is_animatable=False"]:
        """Grease Pencil frames"""
        ...
    @property
    def mask_layers(self) -> Annotated['GreasePencilLayerMasks', "is_animatable=False"]:
        """List of Masking Layers"""
        ...
    @property
    def lock_frame(self) -> Annotated[bool, "is_animatable=False"]:
        """Lock current frame displayed by layer"""
        ...
    @lock_frame.setter
    def lock_frame(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def opacity(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Layer Opacity"""
        ...
    @opacity.setter
    def opacity(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def tint_color(self) -> Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]:
        """Color for tinting stroke colors"""
        ...
    @tint_color.setter
    def tint_color(self, value: Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def tint_factor(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Factor of tinting color"""
        ...
    @tint_factor.setter
    def tint_factor(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def radius_offset(self) -> Annotated[float, "subtype='TRANSLATION'", "unit='LENGTH'", "step=1.0", "precision=5"]:
        """Radius change to apply to current strokes"""
        ...
    @radius_offset.setter
    def radius_offset(self, value: Annotated[float, "subtype='TRANSLATION'", "unit='LENGTH'", "step=1.0", "precision=5"]) -> None:
        ...
    @property
    def use_lights(self) -> bool:
        """Enable the use of lights on stroke and fill materials"""
        ...
    @use_lights.setter
    def use_lights(self, value: bool) -> None:
        ...
    @property
    def pass_index(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Index number for the "Layer Index" pass"""
        ...
    @pass_index.setter
    def pass_index(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1"]) -> None:
        ...
    @property
    def parent(self) -> Annotated[Optional['Object'], "is_animatable=False"]:
        """Parent object"""
        ...
    @parent.setter
    def parent(self, value: Annotated[Optional['Object'], "is_animatable=False"]) -> None:
        ...
    @property
    def parent_bone(self) -> Annotated[str, "is_animatable=False"]:
        """Name of parent bone. Only used when the parent object is an armature."""
        ...
    @parent_bone.setter
    def parent_bone(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def translation(self) -> Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=1.0", "precision=5"]:
        """Translation of the layer"""
        ...
    @translation.setter
    def translation(self, value: Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=1.0", "precision=5"]) -> None:
        ...
    @property
    def rotation(self) -> Annotated[list[float], "subtype='EULER'", "unit='ROTATION'", "step=1.0", "precision=5"]:
        """Euler rotation of the layer"""
        ...
    @rotation.setter
    def rotation(self, value: Annotated[list[float], "subtype='EULER'", "unit='ROTATION'", "step=1.0", "precision=5"]) -> None:
        ...
    @property
    def scale(self) -> Annotated[list[float], "subtype='XYZ'", "step=1.0", "precision=3"]:
        """Scale of the layer"""
        ...
    @scale.setter
    def scale(self, value: Annotated[list[float], "subtype='XYZ'", "step=1.0", "precision=3"]) -> None:
        ...
    @property
    def viewlayer_render(self) -> Annotated[str, "is_animatable=False"]:
        """Only include Layer in this View Layer render output (leave blank to include always)"""
        ...
    @viewlayer_render.setter
    def viewlayer_render(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def use_viewlayer_masks(self) -> bool:
        """Include the mask layers when rendering the view-layer"""
        ...
    @use_viewlayer_masks.setter
    def use_viewlayer_masks(self, value: bool) -> None:
        ...
    @property
    def blend_mode(self) -> Literal['REGULAR', 'HARDLIGHT', 'ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE']:
        """Blend mode"""
        ...
    @blend_mode.setter
    def blend_mode(self, value: Literal['REGULAR', 'HARDLIGHT', 'ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE']) -> None:
        ...
    @property
    def ignore_locked_materials(self) -> Annotated[bool, "is_animatable=False"]:
        """Allow editing strokes even if they use locked materials"""
        ...
    @ignore_locked_materials.setter
    def ignore_locked_materials(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def matrix_local(self) -> Annotated[list[float], "subtype='MATRIX'", "step=10.0", "precision=3"]:
        """Local transformation matrix of the layer"""
        ...
    @property
    def matrix_parent_inverse(self) -> Annotated[list[float], "subtype='MATRIX'", "step=10.0", "precision=3"]:
        """Inverse of layer's parent transformation matrix"""
        ...
    def get_frame_at(self, *args, **kwargs) -> Any: ...
    def current_frame(self, *args, **kwargs) -> Any: ...