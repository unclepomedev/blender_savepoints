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
from .WalkNavigation import WalkNavigation
from .XrNavigation import XrNavigation
class PreferencesInput(bpy_struct):
    view_zoom_method: str
    view_zoom_axis: str
    use_multitouch_gestures: bool
    invert_mouse_zoom: bool
    use_mouse_depth_navigate: bool
    use_zoom_to_mouse: bool
    use_auto_perspective: bool
    use_rotate_around_active: bool
    view_rotate_method: str
    use_mouse_continuous: bool
    use_drag_immediately: bool
    use_numeric_input_advanced: bool
    navigation_mode: str
    walk_navigation: 'WalkNavigation'
    view_rotate_sensitivity_turntable: float
    view_rotate_sensitivity_trackball: float
    drag_threshold_mouse: int
    drag_threshold_tablet: int
    drag_threshold: int
    move_threshold: int
    pressure_threshold_max: float
    pressure_softness: float
    tablet_api: str
    xr_navigation: 'XrNavigation'
    ndof_translation_sensitivity: float
    ndof_rotation_sensitivity: float
    ndof_deadzone: float
    ndof_zoom_direction: str
    ndof_show_guide_orbit_axis: bool
    ndof_show_guide_orbit_center: bool
    ndof_navigation_mode: str
    ndof_lock_horizon: bool
    ndof_fly_speed_auto: bool
    ndof_orbit_center_auto: bool
    ndof_orbit_center_selected: bool
    ndof_rotx_invert_axis: bool
    ndof_roty_invert_axis: bool
    ndof_rotz_invert_axis: bool
    ndof_panx_invert_axis: bool
    ndof_pany_invert_axis: bool
    ndof_panz_invert_axis: bool
    ndof_fly_helicopter: bool
    ndof_lock_camera_pan_zoom: bool
    mouse_double_click_time: int
    use_mouse_emulate_3_button: bool
    mouse_emulate_3_button_modifier: str
    use_emulate_numpad: bool
    invert_zoom_wheel: bool
    touchpad_scroll_direction: str