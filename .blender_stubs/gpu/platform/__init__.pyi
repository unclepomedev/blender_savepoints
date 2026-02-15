# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/gpu.platform.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated


def backend_type_get(*args, **kwargs) -> Any:
    """.. function:: backend_type_get()

   Get actuve GPU backend.

   :return: Backend type ('OPENGL', 'VULKAN', 'METAL', 'NONE', 'UNKNOWN').
   :rtype: str


    Online Documentation:
    https://docs.blender.org/api/current/gpu.platform.html"""
    ...

def device_type_get(*args, **kwargs) -> Any:
    """.. function:: device_type_get()

   Get GPU device type.

   :return: Device type ('APPLE', 'NVIDIA', 'AMD', 'INTEL', 'SOFTWARE', 'QUALCOMM', 'UNKNOWN').
   :rtype: str


    Online Documentation:
    https://docs.blender.org/api/current/gpu.platform.html"""
    ...

def renderer_get(*args, **kwargs) -> Any:
    """.. function:: renderer_get()

   Get GPU to be used for rendering.

   :return: GPU name.
   :rtype: str


    Online Documentation:
    https://docs.blender.org/api/current/gpu.platform.html"""
    ...

def vendor_get(*args, **kwargs) -> Any:
    """.. function:: vendor_get()

   Get GPU vendor.

   :return: Vendor name.
   :rtype: str


    Online Documentation:
    https://docs.blender.org/api/current/gpu.platform.html"""
    ...

def version_get(*args, **kwargs) -> Any:
    """.. function:: version_get()

   Get GPU driver version.

   :return: Driver version.
   :rtype: str


    Online Documentation:
    https://docs.blender.org/api/current/gpu.platform.html"""
    ...
