# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .Modifier import Modifier
class OceanModifier(Modifier):
    name: str
    type: str
    show_viewport: bool
    show_render: bool
    show_in_editmode: bool
    show_on_cage: bool
    show_expanded: bool
    is_active: bool
    use_pin_to_last: bool
    is_override_data: bool
    use_apply_on_spline: bool
    execution_time: float
    persistent_uid: int
    geometry_mode: str
    size: float
    repeat_x: int
    repeat_y: int
    use_normals: bool
    use_foam: bool
    use_spray: bool
    invert_spray: bool
    spray_layer_name: str
    resolution: int
    viewport_resolution: int
    spatial_size: int
    wind_velocity: float
    damping: float
    wave_scale_min: float
    wave_alignment: float
    wave_direction: float
    wave_scale: float
    depth: float
    foam_coverage: float
    bake_foam_fade: float
    foam_layer_name: str
    choppiness: float
    time: float
    spectrum: str
    fetch_jonswap: float
    sharpen_peak_jonswap: float
    random_seed: int
    frame_start: int
    frame_end: int
    is_cached: bool
    filepath: str