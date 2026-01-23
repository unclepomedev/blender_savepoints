# Blender Probe Generated Stub for Blender 5.1.0 Alpha
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

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
from .Stereo3dFormat import Stereo3dFormat
from .UDIMTile import UDIMTile
class Image(ID):
    name: str
    name_full: str
    id_type: str
    session_uid: int
    is_evaluated: bool
    original: 'ID'
    users: int
    use_fake_user: bool
    use_extra_user: bool
    is_embedded_data: bool
    is_linked_packed: bool
    is_missing: bool
    is_runtime_data: bool
    is_editable: bool
    tag: bool
    is_library_indirect: bool
    library: 'Library'
    library_weak_reference: 'LibraryWeakReference'
    asset_data: 'AssetMetaData'
    override_library: 'IDOverrideLibrary'
    preview: 'ImagePreview'
    filepath: str
    filepath_raw: str
    file_format: str
    source: str
    type: str
    packed_file: 'PackedFile'
    packed_files: bpy_prop_collection['ImagePackedFile']
    use_view_as_render: bool
    use_deinterlace: bool
    use_multiview: bool
    is_stereo_3d: bool
    is_multiview: bool
    is_dirty: bool
    generated_type: str
    generated_width: int
    generated_height: int
    use_generated_float: bool
    generated_color: list[float]
    display_aspect: list[float]
    render_slots: bpy_prop_collection['RenderSlot']
    tiles: bpy_prop_collection['UDIMTile']
    has_data: bool
    depth: int
    size: list[int]
    resolution: list[float]
    frame_duration: int
    pixels: list[float]
    channels: int
    is_float: bool
    colorspace_settings: 'ColorManagedInputColorspaceSettings'
    alpha_mode: str
    use_half_precision: bool
    seam_margin: int
    views_format: str
    stereo_3d_format: 'Stereo3dFormat'
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