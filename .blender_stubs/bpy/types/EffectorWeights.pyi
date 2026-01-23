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
from .Collection import Collection
class EffectorWeights(bpy_struct):
    apply_to_hair_growing: bool
    collection: 'Collection'
    gravity: float
    all: float
    force: float
    vortex: float
    magnetic: float
    wind: float
    curve_guide: float
    texture: float
    harmonic: float
    charge: float
    lennardjones: float
    boid: float
    turbulence: float
    drag: float
    smokeflow: float