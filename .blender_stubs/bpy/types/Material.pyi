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
from warnings import deprecated

class Material(ID):

    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:
        """Unique data-block ID name (within a same type and library)"""
        ...
    @name.setter
    def name(self, value: Annotated[str, "is_animatable=False"]):
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
    def use_fake_user(self, value: bool):
        ...
    @property
    def use_extra_user(self) -> bool:
        """Indicates whether an extra user is set or not (mainly for internal/debug usages)"""
        ...
    @use_extra_user.setter
    def use_extra_user(self, value: bool):
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
    def is_runtime_data(self, value: bool):
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
    def tag(self, value: bool):
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
    def asset_data(self, value: Annotated[Optional['AssetMetaData'], "is_animatable=False"]):
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
    def surface_render_method(self) -> Literal['DITHERED', 'BLENDED']:
        """Controls the blending and the compatibility with certain features"""
        ...
    @surface_render_method.setter
    def surface_render_method(self, value: Literal['DITHERED', 'BLENDED']):
        ...
    @property
    def displacement_method(self) -> Literal['BUMP', 'DISPLACEMENT', 'BOTH']:
        """Method to use for the displacement"""
        ...
    @displacement_method.setter
    def displacement_method(self, value: Literal['BUMP', 'DISPLACEMENT', 'BOTH']):
        ...
    @property
    def blend_method(self) -> Literal['OPAQUE', 'CLIP', 'HASHED', 'BLEND']:
        """Blend Mode for Transparent Faces (Deprecated: use 'surface_render_method')"""
        ...
    @blend_method.setter
    def blend_method(self, value: Literal['OPAQUE', 'CLIP', 'HASHED', 'BLEND']):
        ...
    @property
    def alpha_threshold(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """A pixel is rendered only if its alpha value is above this threshold"""
        ...
    @alpha_threshold.setter
    def alpha_threshold(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def use_transparency_overlap(self) -> bool:
        """Render multiple transparent layers (may introduce transparency sorting problems)"""
        ...
    @use_transparency_overlap.setter
    def use_transparency_overlap(self, value: bool):
        ...
    @property
    def show_transparent_back(self) -> bool:
        """Render multiple transparent layers (may introduce transparency sorting problems) (Deprecated: use 'use_tranparency_overlap')"""
        ...
    @show_transparent_back.setter
    def show_transparent_back(self, value: bool):
        ...
    @property
    def use_backface_culling(self) -> bool:
        """Use back face culling to hide the back side of faces"""
        ...
    @use_backface_culling.setter
    def use_backface_culling(self, value: bool):
        ...
    @property
    def use_backface_culling_shadow(self) -> bool:
        """Use back face culling when casting shadows"""
        ...
    @use_backface_culling_shadow.setter
    def use_backface_culling_shadow(self, value: bool):
        ...
    @property
    def use_backface_culling_lightprobe_volume(self) -> bool:
        """Consider material single sided for light probe volume capture. Additionally helps rejecting probes inside the object to avoid light leaks."""
        ...
    @use_backface_culling_lightprobe_volume.setter
    def use_backface_culling_lightprobe_volume(self, value: bool):
        ...
    @property
    def use_transparent_shadow(self) -> bool:
        """Use transparent shadows for this material if it contains a Transparent BSDF, disabling will render faster but not give accurate shadows"""
        ...
    @use_transparent_shadow.setter
    def use_transparent_shadow(self, value: bool):
        ...
    @property
    def use_raytrace_refraction(self) -> bool:
        """Use raytracing to determine transmitted color instead of using only light probes. This prevents the surface from contributing to the lighting of surfaces not using this setting."""
        ...
    @use_raytrace_refraction.setter
    def use_raytrace_refraction(self, value: bool):
        ...
    @property
    def use_screen_refraction(self) -> bool:
        """Use raytracing to determine transmitted color instead of using only light probes. This prevents the surface from contributing to the lighting of surfaces not using this setting. Deprecated: use 'use_raytrace_refraction'."""
        ...
    @use_screen_refraction.setter
    def use_screen_refraction(self, value: bool):
        ...
    @property
    def use_sss_translucency(self) -> bool:
        """Add translucency effect to subsurface (Deprecated)"""
        ...
    @use_sss_translucency.setter
    def use_sss_translucency(self, value: bool):
        ...
    @property
    def refraction_depth(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]:
        """Approximate the thickness of the object to compute two refraction events (0 is disabled) (Deprecated)"""
        ...
    @refraction_depth.setter
    def refraction_depth(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]):
        ...
    @property
    def thickness_mode(self) -> Literal['SPHERE', 'SLAB']:
        """Approximation used to model the light interactions inside the object"""
        ...
    @thickness_mode.setter
    def thickness_mode(self, value: Literal['SPHERE', 'SLAB']):
        ...
    @property
    def use_thickness_from_shadow(self) -> bool:
        """Use the shadow maps from shadow casting lights to refine the thickness defined by the material node tree"""
        ...
    @use_thickness_from_shadow.setter
    def use_thickness_from_shadow(self, value: bool):
        ...
    @property
    def volume_intersection_method(self) -> Literal['FAST', 'ACCURATE']:
        """Determines which inner part of the mesh will produce volumetric effect"""
        ...
    @volume_intersection_method.setter
    def volume_intersection_method(self, value: Literal['FAST', 'ACCURATE']):
        ...
    @property
    def max_vertex_displacement(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]:
        """The max distance a vertex can be displaced. Displacements over this threshold may cause visibility issues."""
        ...
    @max_vertex_displacement.setter
    def max_vertex_displacement(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]):
        ...
    @property
    def preview_render_type(self) -> Literal['FLAT', 'SPHERE', 'CUBE', 'HAIR', 'SHADERBALL', 'CLOTH', 'FLUID']:
        """Type of preview render"""
        ...
    @preview_render_type.setter
    def preview_render_type(self, value: Literal['FLAT', 'SPHERE', 'CUBE', 'HAIR', 'SHADERBALL', 'CLOTH', 'FLUID']):
        ...
    @property
    def use_preview_world(self) -> bool:
        """Use the current world background to light the preview render"""
        ...
    @use_preview_world.setter
    def use_preview_world(self, value: bool):
        ...
    @property
    def pass_index(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Index number for the "Material Index" render pass"""
        ...
    @pass_index.setter
    def pass_index(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1"]):
        ...
    @property
    def node_tree(self) -> Annotated[Optional['NodeTree'], "is_animatable=False"]:
        """Node tree for node based materials"""
        ...
    @deprecated('Deprecated in 5.0.0, Removal in 6.0.0')
    @property
    def use_nodes(self) -> Annotated[bool, "is_animatable=False"]:
        """Use shader nodes to render the material"""
        ...
    @deprecated('Deprecated in 5.0.0, Removal in 6.0.0')
    @use_nodes.setter
    def use_nodes(self, value: Annotated[bool, "is_animatable=False"]):
        ...
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
    @property
    def paint_active_slot(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Index of active texture paint slot"""
        ...
    @paint_active_slot.setter
    def paint_active_slot(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1"]):
        ...
    @property
    def paint_clone_slot(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Index of clone texture paint slot"""
        ...
    @paint_clone_slot.setter
    def paint_clone_slot(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1"]):
        ...
    @property
    def diffuse_color(self) -> Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]:
        """Diffuse color of the material"""
        ...
    @diffuse_color.setter
    def diffuse_color(self, value: Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def specular_color(self) -> Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]:
        """Specular color of the material"""
        ...
    @specular_color.setter
    def specular_color(self, value: Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def roughness(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Roughness of the material"""
        ...
    @roughness.setter
    def roughness(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def specular_intensity(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """How intense (bright) the specular reflection is"""
        ...
    @specular_intensity.setter
    def specular_intensity(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def metallic(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Amount of mirror reflection for raytrace"""
        ...
    @metallic.setter
    def metallic(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def line_color(self) -> Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]:
        """Line color used for Freestyle line rendering"""
        ...
    @line_color.setter
    def line_color(self, value: Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def line_priority(self) -> Annotated[int, "step=1"]:
        """The line color of a higher priority is used at material boundaries"""
        ...
    @line_priority.setter
    def line_priority(self, value: Annotated[int, "step=1"]):
        ...
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