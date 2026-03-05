# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.LightProbeVolume.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .LightProbe import LightProbe
from .AnimData import AnimData
from .AssetMetaData import AssetMetaData
from .Collection import Collection
from .ID import ID
from .IDOverrideLibrary import IDOverrideLibrary
from .ImagePreview import ImagePreview
from .Library import Library
from .LibraryWeakReference import LibraryWeakReference

class LightProbeVolume(LightProbe):

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
    def type(self) -> Literal['SPHERE', 'PLANE', 'VOLUME']:
        """Type of light probe"""
        ...
    @property
    def clip_start(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]:
        """Probe clip start, below which objects will not appear in reflections"""
        ...
    @clip_start.setter
    def clip_start(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def show_clip(self) -> bool:
        """Show the clipping distances in the 3D view"""
        ...
    @show_clip.setter
    def show_clip(self, value: bool) -> None:
        ...
    @property
    def show_influence(self) -> bool:
        """Show the influence volume in the 3D view"""
        ...
    @show_influence.setter
    def show_influence(self, value: bool) -> None:
        ...
    @property
    def influence_distance(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]:
        """Influence distance of the probe"""
        ...
    @influence_distance.setter
    def influence_distance(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def visibility_buffer_bias(self) -> Annotated[float, "step=1.0", "precision=3"]:
        """Bias for reducing self shadowing (Deprecated)"""
        ...
    @visibility_buffer_bias.setter
    def visibility_buffer_bias(self, value: Annotated[float, "step=1.0", "precision=3"]) -> None:
        ...
    @property
    def visibility_bleed_bias(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Bias for reducing light-bleed on variance shadow maps (Deprecated)"""
        ...
    @visibility_bleed_bias.setter
    def visibility_bleed_bias(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def visibility_blur(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Filter size of the visibility blur (Deprecated)"""
        ...
    @visibility_blur.setter
    def visibility_blur(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def visibility_collection(self) -> Annotated[Optional['Collection'], "is_animatable=False"]:
        """Restrict objects visible for this probe (Deprecated)"""
        ...
    @visibility_collection.setter
    def visibility_collection(self, value: Annotated[Optional['Collection'], "is_animatable=False"]) -> None:
        ...
    @property
    def invert_visibility_collection(self) -> bool:
        """Invert visibility collection (Deprecated)"""
        ...
    @invert_visibility_collection.setter
    def invert_visibility_collection(self, value: bool) -> None:
        ...
    @property
    def show_data(self) -> bool:
        """Deprecated, use use_data_display instead"""
        ...
    @show_data.setter
    def show_data(self, value: bool) -> None:
        ...
    @property
    def use_data_display(self) -> bool:
        """Display sampled data in the viewport to debug captured light"""
        ...
    @use_data_display.setter
    def use_data_display(self, value: bool) -> None:
        ...
    @property
    def data_display_size(self) -> Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=3"]:
        """Viewport display size of the sampled data"""
        ...
    @data_display_size.setter
    def data_display_size(self, value: Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=3"]) -> None:
        ...
    @property
    def animation_data(self) -> Annotated[Optional['AnimData'], "is_animatable=False"]:
        """Animation data for this data-block"""
        ...
    @property
    def intensity(self) -> Annotated[float, "step=1.0", "precision=3"]:
        """Modify the intensity of the lighting captured by this probe"""
        ...
    @intensity.setter
    def intensity(self, value: Annotated[float, "step=1.0", "precision=3"]) -> None:
        ...
    @property
    def resolution_x(self) -> Annotated[int, "step=1"]:
        """Number of samples along the x axis of the volume"""
        ...
    @resolution_x.setter
    def resolution_x(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def resolution_y(self) -> Annotated[int, "step=1"]:
        """Number of samples along the y axis of the volume"""
        ...
    @resolution_y.setter
    def resolution_y(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def resolution_z(self) -> Annotated[int, "step=1"]:
        """Number of samples along the z axis of the volume"""
        ...
    @resolution_z.setter
    def resolution_z(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def capture_distance(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=1"]:
        """Distance around the probe volume that will be considered during the bake"""
        ...
    @capture_distance.setter
    def capture_distance(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=1"]) -> None:
        ...
    @property
    def normal_bias(self) -> Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=2"]:
        """Offset sampling of the irradiance grid in the surface normal direction to reduce light bleeding"""
        ...
    @normal_bias.setter
    def normal_bias(self, value: Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=2"]) -> None:
        ...
    @property
    def view_bias(self) -> Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=2"]:
        """Offset sampling of the irradiance grid in the viewing direction to reduce light bleeding"""
        ...
    @view_bias.setter
    def view_bias(self, value: Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=2"]) -> None:
        ...
    @property
    def facing_bias(self) -> Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=2"]:
        """Smoother irradiance interpolation but introduce light bleeding"""
        ...
    @facing_bias.setter
    def facing_bias(self, value: Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=2"]) -> None:
        ...
    @property
    def bake_samples(self) -> Annotated[int, "step=1"]:
        """Number of ray directions to evaluate when baking"""
        ...
    @bake_samples.setter
    def bake_samples(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def surface_bias(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Moves capture points away from surfaces to prevent artifacts"""
        ...
    @surface_bias.setter
    def surface_bias(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def escape_bias(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Distance to search for valid capture positions to prevent lighting artifacts"""
        ...
    @escape_bias.setter
    def escape_bias(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def surfel_density(self) -> Annotated[int, "step=1"]:
        """Number of surfels to spawn in one local unit distance (higher values improve quality)"""
        ...
    @surfel_density.setter
    def surfel_density(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def validity_threshold(self) -> Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=2"]:
        """Ratio of front-facing surface hits under which a grid sample will not be considered for lighting"""
        ...
    @validity_threshold.setter
    def validity_threshold(self, value: Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=2"]) -> None:
        ...
    @property
    def dilation_threshold(self) -> Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=2"]:
        """Ratio of front-facing surface hits under which a grid sample will reuse neighbors grid sample lighting"""
        ...
    @dilation_threshold.setter
    def dilation_threshold(self, value: Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=2"]) -> None:
        ...
    @property
    def dilation_radius(self) -> Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=2"]:
        """Radius in grid sample to search valid grid samples to copy into invalid grid samples"""
        ...
    @dilation_radius.setter
    def dilation_radius(self, value: Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=2"]) -> None:
        ...
    @property
    def capture_world(self) -> bool:
        """Bake incoming light from the world instead of just the visibility for more accurate lighting, but lose correct blending to surrounding irradiance volumes"""
        ...
    @capture_world.setter
    def capture_world(self, value: bool) -> None:
        ...
    @property
    def capture_indirect(self) -> bool:
        """Bake light bounces from light sources for more accurate lighting"""
        ...
    @capture_indirect.setter
    def capture_indirect(self, value: bool) -> None:
        ...
    @property
    def capture_emission(self) -> bool:
        """Bake emissive surfaces for more accurate lighting"""
        ...
    @capture_emission.setter
    def capture_emission(self, value: bool) -> None:
        ...
    @property
    def clamp_direct(self) -> Annotated[float, "step=1.0", "precision=2"]:
        """Clamp the direct lighting intensity to reduce noise (0 to disable)"""
        ...
    @clamp_direct.setter
    def clamp_direct(self, value: Annotated[float, "step=1.0", "precision=2"]) -> None:
        ...
    @property
    def clamp_indirect(self) -> Annotated[float, "step=1.0", "precision=2"]:
        """Clamp the indirect lighting intensity to reduce noise (0 to disable)"""
        ...
    @clamp_indirect.setter
    def clamp_indirect(self, value: Annotated[float, "step=1.0", "precision=2"]) -> None:
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