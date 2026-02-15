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

    name: Annotated[str, "is_animatable=False"]
    """Unique data-block ID name (within a same type and library)"""
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
    use_fake_user: bool
    """Save this data-block even if it has no users"""
    use_extra_user: bool
    """Indicates whether an extra user is set or not (mainly for internal/debug usages)"""
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
    is_runtime_data: bool
    """This data-block is runtime data, i.e. it won't be saved in .blend file. Note that e.g. evaluated IDs are always runtime, so this value is only editable for data-blocks in Main data-base."""
    @property
    def is_editable(self) -> bool:
        """This data-block is editable in the user interface. Linked data-blocks are not editable, except if they were loaded as editable assets."""
        ...
    tag: bool
    """Tools can use this to tag data for their own purposes (initial state is undefined)"""
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
    asset_data: Annotated[Optional['AssetMetaData'], "is_animatable=False"]
    """Additional data for an asset data-block"""
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
    active_texture: Annotated[Optional['Texture'], "is_animatable=False"]
    """Active texture slot being displayed"""
    active_texture_index: Annotated[int, "subtype='UNSIGNED'", "step=1"]
    """Index of active texture slot"""
    panel: Annotated[Literal['STROKES', 'COLOR', 'ALPHA', 'THICKNESS', 'GEOMETRY', 'TEXTURE'], "is_animatable=False"]
    """Select the property panel to be shown"""
    color: Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]
    """Base line color, possibly modified by line color modifiers"""
    alpha: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Base alpha transparency, possibly modified by alpha transparency modifiers"""
    thickness: Annotated[float, "step=10.0", "precision=3"]
    """Base line thickness, possibly modified by line thickness modifiers"""
    thickness_position: Literal['CENTER', 'INSIDE', 'OUTSIDE', 'RELATIVE']
    """Thickness position of silhouettes and border edges (applicable when plain chaining is used with the Same Object option)"""
    thickness_ratio: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """A number between 0 (inside) and 1 (outside) specifying the relative position of stroke thickness"""
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
    use_chaining: bool
    """Enable chaining of feature edges"""
    chaining: Literal['PLAIN', 'SKETCHY']
    """Select the way how feature edges are jointed to form chains"""
    rounds: Annotated[int, "subtype='UNSIGNED'", "step=1"]
    """Number of rounds in a sketchy multiple touch"""
    use_same_object: bool
    """If true, only feature edges of the same object are joined"""
    use_split_length: bool
    """Enable chain splitting by curvilinear 2D length"""
    split_length: Annotated[float, "step=10.0", "precision=3"]
    """Curvilinear 2D length for chain splitting"""
    use_angle_min: bool
    """Split chains at points with angles smaller than the minimum 2D angle"""
    angle_min: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]
    """Minimum 2D angle for splitting chains"""
    use_angle_max: bool
    """Split chains at points with angles larger than the maximum 2D angle"""
    angle_max: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]
    """Maximum 2D angle for splitting chains"""
    use_length_min: bool
    """Enable the selection of chains by a minimum 2D length"""
    length_min: Annotated[float, "step=10.0", "precision=3"]
    """Minimum curvilinear 2D length for the selection of chains"""
    use_length_max: bool
    """Enable the selection of chains by a maximum 2D length"""
    length_max: Annotated[float, "step=10.0", "precision=3"]
    """Maximum curvilinear 2D length for the selection of chains"""
    use_chain_count: bool
    """Enable the selection of first N chains"""
    chain_count: Annotated[int, "subtype='UNSIGNED'", "step=1"]
    """Chain count for the selection of first N chains"""
    use_split_pattern: bool
    """Enable chain splitting by dashed line patterns"""
    split_dash1: Annotated[int, "subtype='UNSIGNED'", "step=1"]
    """Length of the 1st dash for splitting"""
    split_gap1: Annotated[int, "subtype='UNSIGNED'", "step=1"]
    """Length of the 1st gap for splitting"""
    split_dash2: Annotated[int, "subtype='UNSIGNED'", "step=1"]
    """Length of the 2nd dash for splitting"""
    split_gap2: Annotated[int, "subtype='UNSIGNED'", "step=1"]
    """Length of the 2nd gap for splitting"""
    split_dash3: Annotated[int, "subtype='UNSIGNED'", "step=1"]
    """Length of the 3rd dash for splitting"""
    split_gap3: Annotated[int, "subtype='UNSIGNED'", "step=1"]
    """Length of the 3rd gap for splitting"""
    material_boundary: bool
    """If true, chains of feature edges are split at material boundaries"""
    use_sorting: bool
    """Arrange the stacking order of strokes"""
    sort_key: Literal['DISTANCE_FROM_CAMERA', '2D_LENGTH', 'PROJECTED_X', 'PROJECTED_Y']
    """Select the sort key to determine the stacking order of chains"""
    sort_order: Literal['DEFAULT', 'REVERSE']
    """Select the sort order"""
    integration_type: Literal['MEAN', 'MIN', 'MAX', 'FIRST', 'LAST']
    """Select the way how the sort key is computed for each chain"""
    use_dashed_line: bool
    """Enable or disable dashed line"""
    caps: Literal['BUTT', 'ROUND', 'SQUARE']
    """Select the shape of both ends of strokes"""
    dash1: Annotated[int, "subtype='UNSIGNED'", "step=1"]
    """Length of the 1st dash for dashed lines"""
    gap1: Annotated[int, "subtype='UNSIGNED'", "step=1"]
    """Length of the 1st gap for dashed lines"""
    dash2: Annotated[int, "subtype='UNSIGNED'", "step=1"]
    """Length of the 2nd dash for dashed lines"""
    gap2: Annotated[int, "subtype='UNSIGNED'", "step=1"]
    """Length of the 2nd gap for dashed lines"""
    dash3: Annotated[int, "subtype='UNSIGNED'", "step=1"]
    """Length of the 3rd dash for dashed lines"""
    gap3: Annotated[int, "subtype='UNSIGNED'", "step=1"]
    """Length of the 3rd gap for dashed lines"""
    use_texture: bool
    """Enable or disable textured strokes"""
    texture_spacing: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Spacing for textures along stroke length"""
    @property
    def animation_data(self) -> Annotated[Optional['AnimData'], "is_animatable=False"]:
        """Animation data for this data-block"""
        ...
    @property
    def node_tree(self) -> Annotated[Optional['NodeTree'], "is_animatable=False"]:
        """Node tree for node-based shaders"""
        ...
    use_nodes: Annotated[bool, "is_animatable=False"]
    """Use shader nodes for the line style"""
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