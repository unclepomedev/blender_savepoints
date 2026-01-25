# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import typing
import bpy
from typing import Any, Optional, Union, Set, Dict

def color_management_white_balance_preset_add(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, name: str = ..., remove_name: bool = ..., remove_active: bool = ...) -> Set[str]:
    """Add or remove a white balance preset"""
    ...

def cycles_integrator_preset_add(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, name: str = ..., remove_name: bool = ..., remove_active: bool = ...) -> Set[str]:
    """Add an Integrator Preset"""
    ...

def cycles_performance_preset_add(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, name: str = ..., remove_name: bool = ..., remove_active: bool = ...) -> Set[str]:
    """Add an Performance Preset"""
    ...

def cycles_sampling_preset_add(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, name: str = ..., remove_name: bool = ..., remove_active: bool = ...) -> Set[str]:
    """Add a Sampling Preset"""
    ...

def cycles_viewport_sampling_preset_add(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, name: str = ..., remove_name: bool = ..., remove_active: bool = ...) -> Set[str]:
    """Add a Viewport Sampling Preset"""
    ...

def eevee_raytracing_preset_add(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, name: str = ..., remove_name: bool = ..., remove_active: bool = ...) -> Set[str]:
    """Add or remove an EEVEE ray-tracing preset"""
    ...

def opengl(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, animation: bool = ..., render_keyed_only: bool = ..., sequencer: bool = ..., write_still: bool = ..., view_context: bool = ...) -> Set[str]:
    """Take a snapshot of the active viewport"""
    ...

def play_rendered_anim(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Play back rendered frames/movies using an external player"""
    ...

def preset_add(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, name: str = ..., remove_name: bool = ..., remove_active: bool = ...) -> Set[str]:
    """Add or remove a Render Preset"""
    ...

def render(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, animation: bool = ..., write_still: bool = ..., use_viewport: bool = ..., use_sequencer_scene: bool = ..., layer: str = ..., scene: str = ..., frame_start: int = ..., frame_end: int = ...) -> Set[str]:
    """(undocumented operator)"""
    ...

def shutter_curve_preset(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, shape: str = ...) -> Set[str]:
    """Set shutter curve"""
    ...

def view_cancel(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Cancel show render view"""
    ...

def view_show(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Toggle show render view"""
    ...
