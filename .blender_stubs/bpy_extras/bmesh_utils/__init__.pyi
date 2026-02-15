# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy_extras.bmesh_utils.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated


def bmesh_linked_uv_islands(bm, uv_layer) -> Any:
    """
    Returns lists of faces connected by UV islands.

    For meshes use :class:`bpy.types.Mesh.mesh_linked_uv_islands` instead.

    :arg bm: the bmesh used to group with.
    :type bmesh: :class:`BMesh`
    :arg uv_layer: the UV layer to source UVs from.
    :type bmesh: :class:`BMLayerItem`
    :return: list of lists containing polygon indices
    :rtype: list[list[int]]
    

    Online Documentation:
    https://docs.blender.org/api/current/bpy_extras.bmesh_utils.html"""
    ...

def match_uv(face, vert, uv, uv_layer) -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy_extras.bmesh_utils.html"""
    ...
