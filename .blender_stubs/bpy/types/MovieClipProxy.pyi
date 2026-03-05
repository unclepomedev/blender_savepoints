# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.MovieClipProxy.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class MovieClipProxy(bpy_struct):

    @property
    def build_25(self) -> Annotated[bool, "is_animatable=False"]:
        """Build proxy resolution 25% of the original footage dimension"""
        ...
    @build_25.setter
    def build_25(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def build_50(self) -> Annotated[bool, "is_animatable=False"]:
        """Build proxy resolution 50% of the original footage dimension"""
        ...
    @build_50.setter
    def build_50(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def build_75(self) -> Annotated[bool, "is_animatable=False"]:
        """Build proxy resolution 75% of the original footage dimension"""
        ...
    @build_75.setter
    def build_75(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def build_100(self) -> Annotated[bool, "is_animatable=False"]:
        """Build proxy resolution 100% of the original footage dimension"""
        ...
    @build_100.setter
    def build_100(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def build_undistorted_25(self) -> Annotated[bool, "is_animatable=False"]:
        """Build proxy resolution 25% of the original undistorted footage dimension"""
        ...
    @build_undistorted_25.setter
    def build_undistorted_25(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def build_undistorted_50(self) -> Annotated[bool, "is_animatable=False"]:
        """Build proxy resolution 50% of the original undistorted footage dimension"""
        ...
    @build_undistorted_50.setter
    def build_undistorted_50(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def build_undistorted_75(self) -> Annotated[bool, "is_animatable=False"]:
        """Build proxy resolution 75% of the original undistorted footage dimension"""
        ...
    @build_undistorted_75.setter
    def build_undistorted_75(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def build_undistorted_100(self) -> Annotated[bool, "is_animatable=False"]:
        """Build proxy resolution 100% of the original undistorted footage dimension"""
        ...
    @build_undistorted_100.setter
    def build_undistorted_100(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def build_record_run(self) -> Annotated[bool, "is_animatable=False"]:
        """Build record run time code index"""
        ...
    @build_record_run.setter
    def build_record_run(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def quality(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]:
        """JPEG quality of proxy images"""
        ...
    @quality.setter
    def quality(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]):
        ...
    @property
    def timecode(self) -> Annotated[Literal['NONE', 'RECORD_RUN', 'FREE_RUN_NO_GAPS'], "is_animatable=False"]:

        ...
    @timecode.setter
    def timecode(self, value: Annotated[Literal['NONE', 'RECORD_RUN', 'FREE_RUN_NO_GAPS'], "is_animatable=False"]):
        ...
    @property
    def directory(self) -> Annotated[str, "subtype='DIR_PATH'", "is_animatable=False"]:
        """Location to store the proxy files"""
        ...
    @directory.setter
    def directory(self, value: Annotated[str, "subtype='DIR_PATH'", "is_animatable=False"]):
        ...