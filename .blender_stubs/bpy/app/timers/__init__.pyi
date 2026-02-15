# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.app.timers.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated


def is_registered(*args, **kwargs) -> Any:
    """.. function:: is_registered(function)

   Check if this function is registered as a timer.

   :arg function: Function to check.
   :type function: Callable[[], float | None]
   :return: True when this function is registered, otherwise False.
   :rtype: bool


    Online Documentation:
    https://docs.blender.org/api/current/bpy.app.timers.html"""
    ...

def register(*args, **kwargs) -> Any:
    """.. function:: register(function, *, first_interval=0, persistent=False)

   Add a new function that will be called after the specified amount of seconds.
   The function gets no arguments and is expected to return either None or a float.
   If ``None`` is returned, the timer will be unregistered.
   A returned number specifies the delay until the function is called again.
   ``functools.partial`` can be used to assign some parameters.

   :arg function: The function that should called.
   :type function: Callable[[], float | None]
   :arg first_interval: Seconds until the callback should be called the first time.
   :type first_interval: float
   :arg persistent: Don't remove timer when a new file is loaded.
   :type persistent: bool


    Online Documentation:
    https://docs.blender.org/api/current/bpy.app.timers.html"""
    ...

def unregister(*args, **kwargs) -> Any:
    """.. function:: unregister(function)

   Unregister timer.

   :arg function: Function to unregister.
   :type function: Callable[[], float | None]


    Online Documentation:
    https://docs.blender.org/api/current/bpy.app.timers.html"""
    ...
