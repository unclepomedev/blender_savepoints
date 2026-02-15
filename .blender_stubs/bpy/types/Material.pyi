# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.Material.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

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
from .bpy_prop_collection import bpy_prop_collection

class Material(ID):

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
    surface_render_method: Literal['DITHERED', 'BLENDED']
    """Controls the blending and the compatibility with certain features"""
    displacement_method: Literal['BUMP', 'DISPLACEMENT', 'BOTH']
    """Method to use for the displacement"""
    blend_method: Literal['OPAQUE', 'CLIP', 'HASHED', 'BLEND']
    """Blend Mode for Transparent Faces (Deprecated: use 'surface_render_method')"""
    alpha_threshold: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """A pixel is rendered only if its alpha value is above this threshold"""
    use_transparency_overlap: bool
    """Render multiple transparent layers (may introduce transparency sorting problems)"""
    show_transparent_back: bool
    """Render multiple transparent layers (may introduce transparency sorting problems) (Deprecated: use 'use_tranparency_overlap')"""
    use_backface_culling: bool
    """Use back face culling to hide the back side of faces"""
    use_backface_culling_shadow: bool
    """Use back face culling when casting shadows"""
    use_backface_culling_lightprobe_volume: bool
    """Consider material single sided for light probe volume capture. Additionally helps rejecting probes inside the object to avoid light leaks."""
    use_transparent_shadow: bool
    """Use transparent shadows for this material if it contains a Transparent BSDF, disabling will render faster but not give accurate shadows"""
    use_raytrace_refraction: bool
    """Use raytracing to determine transmitted color instead of using only light probes. This prevents the surface from contributing to the lighting of surfaces not using this setting."""
    use_screen_refraction: bool
    """Use raytracing to determine transmitted color instead of using only light probes. This prevents the surface from contributing to the lighting of surfaces not using this setting. Deprecated: use 'use_raytrace_refraction'."""
    use_sss_translucency: bool
    """Add translucency effect to subsurface (Deprecated)"""
    refraction_depth: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]
    """Approximate the thickness of the object to compute two refraction events (0 is disabled) (Deprecated)"""
    thickness_mode: Literal['SPHERE', 'SLAB']
    """Approximation used to model the light interactions inside the object"""
    use_thickness_from_shadow: bool
    """Use the shadow maps from shadow casting lights to refine the thickness defined by the material node tree"""
    volume_intersection_method: Literal['FAST', 'ACCURATE']
    """Determines which inner part of the mesh will produce volumetric effect"""
    max_vertex_displacement: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]
    """The max distance a vertex can be displaced. Displacements over this threshold may cause visibility issues."""
    preview_render_type: Literal['FLAT', 'SPHERE', 'CUBE', 'HAIR', 'SHADERBALL', 'CLOTH', 'FLUID']
    """Type of preview render"""
    use_preview_world: bool
    """Use the current world background to light the preview render"""
    pass_index: Annotated[int, "subtype='UNSIGNED'", "step=1"]
    """Index number for the "Material Index" render pass"""
    @property
    def node_tree(self) -> Annotated[Optional['NodeTree'], "is_animatable=False"]:
        """Node tree for node based materials"""
        ...
    use_nodes: Annotated[bool, "is_animatable=False"]
    """Use shader nodes to render the material"""
    @property
    def animation_data(self) -> Annotated[Optional['AnimData'], "is_animatable=False"]:
        """Animation data for this data-block"""
        ...
    @property
    def texture_paint_images(self) -> Annotated[bpy_prop_collection['Image'], "is_animatable=False"]:
        """Texture images used for texture painting"""
        ...
    @property
    def texture_paint_slots(self) -> Annotated[bpy_prop_collection['TexPaintSlot'], "is_animatable=False"]:
        """Texture slots defining the mapping and influence of textures"""
        ...
    paint_active_slot: Annotated[int, "subtype='UNSIGNED'", "step=1"]
    """Index of active texture paint slot"""
    paint_clone_slot: Annotated[int, "subtype='UNSIGNED'", "step=1"]
    """Index of clone texture paint slot"""
    diffuse_color: Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]
    """Diffuse color of the material"""
    specular_color: Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]
    """Specular color of the material"""
    roughness: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Roughness of the material"""
    specular_intensity: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """How intense (bright) the specular reflection is"""
    metallic: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Amount of mirror reflection for raytrace"""
    line_color: Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]
    """Line color used for Freestyle line rendering"""
    line_priority: Annotated[int, "step=1"]
    """The line color of a higher priority is used at material boundaries"""
    @property
    def grease_pencil(self) -> Annotated[Optional['MaterialGPencilStyle'], "is_animatable=False"]:
        """Grease Pencil color settings for material"""
        ...
    @property
    def is_grease_pencil(self) -> bool:
        """True if this material has Grease Pencil data"""
        ...
    @property
    def lineart(self) -> Annotated[Optional['MaterialLineArt'], "is_animatable=False"]:
        """Line Art settings for material"""
        ...
    @property
    def cycles(self) -> Annotated[Optional['CyclesMaterialSettings'], "is_animatable=False"]:
        """Cycles material settings"""
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