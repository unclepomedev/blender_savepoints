# Blender Probe Generated Stub for Blender 5.1.0 Alpha
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
from .ParticleBrush import ParticleBrush
class ParticleEdit(bpy_struct):
    tool: str
    select_mode: str
    use_preserve_length: bool
    use_preserve_root: bool
    use_emitter_deflect: bool
    emitter_distance: float
    use_fade_time: bool
    use_auto_velocity: bool
    show_particles: bool
    use_default_interpolate: bool
    default_key_count: int
    brush: 'ParticleBrush'
    display_step: int
    fade_frames: int
    type: str
    is_editable: bool
    is_hair: bool
    object: 'Object'
    shape_object: 'Object'