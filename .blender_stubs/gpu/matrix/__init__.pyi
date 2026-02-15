# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/gpu.matrix.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated


def get_model_view_matrix(*args, **kwargs) -> Any:
    """.. function:: get_model_view_matrix()

   Return a copy of the model-view matrix.

   :return: A 4x4 view matrix.
   :rtype: :class:`mathutils.Matrix`


    Online Documentation:
    https://docs.blender.org/api/current/gpu.matrix.html"""
    ...

def get_normal_matrix(*args, **kwargs) -> Any:
    """.. function:: get_normal_matrix()

   Return a copy of the normal matrix.

   :return: A 3x3 normal matrix.
   :rtype: :class:`mathutils.Matrix`


    Online Documentation:
    https://docs.blender.org/api/current/gpu.matrix.html"""
    ...

def get_projection_matrix(*args, **kwargs) -> Any:
    """.. function:: get_projection_matrix()

   Return a copy of the projection matrix.

   :return: A 4x4 projection matrix.
   :rtype: :class:`mathutils.Matrix`


    Online Documentation:
    https://docs.blender.org/api/current/gpu.matrix.html"""
    ...

def load_identity(*args, **kwargs) -> Any:
    """.. function:: load_identity()

   Load an identity matrix into the stack.


    Online Documentation:
    https://docs.blender.org/api/current/gpu.matrix.html"""
    ...

def load_matrix(*args, **kwargs) -> Any:
    """.. function:: load_matrix(matrix)

   Load a matrix into the stack.

   :arg matrix: A 4x4 matrix.
   :type matrix: :class:`mathutils.Matrix`


    Online Documentation:
    https://docs.blender.org/api/current/gpu.matrix.html"""
    ...

def load_projection_matrix(*args, **kwargs) -> Any:
    """.. function:: load_projection_matrix(matrix)

   Load a projection matrix into the stack.

   :arg matrix: A 4x4 matrix.
   :type matrix: :class:`mathutils.Matrix`


    Online Documentation:
    https://docs.blender.org/api/current/gpu.matrix.html"""
    ...

def multiply_matrix(*args, **kwargs) -> Any:
    """.. function:: multiply_matrix(matrix)

   Multiply the current stack matrix.

   :arg matrix: A 4x4 matrix.
   :type matrix: :class:`mathutils.Matrix`


    Online Documentation:
    https://docs.blender.org/api/current/gpu.matrix.html"""
    ...

def pop(*args, **kwargs) -> Any:
    """.. function:: pop()

   Remove the last model-view matrix from the stack.


    Online Documentation:
    https://docs.blender.org/api/current/gpu.matrix.html"""
    ...

def pop_projection(*args, **kwargs) -> Any:
    """.. function:: pop_projection()

   Remove the last projection matrix from the stack.


    Online Documentation:
    https://docs.blender.org/api/current/gpu.matrix.html"""
    ...

def push(*args, **kwargs) -> Any:
    """.. function:: push()

   Add to the model-view matrix stack.


    Online Documentation:
    https://docs.blender.org/api/current/gpu.matrix.html"""
    ...

def push_pop(*args, **kwargs) -> Any:
    """.. function:: push_pop()

   Context manager to ensure balanced push/pop calls, even in the case of an error.


    Online Documentation:
    https://docs.blender.org/api/current/gpu.matrix.html"""
    ...

def push_pop_projection(*args, **kwargs) -> Any:
    """.. function:: push_pop_projection()

   Context manager to ensure balanced push/pop calls, even in the case of an error.


    Online Documentation:
    https://docs.blender.org/api/current/gpu.matrix.html"""
    ...

def push_projection(*args, **kwargs) -> Any:
    """.. function:: push_projection()

   Add to the projection matrix stack.


    Online Documentation:
    https://docs.blender.org/api/current/gpu.matrix.html"""
    ...

def reset(*args, **kwargs) -> Any:
    """.. function:: reset()

   Empty stack and set to identity.


    Online Documentation:
    https://docs.blender.org/api/current/gpu.matrix.html"""
    ...

def scale(*args, **kwargs) -> Any:
    """.. function:: scale(scale)

   Scale the current stack matrix.

   :arg scale: Scale the current stack matrix with 2 or 3 floats.
   :type scale: Sequence[float]


    Online Documentation:
    https://docs.blender.org/api/current/gpu.matrix.html"""
    ...

def scale_uniform(*args, **kwargs) -> Any:
    """.. function:: scale_uniform(scale)

   :arg scale: Scale the current stack matrix.
   :type scale: float


    Online Documentation:
    https://docs.blender.org/api/current/gpu.matrix.html"""
    ...

def translate(*args, **kwargs) -> Any:
    """.. function:: translate(offset)

   Scale the current stack matrix.

   :arg offset: Translate the current stack matrix with 2 or 3 floats.
   :type offset: Sequence[float]


    Online Documentation:
    https://docs.blender.org/api/current/gpu.matrix.html"""
    ...
