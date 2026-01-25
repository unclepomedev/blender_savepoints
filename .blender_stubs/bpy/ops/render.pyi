# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import typing
import bpy
from typing import Any, Optional, Union

def color_management_white_balance_preset_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, name: str = ..., remove_name: bool = ..., remove_active: bool = ...) -> set[str]:
    """Add or remove a white balance preset"""
    ...

def cycles_integrator_preset_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, name: str = ..., remove_name: bool = ..., remove_active: bool = ...) -> set[str]:
    """Add an Integrator Preset"""
    ...

def cycles_performance_preset_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, name: str = ..., remove_name: bool = ..., remove_active: bool = ...) -> set[str]:
    """Add an Performance Preset"""
    ...

def cycles_sampling_preset_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, name: str = ..., remove_name: bool = ..., remove_active: bool = ...) -> set[str]:
    """Add a Sampling Preset"""
    ...

def cycles_viewport_sampling_preset_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, name: str = ..., remove_name: bool = ..., remove_active: bool = ...) -> set[str]:
    """Add a Viewport Sampling Preset"""
    ...

def eevee_raytracing_preset_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, name: str = ..., remove_name: bool = ..., remove_active: bool = ...) -> set[str]:
    """Add or remove an EEVEE ray-tracing preset"""
    ...

def opengl(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, animation: bool = ..., render_keyed_only: bool = ..., sequencer: bool = ..., write_still: bool = ..., view_context: bool = ...) -> set[str]:
    """Take a snapshot of the active viewport"""
    ...

def play_rendered_anim(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Play back rendered frames/movies using an external player"""
    ...

def preset_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, name: str = ..., remove_name: bool = ..., remove_active: bool = ...) -> set[str]:
    """Add or remove a Render Preset"""
    ...

def render(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, animation: bool = ..., write_still: bool = ..., use_viewport: bool = ..., use_sequencer_scene: bool = ..., layer: str = ..., scene: str = ..., frame_start: int = ..., frame_end: int = ...) -> set[str]:
    """(undocumented operator)"""
    ...

def shutter_curve_preset(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, shape: str = ...) -> set[str]:
    """Set shutter curve"""
    ...

def view_cancel(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Cancel show render view"""
    ...

def view_show(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Toggle show render view"""
    ...
