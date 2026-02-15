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
from .MovieReconstructedCamera import MovieReconstructedCamera
from .MovieTrackingReconstructedCameras import MovieTrackingReconstructedCameras
class MovieTrackingReconstruction(bpy_struct):
    @property
    def is_valid(self) -> bool:
        """Whether the tracking data contains valid reconstruction information"""
        ...
    @property
    def average_error(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Average error of reconstruction"""
        ...
    @property
    def cameras(self) -> Annotated['MovieTrackingReconstructedCameras', "is_animatable=False"]:
        """Collection of solved cameras"""
        ...