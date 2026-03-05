# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.PreferencesInput.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .WalkNavigation import WalkNavigation
from .XrNavigation import XrNavigation

class PreferencesInput(bpy_struct):

    @property
    def view_zoom_method(self) -> Literal['CONTINUE', 'DOLLY', 'SCALE']:
        """Which style to use for viewport scaling"""
        ...
    @view_zoom_method.setter
    def view_zoom_method(self, value: Literal['CONTINUE', 'DOLLY', 'SCALE']):
        ...
    @property
    def view_zoom_axis(self) -> Literal['VERTICAL', 'HORIZONTAL']:
        """Axis of mouse movement to zoom in or out on"""
        ...
    @view_zoom_axis.setter
    def view_zoom_axis(self, value: Literal['VERTICAL', 'HORIZONTAL']):
        ...
    @property
    def use_multitouch_gestures(self) -> bool:
        """Use multi-touch gestures for navigation with touchpad, instead of scroll wheel emulation"""
        ...
    @use_multitouch_gestures.setter
    def use_multitouch_gestures(self, value: bool):
        ...
    @property
    def invert_mouse_zoom(self) -> bool:
        """Invert the axis of mouse movement for zooming"""
        ...
    @invert_mouse_zoom.setter
    def invert_mouse_zoom(self, value: bool):
        ...
    @property
    def use_mouse_depth_navigate(self) -> bool:
        """Use the depth under the mouse to improve view pan/rotate/zoom functionality"""
        ...
    @use_mouse_depth_navigate.setter
    def use_mouse_depth_navigate(self, value: bool):
        ...
    @property
    def use_zoom_to_mouse(self) -> bool:
        """Zoom in towards the mouse pointer's position in the 3D view, rather than the 2D window center"""
        ...
    @use_zoom_to_mouse.setter
    def use_zoom_to_mouse(self, value: bool):
        ...
    @property
    def use_auto_perspective(self) -> bool:
        """Automatically switch between orthographic and perspective when changing from top/front/side views"""
        ...
    @use_auto_perspective.setter
    def use_auto_perspective(self, value: bool):
        ...
    @property
    def use_rotate_around_active(self) -> bool:
        """Use selection as the pivot point"""
        ...
    @use_rotate_around_active.setter
    def use_rotate_around_active(self, value: bool):
        ...
    @property
    def view_rotate_method(self) -> Literal['TURNTABLE', 'TRACKBALL']:
        """Orbit method in the viewport"""
        ...
    @view_rotate_method.setter
    def view_rotate_method(self, value: Literal['TURNTABLE', 'TRACKBALL']):
        ...
    @property
    def use_mouse_continuous(self) -> bool:
        """Let the mouse wrap around the view boundaries so mouse movements are not limited by the screen size (used by transform, dragging of UI controls, etc.)"""
        ...
    @use_mouse_continuous.setter
    def use_mouse_continuous(self, value: bool):
        ...
    @property
    def use_drag_immediately(self) -> bool:
        """Moving things with a mouse drag confirms when releasing the button"""
        ...
    @use_drag_immediately.setter
    def use_drag_immediately(self, value: bool):
        ...
    @property
    def use_numeric_input_advanced(self) -> bool:
        """When entering numbers while transforming, default to advanced mode for full math expression evaluation"""
        ...
    @use_numeric_input_advanced.setter
    def use_numeric_input_advanced(self, value: bool):
        ...
    @property
    def navigation_mode(self) -> Literal['WALK', 'FLY']:
        """Which method to use for viewport navigation"""
        ...
    @navigation_mode.setter
    def navigation_mode(self, value: Literal['WALK', 'FLY']):
        ...
    @property
    def walk_navigation(self) -> Annotated['WalkNavigation', "is_animatable=False"]:
        """Settings for walk navigation mode"""
        ...
    @property
    def view_rotate_sensitivity_turntable(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=1.0", "precision=2"]:
        """Rotation amount per pixel to control how fast the viewport orbits"""
        ...
    @view_rotate_sensitivity_turntable.setter
    def view_rotate_sensitivity_turntable(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=1.0", "precision=2"]):
        ...
    @property
    def view_rotate_sensitivity_trackball(self) -> Annotated[float, "subtype='FACTOR'", "step=0.009999999776482582", "precision=2"]:
        """Scale trackball orbit sensitivity"""
        ...
    @view_rotate_sensitivity_trackball.setter
    def view_rotate_sensitivity_trackball(self, value: Annotated[float, "subtype='FACTOR'", "step=0.009999999776482582", "precision=2"]):
        ...
    @property
    def drag_threshold_mouse(self) -> Annotated[int, "subtype='PIXEL'", "step=1"]:
        """Number of pixels to drag before a drag event is triggered for mouse/trackpad input (otherwise click events are detected)"""
        ...
    @drag_threshold_mouse.setter
    def drag_threshold_mouse(self, value: Annotated[int, "subtype='PIXEL'", "step=1"]):
        ...
    @property
    def drag_threshold_tablet(self) -> Annotated[int, "subtype='PIXEL'", "step=1"]:
        """Number of pixels to drag before a drag event is triggered for tablet input (otherwise click events are detected)"""
        ...
    @drag_threshold_tablet.setter
    def drag_threshold_tablet(self, value: Annotated[int, "subtype='PIXEL'", "step=1"]):
        ...
    @property
    def drag_threshold(self) -> Annotated[int, "subtype='PIXEL'", "step=1"]:
        """Number of pixels to drag before a drag event is triggered for keyboard and other non mouse/tablet input (otherwise click events are detected)"""
        ...
    @drag_threshold.setter
    def drag_threshold(self, value: Annotated[int, "subtype='PIXEL'", "step=1"]):
        ...
    @property
    def move_threshold(self) -> Annotated[int, "subtype='PIXEL'", "step=1"]:
        """Number of pixels to before the cursor is considered to have moved (used for cycling selected items on successive clicks)"""
        ...
    @move_threshold.setter
    def move_threshold(self, value: Annotated[int, "subtype='PIXEL'", "step=1"]):
        ...
    @property
    def pressure_threshold_max(self) -> Annotated[float, "subtype='FACTOR'", "step=0.009999999776482582", "precision=3"]:
        """Raw input pressure value that is interpreted as 100% by Blender"""
        ...
    @pressure_threshold_max.setter
    def pressure_threshold_max(self, value: Annotated[float, "subtype='FACTOR'", "step=0.009999999776482582", "precision=3"]):
        ...
    @property
    def pressure_softness(self) -> Annotated[float, "subtype='FACTOR'", "step=0.10000000149011612", "precision=2"]:
        """Adjusts softness of the low pressure response onset using a gamma curve"""
        ...
    @pressure_softness.setter
    def pressure_softness(self, value: Annotated[float, "subtype='FACTOR'", "step=0.10000000149011612", "precision=2"]):
        ...
    @property
    def tablet_api(self) -> Literal['AUTOMATIC', 'WINDOWS_INK', 'WINTAB']:
        """Select the tablet API to use for pressure sensitivity (may require restarting Blender for changes to take effect)"""
        ...
    @tablet_api.setter
    def tablet_api(self, value: Literal['AUTOMATIC', 'WINDOWS_INK', 'WINTAB']):
        ...
    @property
    def xr_navigation(self) -> Annotated['XrNavigation', "is_animatable=False"]:
        """Settings for navigation in XR"""
        ...
    @property
    def ndof_translation_sensitivity(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Overall sensitivity of the 3D Mouse for translation"""
        ...
    @ndof_translation_sensitivity.setter
    def ndof_translation_sensitivity(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def ndof_rotation_sensitivity(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Overall sensitivity of the 3D Mouse for rotation"""
        ...
    @ndof_rotation_sensitivity.setter
    def ndof_rotation_sensitivity(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def ndof_deadzone(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Threshold of initial movement needed from the device's rest position"""
        ...
    @ndof_deadzone.setter
    def ndof_deadzone(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def ndof_zoom_direction(self) -> Literal['NDOF_ZOOM_FORWARD', 'NDOF_ZOOM_UP']:
        """Which axis of the 3D Mouse cap zooms the view"""
        ...
    @ndof_zoom_direction.setter
    def ndof_zoom_direction(self, value: Literal['NDOF_ZOOM_FORWARD', 'NDOF_ZOOM_UP']):
        ...
    @property
    def ndof_show_guide_orbit_axis(self) -> bool:
        """Display the center and axis during rotation"""
        ...
    @ndof_show_guide_orbit_axis.setter
    def ndof_show_guide_orbit_axis(self, value: bool):
        ...
    @property
    def ndof_show_guide_orbit_center(self) -> bool:
        """Display the orbit center during rotation"""
        ...
    @ndof_show_guide_orbit_center.setter
    def ndof_show_guide_orbit_center(self, value: bool):
        ...
    @property
    def ndof_navigation_mode(self) -> Literal['OBJECT', 'FLY']:
        """3D Mouse Navigation Mode"""
        ...
    @ndof_navigation_mode.setter
    def ndof_navigation_mode(self, value: Literal['OBJECT', 'FLY']):
        ...
    @property
    def ndof_lock_horizon(self) -> bool:
        """Lock Horizon forces the horizon to be kept leveled as it currently is"""
        ...
    @ndof_lock_horizon.setter
    def ndof_lock_horizon(self, value: bool):
        ...
    @property
    def ndof_fly_speed_auto(self) -> bool:
        """Automatically adjusts fly navigation speed based on the distance of objects near the center of the viewport, making it easier to navigate complex scenes. Speed is recalculated each time movement starts."""
        ...
    @ndof_fly_speed_auto.setter
    def ndof_fly_speed_auto(self, value: bool):
        ...
    @property
    def ndof_orbit_center_auto(self) -> bool:
        """Auto sets the orbit center dynamically. When the complete model is in view, the center of volume of the whole model is used as the rotation point. When you move closer, the orbit center will be set on an object close to your center of the view."""
        ...
    @ndof_orbit_center_auto.setter
    def ndof_orbit_center_auto(self, value: bool):
        ...
    @property
    def ndof_orbit_center_selected(self) -> bool:
        """Selected Item forces the orbit center to only take the currently selected objects into account."""
        ...
    @ndof_orbit_center_selected.setter
    def ndof_orbit_center_selected(self, value: bool):
        ...
    @property
    def ndof_rotx_invert_axis(self) -> bool:

        ...
    @ndof_rotx_invert_axis.setter
    def ndof_rotx_invert_axis(self, value: bool):
        ...
    @property
    def ndof_roty_invert_axis(self) -> bool:

        ...
    @ndof_roty_invert_axis.setter
    def ndof_roty_invert_axis(self, value: bool):
        ...
    @property
    def ndof_rotz_invert_axis(self) -> bool:

        ...
    @ndof_rotz_invert_axis.setter
    def ndof_rotz_invert_axis(self, value: bool):
        ...
    @property
    def ndof_panx_invert_axis(self) -> bool:

        ...
    @ndof_panx_invert_axis.setter
    def ndof_panx_invert_axis(self, value: bool):
        ...
    @property
    def ndof_pany_invert_axis(self) -> bool:

        ...
    @ndof_pany_invert_axis.setter
    def ndof_pany_invert_axis(self, value: bool):
        ...
    @property
    def ndof_panz_invert_axis(self) -> bool:

        ...
    @ndof_panz_invert_axis.setter
    def ndof_panz_invert_axis(self, value: bool):
        ...
    @property
    def ndof_fly_helicopter(self) -> bool:
        """Device up/down directly controls the Z position of the 3D viewport"""
        ...
    @ndof_fly_helicopter.setter
    def ndof_fly_helicopter(self, value: bool):
        ...
    @property
    def ndof_lock_camera_pan_zoom(self) -> bool:
        """Pan/zoom the camera view instead of leaving the camera view when orbiting"""
        ...
    @ndof_lock_camera_pan_zoom.setter
    def ndof_lock_camera_pan_zoom(self, value: bool):
        ...
    @property
    def mouse_double_click_time(self) -> Annotated[int, "step=1"]:
        """Time/delay (in ms) for a double click"""
        ...
    @mouse_double_click_time.setter
    def mouse_double_click_time(self, value: Annotated[int, "step=1"]):
        ...
    @property
    def use_mouse_emulate_3_button(self) -> bool:
        """Emulate Middle Mouse with Alt+Left Mouse"""
        ...
    @use_mouse_emulate_3_button.setter
    def use_mouse_emulate_3_button(self, value: bool):
        ...
    @property
    def mouse_emulate_3_button_modifier(self) -> Literal['ALT', 'OSKEY']:
        """Hold this modifier to emulate the middle mouse button"""
        ...
    @mouse_emulate_3_button_modifier.setter
    def mouse_emulate_3_button_modifier(self, value: Literal['ALT', 'OSKEY']):
        ...
    @property
    def use_emulate_numpad(self) -> bool:
        """Main 1 to 0 keys act as the numpad ones (useful for laptops)"""
        ...
    @use_emulate_numpad.setter
    def use_emulate_numpad(self, value: bool):
        ...
    @property
    def invert_zoom_wheel(self) -> bool:
        """Swap the Mouse Wheel zoom direction"""
        ...
    @invert_zoom_wheel.setter
    def invert_zoom_wheel(self, value: bool):
        ...
    @property
    def touchpad_scroll_direction(self) -> Literal['TRADITIONAL', 'NATURAL']:
        """Scroll direction (Wayland only)"""
        ...
    @touchpad_scroll_direction.setter
    def touchpad_scroll_direction(self, value: Literal['TRADITIONAL', 'NATURAL']):
        ...