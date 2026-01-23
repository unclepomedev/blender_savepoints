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
from .AnimData import AnimData
from .AssetMetaData import AssetMetaData
from .IDOverrideLibrary import IDOverrideLibrary
from .Image import Image
from .ImagePreview import ImagePreview
from .Library import Library
from .LibraryWeakReference import LibraryWeakReference
from .MaterialGPencilStyle import MaterialGPencilStyle
from .MaterialLineArt import MaterialLineArt
from .NodeTree import NodeTree
from .TexPaintSlot import TexPaintSlot
class Material(ID):
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
    surface_render_method: str
    displacement_method: str
    blend_method: str
    alpha_threshold: float
    use_transparency_overlap: bool
    show_transparent_back: bool
    use_backface_culling: bool
    use_backface_culling_shadow: bool
    use_backface_culling_lightprobe_volume: bool
    use_transparent_shadow: bool
    use_raytrace_refraction: bool
    use_screen_refraction: bool
    use_sss_translucency: bool
    refraction_depth: float
    thickness_mode: str
    use_thickness_from_shadow: bool
    volume_intersection_method: str
    max_vertex_displacement: float
    preview_render_type: str
    use_preview_world: bool
    pass_index: int
    node_tree: 'NodeTree'
    use_nodes: bool
    animation_data: 'AnimData'
    texture_paint_images: bpy_prop_collection['Image']
    texture_paint_slots: bpy_prop_collection['TexPaintSlot']
    paint_active_slot: int
    paint_clone_slot: int
    diffuse_color: list[float]
    specular_color: list[float]
    roughness: float
    specular_intensity: float
    metallic: float
    line_color: list[float]
    line_priority: int
    grease_pencil: 'MaterialGPencilStyle'
    is_grease_pencil: bool
    lineart: 'MaterialLineArt'
    cycles: 'CyclesMaterialSettings'
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