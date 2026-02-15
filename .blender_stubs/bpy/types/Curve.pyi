# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.Curve.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .ID import ID
from .AnimData import AnimData
from .AssetMetaData import AssetMetaData
from .CurveProfile import CurveProfile
from .CurveSplines import CurveSplines
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

class Curve(ID):

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
    @property
    def shape_keys(self) -> Annotated[Optional['Key'], "is_animatable=False"]:

        ...
    @property
    def splines(self) -> Annotated['CurveSplines', "is_animatable=False"]:
        """Collection of splines in this curve data object"""
        ...
    path_duration: Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1"]
    """The number of frames that are needed to traverse the path, defining the maximum value for the 'Evaluation Time' setting"""
    use_path: bool
    """Enable the curve to become a translation path"""
    use_path_follow: bool
    """Make curve path children rotate along the path"""
    use_path_clamp: bool
    """Clamp the curve path children so they cannot travel past the start/end point of the curve"""
    use_stretch: bool
    """Option for curve-deform: make deformed child stretch along entire path"""
    use_deform_bounds: bool
    """Option for curve-deform: Use the mesh bounds to clamp the deformation"""
    use_radius: bool
    """Option for paths and curve-deform: apply the curve radius to objects following it and to deformed objects"""
    bevel_mode: Literal['ROUND', 'OBJECT', 'PROFILE']
    """Determine how to build the curve's bevel geometry"""
    @property
    def bevel_profile(self) -> Annotated[Optional['CurveProfile'], "is_animatable=False"]:
        """The path for the curve's custom profile"""
        ...
    bevel_resolution: Annotated[int, "step=1"]
    """The number of segments in each quarter-circle of the bevel"""
    offset: Annotated[float, "subtype=''", "unit='LENGTH'", "step=0.10000000149011612", "precision=3"]
    """Distance to move the curve parallel to its normals"""
    extrude: Annotated[float, "subtype=''", "unit='LENGTH'", "step=0.10000000149011612", "precision=3"]
    """Length of the depth added in the local Z direction along the curve, perpendicular to its normals"""
    bevel_depth: Annotated[float, "subtype=''", "unit='LENGTH'", "step=0.10000000149011612", "precision=3"]
    """Radius of the bevel geometry, not including extrusion"""
    resolution_u: Annotated[int, "step=1", "is_animatable=False"]
    """Number of computed points in the U direction between every pair of control points"""
    resolution_v: Annotated[int, "step=1", "is_animatable=False"]
    """The number of computed points in the V direction between every pair of control points"""
    render_resolution_u: Annotated[int, "step=1"]
    """Surface resolution in U direction used while rendering (zero uses preview resolution)"""
    render_resolution_v: Annotated[int, "step=1"]
    """Surface resolution in V direction used while rendering (zero uses preview resolution)"""
    eval_time: Annotated[float, "subtype='TIME'", "unit='TIME'", "step=10.0", "precision=3"]
    """Parametric position along the length of the curve that Objects 'following' it should be at (position is evaluated by dividing by the 'Path Length' value)"""
    bevel_object: Annotated[Optional['Object'], "is_animatable=False"]
    """The name of the Curve object that defines the bevel shape"""
    taper_object: Annotated[Optional['Object'], "is_animatable=False"]
    """Curve object name that defines the taper (width)"""
    dimensions: Literal['2D', '3D']
    """Select 2D or 3D curve type"""
    fill_mode: Literal['FULL', 'BACK', 'FRONT', 'HALF']
    """Mode of filling curve"""
    twist_mode: Literal['Z_UP', 'MINIMUM', 'TANGENT']
    """The type of tilt calculation for 3D Curves"""
    taper_radius_mode: Literal['OVERRIDE', 'MULTIPLY', 'ADD']
    """Determine how the effective radius of the spline point is computed when a taper object is specified"""
    bevel_factor_mapping_start: Literal['RESOLUTION', 'SEGMENTS', 'SPLINE']
    """Determine how the geometry start factor is mapped to a spline"""
    bevel_factor_mapping_end: Literal['RESOLUTION', 'SEGMENTS', 'SPLINE']
    """Determine how the geometry end factor is mapped to a spline"""
    twist_smooth: Annotated[float, "step=1.0", "precision=2"]
    """Smoothing iteration for tangents"""
    use_fill_caps: bool
    """Fill caps for beveled curves"""
    use_map_taper: bool
    """Map effect of the taper object to the beveled part of the curve"""
    use_auto_texspace: bool
    """Adjust active object's texture space automatically when transforming object"""
    texspace_location: Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=1.0", "precision=5"]

    texspace_size: Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]

    @property
    def materials(self) -> Annotated['IDMaterials', "is_animatable=False"]:

        ...
    bevel_factor_start: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Define where along the spline the curve geometry starts (0 for the beginning, 1 for the end)"""
    bevel_factor_end: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Define where along the spline the curve geometry ends (0 for the beginning, 1 for the end)"""
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