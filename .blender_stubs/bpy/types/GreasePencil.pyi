# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.GreasePencil.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .ID import ID
from .AnimData import AnimData
from .AssetMetaData import AssetMetaData
from .Attribute import Attribute
from .AttributeGroupGreasePencil import AttributeGroupGreasePencil
from .GreasePencilLayer import GreasePencilLayer
from .GreasePencilLayerGroup import GreasePencilLayerGroup
from .GreasePencilv3LayerGroup import GreasePencilv3LayerGroup
from .GreasePencilv3Layers import GreasePencilv3Layers
from .IDMaterials import IDMaterials
from .IDOverrideLibrary import IDOverrideLibrary
from .ImagePreview import ImagePreview
from .Library import Library
from .LibraryWeakReference import LibraryWeakReference
from .Material import Material
from .bpy_prop_collection import bpy_prop_collection

class GreasePencil(ID):

    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:
        """Unique data-block ID name (within a same type and library)"""
        ...
    @name.setter
    def name(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def name_full(self) -> Annotated[str, "is_animatable=False"]:
        """Unique data-block ID name, including library one if any"""
        ...
    @property
    def id_type(self) -> Literal['ACTION', 'ARMATURE', 'BRUSH', 'CACHEFILE', 'CAMERA', 'COLLECTION', 'CURVE', 'CURVES', 'FONT', 'GREASEPENCIL', 'GREASEPENCIL_V3', 'IMAGE', 'KEY', 'LATTICE', 'LIBRARY', 'LIGHT', 'LIGHT_PROBE', 'LINESTYLE', 'MASK', 'MATERIAL', 'MESH', 'META', 'MOVIECLIP', 'NODETREE', 'OBJECT', 'PAINTCURVE', 'PALETTE', 'PARTICLE', 'POINTCLOUD', 'SCENE', 'SCREEN', 'SOUND', 'SPEAKER', 'TEXT', 'TEXTURE', 'VOLUME', 'WINDOWMANAGER', 'WORKSPACE', 'WORLD']:
        """Type identifier of this data-block"""
        ...
    @property
    def session_uid(self) -> Annotated[int, "step=1"]:
        """A session-wide unique identifier for the data block that remains the same across renames and internal reallocations, unchanged when reloading the file"""
        ...
    @property
    def is_evaluated(self) -> bool:
        """Whether this ID is runtime-only, evaluated data-block, or actual data from .blend file"""
        ...
    @property
    def original(self) -> Annotated[Optional['ID'], "is_animatable=False"]:
        """Actual data-block from .blend file (Main database) that generated that evaluated one"""
        ...
    @property
    def users(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Number of times this data-block is referenced"""
        ...
    @property
    def use_fake_user(self) -> bool:
        """Save this data-block even if it has no users"""
        ...
    @use_fake_user.setter
    def use_fake_user(self, value: bool):
        ...
    @property
    def use_extra_user(self) -> bool:
        """Indicates whether an extra user is set or not (mainly for internal/debug usages)"""
        ...
    @use_extra_user.setter
    def use_extra_user(self, value: bool):
        ...
    @property
    def is_embedded_data(self) -> bool:
        """This data-block is not an independent one, but is actually a sub-data of another ID (typical example: root node trees or master collections)"""
        ...
    @property
    def is_linked_packed(self) -> bool:
        """This data-block is linked and packed into the .blend file"""
        ...
    @property
    def is_missing(self) -> bool:
        """This data-block is a place-holder for missing linked data (i.e. it is [an override of] a linked data that could not be found anymore)"""
        ...
    @property
    def is_runtime_data(self) -> bool:
        """This data-block is runtime data, i.e. it won't be saved in .blend file. Note that e.g. evaluated IDs are always runtime, so this value is only editable for data-blocks in Main data-base."""
        ...
    @is_runtime_data.setter
    def is_runtime_data(self, value: bool):
        ...
    @property
    def is_editable(self) -> bool:
        """This data-block is editable in the user interface. Linked data-blocks are not editable, except if they were loaded as editable assets."""
        ...
    @property
    def tag(self) -> bool:
        """Tools can use this to tag data for their own purposes (initial state is undefined)"""
        ...
    @tag.setter
    def tag(self, value: bool):
        ...
    @property
    def is_library_indirect(self) -> bool:
        """Is this ID block linked indirectly"""
        ...
    @property
    def library(self) -> Annotated[Optional['Library'], "is_animatable=False"]:
        """Library file the data-block is linked from"""
        ...
    @property
    def library_weak_reference(self) -> Annotated[Optional['LibraryWeakReference'], "is_animatable=False"]:
        """Weak reference to a data-block in another library .blend file (used to re-use already appended data instead of appending new copies)"""
        ...
    @property
    def asset_data(self) -> Annotated[Optional['AssetMetaData'], "is_animatable=False"]:
        """Additional data for an asset data-block"""
        ...
    @asset_data.setter
    def asset_data(self, value: Annotated[Optional['AssetMetaData'], "is_animatable=False"]):
        ...
    @property
    def override_library(self) -> Annotated[Optional['IDOverrideLibrary'], "is_animatable=False"]:
        """Library override data"""
        ...
    @property
    def preview(self) -> Annotated[Optional['ImagePreview'], "is_animatable=False"]:
        """Preview image and icon of this data-block (always None if not supported for this type of data)"""
        ...
    @property
    def attributes(self) -> Annotated['AttributeGroupGreasePencil', "is_animatable=False"]:
        """Geometry attributes"""
        ...
    @property
    def color_attributes(self) -> Annotated['AttributeGroupGreasePencil', "is_animatable=False"]:
        """Geometry color attributes"""
        ...
    @property
    def animation_data(self) -> Annotated[Optional['AnimData'], "is_animatable=False"]:
        """Animation data for this data-block"""
        ...
    @property
    def materials(self) -> Annotated['IDMaterials', "is_animatable=False"]:

        ...
    @property
    def layers(self) -> Annotated['GreasePencilv3Layers', "is_animatable=False"]:
        """Grease Pencil layers"""
        ...
    @property
    def layer_groups(self) -> Annotated['GreasePencilv3LayerGroup', "is_animatable=False"]:
        """Grease Pencil layer groups"""
        ...
    @property
    def use_autolock_layers(self) -> bool:
        """Automatically lock all layers except the active one to avoid accidental changes"""
        ...
    @use_autolock_layers.setter
    def use_autolock_layers(self, value: bool):
        ...
    @property
    def stroke_depth_order(self) -> Literal['2D', '3D']:
        """Defines how the strokes are ordered in 3D space (for objects not displayed 'In Front')"""
        ...
    @stroke_depth_order.setter
    def stroke_depth_order(self, value: Literal['2D', '3D']):
        ...
    @property
    def ghost_before_range(self) -> Annotated[int, "step=1", "is_animatable=False"]:
        """Maximum number of frames to show before current frame (0 = don't show any frames before current)"""
        ...
    @ghost_before_range.setter
    def ghost_before_range(self, value: Annotated[int, "step=1", "is_animatable=False"]):
        ...
    @property
    def ghost_after_range(self) -> Annotated[int, "step=1", "is_animatable=False"]:
        """Maximum number of frames to show after current frame (0 = don't show any frames after current)"""
        ...
    @ghost_after_range.setter
    def ghost_after_range(self, value: Annotated[int, "step=1", "is_animatable=False"]):
        ...
    @property
    def use_ghost_custom_colors(self) -> Annotated[bool, "is_animatable=False"]:
        """Use custom colors for ghost frames"""
        ...
    @use_ghost_custom_colors.setter
    def use_ghost_custom_colors(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def before_color(self) -> Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Base color for ghosts before the active frame"""
        ...
    @before_color.setter
    def before_color(self, value: Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def after_color(self) -> Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Base color for ghosts after the active frame"""
        ...
    @after_color.setter
    def after_color(self, value: Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def onion_mode(self) -> Annotated[Literal['ABSOLUTE', 'RELATIVE', 'SELECTED'], "is_animatable=False"]:
        """Mode to display frames"""
        ...
    @onion_mode.setter
    def onion_mode(self, value: Annotated[Literal['ABSOLUTE', 'RELATIVE', 'SELECTED'], "is_animatable=False"]):
        ...
    @property
    def onion_keyframe_type(self) -> Annotated[Literal['ALL', 'KEYFRAME', 'BREAKDOWN', 'MOVING_HOLD', 'EXTREME', 'JITTER', 'GENERATED'], "is_animatable=False"]:
        """Type of keyframe (for filtering)"""
        ...
    @onion_keyframe_type.setter
    def onion_keyframe_type(self, value: Annotated[Literal['ALL', 'KEYFRAME', 'BREAKDOWN', 'MOVING_HOLD', 'EXTREME', 'JITTER', 'GENERATED'], "is_animatable=False"]):
        ...
    @property
    def use_onion_fade(self) -> Annotated[bool, "is_animatable=False"]:
        """Display onion keyframes with a fade in color transparency"""
        ...
    @use_onion_fade.setter
    def use_onion_fade(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_onion_loop(self) -> Annotated[bool, "is_animatable=False"]:
        """Display onion keyframes for looping animations"""
        ...
    @use_onion_loop.setter
    def use_onion_loop(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def onion_factor(self) -> Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]:
        """Change fade opacity of displayed onion frames"""
        ...
    @onion_factor.setter
    def onion_factor(self, value: Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    def bl_system_properties_get(self, *args, **kwargs) -> Any: ...
    def rename(self, *args, **kwargs) -> Any: ...
    def evaluated_get(self, *args, **kwargs) -> Any: ...
    def copy(self, *args, **kwargs) -> Any: ...
    def asset_mark(self, *args, **kwargs) -> Any: ...
    def asset_clear(self, *args, **kwargs) -> Any: ...
    def asset_generate_preview(self, *args, **kwargs) -> Any: ...
    def override_create(self, *args, **kwargs) -> Any: ...
    def override_hierarchy_create(self, *args, **kwargs) -> Any: ...
    def user_clear(self, *args, **kwargs) -> Any: ...
    def user_remap(self, *args, **kwargs) -> Any: ...
    def make_local(self, *args, **kwargs) -> Any: ...
    def user_of_id(self, *args, **kwargs) -> Any: ...
    def animation_data_create(self, *args, **kwargs) -> Any: ...
    def animation_data_clear(self, *args, **kwargs) -> Any: ...
    def update_tag(self, *args, **kwargs) -> Any: ...
    def preview_ensure(self, *args, **kwargs) -> Any: ...