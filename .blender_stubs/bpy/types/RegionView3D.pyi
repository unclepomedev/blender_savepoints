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
class RegionView3D(bpy_struct):
    lock_rotation: bool
    """Lock view rotation of side views to Top/Front/Right"""
    show_sync_view: bool
    """Sync view position between side views"""
    use_box_clip: bool
    """Clip view contents based on what is visible in other side views"""
    @property
    def perspective_matrix(self) -> Annotated[list[float], "subtype='MATRIX'", "step=10.0", "precision=3"]:
        """Current perspective matrix (``window_matrix * view_matrix``)"""
        ...
    @property
    def window_matrix(self) -> Annotated[list[float], "subtype='MATRIX'", "step=10.0", "precision=3"]:
        """Current window matrix"""
        ...
    view_matrix: Annotated[list[float], "subtype='MATRIX'", "step=10.0", "precision=3"]
    """Current view matrix"""
    view_perspective: Literal['PERSP', 'ORTHO', 'CAMERA']
    """View Perspective"""
    is_perspective: bool
    is_orthographic_side_view: bool
    """Whether the current view is aligned to an axis (does not check whether the view is orthographic, use "is_perspective" for that). Setting this will rotate the view to the closest axis"""
    use_clip_planes: bool
    clip_planes: Annotated[list[float], "step=10.0", "precision=3"]
    view_location: Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=10.0", "precision=5"]
    """View pivot location"""
    view_rotation: Annotated[list[float], "subtype='QUATERNION'", "step=10.0", "precision=3"]
    """Rotation in quaternions (keep normalized)"""
    view_distance: Annotated[float, "subtype='UNSIGNED'", "step=10.0", "precision=3"]
    """Distance to the view location"""
    view_camera_zoom: Annotated[float, "subtype='UNSIGNED'", "step=10.0", "precision=3"]
    """Zoom factor in camera view"""
    view_camera_offset: Annotated[list[float], "step=10.0", "precision=3"]
    """View shift in camera view"""
    def update(self, *args, **kwargs) -> Any: ...