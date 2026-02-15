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
from .WalkNavigation import WalkNavigation
from .XrNavigation import XrNavigation
class PreferencesInput(bpy_struct):
    view_zoom_method: Literal['CONTINUE', 'DOLLY', 'SCALE']
    """Which style to use for viewport scaling"""
    view_zoom_axis: Literal['VERTICAL', 'HORIZONTAL']
    """Axis of mouse movement to zoom in or out on"""
    use_multitouch_gestures: bool
    """Use multi-touch gestures for navigation with touchpad, instead of scroll wheel emulation"""
    invert_mouse_zoom: bool
    """Invert the axis of mouse movement for zooming"""
    use_mouse_depth_navigate: bool
    """Use the depth under the mouse to improve view pan/rotate/zoom functionality"""
    use_zoom_to_mouse: bool
    """Zoom in towards the mouse pointer's position in the 3D view, rather than the 2D window center"""
    use_auto_perspective: bool
    """Automatically switch between orthographic and perspective when changing from top/front/side views"""
    use_rotate_around_active: bool
    """Use selection as the pivot point"""
    view_rotate_method: Literal['TURNTABLE', 'TRACKBALL']
    """Orbit method in the viewport"""
    use_mouse_continuous: bool
    """Let the mouse wrap around the view boundaries so mouse movements are not limited by the screen size (used by transform, dragging of UI controls, etc.)"""
    use_drag_immediately: bool
    """Moving things with a mouse drag confirms when releasing the button"""
    use_numeric_input_advanced: bool
    """When entering numbers while transforming, default to advanced mode for full math expression evaluation"""
    navigation_mode: Literal['WALK', 'FLY']
    """Which method to use for viewport navigation"""
    @property
    def walk_navigation(self) -> Annotated['WalkNavigation', "is_animatable=False"]:
        """Settings for walk navigation mode"""
        ...
    view_rotate_sensitivity_turntable: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=1.0", "precision=2"]
    """Rotation amount per pixel to control how fast the viewport orbits"""
    view_rotate_sensitivity_trackball: Annotated[float, "subtype='FACTOR'", "step=0.009999999776482582", "precision=2"]
    """Scale trackball orbit sensitivity"""
    drag_threshold_mouse: Annotated[int, "subtype='PIXEL'", "step=1"]
    """Number of pixels to drag before a drag event is triggered for mouse/trackpad input (otherwise click events are detected)"""
    drag_threshold_tablet: Annotated[int, "subtype='PIXEL'", "step=1"]
    """Number of pixels to drag before a drag event is triggered for tablet input (otherwise click events are detected)"""
    drag_threshold: Annotated[int, "subtype='PIXEL'", "step=1"]
    """Number of pixels to drag before a drag event is triggered for keyboard and other non mouse/tablet input (otherwise click events are detected)"""
    move_threshold: Annotated[int, "subtype='PIXEL'", "step=1"]
    """Number of pixels to before the cursor is considered to have moved (used for cycling selected items on successive clicks)"""
    pressure_threshold_max: Annotated[float, "subtype='FACTOR'", "step=0.009999999776482582", "precision=3"]
    """Raw input pressure value that is interpreted as 100% by Blender"""
    pressure_softness: Annotated[float, "subtype='FACTOR'", "step=0.10000000149011612", "precision=2"]
    """Adjusts softness of the low pressure response onset using a gamma curve"""
    tablet_api: Literal['AUTOMATIC', 'WINDOWS_INK', 'WINTAB']
    """Select the tablet API to use for pressure sensitivity (may require restarting Blender for changes to take effect)"""
    @property
    def xr_navigation(self) -> Annotated['XrNavigation', "is_animatable=False"]:
        """Settings for navigation in XR"""
        ...
    ndof_translation_sensitivity: Annotated[float, "step=10.0", "precision=3"]
    """Overall sensitivity of the 3D Mouse for translation"""
    ndof_rotation_sensitivity: Annotated[float, "step=10.0", "precision=3"]
    """Overall sensitivity of the 3D Mouse for rotation"""
    ndof_deadzone: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Threshold of initial movement needed from the device's rest position"""
    ndof_zoom_direction: Literal['NDOF_ZOOM_FORWARD', 'NDOF_ZOOM_UP']
    """Which axis of the 3D Mouse cap zooms the view"""
    ndof_show_guide_orbit_axis: bool
    """Display the center and axis during rotation"""
    ndof_show_guide_orbit_center: bool
    """Display the orbit center during rotation"""
    ndof_navigation_mode: Literal['OBJECT', 'FLY']
    """3D Mouse Navigation Mode"""
    ndof_lock_horizon: bool
    """Lock Horizon forces the horizon to be kept leveled as it currently is"""
    ndof_fly_speed_auto: bool
    """Automatically adjusts fly navigation speed based on the distance of objects near the center of the viewport, making it easier to navigate complex scenes. Speed is recalculated each time movement starts."""
    ndof_orbit_center_auto: bool
    """Auto sets the orbit center dynamically. When the complete model is in view, the center of volume of the whole model is used as the rotation point. When you move closer, the orbit center will be set on an object close to your center of the view."""
    ndof_orbit_center_selected: bool
    """Selected Item forces the orbit center to only take the currently selected objects into account."""
    ndof_rotx_invert_axis: bool
    ndof_roty_invert_axis: bool
    ndof_rotz_invert_axis: bool
    ndof_panx_invert_axis: bool
    ndof_pany_invert_axis: bool
    ndof_panz_invert_axis: bool
    ndof_fly_helicopter: bool
    """Device up/down directly controls the Z position of the 3D viewport"""
    ndof_lock_camera_pan_zoom: bool
    """Pan/zoom the camera view instead of leaving the camera view when orbiting"""
    mouse_double_click_time: Annotated[int, "step=1"]
    """Time/delay (in ms) for a double click"""
    use_mouse_emulate_3_button: bool
    """Emulate Middle Mouse with Alt+Left Mouse"""
    mouse_emulate_3_button_modifier: Literal['ALT', 'OSKEY']
    """Hold this modifier to emulate the middle mouse button"""
    use_emulate_numpad: bool
    """Main 1 to 0 keys act as the numpad ones (useful for laptops)"""
    invert_zoom_wheel: bool
    """Swap the Mouse Wheel zoom direction"""
    touchpad_scroll_direction: Literal['TRADITIONAL', 'NATURAL']
    """Scroll direction (Wayland only)"""