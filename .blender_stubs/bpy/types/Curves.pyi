# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.Curves.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .ID import ID
from .AnimData import AnimData
from .AssetMetaData import AssetMetaData
from .Attribute import Attribute
from .AttributeGroupCurves import AttributeGroupCurves
from .CurvePoint import CurvePoint
from .CurveSlice import CurveSlice
from .FloatVectorAttributeValue import FloatVectorAttributeValue
from .FloatVectorValueReadOnly import FloatVectorValueReadOnly
from .IDMaterials import IDMaterials
from .IDOverrideLibrary import IDOverrideLibrary
from .ImagePreview import ImagePreview
from .IntAttributeValue import IntAttributeValue
from .Library import Library
from .LibraryWeakReference import LibraryWeakReference
from .Material import Material
from .Object import Object
from .bpy_prop_collection import bpy_prop_collection

class Curves(ID):

    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:
        """Unique data-block ID name (within a same type and library)"""
        ...
    @name.setter
    def name(self, value: Annotated[str, "is_animatable=False"]) -> None:
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
    def use_fake_user(self, value: bool) -> None:
        ...
    @property
    def use_extra_user(self) -> bool:
        """Indicates whether an extra user is set or not (mainly for internal/debug usages)"""
        ...
    @use_extra_user.setter
    def use_extra_user(self, value: bool) -> None:
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
    def is_runtime_data(self, value: bool) -> None:
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
    def tag(self, value: bool) -> None:
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
    def asset_data(self, value: Annotated[Optional['AssetMetaData'], "is_animatable=False"]) -> None:
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
    def curves(self) -> Annotated[bpy_prop_collection['CurveSlice'], "is_animatable=False"]:
        """All curves in the data-block"""
        ...
    @property
    def points(self) -> Annotated[bpy_prop_collection['CurvePoint'], "is_animatable=False"]:
        """Control points of all curves"""
        ...
    @property
    def position_data(self) -> Annotated[bpy_prop_collection['FloatVectorAttributeValue'], "is_animatable=False"]:

        ...
    @property
    def curve_offset_data(self) -> Annotated[bpy_prop_collection['IntAttributeValue'], "is_animatable=False"]:

        ...
    @property
    def normals(self) -> Annotated[bpy_prop_collection['FloatVectorValueReadOnly'], "is_animatable=False"]:
        """The curve normal value at each of the curve's control points"""
        ...
    @property
    def materials(self) -> Annotated['IDMaterials', "is_animatable=False"]:

        ...
    @property
    def surface(self) -> Annotated[Optional['Object'], "is_animatable=False"]:
        """Mesh object that the curves can be attached to"""
        ...
    @surface.setter
    def surface(self, value: Annotated[Optional['Object'], "is_animatable=False"]) -> None:
        ...
    @property
    def surface_uv_map(self) -> Annotated[str, "is_animatable=False"]:
        """The name of the attribute on the surface mesh used to define the attachment of each curve"""
        ...
    @surface_uv_map.setter
    def surface_uv_map(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def use_mirror_x(self) -> bool:
        """Enable symmetry in the X axis"""
        ...
    @use_mirror_x.setter
    def use_mirror_x(self, value: bool) -> None:
        ...
    @property
    def use_mirror_y(self) -> bool:
        """Enable symmetry in the Y axis"""
        ...
    @use_mirror_y.setter
    def use_mirror_y(self, value: bool) -> None:
        ...
    @property
    def use_mirror_z(self) -> bool:
        """Enable symmetry in the Z axis"""
        ...
    @use_mirror_z.setter
    def use_mirror_z(self, value: bool) -> None:
        ...
    @property
    def selection_domain(self) -> Annotated[Literal['POINT', 'CURVE'], "is_animatable=False"]:

        ...
    @selection_domain.setter
    def selection_domain(self, value: Annotated[Literal['POINT', 'CURVE'], "is_animatable=False"]) -> None:
        ...
    @property
    def use_sculpt_collision(self) -> Annotated[bool, "is_animatable=False"]:
        """Enable collision with the surface while sculpting"""
        ...
    @use_sculpt_collision.setter
    def use_sculpt_collision(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def surface_collision_distance(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.0010000000474974513", "precision=3"]:
        """Distance to keep the curves away from the surface"""
        ...
    @surface_collision_distance.setter
    def surface_collision_distance(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.0010000000474974513", "precision=3"]) -> None:
        ...
    @property
    def attributes(self) -> Annotated['AttributeGroupCurves', "is_animatable=False"]:
        """Geometry attributes"""
        ...
    @property
    def color_attributes(self) -> Annotated['AttributeGroupCurves', "is_animatable=False"]:
        """Geometry color attributes"""
        ...
    @property
    def animation_data(self) -> Annotated[Optional['AnimData'], "is_animatable=False"]:
        """Animation data for this data-block"""
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
    def add_curves(self, *args, **kwargs) -> Any: ...
    def remove_curves(self, *args, **kwargs) -> Any: ...
    def resize_curves(self, *args, **kwargs) -> Any: ...
    def reorder_curves(self, *args, **kwargs) -> Any: ...
    def set_types(self, *args, **kwargs) -> Any: ...
    def unit_test_compare(self, *args, **kwargs) -> Any: ...