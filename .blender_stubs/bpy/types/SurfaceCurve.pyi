# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.SurfaceCurve.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .Curve import Curve
from .AnimData import AnimData
from .AssetMetaData import AssetMetaData
from .CurveProfile import CurveProfile
from .CurveSplines import CurveSplines
from .ID import ID
from .IDMaterials import IDMaterials
from .IDOverrideLibrary import IDOverrideLibrary
from .ImagePreview import ImagePreview
from .Key import Key
from .Library import Library
from .LibraryWeakReference import LibraryWeakReference
from .Material import Material
from .Object import Object
from .Spline import Spline
from .bpy_prop_collection import bpy_prop_collection

class SurfaceCurve(Curve):

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
    def shape_keys(self) -> Annotated[Optional['Key'], "is_animatable=False"]:

        ...
    @property
    def splines(self) -> Annotated['CurveSplines', "is_animatable=False"]:
        """Collection of splines in this curve data object"""
        ...
    @property
    def path_duration(self) -> Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1"]:
        """The number of frames that are needed to traverse the path, defining the maximum value for the 'Evaluation Time' setting"""
        ...
    @path_duration.setter
    def path_duration(self, value: Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1"]):
        ...
    @property
    def use_path(self) -> bool:
        """Enable the curve to become a translation path"""
        ...
    @use_path.setter
    def use_path(self, value: bool):
        ...
    @property
    def use_path_follow(self) -> bool:
        """Make curve path children rotate along the path"""
        ...
    @use_path_follow.setter
    def use_path_follow(self, value: bool):
        ...
    @property
    def use_path_clamp(self) -> bool:
        """Clamp the curve path children so they cannot travel past the start/end point of the curve"""
        ...
    @use_path_clamp.setter
    def use_path_clamp(self, value: bool):
        ...
    @property
    def use_stretch(self) -> bool:
        """Option for curve-deform: make deformed child stretch along entire path"""
        ...
    @use_stretch.setter
    def use_stretch(self, value: bool):
        ...
    @property
    def use_deform_bounds(self) -> bool:
        """Option for curve-deform: Use the mesh bounds to clamp the deformation"""
        ...
    @use_deform_bounds.setter
    def use_deform_bounds(self, value: bool):
        ...
    @property
    def use_radius(self) -> bool:
        """Option for paths and curve-deform: apply the curve radius to objects following it and to deformed objects"""
        ...
    @use_radius.setter
    def use_radius(self, value: bool):
        ...
    @property
    def bevel_mode(self) -> Literal['ROUND', 'OBJECT', 'PROFILE']:
        """Determine how to build the curve's bevel geometry"""
        ...
    @bevel_mode.setter
    def bevel_mode(self, value: Literal['ROUND', 'OBJECT', 'PROFILE']):
        ...
    @property
    def bevel_profile(self) -> Annotated[Optional['CurveProfile'], "is_animatable=False"]:
        """The path for the curve's custom profile"""
        ...
    @property
    def bevel_resolution(self) -> Annotated[int, "step=1"]:
        """The number of segments in each quarter-circle of the bevel"""
        ...
    @bevel_resolution.setter
    def bevel_resolution(self, value: Annotated[int, "step=1"]):
        ...
    @property
    def offset(self) -> Annotated[float, "subtype=''", "unit='LENGTH'", "step=0.10000000149011612", "precision=3"]:
        """Distance to move the curve parallel to its normals"""
        ...
    @offset.setter
    def offset(self, value: Annotated[float, "subtype=''", "unit='LENGTH'", "step=0.10000000149011612", "precision=3"]):
        ...
    @property
    def extrude(self) -> Annotated[float, "subtype=''", "unit='LENGTH'", "step=0.10000000149011612", "precision=3"]:
        """Length of the depth added in the local Z direction along the curve, perpendicular to its normals"""
        ...
    @extrude.setter
    def extrude(self, value: Annotated[float, "subtype=''", "unit='LENGTH'", "step=0.10000000149011612", "precision=3"]):
        ...
    @property
    def bevel_depth(self) -> Annotated[float, "subtype=''", "unit='LENGTH'", "step=0.10000000149011612", "precision=3"]:
        """Radius of the bevel geometry, not including extrusion"""
        ...
    @bevel_depth.setter
    def bevel_depth(self, value: Annotated[float, "subtype=''", "unit='LENGTH'", "step=0.10000000149011612", "precision=3"]):
        ...
    @property
    def resolution_u(self) -> Annotated[int, "step=1", "is_animatable=False"]:
        """Number of computed points in the U direction between every pair of control points"""
        ...
    @resolution_u.setter
    def resolution_u(self, value: Annotated[int, "step=1", "is_animatable=False"]):
        ...
    @property
    def resolution_v(self) -> Annotated[int, "step=1", "is_animatable=False"]:
        """The number of computed points in the V direction between every pair of control points"""
        ...
    @resolution_v.setter
    def resolution_v(self, value: Annotated[int, "step=1", "is_animatable=False"]):
        ...
    @property
    def render_resolution_u(self) -> Annotated[int, "step=1"]:
        """Surface resolution in U direction used while rendering (zero uses preview resolution)"""
        ...
    @render_resolution_u.setter
    def render_resolution_u(self, value: Annotated[int, "step=1"]):
        ...
    @property
    def render_resolution_v(self) -> Annotated[int, "step=1"]:
        """Surface resolution in V direction used while rendering (zero uses preview resolution)"""
        ...
    @render_resolution_v.setter
    def render_resolution_v(self, value: Annotated[int, "step=1"]):
        ...
    @property
    def eval_time(self) -> Annotated[float, "subtype='TIME'", "unit='TIME'", "step=10.0", "precision=3"]:
        """Parametric position along the length of the curve that Objects 'following' it should be at (position is evaluated by dividing by the 'Path Length' value)"""
        ...
    @eval_time.setter
    def eval_time(self, value: Annotated[float, "subtype='TIME'", "unit='TIME'", "step=10.0", "precision=3"]):
        ...
    @property
    def bevel_object(self) -> Annotated[Optional['Object'], "is_animatable=False"]:
        """The name of the Curve object that defines the bevel shape"""
        ...
    @bevel_object.setter
    def bevel_object(self, value: Annotated[Optional['Object'], "is_animatable=False"]):
        ...
    @property
    def taper_object(self) -> Annotated[Optional['Object'], "is_animatable=False"]:
        """Curve object name that defines the taper (width)"""
        ...
    @taper_object.setter
    def taper_object(self, value: Annotated[Optional['Object'], "is_animatable=False"]):
        ...
    @property
    def dimensions(self) -> Literal['2D', '3D']:
        """Select 2D or 3D curve type"""
        ...
    @dimensions.setter
    def dimensions(self, value: Literal['2D', '3D']):
        ...
    @property
    def fill_mode(self) -> Literal['FULL', 'BACK', 'FRONT', 'HALF']:
        """Mode of filling curve"""
        ...
    @fill_mode.setter
    def fill_mode(self, value: Literal['FULL', 'BACK', 'FRONT', 'HALF']):
        ...
    @property
    def twist_mode(self) -> Literal['Z_UP', 'MINIMUM', 'TANGENT']:
        """The type of tilt calculation for 3D Curves"""
        ...
    @twist_mode.setter
    def twist_mode(self, value: Literal['Z_UP', 'MINIMUM', 'TANGENT']):
        ...
    @property
    def taper_radius_mode(self) -> Literal['OVERRIDE', 'MULTIPLY', 'ADD']:
        """Determine how the effective radius of the spline point is computed when a taper object is specified"""
        ...
    @taper_radius_mode.setter
    def taper_radius_mode(self, value: Literal['OVERRIDE', 'MULTIPLY', 'ADD']):
        ...
    @property
    def bevel_factor_mapping_start(self) -> Literal['RESOLUTION', 'SEGMENTS', 'SPLINE']:
        """Determine how the geometry start factor is mapped to a spline"""
        ...
    @bevel_factor_mapping_start.setter
    def bevel_factor_mapping_start(self, value: Literal['RESOLUTION', 'SEGMENTS', 'SPLINE']):
        ...
    @property
    def bevel_factor_mapping_end(self) -> Literal['RESOLUTION', 'SEGMENTS', 'SPLINE']:
        """Determine how the geometry end factor is mapped to a spline"""
        ...
    @bevel_factor_mapping_end.setter
    def bevel_factor_mapping_end(self, value: Literal['RESOLUTION', 'SEGMENTS', 'SPLINE']):
        ...
    @property
    def twist_smooth(self) -> Annotated[float, "step=1.0", "precision=2"]:
        """Smoothing iteration for tangents"""
        ...
    @twist_smooth.setter
    def twist_smooth(self, value: Annotated[float, "step=1.0", "precision=2"]):
        ...
    @property
    def use_fill_caps(self) -> bool:
        """Fill caps for beveled curves"""
        ...
    @use_fill_caps.setter
    def use_fill_caps(self, value: bool):
        ...
    @property
    def use_map_taper(self) -> bool:
        """Map effect of the taper object to the beveled part of the curve"""
        ...
    @use_map_taper.setter
    def use_map_taper(self, value: bool):
        ...
    @property
    def use_auto_texspace(self) -> bool:
        """Adjust active object's texture space automatically when transforming object"""
        ...
    @use_auto_texspace.setter
    def use_auto_texspace(self, value: bool):
        ...
    @property
    def texspace_location(self) -> Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=1.0", "precision=5"]:

        ...
    @texspace_location.setter
    def texspace_location(self, value: Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=1.0", "precision=5"]):
        ...
    @property
    def texspace_size(self) -> Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]:

        ...
    @texspace_size.setter
    def texspace_size(self, value: Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]):
        ...
    @property
    def materials(self) -> Annotated['IDMaterials', "is_animatable=False"]:

        ...
    @property
    def bevel_factor_start(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Define where along the spline the curve geometry starts (0 for the beginning, 1 for the end)"""
        ...
    @bevel_factor_start.setter
    def bevel_factor_start(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def bevel_factor_end(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Define where along the spline the curve geometry ends (0 for the beginning, 1 for the end)"""
        ...
    @bevel_factor_end.setter
    def bevel_factor_end(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def is_editmode(self) -> bool:
        """True when used in editmode"""
        ...
    @property
    def animation_data(self) -> Annotated[Optional['AnimData'], "is_animatable=False"]:
        """Animation data for this data-block"""
        ...
    @property
    def cycles(self) -> Annotated[Optional['CyclesMeshSettings'], "is_animatable=False"]:
        """Cycles mesh settings"""
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
    def transform(self, *args, **kwargs) -> Any: ...
    def validate_material_indices(self, *args, **kwargs) -> Any: ...
    def update_gpu_tag(self, *args, **kwargs) -> Any: ...