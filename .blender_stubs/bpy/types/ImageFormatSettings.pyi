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

    media_type: Annotated[Literal['IMAGE', 'MULTI_LAYER_IMAGE', 'VIDEO'], "is_animatable=False"]
    """The type of media to save"""
    file_format: Annotated[Literal['JPEG', 'OPEN_EXR', 'PNG', 'WEBP', 'BMP', 'CINEON', 'DPX', 'IRIS', 'JPEG2000', 'HDR', 'TARGA', 'TARGA_RAW', 'TIFF', 'OPEN_EXR_MULTILAYER', 'FFMPEG'], "is_animatable=False"]
    """File format to save the rendered images as"""
    color_mode: Annotated[Literal['BW', 'RGB', 'RGBA'], "is_animatable=False"]
    """Choose BW for saving grayscale images, RGB for saving red, green and blue channels, and RGBA for saving red, green, blue and alpha channels"""
    color_depth: Annotated[Literal['8', '10', '12', '16', '32'], "is_animatable=False"]
    """Bit depth per channel"""
    quality: Annotated[int, "subtype='PERCENTAGE'", "step=1", "is_animatable=False"]
    """Quality for image formats that support lossy compression"""
    compression: Annotated[int, "subtype='PERCENTAGE'", "step=1", "is_animatable=False"]
    """Amount of time to determine best compression: 0 = no compression with fast file output, 100 = maximum lossless compression with slow file output"""
    use_preview: Annotated[bool, "is_animatable=False"]
    """When rendering animations, save JPG preview images in same directory"""
    exr_codec: Annotated[Literal['NONE', 'ZIP', 'PIZ', 'DWAA', 'DWAB', 'ZIPS', 'RLE', 'PXR24', 'B44', 'B44A'], "is_animatable=False"]
    """Compression codec settings for OpenEXR"""
    use_exr_interleave: Annotated[bool, "is_animatable=False"]
    """Use legacy interleaved storage of views, layers and passes for compatibility with applications that do not support more efficient multi-part OpenEXR files."""
    use_jpeg2k_ycc: Annotated[bool, "is_animatable=False"]
    """Save luminance-chrominance-chrominance channels instead of RGB colors"""
    use_jpeg2k_cinema_preset: Annotated[bool, "is_animatable=False"]
    """Use OpenJPEG Cinema Preset"""
    use_jpeg2k_cinema_48: Annotated[bool, "is_animatable=False"]
    """Use OpenJPEG Cinema Preset (48fps)"""
    jpeg2k_codec: Annotated[Literal['JP2', 'J2K'], "is_animatable=False"]
    """Codec settings for JPEG 2000"""
    tiff_codec: Annotated[Literal['NONE', 'DEFLATE', 'LZW', 'PACKBITS'], "is_animatable=False"]
    """Compression mode for TIFF"""
    use_cineon_log: Annotated[bool, "is_animatable=False"]
    """Convert to logarithmic color space"""
    cineon_black: Annotated[int, "step=1", "is_animatable=False"]
    """Log conversion reference blackpoint"""
    cineon_white: Annotated[int, "step=1", "is_animatable=False"]
    """Log conversion reference whitepoint"""
    cineon_gamma: Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]
    """Log conversion gamma"""
    views_format: Annotated[Literal['INDIVIDUAL', 'STEREO_3D', 'MULTIVIEW'], "is_animatable=False"]
    """Format of multiview media"""
    @property
    def stereo_3d_format(self) -> Annotated['Stereo3dFormat', "is_animatable=False"]:
        """Settings for stereo 3D"""
        ...
    color_management: Annotated[Literal['FOLLOW_SCENE', 'OVERRIDE'], "is_animatable=False"]
    """Which color management settings to use for file saving"""
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