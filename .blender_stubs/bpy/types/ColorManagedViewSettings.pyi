# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.ColorManagedViewSettings.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .CurveMapping import CurveMapping

class ColorManagedViewSettings(bpy_struct):

    look: Literal['NONE']
    """Additional transform applied before view transform for artistic needs"""
    view_transform: Literal['NONE']
    """View used when converting image to a display space"""
    exposure: Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=3"]
    """Exposure (stops) applied before display transform, multiplying by 2^exposure"""
    gamma: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Additional gamma encoding after display transform, for output with custom gamma"""
    @property
    def curve_mapping(self) -> Annotated[Optional['CurveMapping'], "is_animatable=False"]:
        """Color curve mapping applied before display transform"""
        ...
    use_curve_mapping: bool
    """Use RGB curved for pre-display transformation"""
    use_white_balance: bool
    """Perform chromatic adaption from a different white point"""
    white_balance_temperature: Annotated[float, "subtype='COLOR_TEMPERATURE'", "unit='COLOR_TEMPERATURE'", "step=100.0", "precision=0"]
    """Color temperature of the scene's white point"""
    white_balance_tint: Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=1"]
    """Color tint of the scene's white point (the default of 10 matches daylight)"""
    white_balance_whitepoint: Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]
    """The color which gets mapped to white (automatically converted to/from temperature and tint)"""
    @property
    def is_hdr(self) -> bool:
        """The display and view transform supports high dynamic range colors"""
        ...
    @property
    def support_emulation(self) -> bool:
        """The display and view transform supports automatic emulation for another display device, using the display color spaces mechanism in OpenColorIO v2 configurations"""
        ...