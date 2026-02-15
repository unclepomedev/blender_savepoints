# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated
from .bpy_prop_collection import bpy_prop_collection

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
    type: Literal['POINT', 'SUN', 'SPOT', 'AREA']
    """Type of light"""
    use_temperature: bool
    """Use blackbody temperature to define a natural light color"""
    color: Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]
    """Light color"""
    temperature: Annotated[float, "subtype='COLOR_TEMPERATURE'", "unit='COLOR_TEMPERATURE'", "step=400.0", "precision=1"]
    """Light color temperature in Kelvin"""
    @property
    def temperature_color(self) -> Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]:
        """Color from Temperature"""
        ...
    specular_factor: Annotated[float, "subtype='FACTOR'", "step=0.009999999776482582", "precision=2"]
    """Specular reflection multiplier"""
    diffuse_factor: Annotated[float, "subtype='FACTOR'", "step=0.009999999776482582", "precision=2"]
    """Diffuse reflection multiplier"""
    transmission_factor: Annotated[float, "subtype='FACTOR'", "step=0.009999999776482582", "precision=2"]
    """Transmission light multiplier"""
    volume_factor: Annotated[float, "subtype='FACTOR'", "step=0.009999999776482582", "precision=2"]
    """Volume light multiplier"""
    use_custom_distance: bool
    """Use custom attenuation distance instead of global light threshold"""
    cutoff_distance: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=1.0", "precision=2"]
    """Distance at which the light influence will be set to 0"""
    use_shadow: bool
    exposure: Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=3"]
    """Scales the power of the light exponentially, multiplying the intensity by 2^exposure"""
    normalize: Annotated[bool, "is_animatable=False"]
    """Normalize intensity by light area, for consistent total light output regardless of size and shape"""
    @property
    def node_tree(self) -> Annotated[Optional['NodeTree'], "is_animatable=False"]:
        """Node tree for node based lights"""
        ...
    use_nodes: Annotated[bool, "is_animatable=False"]
    """Use shader nodes to render the light"""
    @property
    def animation_data(self) -> Annotated[Optional['AnimData'], "is_animatable=False"]:
        """Animation data for this data-block"""
        ...
    @property
    def cycles(self) -> Annotated[Optional['CyclesLightSettings'], "is_animatable=False"]:
        """Cycles light settings"""
        ...
    angle: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]
    """Angular diameter of the Sun as seen from the Earth"""
    energy: Annotated[float, "step=1.0", "precision=3"]
    """Sunlight strength in watts per meter squared (W/m²)"""
    shadow_buffer_clip_start: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]
    """Shadow map clip start, below which objects will not generate shadows"""
    shadow_soft_size: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.10000000149011612", "precision=3"]
    """Light size for ray shadow sampling (Raytraced shadows)"""
    shadow_filter_radius: Annotated[float, "step=1.0", "precision=2"]
    """Blur shadow aliasing using Percentage Closer Filtering"""
    shadow_maximum_resolution: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.05000000074505806", "precision=4"]
    """Minimum size of a shadow map pixel. Higher values use less memory at the cost of shadow quality."""
    use_shadow_jitter: bool
    """Enable jittered soft shadows to increase shadow precision (disabled in viewport unless enabled in the render settings). Has a high performance impact."""
    shadow_jitter_overblur: Annotated[float, "subtype='PERCENTAGE'", "step=10.0", "precision=0"]
    """Apply shadow tracing to each jittered sample to reduce under-sampling artifacts"""
    shadow_cascade_max_distance: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]
    """End distance of the cascaded shadow map (only in perspective view)"""
    shadow_cascade_count: Annotated[int, "step=1"]
    """Number of texture used by the cascaded shadow map"""
    shadow_cascade_exponent: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Higher value increase resolution towards the viewpoint"""
    shadow_cascade_fade: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """How smooth is the transition between each cascade"""
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