# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.MovieTrackingCamera.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class MovieTrackingCamera(bpy_struct):

    @property
    def distortion_model(self) -> Annotated[Literal['POLYNOMIAL', 'DIVISION', 'NUKE', 'BROWN'], "is_animatable=False"]:
        """Distortion model used for camera lenses"""
        ...
    @distortion_model.setter
    def distortion_model(self, value: Annotated[Literal['POLYNOMIAL', 'DIVISION', 'NUKE', 'BROWN'], "is_animatable=False"]) -> None:
        ...
    @property
    def sensor_width(self) -> Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]:
        """Width of CCD sensor in millimeters"""
        ...
    @sensor_width.setter
    def sensor_width(self, value: Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]) -> None:
        ...
    @property
    def focal_length(self) -> Annotated[float, "step=1.0", "precision=2", "is_animatable=False"]:
        """Camera's focal length"""
        ...
    @focal_length.setter
    def focal_length(self, value: Annotated[float, "step=1.0", "precision=2", "is_animatable=False"]) -> None:
        ...
    @property
    def focal_length_pixels(self) -> Annotated[float, "step=1.0", "precision=2", "is_animatable=False"]:
        """Camera's focal length"""
        ...
    @focal_length_pixels.setter
    def focal_length_pixels(self, value: Annotated[float, "step=1.0", "precision=2", "is_animatable=False"]) -> None:
        ...
    @property
    def units(self) -> Annotated[Literal['PIXELS', 'MILLIMETERS'], "is_animatable=False"]:
        """Units used for camera focal length"""
        ...
    @units.setter
    def units(self, value: Annotated[Literal['PIXELS', 'MILLIMETERS'], "is_animatable=False"]) -> None:
        ...
    @property
    def principal_point(self) -> Annotated[list[float], "step=0.10000000149011612", "precision=3", "is_animatable=False"]:
        """Optical center of lens"""
        ...
    @principal_point.setter
    def principal_point(self, value: Annotated[list[float], "step=0.10000000149011612", "precision=3", "is_animatable=False"]) -> None:
        ...
    @property
    def principal_point_pixels(self) -> Annotated[list[float], "subtype='PIXEL'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Optical center of lens in pixels"""
        ...
    @principal_point_pixels.setter
    def principal_point_pixels(self, value: Annotated[list[float], "subtype='PIXEL'", "step=10.0", "precision=3", "is_animatable=False"]) -> None:
        ...
    @property
    def k1(self) -> Annotated[float, "step=0.10000000149011612", "precision=3", "is_animatable=False"]:
        """First coefficient of third order polynomial radial distortion"""
        ...
    @k1.setter
    def k1(self, value: Annotated[float, "step=0.10000000149011612", "precision=3", "is_animatable=False"]) -> None:
        ...
    @property
    def k2(self) -> Annotated[float, "step=0.10000000149011612", "precision=3", "is_animatable=False"]:
        """Second coefficient of third order polynomial radial distortion"""
        ...
    @k2.setter
    def k2(self, value: Annotated[float, "step=0.10000000149011612", "precision=3", "is_animatable=False"]) -> None:
        ...
    @property
    def k3(self) -> Annotated[float, "step=0.10000000149011612", "precision=3", "is_animatable=False"]:
        """Third coefficient of third order polynomial radial distortion"""
        ...
    @k3.setter
    def k3(self, value: Annotated[float, "step=0.10000000149011612", "precision=3", "is_animatable=False"]) -> None:
        ...
    @property
    def division_k1(self) -> Annotated[float, "step=0.10000000149011612", "precision=3", "is_animatable=False"]:
        """First coefficient of second order division distortion"""
        ...
    @division_k1.setter
    def division_k1(self, value: Annotated[float, "step=0.10000000149011612", "precision=3", "is_animatable=False"]) -> None:
        ...
    @property
    def division_k2(self) -> Annotated[float, "step=0.10000000149011612", "precision=3", "is_animatable=False"]:
        """Second coefficient of second order division distortion"""
        ...
    @division_k2.setter
    def division_k2(self, value: Annotated[float, "step=0.10000000149011612", "precision=3", "is_animatable=False"]) -> None:
        ...
    @property
    def nuke_k1(self) -> Annotated[float, "step=0.10000000149011612", "precision=3", "is_animatable=False"]:
        """First coefficient of second order Nuke distortion"""
        ...
    @nuke_k1.setter
    def nuke_k1(self, value: Annotated[float, "step=0.10000000149011612", "precision=3", "is_animatable=False"]) -> None:
        ...
    @property
    def nuke_k2(self) -> Annotated[float, "step=0.10000000149011612", "precision=3", "is_animatable=False"]:
        """Second coefficient of second order Nuke distortion"""
        ...
    @nuke_k2.setter
    def nuke_k2(self, value: Annotated[float, "step=0.10000000149011612", "precision=3", "is_animatable=False"]) -> None:
        ...
    @property
    def brown_k1(self) -> Annotated[float, "step=0.10000000149011612", "precision=3", "is_animatable=False"]:
        """First coefficient of fourth order Brown-Conrady radial distortion"""
        ...
    @brown_k1.setter
    def brown_k1(self, value: Annotated[float, "step=0.10000000149011612", "precision=3", "is_animatable=False"]) -> None:
        ...
    @property
    def brown_k2(self) -> Annotated[float, "step=0.10000000149011612", "precision=3", "is_animatable=False"]:
        """Second coefficient of fourth order Brown-Conrady radial distortion"""
        ...
    @brown_k2.setter
    def brown_k2(self, value: Annotated[float, "step=0.10000000149011612", "precision=3", "is_animatable=False"]) -> None:
        ...
    @property
    def brown_k3(self) -> Annotated[float, "step=0.10000000149011612", "precision=3", "is_animatable=False"]:
        """Third coefficient of fourth order Brown-Conrady radial distortion"""
        ...
    @brown_k3.setter
    def brown_k3(self, value: Annotated[float, "step=0.10000000149011612", "precision=3", "is_animatable=False"]) -> None:
        ...
    @property
    def brown_k4(self) -> Annotated[float, "step=0.10000000149011612", "precision=3", "is_animatable=False"]:
        """Fourth coefficient of fourth order Brown-Conrady radial distortion"""
        ...
    @brown_k4.setter
    def brown_k4(self, value: Annotated[float, "step=0.10000000149011612", "precision=3", "is_animatable=False"]) -> None:
        ...
    @property
    def brown_p1(self) -> Annotated[float, "step=0.10000000149011612", "precision=3", "is_animatable=False"]:
        """First coefficient of second order Brown-Conrady tangential distortion"""
        ...
    @brown_p1.setter
    def brown_p1(self, value: Annotated[float, "step=0.10000000149011612", "precision=3", "is_animatable=False"]) -> None:
        ...
    @property
    def brown_p2(self) -> Annotated[float, "step=0.10000000149011612", "precision=3", "is_animatable=False"]:
        """Second coefficient of second order Brown-Conrady tangential distortion"""
        ...
    @brown_p2.setter
    def brown_p2(self, value: Annotated[float, "step=0.10000000149011612", "precision=3", "is_animatable=False"]) -> None:
        ...
    @property
    def pixel_aspect(self) -> Annotated[float, "subtype='XYZ'", "step=1.0", "precision=2", "is_animatable=False"]:
        """Pixel aspect ratio"""
        ...
    @pixel_aspect.setter
    def pixel_aspect(self, value: Annotated[float, "subtype='XYZ'", "step=1.0", "precision=2", "is_animatable=False"]) -> None:
        ...