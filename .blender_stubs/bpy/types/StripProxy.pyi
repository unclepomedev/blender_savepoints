# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
class StripProxy(bpy_struct):
    directory: Annotated[str, "subtype='DIR_PATH'", "is_animatable=False"]
    """Location to store the proxy files"""
    filepath: Annotated[str, "subtype='FILE_PATH'", "is_animatable=False"]
    """Location of custom proxy file"""
    use_overwrite: bool
    """Overwrite existing proxy files when building"""
    build_25: bool
    """Build 25% proxy resolution"""
    build_50: bool
    """Build 50% proxy resolution"""
    build_75: bool
    """Build 75% proxy resolution"""
    build_100: bool
    """Build 100% proxy resolution"""
    build_record_run: bool
    """Build record run time code index"""
    quality: Annotated[int, "subtype='UNSIGNED'", "step=1"]
    """Quality of proxies to build"""
    timecode: Literal['NONE', 'RECORD_RUN', 'RECORD_RUN_NO_GAPS']
    """Method for reading the inputs timecode"""
    use_proxy_custom_directory: bool
    """Use a custom directory to store data"""
    use_proxy_custom_file: bool
    """Use a custom file to read proxy data from"""