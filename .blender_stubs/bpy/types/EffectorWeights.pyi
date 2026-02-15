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
from .Collection import Collection
class EffectorWeights(bpy_struct):
    apply_to_hair_growing: bool
    """Use force fields when growing hair"""
    collection: Annotated[Optional['Collection'], "is_animatable=False"]
    """Limit effectors to this collection"""
    gravity: Annotated[float, "step=0.10000000149011612", "precision=3"]
    """Global gravity weight"""
    all: Annotated[float, "step=0.10000000149011612", "precision=3"]
    """All effector's weight"""
    force: Annotated[float, "step=0.10000000149011612", "precision=3"]
    """Force effector weight"""
    vortex: Annotated[float, "step=0.10000000149011612", "precision=3"]
    """Vortex effector weight"""
    magnetic: Annotated[float, "step=0.10000000149011612", "precision=3"]
    """Magnetic effector weight"""
    wind: Annotated[float, "step=0.10000000149011612", "precision=3"]
    """Wind effector weight"""
    curve_guide: Annotated[float, "step=0.10000000149011612", "precision=3"]
    """Curve guide effector weight"""
    texture: Annotated[float, "step=0.10000000149011612", "precision=3"]
    """Texture effector weight"""
    harmonic: Annotated[float, "step=0.10000000149011612", "precision=3"]
    """Harmonic effector weight"""
    charge: Annotated[float, "step=0.10000000149011612", "precision=3"]
    """Charge effector weight"""
    lennardjones: Annotated[float, "step=0.10000000149011612", "precision=3"]
    """Lennard-Jones effector weight"""
    boid: Annotated[float, "step=0.10000000149011612", "precision=3"]
    """Boid effector weight"""
    turbulence: Annotated[float, "step=0.10000000149011612", "precision=3"]
    """Turbulence effector weight"""
    drag: Annotated[float, "step=0.10000000149011612", "precision=3"]
    """Drag effector weight"""
    smokeflow: Annotated[float, "step=0.10000000149011612", "precision=3"]
    """Fluid Flow effector weight"""