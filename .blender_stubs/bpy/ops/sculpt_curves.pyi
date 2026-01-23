# Blender Probe Generated Stub for Blender 5.1.0 Alpha
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import typing
import bpy
from typing import Any, Optional, Union

def brush_stroke(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, stroke: bpy_prop_collection['OperatorStrokeElement'] = ..., mode: str = ..., pen_flip: bool = ...) -> set[str]:
    """Sculpt curves using a brush"""
    ...

def min_distance_edit(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Change the minimum distance used by the density brush"""
    ...

def select_grow(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, distance: float = ...) -> set[str]:
    """Select curves which are close to curves that are selected already"""
    ...

def select_random(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, seed: int = ..., partial: bool = ..., probability: float = ..., min: float = ..., constant_per_curve: bool = ...) -> set[str]:
    """Randomizes existing selection or create new random selection"""
    ...
