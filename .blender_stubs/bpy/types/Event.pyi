# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.Event.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .NDOFMotionEventData import NDOFMotionEventData
from .XrEventData import XrEventData

class Event(bpy_struct):

    @property
    def ascii(self) -> Annotated[str, "is_animatable=False"]:
        """Single ASCII character for this event"""
        ...
    @property
    def unicode(self) -> Annotated[str, "is_animatable=False"]:
        """Single unicode character for this event"""
        ...
    @property
    def value(self) -> Literal['ANY', 'PRESS', 'RELEASE', 'CLICK', 'DOUBLE_CLICK', 'CLICK_DRAG', 'NOTHING']:
        """The type of event, only applies to some"""
        ...
    @property
    def value_prev(self) -> Literal['ANY', 'PRESS', 'RELEASE', 'CLICK', 'DOUBLE_CLICK', 'CLICK_DRAG', 'NOTHING']:
        """The type of event, only applies to some"""
        ...
    @property
    def type(self) -> Literal['NONE', 'LEFTMOUSE', 'MIDDLEMOUSE', 'RIGHTMOUSE', 'BUTTON4MOUSE', 'BUTTON5MOUSE', 'BUTTON6MOUSE', 'BUTTON7MOUSE', 'PEN', 'ERASER', 'MOUSEMOVE', 'INBETWEEN_MOUSEMOVE', 'TRACKPADPAN', 'TRACKPADZOOM', 'MOUSEROTATE', 'MOUSESMARTZOOM', 'WHEELUPMOUSE', 'WHEELDOWNMOUSE', 'WHEELINMOUSE', 'WHEELOUTMOUSE', 'WHEELLEFTMOUSE', 'WHEELRIGHTMOUSE', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE', 'LEFT_CTRL', 'LEFT_ALT', 'LEFT_SHIFT', 'RIGHT_ALT', 'RIGHT_CTRL', 'RIGHT_SHIFT', 'OSKEY', 'HYPER', 'APP', 'GRLESS', 'ESC', 'TAB', 'RET', 'SPACE', 'LINE_FEED', 'BACK_SPACE', 'DEL', 'SEMI_COLON', 'PERIOD', 'COMMA', 'QUOTE', 'ACCENT_GRAVE', 'MINUS', 'PLUS', 'SLASH', 'BACK_SLASH', 'EQUAL', 'LEFT_BRACKET', 'RIGHT_BRACKET', 'LEFT_ARROW', 'DOWN_ARROW', 'RIGHT_ARROW', 'UP_ARROW', 'NUMPAD_2', 'NUMPAD_4', 'NUMPAD_6', 'NUMPAD_8', 'NUMPAD_1', 'NUMPAD_3', 'NUMPAD_5', 'NUMPAD_7', 'NUMPAD_9', 'NUMPAD_PERIOD', 'NUMPAD_SLASH', 'NUMPAD_ASTERIX', 'NUMPAD_0', 'NUMPAD_MINUS', 'NUMPAD_ENTER', 'NUMPAD_PLUS', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12', 'F13', 'F14', 'F15', 'F16', 'F17', 'F18', 'F19', 'F20', 'F21', 'F22', 'F23', 'F24', 'PAUSE', 'INSERT', 'HOME', 'PAGE_UP', 'PAGE_DOWN', 'END', 'MEDIA_PLAY', 'MEDIA_STOP', 'MEDIA_FIRST', 'MEDIA_LAST', 'TEXTINPUT', 'WINDOW_DEACTIVATE', 'TIMER', 'TIMER0', 'TIMER1', 'TIMER2', 'TIMER_JOBS', 'TIMER_AUTOSAVE', 'TIMER_REPORT', 'TIMERREGION', 'NDOF_MOTION', 'NDOF_BUTTON_MENU', 'NDOF_BUTTON_FIT', 'NDOF_BUTTON_TOP', 'NDOF_BUTTON_BOTTOM', 'NDOF_BUTTON_LEFT', 'NDOF_BUTTON_RIGHT', 'NDOF_BUTTON_FRONT', 'NDOF_BUTTON_BACK', 'NDOF_BUTTON_ISO1', 'NDOF_BUTTON_ISO2', 'NDOF_BUTTON_ROLL_CW', 'NDOF_BUTTON_ROLL_CCW', 'NDOF_BUTTON_SPIN_CW', 'NDOF_BUTTON_SPIN_CCW', 'NDOF_BUTTON_TILT_CW', 'NDOF_BUTTON_TILT_CCW', 'NDOF_BUTTON_ROTATE', 'NDOF_BUTTON_PANZOOM', 'NDOF_BUTTON_DOMINANT', 'NDOF_BUTTON_PLUS', 'NDOF_BUTTON_MINUS', 'NDOF_BUTTON_V1', 'NDOF_BUTTON_V2', 'NDOF_BUTTON_V3', 'NDOF_BUTTON_SAVE_V1', 'NDOF_BUTTON_SAVE_V2', 'NDOF_BUTTON_SAVE_V3', 'NDOF_BUTTON_1', 'NDOF_BUTTON_2', 'NDOF_BUTTON_3', 'NDOF_BUTTON_4', 'NDOF_BUTTON_5', 'NDOF_BUTTON_6', 'NDOF_BUTTON_7', 'NDOF_BUTTON_8', 'NDOF_BUTTON_9', 'NDOF_BUTTON_10', 'NDOF_BUTTON_11', 'NDOF_BUTTON_12', 'ACTIONZONE_AREA', 'ACTIONZONE_REGION', 'ACTIONZONE_FULLSCREEN', 'XR_ACTION']:

        ...
    @property
    def type_prev(self) -> Literal['NONE', 'LEFTMOUSE', 'MIDDLEMOUSE', 'RIGHTMOUSE', 'BUTTON4MOUSE', 'BUTTON5MOUSE', 'BUTTON6MOUSE', 'BUTTON7MOUSE', 'PEN', 'ERASER', 'MOUSEMOVE', 'INBETWEEN_MOUSEMOVE', 'TRACKPADPAN', 'TRACKPADZOOM', 'MOUSEROTATE', 'MOUSESMARTZOOM', 'WHEELUPMOUSE', 'WHEELDOWNMOUSE', 'WHEELINMOUSE', 'WHEELOUTMOUSE', 'WHEELLEFTMOUSE', 'WHEELRIGHTMOUSE', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE', 'LEFT_CTRL', 'LEFT_ALT', 'LEFT_SHIFT', 'RIGHT_ALT', 'RIGHT_CTRL', 'RIGHT_SHIFT', 'OSKEY', 'HYPER', 'APP', 'GRLESS', 'ESC', 'TAB', 'RET', 'SPACE', 'LINE_FEED', 'BACK_SPACE', 'DEL', 'SEMI_COLON', 'PERIOD', 'COMMA', 'QUOTE', 'ACCENT_GRAVE', 'MINUS', 'PLUS', 'SLASH', 'BACK_SLASH', 'EQUAL', 'LEFT_BRACKET', 'RIGHT_BRACKET', 'LEFT_ARROW', 'DOWN_ARROW', 'RIGHT_ARROW', 'UP_ARROW', 'NUMPAD_2', 'NUMPAD_4', 'NUMPAD_6', 'NUMPAD_8', 'NUMPAD_1', 'NUMPAD_3', 'NUMPAD_5', 'NUMPAD_7', 'NUMPAD_9', 'NUMPAD_PERIOD', 'NUMPAD_SLASH', 'NUMPAD_ASTERIX', 'NUMPAD_0', 'NUMPAD_MINUS', 'NUMPAD_ENTER', 'NUMPAD_PLUS', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12', 'F13', 'F14', 'F15', 'F16', 'F17', 'F18', 'F19', 'F20', 'F21', 'F22', 'F23', 'F24', 'PAUSE', 'INSERT', 'HOME', 'PAGE_UP', 'PAGE_DOWN', 'END', 'MEDIA_PLAY', 'MEDIA_STOP', 'MEDIA_FIRST', 'MEDIA_LAST', 'TEXTINPUT', 'WINDOW_DEACTIVATE', 'TIMER', 'TIMER0', 'TIMER1', 'TIMER2', 'TIMER_JOBS', 'TIMER_AUTOSAVE', 'TIMER_REPORT', 'TIMERREGION', 'NDOF_MOTION', 'NDOF_BUTTON_MENU', 'NDOF_BUTTON_FIT', 'NDOF_BUTTON_TOP', 'NDOF_BUTTON_BOTTOM', 'NDOF_BUTTON_LEFT', 'NDOF_BUTTON_RIGHT', 'NDOF_BUTTON_FRONT', 'NDOF_BUTTON_BACK', 'NDOF_BUTTON_ISO1', 'NDOF_BUTTON_ISO2', 'NDOF_BUTTON_ROLL_CW', 'NDOF_BUTTON_ROLL_CCW', 'NDOF_BUTTON_SPIN_CW', 'NDOF_BUTTON_SPIN_CCW', 'NDOF_BUTTON_TILT_CW', 'NDOF_BUTTON_TILT_CCW', 'NDOF_BUTTON_ROTATE', 'NDOF_BUTTON_PANZOOM', 'NDOF_BUTTON_DOMINANT', 'NDOF_BUTTON_PLUS', 'NDOF_BUTTON_MINUS', 'NDOF_BUTTON_V1', 'NDOF_BUTTON_V2', 'NDOF_BUTTON_V3', 'NDOF_BUTTON_SAVE_V1', 'NDOF_BUTTON_SAVE_V2', 'NDOF_BUTTON_SAVE_V3', 'NDOF_BUTTON_1', 'NDOF_BUTTON_2', 'NDOF_BUTTON_3', 'NDOF_BUTTON_4', 'NDOF_BUTTON_5', 'NDOF_BUTTON_6', 'NDOF_BUTTON_7', 'NDOF_BUTTON_8', 'NDOF_BUTTON_9', 'NDOF_BUTTON_10', 'NDOF_BUTTON_11', 'NDOF_BUTTON_12', 'ACTIONZONE_AREA', 'ACTIONZONE_REGION', 'ACTIONZONE_FULLSCREEN', 'XR_ACTION']:

        ...
    @property
    def direction(self) -> Literal['ANY', 'NORTH', 'NORTH_EAST', 'EAST', 'SOUTH_EAST', 'SOUTH', 'SOUTH_WEST', 'WEST', 'NORTH_WEST']:
        """The direction (only applies to drag events)"""
        ...
    @property
    def is_repeat(self) -> bool:
        """The event is generated by holding a key down"""
        ...
    @property
    def is_consecutive(self) -> bool:
        """Part of a trackpad or NDOF motion, interrupted by cursor motion, button or key press events"""
        ...
    @property
    def mouse_x(self) -> Annotated[int, "step=1"]:
        """The window relative horizontal location of the mouse"""
        ...
    @property
    def mouse_y(self) -> Annotated[int, "step=1"]:
        """The window relative vertical location of the mouse"""
        ...
    @property
    def mouse_region_x(self) -> Annotated[int, "step=1"]:
        """The region relative horizontal location of the mouse"""
        ...
    @property
    def mouse_region_y(self) -> Annotated[int, "step=1"]:
        """The region relative vertical location of the mouse"""
        ...
    @property
    def mouse_prev_x(self) -> Annotated[int, "step=1"]:
        """The window relative horizontal location of the mouse"""
        ...
    @property
    def mouse_prev_y(self) -> Annotated[int, "step=1"]:
        """The window relative vertical location of the mouse"""
        ...
    @property
    def mouse_prev_press_x(self) -> Annotated[int, "step=1"]:
        """The window relative horizontal location of the last press event"""
        ...
    @property
    def mouse_prev_press_y(self) -> Annotated[int, "step=1"]:
        """The window relative vertical location of the last press event"""
        ...
    @property
    def pressure(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """The pressure of the tablet or 1.0 if no tablet present"""
        ...
    @property
    def tilt(self) -> Annotated[list[float], "subtype='XYZ_LENGTH'", "unit='LENGTH'", "step=10.0", "precision=3"]:
        """The pressure of the tablet or zeroes if no tablet present"""
        ...
    @property
    def is_tablet(self) -> bool:
        """The event has tablet data"""
        ...
    @property
    def is_mouse_absolute(self) -> bool:
        """The last motion event was an absolute input"""
        ...
    @property
    def ndof_motion(self) -> Annotated[Optional['NDOFMotionEventData'], "is_animatable=False"]:
        """NDOF motion event data"""
        ...
    @property
    def xr(self) -> Annotated[Optional['XrEventData'], "is_animatable=False"]:
        """XR event data"""
        ...
    @property
    def shift(self) -> bool:
        """True when the Shift key is held"""
        ...
    @property
    def ctrl(self) -> bool:
        """True when the Ctrl key is held"""
        ...
    @property
    def alt(self) -> bool:
        """True when the Alt/Option key is held"""
        ...
    @property
    def oskey(self) -> bool:
        """True when the Cmd key is held"""
        ...
    @property
    def hyper(self) -> bool:
        """True when the Hyper key is held"""
        ...