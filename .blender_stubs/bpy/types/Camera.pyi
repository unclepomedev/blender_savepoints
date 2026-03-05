# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.Camera.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .ID import ID
from .AnimData import AnimData
from .AssetMetaData import AssetMetaData
from .CameraBackgroundImage import CameraBackgroundImage
from .CameraBackgroundImages import CameraBackgroundImages
from .CameraDOFSettings import CameraDOFSettings
from .CameraStereoData import CameraStereoData
from .IDOverrideLibrary import IDOverrideLibrary
from .ImagePreview import ImagePreview
from .Library import Library
from .LibraryWeakReference import LibraryWeakReference
from .Text import Text
from .bpy_prop_collection import bpy_prop_collection

class Camera(ID):

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
    def type(self) -> Literal['PERSP', 'ORTHO', 'PANO', 'CUSTOM']:
        """Camera types"""
        ...
    @type.setter
    def type(self, value: Literal['PERSP', 'ORTHO', 'PANO', 'CUSTOM']) -> None:
        ...
    @property
    def sensor_fit(self) -> Literal['AUTO', 'HORIZONTAL', 'VERTICAL']:
        """Method to fit image and field of view angle inside the sensor"""
        ...
    @sensor_fit.setter
    def sensor_fit(self, value: Literal['AUTO', 'HORIZONTAL', 'VERTICAL']) -> None:
        ...
    @property
    def passepartout_alpha(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Opacity (alpha) of the darkened overlay in Camera view"""
        ...
    @passepartout_alpha.setter
    def passepartout_alpha(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def angle_x(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Camera lens horizontal field of view"""
        ...
    @angle_x.setter
    def angle_x(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3", "is_animatable=False"]) -> None:
        ...
    @property
    def angle_y(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Camera lens vertical field of view"""
        ...
    @angle_y.setter
    def angle_y(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3", "is_animatable=False"]) -> None:
        ...
    @property
    def angle(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Camera lens field of view"""
        ...
    @angle.setter
    def angle(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3", "is_animatable=False"]) -> None:
        ...
    @property
    def clip_start(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]:
        """Camera near clipping distance"""
        ...
    @clip_start.setter
    def clip_start(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def clip_end(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]:
        """Camera far clipping distance"""
        ...
    @clip_end.setter
    def clip_end(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def lens(self) -> Annotated[float, "subtype='DISTANCE_CAMERA'", "unit='CAMERA'", "step=100.0", "precision=4"]:
        """Perspective Camera focal length value in millimeters"""
        ...
    @lens.setter
    def lens(self, value: Annotated[float, "subtype='DISTANCE_CAMERA'", "unit='CAMERA'", "step=100.0", "precision=4"]) -> None:
        ...
    @property
    def sensor_width(self) -> Annotated[float, "subtype='DISTANCE_CAMERA'", "unit='CAMERA'", "step=100.0", "precision=4"]:
        """Horizontal size of the image sensor area in millimeters"""
        ...
    @sensor_width.setter
    def sensor_width(self, value: Annotated[float, "subtype='DISTANCE_CAMERA'", "unit='CAMERA'", "step=100.0", "precision=4"]) -> None:
        ...
    @property
    def sensor_height(self) -> Annotated[float, "subtype='DISTANCE_CAMERA'", "unit='CAMERA'", "step=100.0", "precision=4"]:
        """Vertical size of the image sensor area in millimeters"""
        ...
    @sensor_height.setter
    def sensor_height(self, value: Annotated[float, "subtype='DISTANCE_CAMERA'", "unit='CAMERA'", "step=100.0", "precision=4"]) -> None:
        ...
    @property
    def ortho_scale(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Orthographic Camera scale (similar to zoom)"""
        ...
    @ortho_scale.setter
    def ortho_scale(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def display_size(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=1.0", "precision=2"]:
        """Apparent size of the Camera object in the 3D View"""
        ...
    @display_size.setter
    def display_size(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=1.0", "precision=2"]) -> None:
        ...
    @property
    def shift_x(self) -> Annotated[float, "step=1.0", "precision=3"]:
        """Camera horizontal shift"""
        ...
    @shift_x.setter
    def shift_x(self, value: Annotated[float, "step=1.0", "precision=3"]) -> None:
        ...
    @property
    def shift_y(self) -> Annotated[float, "step=1.0", "precision=3"]:
        """Camera vertical shift"""
        ...
    @shift_y.setter
    def shift_y(self, value: Annotated[float, "step=1.0", "precision=3"]) -> None:
        ...
    @property
    def stereo(self) -> Annotated['CameraStereoData', "is_animatable=False"]:

        ...
    @property
    def show_limits(self) -> bool:
        """Display the clipping range and focus point on the camera"""
        ...
    @show_limits.setter
    def show_limits(self, value: bool) -> None:
        ...
    @property
    def show_mist(self) -> bool:
        """Display a line from the Camera to indicate the mist area"""
        ...
    @show_mist.setter
    def show_mist(self, value: bool) -> None:
        ...
    @property
    def show_passepartout(self) -> bool:
        """Show a darkened overlay outside the image area in Camera view"""
        ...
    @show_passepartout.setter
    def show_passepartout(self, value: bool) -> None:
        ...
    @property
    def show_safe_areas(self) -> bool:
        """Show TV title safe and action safe areas in Camera view"""
        ...
    @show_safe_areas.setter
    def show_safe_areas(self, value: bool) -> None:
        ...
    @property
    def show_safe_center(self) -> bool:
        """Show safe areas to fit content in a different aspect ratio"""
        ...
    @show_safe_center.setter
    def show_safe_center(self, value: bool) -> None:
        ...
    @property
    def show_name(self) -> bool:
        """Show the active Camera's name in Camera view"""
        ...
    @show_name.setter
    def show_name(self, value: bool) -> None:
        ...
    @property
    def show_sensor(self) -> bool:
        """Show sensor size (film gate) in Camera view"""
        ...
    @show_sensor.setter
    def show_sensor(self, value: bool) -> None:
        ...
    @property
    def show_background_images(self) -> bool:
        """Display reference images behind objects in the 3D View"""
        ...
    @show_background_images.setter
    def show_background_images(self, value: bool) -> None:
        ...
    @property
    def lens_unit(self) -> Literal['MILLIMETERS', 'FOV']:
        """Unit to edit lens in for the user interface"""
        ...
    @lens_unit.setter
    def lens_unit(self, value: Literal['MILLIMETERS', 'FOV']) -> None:
        ...
    @property
    def composition_guide_color(self) -> Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]:
        """Color and alpha for compositional guide overlays"""
        ...
    @composition_guide_color.setter
    def composition_guide_color(self, value: Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def show_composition_center(self) -> bool:
        """Display center composition guide inside the camera view"""
        ...
    @show_composition_center.setter
    def show_composition_center(self, value: bool) -> None:
        ...
    @property
    def show_composition_center_diagonal(self) -> bool:
        """Display diagonal center composition guide inside the camera view"""
        ...
    @show_composition_center_diagonal.setter
    def show_composition_center_diagonal(self, value: bool) -> None:
        ...
    @property
    def show_composition_thirds(self) -> bool:
        """Display rule of thirds composition guide inside the camera view"""
        ...
    @show_composition_thirds.setter
    def show_composition_thirds(self, value: bool) -> None:
        ...
    @property
    def show_composition_golden(self) -> bool:
        """Display golden ratio composition guide inside the camera view"""
        ...
    @show_composition_golden.setter
    def show_composition_golden(self, value: bool) -> None:
        ...
    @property
    def show_composition_golden_tria_a(self) -> bool:
        """Display golden triangle A composition guide inside the camera view"""
        ...
    @show_composition_golden_tria_a.setter
    def show_composition_golden_tria_a(self, value: bool) -> None:
        ...
    @property
    def show_composition_golden_tria_b(self) -> bool:
        """Display golden triangle B composition guide inside the camera view"""
        ...
    @show_composition_golden_tria_b.setter
    def show_composition_golden_tria_b(self, value: bool) -> None:
        ...
    @property
    def show_composition_harmony_tri_a(self) -> bool:
        """Display harmony A composition guide inside the camera view"""
        ...
    @show_composition_harmony_tri_a.setter
    def show_composition_harmony_tri_a(self, value: bool) -> None:
        ...
    @property
    def show_composition_harmony_tri_b(self) -> bool:
        """Display harmony B composition guide inside the camera view"""
        ...
    @show_composition_harmony_tri_b.setter
    def show_composition_harmony_tri_b(self, value: bool) -> None:
        ...
    @property
    def panorama_type(self) -> Literal['EQUIRECTANGULAR', 'EQUIANGULAR_CUBEMAP_FACE', 'MIRRORBALL', 'FISHEYE_EQUIDISTANT', 'FISHEYE_EQUISOLID', 'FISHEYE_LENS_POLYNOMIAL', 'CENTRAL_CYLINDRICAL']:
        """Distortion to use for the calculation"""
        ...
    @panorama_type.setter
    def panorama_type(self, value: Literal['EQUIRECTANGULAR', 'EQUIANGULAR_CUBEMAP_FACE', 'MIRRORBALL', 'FISHEYE_EQUIDISTANT', 'FISHEYE_EQUISOLID', 'FISHEYE_LENS_POLYNOMIAL', 'CENTRAL_CYLINDRICAL']) -> None:
        ...
    @property
    def fisheye_fov(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=3.0", "precision=2"]:
        """Field of view for the fisheye lens"""
        ...
    @fisheye_fov.setter
    def fisheye_fov(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=3.0", "precision=2"]) -> None:
        ...
    @property
    def fisheye_lens(self) -> Annotated[float, "step=3.0", "precision=2"]:
        """Lens focal length (mm)"""
        ...
    @fisheye_lens.setter
    def fisheye_lens(self, value: Annotated[float, "step=3.0", "precision=2"]) -> None:
        ...
    @property
    def latitude_min(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=3.0", "precision=2"]:
        """Minimum latitude (vertical angle) for the equirectangular lens"""
        ...
    @latitude_min.setter
    def latitude_min(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=3.0", "precision=2"]) -> None:
        ...
    @property
    def latitude_max(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=3.0", "precision=2"]:
        """Maximum latitude (vertical angle) for the equirectangular lens"""
        ...
    @latitude_max.setter
    def latitude_max(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=3.0", "precision=2"]) -> None:
        ...
    @property
    def longitude_min(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=3.0", "precision=2"]:
        """Minimum longitude (horizontal angle) for the equirectangular lens"""
        ...
    @longitude_min.setter
    def longitude_min(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=3.0", "precision=2"]) -> None:
        ...
    @property
    def longitude_max(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=3.0", "precision=2"]:
        """Maximum longitude (horizontal angle) for the equirectangular lens"""
        ...
    @longitude_max.setter
    def longitude_max(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=3.0", "precision=2"]) -> None:
        ...
    @property
    def fisheye_polynomial_k0(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=0.10000000149011612", "precision=6"]:
        """Coefficient K0 of the lens polynomial"""
        ...
    @fisheye_polynomial_k0.setter
    def fisheye_polynomial_k0(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=0.10000000149011612", "precision=6"]) -> None:
        ...
    @property
    def fisheye_polynomial_k1(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=0.10000000149011612", "precision=6"]:
        """Coefficient K1 of the lens polynomial"""
        ...
    @fisheye_polynomial_k1.setter
    def fisheye_polynomial_k1(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=0.10000000149011612", "precision=6"]) -> None:
        ...
    @property
    def fisheye_polynomial_k2(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=0.10000000149011612", "precision=6"]:
        """Coefficient K2 of the lens polynomial"""
        ...
    @fisheye_polynomial_k2.setter
    def fisheye_polynomial_k2(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=0.10000000149011612", "precision=6"]) -> None:
        ...
    @property
    def fisheye_polynomial_k3(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=0.10000000149011612", "precision=6"]:
        """Coefficient K3 of the lens polynomial"""
        ...
    @fisheye_polynomial_k3.setter
    def fisheye_polynomial_k3(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=0.10000000149011612", "precision=6"]) -> None:
        ...
    @property
    def fisheye_polynomial_k4(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=0.10000000149011612", "precision=6"]:
        """Coefficient K4 of the lens polynomial"""
        ...
    @fisheye_polynomial_k4.setter
    def fisheye_polynomial_k4(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=0.10000000149011612", "precision=6"]) -> None:
        ...
    @property
    def central_cylindrical_range_u_min(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=3.0", "precision=2"]:
        """Minimum Longitude value for the central cylindrical lens"""
        ...
    @central_cylindrical_range_u_min.setter
    def central_cylindrical_range_u_min(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=3.0", "precision=2"]) -> None:
        ...
    @property
    def central_cylindrical_range_u_max(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=3.0", "precision=2"]:
        """Maximum Longitude value for the central cylindrical lens"""
        ...
    @central_cylindrical_range_u_max.setter
    def central_cylindrical_range_u_max(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=3.0", "precision=2"]) -> None:
        ...
    @property
    def central_cylindrical_range_v_min(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.10000000149011612", "precision=3"]:
        """Minimum Height value for the central cylindrical lens"""
        ...
    @central_cylindrical_range_v_min.setter
    def central_cylindrical_range_v_min(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.10000000149011612", "precision=3"]) -> None:
        ...
    @property
    def central_cylindrical_range_v_max(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.10000000149011612", "precision=3"]:
        """Maximum Height value for the central cylindrical lens"""
        ...
    @central_cylindrical_range_v_max.setter
    def central_cylindrical_range_v_max(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.10000000149011612", "precision=3"]) -> None:
        ...
    @property
    def central_cylindrical_radius(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.10000000149011612", "precision=3"]:
        """Radius of the virtual cylinder"""
        ...
    @central_cylindrical_radius.setter
    def central_cylindrical_radius(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.10000000149011612", "precision=3"]) -> None:
        ...
    @property
    def custom_filepath(self) -> Annotated[str, "subtype='FILE_PATH'", "is_animatable=False"]:
        """Path to the shader defining the custom camera"""
        ...
    @custom_filepath.setter
    def custom_filepath(self, value: Annotated[str, "subtype='FILE_PATH'", "is_animatable=False"]) -> None:
        ...
    @property
    def custom_shader(self) -> Annotated[Optional['Text'], "is_animatable=False"]:
        """Shader defining the custom camera"""
        ...
    @custom_shader.setter
    def custom_shader(self, value: Annotated[Optional['Text'], "is_animatable=False"]) -> None:
        ...
    @property
    def custom_mode(self) -> Literal['INTERNAL', 'EXTERNAL']:

        ...
    @custom_mode.setter
    def custom_mode(self, value: Literal['INTERNAL', 'EXTERNAL']) -> None:
        ...
    @property
    def custom_bytecode(self) -> Annotated[str, "is_animatable=False"]:
        """Compiled bytecode of the custom shader"""
        ...
    @custom_bytecode.setter
    def custom_bytecode(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def custom_bytecode_hash(self) -> Annotated[str, "is_animatable=False"]:
        """Hash of the compiled bytecode of the custom shader, for quick equality checking"""
        ...
    @custom_bytecode_hash.setter
    def custom_bytecode_hash(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def dof(self) -> Annotated[Optional['CameraDOFSettings'], "is_animatable=False"]:

        ...
    @property
    def background_images(self) -> Annotated['CameraBackgroundImages', "is_animatable=False"]:
        """List of background images"""
        ...
    @property
    def animation_data(self) -> Annotated[Optional['AnimData'], "is_animatable=False"]:
        """Animation data for this data-block"""
        ...
    @property
    def cycles_custom(self) -> Annotated[Optional['CyclesCustomCameraSettings'], "is_animatable=False"]:
        """Parameters for custom (OSL-based) cameras"""
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
    def view_frame(self, *args, **kwargs) -> Any: ...