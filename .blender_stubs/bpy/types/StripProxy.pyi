# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.StripProxy.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class StripProxy(bpy_struct):

    @property
    def directory(self) -> Annotated[str, "subtype='DIR_PATH'", "is_animatable=False"]:
        """Location to store the proxy files"""
        ...
    @directory.setter
    def directory(self, value: Annotated[str, "subtype='DIR_PATH'", "is_animatable=False"]) -> None:
        ...
    @property
    def filepath(self) -> Annotated[str, "subtype='FILE_PATH'", "is_animatable=False"]:
        """Location of custom proxy file"""
        ...
    @filepath.setter
    def filepath(self, value: Annotated[str, "subtype='FILE_PATH'", "is_animatable=False"]) -> None:
        ...
    @property
    def use_overwrite(self) -> bool:
        """Overwrite existing proxy files when building"""
        ...
    @use_overwrite.setter
    def use_overwrite(self, value: bool) -> None:
        ...
    @property
    def build_25(self) -> bool:
        """Build 25% proxy resolution"""
        ...
    @build_25.setter
    def build_25(self, value: bool) -> None:
        ...
    @property
    def build_50(self) -> bool:
        """Build 50% proxy resolution"""
        ...
    @build_50.setter
    def build_50(self, value: bool) -> None:
        ...
    @property
    def build_75(self) -> bool:
        """Build 75% proxy resolution"""
        ...
    @build_75.setter
    def build_75(self, value: bool) -> None:
        ...
    @property
    def build_100(self) -> bool:
        """Build 100% proxy resolution"""
        ...
    @build_100.setter
    def build_100(self, value: bool) -> None:
        ...
    @property
    def build_record_run(self) -> bool:
        """Build record run time code index"""
        ...
    @build_record_run.setter
    def build_record_run(self, value: bool) -> None:
        ...
    @property
    def quality(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Quality of proxies to build"""
        ...
    @quality.setter
    def quality(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1"]) -> None:
        ...
    @property
    def timecode(self) -> Literal['NONE', 'RECORD_RUN', 'RECORD_RUN_NO_GAPS']:
        """Method for reading the inputs timecode"""
        ...
    @timecode.setter
    def timecode(self, value: Literal['NONE', 'RECORD_RUN', 'RECORD_RUN_NO_GAPS']) -> None:
        ...
    @property
    def use_proxy_custom_directory(self) -> bool:
        """Use a custom directory to store data"""
        ...
    @use_proxy_custom_directory.setter
    def use_proxy_custom_directory(self, value: bool) -> None:
        ...
    @property
    def use_proxy_custom_file(self) -> bool:
        """Use a custom file to read proxy data from"""
        ...
    @use_proxy_custom_file.setter
    def use_proxy_custom_file(self, value: bool) -> None:
        ...