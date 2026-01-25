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
from .Object import Object
from .ParticleSystem import ParticleSystem
class ParticleInstanceModifier(Modifier):
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
    object: 'Object'
    particle_system_index: int
    particle_system: 'ParticleSystem'
    axis: str
    space: str
    use_normal: bool
    use_children: bool
    use_path: bool
    show_unborn: bool
    show_alive: bool
    show_dead: bool
    use_preserve_shape: bool
    use_size: bool
    position: float
    random_position: float
    rotation: float
    random_rotation: float
    particle_amount: float
    particle_offset: float
    index_layer_name: str
    value_layer_name: str