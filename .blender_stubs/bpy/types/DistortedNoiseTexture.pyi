# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.DistortedNoiseTexture.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .Texture import Texture
from .AnimData import AnimData
from .AssetMetaData import AssetMetaData
from .ColorRamp import ColorRamp
from .ID import ID
from .IDOverrideLibrary import IDOverrideLibrary
from .ImagePreview import ImagePreview
from .Library import Library
from .LibraryWeakReference import LibraryWeakReference
from .NodeTree import NodeTree

class DistortedNoiseTexture(Texture):

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
    def type(self) -> Literal['NONE', 'BLEND', 'CLOUDS', 'DISTORTED_NOISE', 'IMAGE', 'MAGIC', 'MARBLE', 'MUSGRAVE', 'NOISE', 'STUCCI', 'VORONOI', 'WOOD']:

        ...
    @type.setter
    def type(self, value: Literal['NONE', 'BLEND', 'CLOUDS', 'DISTORTED_NOISE', 'IMAGE', 'MAGIC', 'MARBLE', 'MUSGRAVE', 'NOISE', 'STUCCI', 'VORONOI', 'WOOD']) -> None:
        ...
    @property
    def use_clamp(self) -> bool:
        """Set negative texture RGB and intensity values to zero, for some uses like displacement this option can be disabled to get the full range"""
        ...
    @use_clamp.setter
    def use_clamp(self, value: bool) -> None:
        ...
    @property
    def use_color_ramp(self) -> bool:
        """Map the texture intensity to the color ramp. Note that the alpha value is used for image textures, enable "Calculate Alpha" for images without an alpha channel."""
        ...
    @use_color_ramp.setter
    def use_color_ramp(self, value: bool) -> None:
        ...
    @property
    def color_ramp(self) -> Annotated[Optional['ColorRamp'], "subtype=''", "unit='MASS'", "is_animatable=False"]:

        ...
    @property
    def intensity(self) -> Annotated[float, "step=1.0", "precision=3"]:
        """Adjust the brightness of the texture"""
        ...
    @intensity.setter
    def intensity(self, value: Annotated[float, "step=1.0", "precision=3"]) -> None:
        ...
    @property
    def contrast(self) -> Annotated[float, "step=1.0", "precision=3"]:
        """Adjust the contrast of the texture"""
        ...
    @contrast.setter
    def contrast(self, value: Annotated[float, "step=1.0", "precision=3"]) -> None:
        ...
    @property
    def saturation(self) -> Annotated[float, "step=1.0", "precision=3"]:
        """Adjust the saturation of colors in the texture"""
        ...
    @saturation.setter
    def saturation(self, value: Annotated[float, "step=1.0", "precision=3"]) -> None:
        ...
    @property
    def factor_red(self) -> Annotated[float, "step=1.0", "precision=3"]:

        ...
    @factor_red.setter
    def factor_red(self, value: Annotated[float, "step=1.0", "precision=3"]) -> None:
        ...
    @property
    def factor_green(self) -> Annotated[float, "step=1.0", "precision=3"]:

        ...
    @factor_green.setter
    def factor_green(self, value: Annotated[float, "step=1.0", "precision=3"]) -> None:
        ...
    @property
    def factor_blue(self) -> Annotated[float, "step=1.0", "precision=3"]:

        ...
    @factor_blue.setter
    def factor_blue(self, value: Annotated[float, "step=1.0", "precision=3"]) -> None:
        ...
    @property
    def use_preview_alpha(self) -> bool:
        """Show Alpha in Preview Render"""
        ...
    @use_preview_alpha.setter
    def use_preview_alpha(self, value: bool) -> None:
        ...
    @property
    def use_nodes(self) -> bool:
        """Make this a node-based texture"""
        ...
    @use_nodes.setter
    def use_nodes(self, value: bool) -> None:
        ...
    @property
    def node_tree(self) -> Annotated[Optional['NodeTree'], "is_animatable=False"]:
        """Node tree for node-based textures"""
        ...
    @property
    def animation_data(self) -> Annotated[Optional['AnimData'], "is_animatable=False"]:
        """Animation data for this data-block"""
        ...
    @property
    def distortion(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Amount of distortion"""
        ...
    @distortion.setter
    def distortion(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def noise_scale(self) -> Annotated[float, "step=1.0", "precision=2"]:
        """Scaling for noise input"""
        ...
    @noise_scale.setter
    def noise_scale(self, value: Annotated[float, "step=1.0", "precision=2"]) -> None:
        ...
    @property
    def noise_basis(self) -> Literal['BLENDER_ORIGINAL', 'ORIGINAL_PERLIN', 'IMPROVED_PERLIN', 'VORONOI_F1', 'VORONOI_F2', 'VORONOI_F3', 'VORONOI_F4', 'VORONOI_F2_F1', 'VORONOI_CRACKLE', 'CELL_NOISE']:
        """Noise basis used for turbulence"""
        ...
    @noise_basis.setter
    def noise_basis(self, value: Literal['BLENDER_ORIGINAL', 'ORIGINAL_PERLIN', 'IMPROVED_PERLIN', 'VORONOI_F1', 'VORONOI_F2', 'VORONOI_F3', 'VORONOI_F4', 'VORONOI_F2_F1', 'VORONOI_CRACKLE', 'CELL_NOISE']) -> None:
        ...
    @property
    def noise_distortion(self) -> Literal['BLENDER_ORIGINAL', 'ORIGINAL_PERLIN', 'IMPROVED_PERLIN', 'VORONOI_F1', 'VORONOI_F2', 'VORONOI_F3', 'VORONOI_F4', 'VORONOI_F2_F1', 'VORONOI_CRACKLE', 'CELL_NOISE']:
        """Noise basis for the distortion"""
        ...
    @noise_distortion.setter
    def noise_distortion(self, value: Literal['BLENDER_ORIGINAL', 'ORIGINAL_PERLIN', 'IMPROVED_PERLIN', 'VORONOI_F1', 'VORONOI_F2', 'VORONOI_F3', 'VORONOI_F4', 'VORONOI_F2_F1', 'VORONOI_CRACKLE', 'CELL_NOISE']) -> None:
        ...
    @property
    def nabla(self) -> Annotated[float, "step=1.0", "precision=2"]:
        """Size of derivative offset used for calculating normal"""
        ...
    @nabla.setter
    def nabla(self, value: Annotated[float, "step=1.0", "precision=2"]) -> None:
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
    def evaluate(self, *args, **kwargs) -> Any: ...