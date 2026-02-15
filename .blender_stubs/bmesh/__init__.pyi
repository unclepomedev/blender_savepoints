# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bmesh.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated


def from_edit_mesh(*args, **kwargs) -> Any:
    """.. method:: from_edit_mesh(mesh)

   Return a BMesh from this mesh, currently the mesh must already be in editmode.

   :arg mesh: The editmode mesh.
   :type mesh: :class:`bpy.types.Mesh`
   :return: the BMesh associated with this mesh.
   :rtype: :class:`bmesh.types.BMesh`


    Online Documentation:
    https://docs.blender.org/api/current/bmesh.html"""
    ...

def new(*args, **kwargs) -> Any:
    """.. method:: new(*, use_operators=True)

   :arg use_operators: Support calling operators in :mod:`bmesh.ops` (uses some extra memory per vert/edge/face).
   :type use_operators: bool
   :return: Return a new, empty BMesh.
   :rtype: :class:`bmesh.types.BMesh`


    Online Documentation:
    https://docs.blender.org/api/current/bmesh.html"""
    ...

def update_edit_mesh(*args, **kwargs) -> Any:
    """.. method:: update_edit_mesh(mesh, *, loop_triangles=True, destructive=True)

   Update the mesh after changes to the BMesh in editmode,
   optionally recalculating n-gon tessellation.

   :arg mesh: The editmode mesh.
   :type mesh: :class:`bpy.types.Mesh`
   :arg loop_triangles: Option to recalculate n-gon tessellation.
   :type loop_triangles: bool
   :arg destructive: Use when geometry has been added or removed.
   :type destructive: bool


    Online Documentation:
    https://docs.blender.org/api/current/bmesh.html"""
    ...

from . import geometry as geometry
# Documentation: https://docs.blender.org/api/current/bmesh.geometry.html
from . import ops as ops
# Documentation: https://docs.blender.org/api/current/bmesh.ops.html
from . import types as types
# Documentation: https://docs.blender.org/api/current/bmesh.types.html
from . import utils as utils
# Documentation: https://docs.blender.org/api/current/bmesh.utils.html