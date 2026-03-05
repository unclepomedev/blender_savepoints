# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.RegionView3D.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class RegionView3D(bpy_struct):

    @property
    def lock_rotation(self) -> bool:
        """Lock view rotation of side views to Top/Front/Right"""
        ...
    @lock_rotation.setter
    def lock_rotation(self, value: bool):
        ...
    @property
    def show_sync_view(self) -> bool:
        """Sync view position between side views"""
        ...
    @show_sync_view.setter
    def show_sync_view(self, value: bool):
        ...
    @property
    def use_box_clip(self) -> bool:
        """Clip view contents based on what is visible in other side views"""
        ...
    @use_box_clip.setter
    def use_box_clip(self, value: bool):
        ...
    @property
    def perspective_matrix(self) -> Annotated[list[float], "subtype='MATRIX'", "step=10.0", "precision=3"]:
        """Current perspective matrix (``window_matrix * view_matrix``)"""
        ...
    @property
    def window_matrix(self) -> Annotated[list[float], "subtype='MATRIX'", "step=10.0", "precision=3"]:
        """Current window matrix"""
        ...
    @property
    def view_matrix(self) -> Annotated[list[float], "subtype='MATRIX'", "step=10.0", "precision=3"]:
        """Current view matrix"""
        ...
    @view_matrix.setter
    def view_matrix(self, value: Annotated[list[float], "subtype='MATRIX'", "step=10.0", "precision=3"]):
        ...
    @property
    def view_perspective(self) -> Literal['PERSP', 'ORTHO', 'CAMERA']:
        """View Perspective"""
        ...
    @view_perspective.setter
    def view_perspective(self, value: Literal['PERSP', 'ORTHO', 'CAMERA']):
        ...
    @property
    def is_perspective(self) -> bool:

        ...
    @is_perspective.setter
    def is_perspective(self, value: bool):
        ...
    @property
    def is_orthographic_side_view(self) -> bool:
        """Whether the current view is aligned to an axis (does not check whether the view is orthographic, use "is_perspective" for that). Setting this will rotate the view to the closest axis"""
        ...
    @is_orthographic_side_view.setter
    def is_orthographic_side_view(self, value: bool):
        ...
    @property
    def use_clip_planes(self) -> bool:

        ...
    @use_clip_planes.setter
    def use_clip_planes(self, value: bool):
        ...
    @property
    def clip_planes(self) -> Annotated[list[float], "step=10.0", "precision=3"]:

        ...
    @clip_planes.setter
    def clip_planes(self, value: Annotated[list[float], "step=10.0", "precision=3"]):
        ...
    @property
    def view_location(self) -> Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=10.0", "precision=5"]:
        """View pivot location"""
        ...
    @view_location.setter
    def view_location(self, value: Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=10.0", "precision=5"]):
        ...
    @property
    def view_rotation(self) -> Annotated[list[float], "subtype='QUATERNION'", "step=10.0", "precision=3"]:
        """Rotation in quaternions (keep normalized)"""
        ...
    @view_rotation.setter
    def view_rotation(self, value: Annotated[list[float], "subtype='QUATERNION'", "step=10.0", "precision=3"]):
        ...
    @property
    def view_distance(self) -> Annotated[float, "subtype='UNSIGNED'", "step=10.0", "precision=3"]:
        """Distance to the view location"""
        ...
    @view_distance.setter
    def view_distance(self, value: Annotated[float, "subtype='UNSIGNED'", "step=10.0", "precision=3"]):
        ...
    @property
    def view_camera_zoom(self) -> Annotated[float, "subtype='UNSIGNED'", "step=10.0", "precision=3"]:
        """Zoom factor in camera view"""
        ...
    @view_camera_zoom.setter
    def view_camera_zoom(self, value: Annotated[float, "subtype='UNSIGNED'", "step=10.0", "precision=3"]):
        ...
    @property
    def view_camera_offset(self) -> Annotated[list[float], "step=10.0", "precision=3"]:
        """View shift in camera view"""
        ...
    @view_camera_offset.setter
    def view_camera_offset(self, value: Annotated[list[float], "step=10.0", "precision=3"]):
        ...
    def update(self, *args, **kwargs) -> Any: ...