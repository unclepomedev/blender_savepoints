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
from .View3DShading import View3DShading
class SceneDisplay(bpy_struct):
    light_direction: float
    shadow_shift: float
    shadow_focus: float
    matcap_ssao_distance: float
    matcap_ssao_attenuation: float
    matcap_ssao_samples: int
    render_aa: str
    viewport_aa: str
    shading: 'View3DShading'