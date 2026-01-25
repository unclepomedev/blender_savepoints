# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .Texture import Texture
from .AnimData import AnimData
from .AssetMetaData import AssetMetaData
from .ColorRamp import ColorRamp
from .ID import ID
from .IDOverrideLibrary import IDOverrideLibrary
from .Image import Image
from .ImagePreview import ImagePreview
from .ImageUser import ImageUser
from .Library import Library
from .LibraryWeakReference import LibraryWeakReference
from .NodeTree import NodeTree
class ImageTexture(Texture):
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
    type: str
    use_clamp: bool
    use_color_ramp: bool
    color_ramp: 'ColorRamp'
    intensity: float
    contrast: float
    saturation: float
    factor_red: float
    factor_green: float
    factor_blue: float
    use_preview_alpha: bool
    use_nodes: bool
    node_tree: 'NodeTree'
    animation_data: 'AnimData'
    use_interpolation: bool
    use_flip_axis: bool
    use_alpha: bool
    use_calculate_alpha: bool
    invert_alpha: bool
    filter_size: float
    extension: str
    repeat_x: int
    repeat_y: int
    use_mirror_x: bool
    use_mirror_y: bool
    use_checker_odd: bool
    use_checker_even: bool
    checker_distance: float
    crop_min_x: float
    crop_min_y: float
    crop_max_x: float
    crop_max_y: float
    image: 'Image'
    image_user: 'ImageUser'
    use_normal_map: bool
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
    def evaluate(self, *args, **kwargs) -> Any: ...