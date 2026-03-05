# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.SunLight.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .Light import Light
from .AnimData import AnimData
from .AssetMetaData import AssetMetaData
from .ID import ID
from .IDOverrideLibrary import IDOverrideLibrary
from .ImagePreview import ImagePreview
from .Library import Library
from .LibraryWeakReference import LibraryWeakReference
from .NodeTree import NodeTree

class SunLight(Light):

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
    def type(self) -> Literal['POINT', 'SUN', 'SPOT', 'AREA']:
        """Type of light"""
        ...
    @type.setter
    def type(self, value: Literal['POINT', 'SUN', 'SPOT', 'AREA']):
        ...
    @property
    def use_temperature(self) -> bool:
        """Use blackbody temperature to define a natural light color"""
        ...
    @use_temperature.setter
    def use_temperature(self, value: bool):
        ...
    @property
    def color(self) -> Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]:
        """Light color"""
        ...
    @color.setter
    def color(self, value: Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def temperature(self) -> Annotated[float, "subtype='COLOR_TEMPERATURE'", "unit='COLOR_TEMPERATURE'", "step=400.0", "precision=1"]:
        """Light color temperature in Kelvin"""
        ...
    @temperature.setter
    def temperature(self, value: Annotated[float, "subtype='COLOR_TEMPERATURE'", "unit='COLOR_TEMPERATURE'", "step=400.0", "precision=1"]):
        ...
    @property
    def temperature_color(self) -> Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]:
        """Color from Temperature"""
        ...
    @property
    def specular_factor(self) -> Annotated[float, "subtype='FACTOR'", "step=0.009999999776482582", "precision=2"]:
        """Specular reflection multiplier"""
        ...
    @specular_factor.setter
    def specular_factor(self, value: Annotated[float, "subtype='FACTOR'", "step=0.009999999776482582", "precision=2"]):
        ...
    @property
    def diffuse_factor(self) -> Annotated[float, "subtype='FACTOR'", "step=0.009999999776482582", "precision=2"]:
        """Diffuse reflection multiplier"""
        ...
    @diffuse_factor.setter
    def diffuse_factor(self, value: Annotated[float, "subtype='FACTOR'", "step=0.009999999776482582", "precision=2"]):
        ...
    @property
    def transmission_factor(self) -> Annotated[float, "subtype='FACTOR'", "step=0.009999999776482582", "precision=2"]:
        """Transmission light multiplier"""
        ...
    @transmission_factor.setter
    def transmission_factor(self, value: Annotated[float, "subtype='FACTOR'", "step=0.009999999776482582", "precision=2"]):
        ...
    @property
    def volume_factor(self) -> Annotated[float, "subtype='FACTOR'", "step=0.009999999776482582", "precision=2"]:
        """Volume light multiplier"""
        ...
    @volume_factor.setter
    def volume_factor(self, value: Annotated[float, "subtype='FACTOR'", "step=0.009999999776482582", "precision=2"]):
        ...
    @property
    def use_custom_distance(self) -> bool:
        """Use custom attenuation distance instead of global light threshold"""
        ...
    @use_custom_distance.setter
    def use_custom_distance(self, value: bool):
        ...
    @property
    def cutoff_distance(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=1.0", "precision=2"]:
        """Distance at which the light influence will be set to 0"""
        ...
    @cutoff_distance.setter
    def cutoff_distance(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=1.0", "precision=2"]):
        ...
    @property
    def use_shadow(self) -> bool:

        ...
    @use_shadow.setter
    def use_shadow(self, value: bool):
        ...
    @property
    def exposure(self) -> Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=3"]:
        """Scales the power of the light exponentially, multiplying the intensity by 2^exposure"""
        ...
    @exposure.setter
    def exposure(self, value: Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=3"]):
        ...
    @property
    def normalize(self) -> Annotated[bool, "is_animatable=False"]:
        """Normalize intensity by light area, for consistent total light output regardless of size and shape"""
        ...
    @normalize.setter
    def normalize(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def node_tree(self) -> Annotated[Optional['NodeTree'], "is_animatable=False"]:
        """Node tree for node based lights"""
        ...
    @property
    def use_nodes(self) -> Annotated[bool, "is_animatable=False"]:
        """Use shader nodes to render the light"""
        ...
    @use_nodes.setter
    def use_nodes(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def animation_data(self) -> Annotated[Optional['AnimData'], "is_animatable=False"]:
        """Animation data for this data-block"""
        ...
    @property
    def cycles(self) -> Annotated[Optional['CyclesLightSettings'], "is_animatable=False"]:
        """Cycles light settings"""
        ...
    @property
    def angle(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]:
        """Angular diameter of the Sun as seen from the Earth"""
        ...
    @angle.setter
    def angle(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]):
        ...
    @property
    def energy(self) -> Annotated[float, "step=1.0", "precision=3"]:
        """Sunlight strength in watts per meter squared (W/m²)"""
        ...
    @energy.setter
    def energy(self, value: Annotated[float, "step=1.0", "precision=3"]):
        ...
    @property
    def shadow_buffer_clip_start(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]:
        """Shadow map clip start, below which objects will not generate shadows"""
        ...
    @shadow_buffer_clip_start.setter
    def shadow_buffer_clip_start(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]):
        ...
    @property
    def shadow_soft_size(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.10000000149011612", "precision=3"]:
        """Light size for ray shadow sampling (Raytraced shadows)"""
        ...
    @shadow_soft_size.setter
    def shadow_soft_size(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.10000000149011612", "precision=3"]):
        ...
    @property
    def shadow_filter_radius(self) -> Annotated[float, "step=1.0", "precision=2"]:
        """Blur shadow aliasing using Percentage Closer Filtering"""
        ...
    @shadow_filter_radius.setter
    def shadow_filter_radius(self, value: Annotated[float, "step=1.0", "precision=2"]):
        ...
    @property
    def shadow_maximum_resolution(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.05000000074505806", "precision=4"]:
        """Minimum size of a shadow map pixel. Higher values use less memory at the cost of shadow quality."""
        ...
    @shadow_maximum_resolution.setter
    def shadow_maximum_resolution(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.05000000074505806", "precision=4"]):
        ...
    @property
    def use_shadow_jitter(self) -> bool:
        """Enable jittered soft shadows to increase shadow precision (disabled in viewport unless enabled in the render settings). Has a high performance impact."""
        ...
    @use_shadow_jitter.setter
    def use_shadow_jitter(self, value: bool):
        ...
    @property
    def shadow_jitter_overblur(self) -> Annotated[float, "subtype='PERCENTAGE'", "step=10.0", "precision=0"]:
        """Apply shadow tracing to each jittered sample to reduce under-sampling artifacts"""
        ...
    @shadow_jitter_overblur.setter
    def shadow_jitter_overblur(self, value: Annotated[float, "subtype='PERCENTAGE'", "step=10.0", "precision=0"]):
        ...
    @property
    def shadow_cascade_max_distance(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]:
        """End distance of the cascaded shadow map (only in perspective view)"""
        ...
    @shadow_cascade_max_distance.setter
    def shadow_cascade_max_distance(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]):
        ...
    @property
    def shadow_cascade_count(self) -> Annotated[int, "step=1"]:
        """Number of texture used by the cascaded shadow map"""
        ...
    @shadow_cascade_count.setter
    def shadow_cascade_count(self, value: Annotated[int, "step=1"]):
        ...
    @property
    def shadow_cascade_exponent(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Higher value increase resolution towards the viewpoint"""
        ...
    @shadow_cascade_exponent.setter
    def shadow_cascade_exponent(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def shadow_cascade_fade(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """How smooth is the transition between each cascade"""
        ...
    @shadow_cascade_fade.setter
    def shadow_cascade_fade(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]):
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
    def area(self, *args, **kwargs) -> Any: ...