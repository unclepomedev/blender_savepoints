# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.World.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .ID import ID
from .AnimData import AnimData
from .AssetMetaData import AssetMetaData
from .IDOverrideLibrary import IDOverrideLibrary
from .ImagePreview import ImagePreview
from .Library import Library
from .LibraryWeakReference import LibraryWeakReference
from .NodeTree import NodeTree
from .WorldLighting import WorldLighting
from .WorldMistSettings import WorldMistSettings
from warnings import deprecated

class World(ID):

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
    def animation_data(self) -> Annotated[Optional['AnimData'], "is_animatable=False"]:
        """Animation data for this data-block"""
        ...
    @property
    def use_eevee_finite_volume(self) -> Annotated[bool, "is_animatable=False"]:
        """The world's volume used to be rendered by EEVEE Legacy. Conversion is needed for it to render properly."""
        ...
    @use_eevee_finite_volume.setter
    def use_eevee_finite_volume(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def color(self) -> Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]:
        """Color of the background"""
        ...
    @color.setter
    def color(self, value: Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def light_settings(self) -> Annotated['WorldLighting', "is_animatable=False"]:
        """World lighting settings"""
        ...
    @property
    def mist_settings(self) -> Annotated['WorldMistSettings', "is_animatable=False"]:
        """World mist settings"""
        ...
    @property
    def node_tree(self) -> Annotated[Optional['NodeTree'], "is_animatable=False"]:
        """Node tree for node based worlds"""
        ...
    @deprecated('Deprecated in 5.0.0, Removal in 6.0.0')
    @property
    def use_nodes(self) -> Annotated[bool, "is_animatable=False"]:
        """Use shader nodes to render the world"""
        ...
    @deprecated('Deprecated in 5.0.0, Removal in 6.0.0')
    @use_nodes.setter
    def use_nodes(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def lightgroup(self) -> Annotated[str, "is_animatable=False"]:
        """Lightgroup that the world belongs to"""
        ...
    @lightgroup.setter
    def lightgroup(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def probe_resolution(self) -> Literal['128', '256', '512', '1024', '2048', '4096']:
        """Resolution when baked to a texture"""
        ...
    @probe_resolution.setter
    def probe_resolution(self, value: Literal['128', '256', '512', '1024', '2048', '4096']):
        ...
    @property
    def sun_threshold(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """If non-zero, the maximum value for world contribution that will be recorded inside the world light probe. The excess contribution is converted to a sun light. This reduces the light bleeding caused by very bright light sources."""
        ...
    @sun_threshold.setter
    def sun_threshold(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def sun_angle(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]:
        """Angular diameter of the Sun as seen from the Earth"""
        ...
    @sun_angle.setter
    def sun_angle(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]):
        ...
    @property
    def use_sun_shadow(self) -> bool:
        """Enable sun shadow casting"""
        ...
    @use_sun_shadow.setter
    def use_sun_shadow(self, value: bool):
        ...
    @property
    def sun_shadow_maximum_resolution(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.05000000074505806", "precision=4"]:
        """Maximum size of a shadow map pixel. Higher values use less memory at the cost of shadow quality."""
        ...
    @sun_shadow_maximum_resolution.setter
    def sun_shadow_maximum_resolution(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.05000000074505806", "precision=4"]):
        ...
    @property
    def sun_shadow_filter_radius(self) -> Annotated[float, "step=1.0", "precision=2"]:
        """Blur shadow aliasing using Percentage Closer Filtering"""
        ...
    @sun_shadow_filter_radius.setter
    def sun_shadow_filter_radius(self, value: Annotated[float, "step=1.0", "precision=2"]):
        ...
    @property
    def use_sun_shadow_jitter(self) -> bool:
        """Enable jittered soft shadows to increase shadow precision (disabled in viewport unless enabled in the render settings). Has a high performance impact."""
        ...
    @use_sun_shadow_jitter.setter
    def use_sun_shadow_jitter(self, value: bool):
        ...
    @property
    def sun_shadow_jitter_overblur(self) -> Annotated[float, "subtype='PERCENTAGE'", "step=10.0", "precision=0"]:
        """Apply shadow tracing to each jittered sample to reduce under-sampling artifacts"""
        ...
    @sun_shadow_jitter_overblur.setter
    def sun_shadow_jitter_overblur(self, value: Annotated[float, "subtype='PERCENTAGE'", "step=10.0", "precision=0"]):
        ...
    @property
    def cycles(self) -> Annotated[Optional['CyclesWorldSettings'], "is_animatable=False"]:
        """Cycles world settings"""
        ...
    @property
    def cycles_visibility(self) -> Annotated[Optional['CyclesVisibilitySettings'], "is_animatable=False"]:
        """Cycles visibility settings"""
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