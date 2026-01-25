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
from .Object import Object
from .Texture import Texture
class FieldSettings(bpy_struct):
    type: str
    shape: str
    falloff_type: str
    texture_mode: str
    z_direction: str
    strength: float
    linear_drag: float
    harmonic_damping: float
    quadratic_drag: float
    flow: float
    wind_factor: float
    inflow: float
    size: float
    rest_length: float
    falloff_power: float
    distance_min: float
    distance_max: float
    radial_min: float
    radial_max: float
    radial_falloff: float
    texture_nabla: float
    noise: float
    seed: int
    use_min_distance: bool
    use_max_distance: bool
    use_radial_min: bool
    use_radial_max: bool
    use_object_coords: bool
    use_global_coords: bool
    use_2d_force: bool
    use_root_coords: bool
    apply_to_location: bool
    apply_to_rotation: bool
    use_absorption: bool
    use_multiple_springs: bool
    use_smoke_density: bool
    use_gravity_falloff: bool
    texture: 'Texture'
    source_object: 'Object'
    guide_minimum: float
    guide_free: float
    use_guide_path_add: bool
    use_guide_path_weight: bool
    guide_clump_amount: float
    guide_clump_shape: float
    guide_kink_type: str
    guide_kink_axis: str
    guide_kink_frequency: float
    guide_kink_shape: float
    guide_kink_amplitude: float