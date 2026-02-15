# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated
from .bpy_prop_collection import bpy_prop_collection

from .GreasePencilTreeNode import GreasePencilTreeNode
from .GreasePencilFrame import GreasePencilFrame
from .GreasePencilFrames import GreasePencilFrames
from .GreasePencilLayerGroup import GreasePencilLayerGroup
from .GreasePencilLayerMask import GreasePencilLayerMask
from .GreasePencilLayerMasks import GreasePencilLayerMasks
from .Object import Object
class GreasePencilLayer(GreasePencilTreeNode):
    name: Annotated[str, "is_animatable=False"]
    """The name of the tree node"""
    hide: bool
    """Set tree node visibility"""
    lock: bool
    """Protect tree node from editing"""
    select: bool
    """Tree node is selected"""
    use_onion_skinning: bool
    """Display onion skins before and after the current frame"""
    use_masks: bool
    """The visibility of drawings in this tree node is affected by the layers in the masks list"""
    channel_color: Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]
    """Color of the channel in the dope sheet"""
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
    lock_frame: Annotated[bool, "is_animatable=False"]
    """Lock current frame displayed by layer"""
    opacity: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Layer Opacity"""
    tint_color: Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]
    """Color for tinting stroke colors"""
    tint_factor: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Factor of tinting color"""
    radius_offset: Annotated[float, "subtype='TRANSLATION'", "unit='LENGTH'", "step=1.0", "precision=5"]
    """Radius change to apply to current strokes"""
    use_lights: bool
    """Enable the use of lights on stroke and fill materials"""
    pass_index: Annotated[int, "subtype='UNSIGNED'", "step=1"]
    """Index number for the "Layer Index" pass"""
    parent: Annotated[Optional['Object'], "is_animatable=False"]
    """Parent object"""
    parent_bone: Annotated[str, "is_animatable=False"]
    """Name of parent bone. Only used when the parent object is an armature."""
    translation: Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=1.0", "precision=5"]
    """Translation of the layer"""
    rotation: Annotated[list[float], "subtype='EULER'", "unit='ROTATION'", "step=1.0", "precision=5"]
    """Euler rotation of the layer"""
    scale: Annotated[list[float], "subtype='XYZ'", "step=1.0", "precision=3"]
    """Scale of the layer"""
    viewlayer_render: Annotated[str, "is_animatable=False"]
    """Only include Layer in this View Layer render output (leave blank to include always)"""
    use_viewlayer_masks: bool
    """Include the mask layers when rendering the view-layer"""
    blend_mode: Literal['REGULAR', 'HARDLIGHT', 'ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE']
    """Blend mode"""
    ignore_locked_materials: Annotated[bool, "is_animatable=False"]
    """Allow editing strokes even if they use locked materials"""
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