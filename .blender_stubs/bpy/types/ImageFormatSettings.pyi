# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.ImageFormatSettings.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .ColorManagedDisplaySettings import ColorManagedDisplaySettings
from .ColorManagedInputColorspaceSettings import ColorManagedInputColorspaceSettings
from .ColorManagedViewSettings import ColorManagedViewSettings
from .Stereo3dFormat import Stereo3dFormat

class ImageFormatSettings(bpy_struct):

    @property
    def media_type(self) -> Annotated[Literal['IMAGE', 'MULTI_LAYER_IMAGE', 'VIDEO'], "is_animatable=False"]:
        """The type of media to save"""
        ...
    @media_type.setter
    def media_type(self, value: Annotated[Literal['IMAGE', 'MULTI_LAYER_IMAGE', 'VIDEO'], "is_animatable=False"]):
        ...
    @property
    def file_format(self) -> Annotated[Literal['JPEG', 'OPEN_EXR', 'PNG', 'WEBP', 'BMP', 'CINEON', 'DPX', 'IRIS', 'JPEG2000', 'HDR', 'TARGA', 'TARGA_RAW', 'TIFF', 'OPEN_EXR_MULTILAYER', 'FFMPEG'], "is_animatable=False"]:
        """File format to save the rendered images as"""
        ...
    @file_format.setter
    def file_format(self, value: Annotated[Literal['JPEG', 'OPEN_EXR', 'PNG', 'WEBP', 'BMP', 'CINEON', 'DPX', 'IRIS', 'JPEG2000', 'HDR', 'TARGA', 'TARGA_RAW', 'TIFF', 'OPEN_EXR_MULTILAYER', 'FFMPEG'], "is_animatable=False"]):
        ...
    @property
    def color_mode(self) -> Annotated[Literal['BW', 'RGB', 'RGBA'], "is_animatable=False"]:
        """Choose BW for saving grayscale images, RGB for saving red, green and blue channels, and RGBA for saving red, green, blue and alpha channels"""
        ...
    @color_mode.setter
    def color_mode(self, value: Annotated[Literal['BW', 'RGB', 'RGBA'], "is_animatable=False"]):
        ...
    @property
    def color_depth(self) -> Annotated[Literal['8', '10', '12', '16', '32'], "is_animatable=False"]:
        """Bit depth per channel"""
        ...
    @color_depth.setter
    def color_depth(self, value: Annotated[Literal['8', '10', '12', '16', '32'], "is_animatable=False"]):
        ...
    @property
    def quality(self) -> Annotated[int, "subtype='PERCENTAGE'", "step=1", "is_animatable=False"]:
        """Quality for image formats that support lossy compression"""
        ...
    @quality.setter
    def quality(self, value: Annotated[int, "subtype='PERCENTAGE'", "step=1", "is_animatable=False"]):
        ...
    @property
    def compression(self) -> Annotated[int, "subtype='PERCENTAGE'", "step=1", "is_animatable=False"]:
        """Amount of time to determine best compression: 0 = no compression with fast file output, 100 = maximum lossless compression with slow file output"""
        ...
    @compression.setter
    def compression(self, value: Annotated[int, "subtype='PERCENTAGE'", "step=1", "is_animatable=False"]):
        ...
    @property
    def use_preview(self) -> Annotated[bool, "is_animatable=False"]:
        """When rendering animations, save JPG preview images in same directory"""
        ...
    @use_preview.setter
    def use_preview(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def exr_codec(self) -> Annotated[Literal['NONE', 'ZIP', 'PIZ', 'DWAA', 'DWAB', 'ZIPS', 'RLE', 'PXR24', 'B44', 'B44A'], "is_animatable=False"]:
        """Compression codec settings for OpenEXR"""
        ...
    @exr_codec.setter
    def exr_codec(self, value: Annotated[Literal['NONE', 'ZIP', 'PIZ', 'DWAA', 'DWAB', 'ZIPS', 'RLE', 'PXR24', 'B44', 'B44A'], "is_animatable=False"]):
        ...
    @property
    def use_exr_interleave(self) -> Annotated[bool, "is_animatable=False"]:
        """Use legacy interleaved storage of views, layers and passes for compatibility with applications that do not support more efficient multi-part OpenEXR files."""
        ...
    @use_exr_interleave.setter
    def use_exr_interleave(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_jpeg2k_ycc(self) -> Annotated[bool, "is_animatable=False"]:
        """Save luminance-chrominance-chrominance channels instead of RGB colors"""
        ...
    @use_jpeg2k_ycc.setter
    def use_jpeg2k_ycc(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_jpeg2k_cinema_preset(self) -> Annotated[bool, "is_animatable=False"]:
        """Use OpenJPEG Cinema Preset"""
        ...
    @use_jpeg2k_cinema_preset.setter
    def use_jpeg2k_cinema_preset(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_jpeg2k_cinema_48(self) -> Annotated[bool, "is_animatable=False"]:
        """Use OpenJPEG Cinema Preset (48fps)"""
        ...
    @use_jpeg2k_cinema_48.setter
    def use_jpeg2k_cinema_48(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def jpeg2k_codec(self) -> Annotated[Literal['JP2', 'J2K'], "is_animatable=False"]:
        """Codec settings for JPEG 2000"""
        ...
    @jpeg2k_codec.setter
    def jpeg2k_codec(self, value: Annotated[Literal['JP2', 'J2K'], "is_animatable=False"]):
        ...
    @property
    def tiff_codec(self) -> Annotated[Literal['NONE', 'DEFLATE', 'LZW', 'PACKBITS'], "is_animatable=False"]:
        """Compression mode for TIFF"""
        ...
    @tiff_codec.setter
    def tiff_codec(self, value: Annotated[Literal['NONE', 'DEFLATE', 'LZW', 'PACKBITS'], "is_animatable=False"]):
        ...
    @property
    def use_cineon_log(self) -> Annotated[bool, "is_animatable=False"]:
        """Convert to logarithmic color space"""
        ...
    @use_cineon_log.setter
    def use_cineon_log(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def cineon_black(self) -> Annotated[int, "step=1", "is_animatable=False"]:
        """Log conversion reference blackpoint"""
        ...
    @cineon_black.setter
    def cineon_black(self, value: Annotated[int, "step=1", "is_animatable=False"]):
        ...
    @property
    def cineon_white(self) -> Annotated[int, "step=1", "is_animatable=False"]:
        """Log conversion reference whitepoint"""
        ...
    @cineon_white.setter
    def cineon_white(self, value: Annotated[int, "step=1", "is_animatable=False"]):
        ...
    @property
    def cineon_gamma(self) -> Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]:
        """Log conversion gamma"""
        ...
    @cineon_gamma.setter
    def cineon_gamma(self, value: Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def views_format(self) -> Annotated[Literal['INDIVIDUAL', 'STEREO_3D', 'MULTIVIEW'], "is_animatable=False"]:
        """Format of multiview media"""
        ...
    @views_format.setter
    def views_format(self, value: Annotated[Literal['INDIVIDUAL', 'STEREO_3D', 'MULTIVIEW'], "is_animatable=False"]):
        ...
    @property
    def stereo_3d_format(self) -> Annotated['Stereo3dFormat', "is_animatable=False"]:
        """Settings for stereo 3D"""
        ...
    @property
    def color_management(self) -> Annotated[Literal['FOLLOW_SCENE', 'OVERRIDE'], "is_animatable=False"]:
        """Which color management settings to use for file saving"""
        ...
    @color_management.setter
    def color_management(self, value: Annotated[Literal['FOLLOW_SCENE', 'OVERRIDE'], "is_animatable=False"]):
        ...
    @property
    def view_settings(self) -> Annotated[Optional['ColorManagedViewSettings'], "is_animatable=False"]:
        """Color management settings applied on image before saving"""
        ...
    @property
    def display_settings(self) -> Annotated[Optional['ColorManagedDisplaySettings'], "is_animatable=False"]:
        """Settings of device saved image would be displayed on"""
        ...
    @property
    def linear_colorspace_settings(self) -> Annotated[Optional['ColorManagedInputColorspaceSettings'], "is_animatable=False"]:
        """Output color space settings"""
        ...
    @property
    def has_linear_colorspace(self) -> Annotated[bool, "is_animatable=False"]:
        """File format expects linear color space"""
        ...