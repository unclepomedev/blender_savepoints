# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.MovieClip.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .ID import ID
from .AnimData import AnimData
from .Annotation import Annotation
from .AssetMetaData import AssetMetaData
from .ColorManagedInputColorspaceSettings import ColorManagedInputColorspaceSettings
from .IDOverrideLibrary import IDOverrideLibrary
from .ImagePreview import ImagePreview
from .Library import Library
from .LibraryWeakReference import LibraryWeakReference
from .MovieClipProxy import MovieClipProxy
from .MovieTracking import MovieTracking

class MovieClip(ID):

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
    def filepath(self) -> Annotated[str, "subtype='FILE_PATH'", "is_animatable=False"]:
        """Filename of the movie or sequence file"""
        ...
    @filepath.setter
    def filepath(self, value: Annotated[str, "subtype='FILE_PATH'", "is_animatable=False"]) -> None:
        ...
    @property
    def tracking(self) -> Annotated[Optional['MovieTracking'], "is_animatable=False"]:

        ...
    @property
    def proxy(self) -> Annotated[Optional['MovieClipProxy'], "is_animatable=False"]:

        ...
    @property
    def use_proxy(self) -> Annotated[bool, "is_animatable=False"]:
        """Use a preview proxy and/or timecode index for this clip"""
        ...
    @use_proxy.setter
    def use_proxy(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def size(self) -> Annotated[list[int], "subtype='XYZ'", "step=1"]:
        """Width and height in pixels, zero when image data cannot be loaded"""
        ...
    @property
    def display_aspect(self) -> Annotated[list[float], "subtype='XYZ'", "step=1.0", "precision=2", "is_animatable=False"]:
        """Display Aspect for this clip, does not affect rendering"""
        ...
    @display_aspect.setter
    def display_aspect(self, value: Annotated[list[float], "subtype='XYZ'", "step=1.0", "precision=2", "is_animatable=False"]) -> None:
        ...
    @property
    def source(self) -> Literal['SEQUENCE', 'MOVIE']:
        """Where the clip comes from"""
        ...
    @property
    def use_proxy_custom_directory(self) -> Annotated[bool, "is_animatable=False"]:
        """Create proxy images in a custom directory (default is movie location)"""
        ...
    @use_proxy_custom_directory.setter
    def use_proxy_custom_directory(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def annotation(self) -> Annotated[Optional['Annotation'], "is_animatable=False"]:
        """Annotation data for this movie clip"""
        ...
    @annotation.setter
    def annotation(self, value: Annotated[Optional['Annotation'], "is_animatable=False"]) -> None:
        ...
    @property
    def frame_start(self) -> Annotated[int, "step=1"]:
        """Global scene frame number at which this movie starts playing (affects all data associated with a clip)"""
        ...
    @frame_start.setter
    def frame_start(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def frame_offset(self) -> Annotated[int, "step=1"]:
        """Offset of footage first frame relative to its file name (affects only how footage is loading, does not change data associated with a clip)"""
        ...
    @frame_offset.setter
    def frame_offset(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def frame_duration(self) -> Annotated[int, "step=1"]:
        """Detected duration of movie clip in frames"""
        ...
    @property
    def fps(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Detected frame rate of the movie clip in frames per second"""
        ...
    @property
    def colorspace_settings(self) -> Annotated[Optional['ColorManagedInputColorspaceSettings'], "is_animatable=False"]:
        """Input color space settings"""
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
    def metadata(self, *args, **kwargs) -> Any: ...