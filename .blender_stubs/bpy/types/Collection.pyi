# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.Collection.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .ID import ID
from .AssetMetaData import AssetMetaData
from .CollectionChild import CollectionChild
from .CollectionChildren import CollectionChildren
from .CollectionExport import CollectionExport
from .CollectionExports import CollectionExports
from .CollectionObject import CollectionObject
from .CollectionObjects import CollectionObjects
from .IDOverrideLibrary import IDOverrideLibrary
from .ImagePreview import ImagePreview
from .Library import Library
from .LibraryWeakReference import LibraryWeakReference
from .Object import Object
from .bpy_prop_collection import bpy_prop_collection

class Collection(ID):

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
    instance_offset: Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=10.0", "precision=5"]
    """Offset from the origin to use when instancing"""
    @property
    def objects(self) -> Annotated['CollectionObjects', "is_animatable=False"]:
        """Objects that are directly in this collection"""
        ...
    @property
    def all_objects(self) -> Annotated[bpy_prop_collection['Object'], "is_animatable=False"]:
        """Objects that are in this collection and its child collections"""
        ...
    @property
    def children(self) -> Annotated['CollectionChildren', "is_animatable=False"]:
        """Collections that are immediate children of this collection"""
        ...
    @property
    def collection_objects(self) -> Annotated[bpy_prop_collection['CollectionObject'], "is_animatable=False"]:
        """Objects of the collection with their parent-collection-specific settings"""
        ...
    @property
    def collection_children(self) -> Annotated[bpy_prop_collection['CollectionChild'], "is_animatable=False"]:
        """Children collections with their parent-collection-specific settings"""
        ...
    @property
    def exporters(self) -> Annotated['CollectionExports', "is_animatable=False"]:
        """Export Handlers configured for the collection"""
        ...
    active_exporter_index: Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]
    """Active index in the exporters list"""
    hide_select: Annotated[bool, "is_animatable=False"]
    """Disable selection in viewport"""
    hide_viewport: Annotated[bool, "is_animatable=False"]
    """Globally disable in viewports"""
    hide_render: Annotated[bool, "is_animatable=False"]
    """Globally disable in renders"""
    lineart_usage: Literal['INCLUDE', 'OCCLUSION_ONLY', 'EXCLUDE', 'INTERSECTION_ONLY', 'NO_INTERSECTION', 'FORCE_INTERSECTION']
    """How to use this collection in Line Art calculation"""
    lineart_use_intersection_mask: bool
    """Use custom intersection mask for faces in this collection"""
    lineart_intersection_mask: list[bool]
    """Intersection generated by this collection will have this mask value"""
    lineart_intersection_priority: Annotated[int, "step=1"]
    """The intersection line will be included into the object with the higher intersection priority value"""
    use_lineart_intersection_priority: bool
    """Assign intersection priority value for this collection"""
    color_tag: Literal['NONE', 'COLOR_01', 'COLOR_02', 'COLOR_03', 'COLOR_04', 'COLOR_05', 'COLOR_06', 'COLOR_07', 'COLOR_08']
    """Color tag for a collection"""
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
    # --- Injected Methods ---
    def temp_override(self, window=None, area=None, region=None, **kwargs) -> Any: ...