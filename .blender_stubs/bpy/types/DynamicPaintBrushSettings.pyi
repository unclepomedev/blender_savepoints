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
from .ColorRamp import ColorRamp
from .ParticleSystem import ParticleSystem
class DynamicPaintBrushSettings(bpy_struct):
    paint_color: list[float]
    paint_alpha: float
    use_absolute_alpha: bool
    paint_wetness: float
    use_paint_erase: bool
    wave_type: str
    wave_factor: float
    wave_clamp: float
    use_smudge: bool
    smudge_strength: float
    velocity_max: float
    use_velocity_alpha: bool
    use_velocity_depth: bool
    use_velocity_color: bool
    paint_source: str
    paint_distance: float
    use_proximity_ramp_alpha: bool
    proximity_falloff: str
    use_proximity_project: bool
    ray_direction: str
    invert_proximity: bool
    use_negative_volume: bool
    particle_system: 'ParticleSystem'
    use_particle_radius: bool
    solid_radius: float
    smooth_radius: float
    paint_ramp: 'ColorRamp'
    velocity_ramp: 'ColorRamp'