# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
from .ColorManagedDisplaySettings import ColorManagedDisplaySettings
from .ColorManagedInputColorspaceSettings import ColorManagedInputColorspaceSettings
from .ColorManagedViewSettings import ColorManagedViewSettings
from .Stereo3dFormat import Stereo3dFormat
class ImageFormatSettings(bpy_struct):
    media_type: str
    file_format: str
    color_mode: str
    color_depth: str
    quality: int
    compression: int
    use_preview: bool
    exr_codec: str
    use_exr_interleave: bool
    use_jpeg2k_ycc: bool
    use_jpeg2k_cinema_preset: bool
    use_jpeg2k_cinema_48: bool
    jpeg2k_codec: str
    tiff_codec: str
    use_cineon_log: bool
    cineon_black: int
    cineon_white: int
    cineon_gamma: float
    views_format: str
    stereo_3d_format: 'Stereo3dFormat'
    color_management: str
    view_settings: 'ColorManagedViewSettings'
    display_settings: 'ColorManagedDisplaySettings'
    linear_colorspace_settings: 'ColorManagedInputColorspaceSettings'
    has_linear_colorspace: bool