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
class MovieTrackingCamera(bpy_struct):
    distortion_model: Annotated[Literal['POLYNOMIAL', 'DIVISION', 'NUKE', 'BROWN'], "is_animatable=False"]
    """Distortion model used for camera lenses"""
    sensor_width: Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]
    """Width of CCD sensor in millimeters"""
    focal_length: Annotated[float, "step=1.0", "precision=2", "is_animatable=False"]
    """Camera's focal length"""
    focal_length_pixels: Annotated[float, "step=1.0", "precision=2", "is_animatable=False"]
    """Camera's focal length"""
    units: Annotated[Literal['PIXELS', 'MILLIMETERS'], "is_animatable=False"]
    """Units used for camera focal length"""
    principal_point: Annotated[list[float], "step=0.10000000149011612", "precision=3", "is_animatable=False"]
    """Optical center of lens"""
    principal_point_pixels: Annotated[list[float], "subtype='PIXEL'", "step=10.0", "precision=3", "is_animatable=False"]
    """Optical center of lens in pixels"""
    k1: Annotated[float, "step=0.10000000149011612", "precision=3", "is_animatable=False"]
    """First coefficient of third order polynomial radial distortion"""
    k2: Annotated[float, "step=0.10000000149011612", "precision=3", "is_animatable=False"]
    """Second coefficient of third order polynomial radial distortion"""
    k3: Annotated[float, "step=0.10000000149011612", "precision=3", "is_animatable=False"]
    """Third coefficient of third order polynomial radial distortion"""
    division_k1: Annotated[float, "step=0.10000000149011612", "precision=3", "is_animatable=False"]
    """First coefficient of second order division distortion"""
    division_k2: Annotated[float, "step=0.10000000149011612", "precision=3", "is_animatable=False"]
    """Second coefficient of second order division distortion"""
    nuke_k1: Annotated[float, "step=0.10000000149011612", "precision=3", "is_animatable=False"]
    """First coefficient of second order Nuke distortion"""
    nuke_k2: Annotated[float, "step=0.10000000149011612", "precision=3", "is_animatable=False"]
    """Second coefficient of second order Nuke distortion"""
    brown_k1: Annotated[float, "step=0.10000000149011612", "precision=3", "is_animatable=False"]
    """First coefficient of fourth order Brown-Conrady radial distortion"""
    brown_k2: Annotated[float, "step=0.10000000149011612", "precision=3", "is_animatable=False"]
    """Second coefficient of fourth order Brown-Conrady radial distortion"""
    brown_k3: Annotated[float, "step=0.10000000149011612", "precision=3", "is_animatable=False"]
    """Third coefficient of fourth order Brown-Conrady radial distortion"""
    brown_k4: Annotated[float, "step=0.10000000149011612", "precision=3", "is_animatable=False"]
    """Fourth coefficient of fourth order Brown-Conrady radial distortion"""
    brown_p1: Annotated[float, "step=0.10000000149011612", "precision=3", "is_animatable=False"]
    """First coefficient of second order Brown-Conrady tangential distortion"""
    brown_p2: Annotated[float, "step=0.10000000149011612", "precision=3", "is_animatable=False"]
    """Second coefficient of second order Brown-Conrady tangential distortion"""
    pixel_aspect: Annotated[float, "subtype='XYZ'", "step=1.0", "precision=2", "is_animatable=False"]
    """Pixel aspect ratio"""