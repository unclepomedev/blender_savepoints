# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.Image.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .ID import ID
from .AssetMetaData import AssetMetaData
from .ColorManagedInputColorspaceSettings import ColorManagedInputColorspaceSettings
from .IDOverrideLibrary import IDOverrideLibrary
from .ImagePackedFile import ImagePackedFile
from .ImagePreview import ImagePreview
from .Library import Library
from .LibraryWeakReference import LibraryWeakReference
from .PackedFile import PackedFile
from .RenderSlot import RenderSlot
from .RenderSlots import RenderSlots
from .Stereo3dFormat import Stereo3dFormat
from .UDIMTile import UDIMTile
from .UDIMTiles import UDIMTiles
from .bpy_prop_collection import bpy_prop_collection

class Image(ID):

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
    filepath: Annotated[str, "subtype='FILE_PATH'", "is_animatable=False"]
    """Image/Movie file name"""
    filepath_raw: Annotated[str, "subtype='FILE_PATH'", "is_animatable=False"]
    """Image/Movie file name (without data refreshing)"""
    file_format: Literal['JPEG', 'OPEN_EXR', 'PNG', 'WEBP', 'BMP', 'CINEON', 'DPX', 'IRIS', 'JPEG2000', 'HDR', 'TARGA', 'TARGA_RAW', 'TIFF', 'OPEN_EXR_MULTILAYER', 'FFMPEG']
    """Format used for re-saving this file"""
    source: Literal['FILE', 'SEQUENCE', 'MOVIE', 'GENERATED', 'VIEWER', 'TILED']
    """Where the image comes from"""
    @property
    def type(self) -> Literal['IMAGE', 'MULTILAYER', 'UV_TEST', 'RENDER_RESULT', 'COMPOSITING']:
        """How to generate the image"""
        ...
    @property
    def packed_file(self) -> Annotated[Optional['PackedFile'], "is_animatable=False"]:
        """First packed file of the image"""
        ...
    @property
    def packed_files(self) -> Annotated[bpy_prop_collection['ImagePackedFile'], "is_animatable=False"]:
        """Collection of packed images"""
        ...
    use_view_as_render: bool
    """Apply render part of display transformation when displaying this image on the screen"""
    use_deinterlace: bool
    """Deinterlace movie file on load"""
    use_multiview: bool
    """Use Multiple Views (when available)"""
    @property
    def is_stereo_3d(self) -> bool:
        """Image has left and right views"""
        ...
    @property
    def is_multiview(self) -> bool:
        """Image has more than one view"""
        ...
    @property
    def is_dirty(self) -> bool:
        """Image has changed and is not saved"""
        ...
    generated_type: Annotated[Literal['BLANK', 'UV_GRID', 'COLOR_GRID'], "is_animatable=False"]
    """Generated image type"""
    generated_width: Annotated[int, "subtype='PIXEL'", "step=1", "is_animatable=False"]
    """Generated image width"""
    generated_height: Annotated[int, "subtype='PIXEL'", "step=1", "is_animatable=False"]
    """Generated image height"""
    use_generated_float: Annotated[bool, "is_animatable=False"]
    """Generate floating-point buffer"""
    generated_color: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3", "is_animatable=False"]
    """Fill color for the generated image"""
    display_aspect: Annotated[list[float], "subtype='XYZ'", "step=1.0", "precision=2"]
    """Display Aspect for this image, does not affect rendering"""
    @property
    def render_slots(self) -> Annotated['RenderSlots', "is_animatable=False"]:
        """Render slots of the image"""
        ...
    @property
    def tiles(self) -> Annotated['UDIMTiles', "is_animatable=False"]:
        """Tiles of the image"""
        ...
    @property
    def has_data(self) -> bool:
        """True if the image data is loaded into memory"""
        ...
    @property
    def depth(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Image bit depth"""
        ...
    @property
    def size(self) -> Annotated[list[int], "subtype='PIXEL'", "step=1"]:
        """Width and height of the image buffer in pixels, zero when image data cannot be loaded"""
        ...
    resolution: Annotated[list[float], "subtype='XYZ'", "step=1.0", "precision=3"]
    """X/Y pixels per meter, for the image buffer"""
    @property
    def frame_duration(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Duration (in frames) of the image (1 when not a video/sequence)"""
        ...
    pixels: Annotated[list[float], "step=10.0", "precision=3"]
    """Image buffer pixels in floating-point values"""
    @property
    def channels(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Number of channels in pixels buffer"""
        ...
    @property
    def is_float(self) -> bool:
        """True if this image is stored in floating-point buffer"""
        ...
    @property
    def colorspace_settings(self) -> Annotated[Optional['ColorManagedInputColorspaceSettings'], "is_animatable=False"]:
        """Input color space settings"""
        ...
    alpha_mode: Literal['STRAIGHT', 'PREMUL', 'CHANNEL_PACKED', 'NONE']
    """Representation of alpha in the image file, to convert to and from when saving and loading the image"""
    use_half_precision: bool
    """Use 16 bits per channel to lower the memory usage during rendering"""
    seam_margin: Annotated[int, "step=1"]
    """Margin to take into account when fixing UV seams during painting. Higher number would improve seam-fixes for mipmaps, but decreases performance."""
    views_format: Literal['INDIVIDUAL', 'STEREO_3D']
    """Mode to load image views"""
    @property
    def stereo_3d_format(self) -> Annotated['Stereo3dFormat', "is_animatable=False"]:
        """Settings for stereo 3d"""
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
    def save_render(self, *args, **kwargs) -> Any: ...
    def save(self, *args, **kwargs) -> Any: ...
    def pack(self, *args, **kwargs) -> Any: ...
    def unpack(self, *args, **kwargs) -> Any: ...
    def reload(self, *args, **kwargs) -> Any: ...
    def update(self, *args, **kwargs) -> Any: ...
    def scale(self, *args, **kwargs) -> Any: ...
    def gl_touch(self, *args, **kwargs) -> Any: ...
    def gl_load(self, *args, **kwargs) -> Any: ...
    def gl_free(self, *args, **kwargs) -> Any: ...
    def filepath_from_user(self, *args, **kwargs) -> Any: ...
    def buffers_free(self, *args, **kwargs) -> Any: ...