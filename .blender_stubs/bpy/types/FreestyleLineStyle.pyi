# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.FreestyleLineStyle.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .ID import ID
from .AnimData import AnimData
from .AssetMetaData import AssetMetaData
from .IDOverrideLibrary import IDOverrideLibrary
from .ImagePreview import ImagePreview
from .Library import Library
from .LibraryWeakReference import LibraryWeakReference
from .LineStyleAlphaModifier import LineStyleAlphaModifier
from .LineStyleAlphaModifiers import LineStyleAlphaModifiers
from .LineStyleColorModifier import LineStyleColorModifier
from .LineStyleColorModifiers import LineStyleColorModifiers
from .LineStyleGeometryModifier import LineStyleGeometryModifier
from .LineStyleGeometryModifiers import LineStyleGeometryModifiers
from .LineStyleTextureSlot import LineStyleTextureSlot
from .LineStyleTextureSlots import LineStyleTextureSlots
from .LineStyleThicknessModifier import LineStyleThicknessModifier
from .LineStyleThicknessModifiers import LineStyleThicknessModifiers
from .NodeTree import NodeTree
from .Texture import Texture
from .bpy_prop_collection import bpy_prop_collection

class FreestyleLineStyle(ID):

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
    def texture_slots(self) -> Annotated['LineStyleTextureSlots', "is_animatable=False"]:
        """Texture slots defining the mapping and influence of textures"""
        ...
    @property
    def active_texture(self) -> Annotated[Optional['Texture'], "is_animatable=False"]:
        """Active texture slot being displayed"""
        ...
    @active_texture.setter
    def active_texture(self, value: Annotated[Optional['Texture'], "is_animatable=False"]):
        ...
    @property
    def active_texture_index(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Index of active texture slot"""
        ...
    @active_texture_index.setter
    def active_texture_index(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1"]):
        ...
    @property
    def panel(self) -> Annotated[Literal['STROKES', 'COLOR', 'ALPHA', 'THICKNESS', 'GEOMETRY', 'TEXTURE'], "is_animatable=False"]:
        """Select the property panel to be shown"""
        ...
    @panel.setter
    def panel(self, value: Annotated[Literal['STROKES', 'COLOR', 'ALPHA', 'THICKNESS', 'GEOMETRY', 'TEXTURE'], "is_animatable=False"]):
        ...
    @property
    def color(self) -> Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]:
        """Base line color, possibly modified by line color modifiers"""
        ...
    @color.setter
    def color(self, value: Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def alpha(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Base alpha transparency, possibly modified by alpha transparency modifiers"""
        ...
    @alpha.setter
    def alpha(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def thickness(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Base line thickness, possibly modified by line thickness modifiers"""
        ...
    @thickness.setter
    def thickness(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def thickness_position(self) -> Literal['CENTER', 'INSIDE', 'OUTSIDE', 'RELATIVE']:
        """Thickness position of silhouettes and border edges (applicable when plain chaining is used with the Same Object option)"""
        ...
    @thickness_position.setter
    def thickness_position(self, value: Literal['CENTER', 'INSIDE', 'OUTSIDE', 'RELATIVE']):
        ...
    @property
    def thickness_ratio(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """A number between 0 (inside) and 1 (outside) specifying the relative position of stroke thickness"""
        ...
    @thickness_ratio.setter
    def thickness_ratio(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def color_modifiers(self) -> Annotated['LineStyleColorModifiers', "is_animatable=False"]:
        """List of line color modifiers"""
        ...
    @property
    def alpha_modifiers(self) -> Annotated['LineStyleAlphaModifiers', "is_animatable=False"]:
        """List of alpha transparency modifiers"""
        ...
    @property
    def thickness_modifiers(self) -> Annotated['LineStyleThicknessModifiers', "is_animatable=False"]:
        """List of line thickness modifiers"""
        ...
    @property
    def geometry_modifiers(self) -> Annotated['LineStyleGeometryModifiers', "is_animatable=False"]:
        """List of stroke geometry modifiers"""
        ...
    @property
    def use_chaining(self) -> bool:
        """Enable chaining of feature edges"""
        ...
    @use_chaining.setter
    def use_chaining(self, value: bool):
        ...
    @property
    def chaining(self) -> Literal['PLAIN', 'SKETCHY']:
        """Select the way how feature edges are jointed to form chains"""
        ...
    @chaining.setter
    def chaining(self, value: Literal['PLAIN', 'SKETCHY']):
        ...
    @property
    def rounds(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Number of rounds in a sketchy multiple touch"""
        ...
    @rounds.setter
    def rounds(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1"]):
        ...
    @property
    def use_same_object(self) -> bool:
        """If true, only feature edges of the same object are joined"""
        ...
    @use_same_object.setter
    def use_same_object(self, value: bool):
        ...
    @property
    def use_split_length(self) -> bool:
        """Enable chain splitting by curvilinear 2D length"""
        ...
    @use_split_length.setter
    def use_split_length(self, value: bool):
        ...
    @property
    def split_length(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Curvilinear 2D length for chain splitting"""
        ...
    @split_length.setter
    def split_length(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def use_angle_min(self) -> bool:
        """Split chains at points with angles smaller than the minimum 2D angle"""
        ...
    @use_angle_min.setter
    def use_angle_min(self, value: bool):
        ...
    @property
    def angle_min(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]:
        """Minimum 2D angle for splitting chains"""
        ...
    @angle_min.setter
    def angle_min(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]):
        ...
    @property
    def use_angle_max(self) -> bool:
        """Split chains at points with angles larger than the maximum 2D angle"""
        ...
    @use_angle_max.setter
    def use_angle_max(self, value: bool):
        ...
    @property
    def angle_max(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]:
        """Maximum 2D angle for splitting chains"""
        ...
    @angle_max.setter
    def angle_max(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]):
        ...
    @property
    def use_length_min(self) -> bool:
        """Enable the selection of chains by a minimum 2D length"""
        ...
    @use_length_min.setter
    def use_length_min(self, value: bool):
        ...
    @property
    def length_min(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Minimum curvilinear 2D length for the selection of chains"""
        ...
    @length_min.setter
    def length_min(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def use_length_max(self) -> bool:
        """Enable the selection of chains by a maximum 2D length"""
        ...
    @use_length_max.setter
    def use_length_max(self, value: bool):
        ...
    @property
    def length_max(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Maximum curvilinear 2D length for the selection of chains"""
        ...
    @length_max.setter
    def length_max(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def use_chain_count(self) -> bool:
        """Enable the selection of first N chains"""
        ...
    @use_chain_count.setter
    def use_chain_count(self, value: bool):
        ...
    @property
    def chain_count(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Chain count for the selection of first N chains"""
        ...
    @chain_count.setter
    def chain_count(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1"]):
        ...
    @property
    def use_split_pattern(self) -> bool:
        """Enable chain splitting by dashed line patterns"""
        ...
    @use_split_pattern.setter
    def use_split_pattern(self, value: bool):
        ...
    @property
    def split_dash1(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Length of the 1st dash for splitting"""
        ...
    @split_dash1.setter
    def split_dash1(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1"]):
        ...
    @property
    def split_gap1(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Length of the 1st gap for splitting"""
        ...
    @split_gap1.setter
    def split_gap1(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1"]):
        ...
    @property
    def split_dash2(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Length of the 2nd dash for splitting"""
        ...
    @split_dash2.setter
    def split_dash2(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1"]):
        ...
    @property
    def split_gap2(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Length of the 2nd gap for splitting"""
        ...
    @split_gap2.setter
    def split_gap2(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1"]):
        ...
    @property
    def split_dash3(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Length of the 3rd dash for splitting"""
        ...
    @split_dash3.setter
    def split_dash3(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1"]):
        ...
    @property
    def split_gap3(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Length of the 3rd gap for splitting"""
        ...
    @split_gap3.setter
    def split_gap3(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1"]):
        ...
    @property
    def material_boundary(self) -> bool:
        """If true, chains of feature edges are split at material boundaries"""
        ...
    @material_boundary.setter
    def material_boundary(self, value: bool):
        ...
    @property
    def use_sorting(self) -> bool:
        """Arrange the stacking order of strokes"""
        ...
    @use_sorting.setter
    def use_sorting(self, value: bool):
        ...
    @property
    def sort_key(self) -> Literal['DISTANCE_FROM_CAMERA', '2D_LENGTH', 'PROJECTED_X', 'PROJECTED_Y']:
        """Select the sort key to determine the stacking order of chains"""
        ...
    @sort_key.setter
    def sort_key(self, value: Literal['DISTANCE_FROM_CAMERA', '2D_LENGTH', 'PROJECTED_X', 'PROJECTED_Y']):
        ...
    @property
    def sort_order(self) -> Literal['DEFAULT', 'REVERSE']:
        """Select the sort order"""
        ...
    @sort_order.setter
    def sort_order(self, value: Literal['DEFAULT', 'REVERSE']):
        ...
    @property
    def integration_type(self) -> Literal['MEAN', 'MIN', 'MAX', 'FIRST', 'LAST']:
        """Select the way how the sort key is computed for each chain"""
        ...
    @integration_type.setter
    def integration_type(self, value: Literal['MEAN', 'MIN', 'MAX', 'FIRST', 'LAST']):
        ...
    @property
    def use_dashed_line(self) -> bool:
        """Enable or disable dashed line"""
        ...
    @use_dashed_line.setter
    def use_dashed_line(self, value: bool):
        ...
    @property
    def caps(self) -> Literal['BUTT', 'ROUND', 'SQUARE']:
        """Select the shape of both ends of strokes"""
        ...
    @caps.setter
    def caps(self, value: Literal['BUTT', 'ROUND', 'SQUARE']):
        ...
    @property
    def dash1(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Length of the 1st dash for dashed lines"""
        ...
    @dash1.setter
    def dash1(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1"]):
        ...
    @property
    def gap1(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Length of the 1st gap for dashed lines"""
        ...
    @gap1.setter
    def gap1(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1"]):
        ...
    @property
    def dash2(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Length of the 2nd dash for dashed lines"""
        ...
    @dash2.setter
    def dash2(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1"]):
        ...
    @property
    def gap2(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Length of the 2nd gap for dashed lines"""
        ...
    @gap2.setter
    def gap2(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1"]):
        ...
    @property
    def dash3(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Length of the 3rd dash for dashed lines"""
        ...
    @dash3.setter
    def dash3(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1"]):
        ...
    @property
    def gap3(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Length of the 3rd gap for dashed lines"""
        ...
    @gap3.setter
    def gap3(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1"]):
        ...
    @property
    def use_texture(self) -> bool:
        """Enable or disable textured strokes"""
        ...
    @use_texture.setter
    def use_texture(self, value: bool):
        ...
    @property
    def texture_spacing(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Spacing for textures along stroke length"""
        ...
    @texture_spacing.setter
    def texture_spacing(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def animation_data(self) -> Annotated[Optional['AnimData'], "is_animatable=False"]:
        """Animation data for this data-block"""
        ...
    @property
    def node_tree(self) -> Annotated[Optional['NodeTree'], "is_animatable=False"]:
        """Node tree for node-based shaders"""
        ...
    @property
    def use_nodes(self) -> Annotated[bool, "is_animatable=False"]:
        """Use shader nodes for the line style"""
        ...
    @use_nodes.setter
    def use_nodes(self, value: Annotated[bool, "is_animatable=False"]):
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