# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.Armature.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .ID import ID
from .AnimData import AnimData
from .ArmatureBones import ArmatureBones
from .ArmatureEditBones import ArmatureEditBones
from .AssetMetaData import AssetMetaData
from .Bone import Bone
from .BoneCollection import BoneCollection
from .BoneCollections import BoneCollections
from .EditBone import EditBone
from .IDOverrideLibrary import IDOverrideLibrary
from .ImagePreview import ImagePreview
from .Library import Library
from .LibraryWeakReference import LibraryWeakReference
from .bpy_prop_collection import bpy_prop_collection

class Armature(ID):

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
    def animation_data(self) -> Annotated[Optional['AnimData'], "is_animatable=False"]:
        """Animation data for this data-block"""
        ...
    @property
    def bones(self) -> Annotated['ArmatureBones', "is_animatable=False"]:

        ...
    @property
    def edit_bones(self) -> Annotated['ArmatureEditBones', "is_animatable=False"]:

        ...
    @property
    def collections(self) -> Annotated['BoneCollections', "is_animatable=False"]:

        ...
    @collections.setter
    def collections(self, value: Annotated['BoneCollections', "is_animatable=False"]) -> None:
        ...
    @property
    def collections_all(self) -> Annotated[bpy_prop_collection['BoneCollection'], "is_animatable=False"]:
        """List of all bone collections of the armature"""
        ...
    @property
    def pose_position(self) -> Literal['POSE', 'REST']:
        """Show armature in binding pose or final posed state"""
        ...
    @pose_position.setter
    def pose_position(self, value: Literal['POSE', 'REST']) -> None:
        ...
    @property
    def display_type(self) -> Literal['OCTAHEDRAL', 'STICK', 'BBONE', 'ENVELOPE', 'WIRE']:

        ...
    @display_type.setter
    def display_type(self, value: Literal['OCTAHEDRAL', 'STICK', 'BBONE', 'ENVELOPE', 'WIRE']) -> None:
        ...
    @property
    def show_axes(self) -> bool:
        """Display bone axes"""
        ...
    @show_axes.setter
    def show_axes(self, value: bool) -> None:
        ...
    @property
    def axes_position(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=1"]:
        """The position for the axes on the bone. Increasing the value moves it closer to the tip; decreasing moves it closer to the root."""
        ...
    @axes_position.setter
    def axes_position(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=1"]) -> None:
        ...
    @property
    def relation_line_position(self) -> Literal['TAIL', 'HEAD']:
        """The start position of the relation lines from parent to child bones"""
        ...
    @relation_line_position.setter
    def relation_line_position(self, value: Literal['TAIL', 'HEAD']) -> None:
        ...
    @property
    def show_names(self) -> bool:
        """Display bone names"""
        ...
    @show_names.setter
    def show_names(self, value: bool) -> None:
        ...
    @property
    def use_mirror_x(self) -> bool:
        """Apply changes to matching bone on opposite side of X-Axis"""
        ...
    @use_mirror_x.setter
    def use_mirror_x(self, value: bool) -> None:
        ...
    @property
    def show_bone_custom_shapes(self) -> bool:
        """Display bones with their custom shapes"""
        ...
    @show_bone_custom_shapes.setter
    def show_bone_custom_shapes(self, value: bool) -> None:
        ...
    @property
    def show_bone_colors(self) -> bool:
        """Display bone colors"""
        ...
    @show_bone_colors.setter
    def show_bone_colors(self, value: bool) -> None:
        ...
    @property
    def is_editmode(self) -> bool:
        """True when used in editmode"""
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
    def transform(self, *args, **kwargs) -> Any: ...