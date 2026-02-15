# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy_extras.mesh_utils.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated


def edge_face_count(mesh) -> Any:
    """
    :return: list face users for each item in mesh.edges.
    :rtype: list[int]
    

    Online Documentation:
    https://docs.blender.org/api/current/bpy_extras.mesh_utils.html"""
    ...

def edge_face_count_dict(mesh) -> Any:
    """
    :return: Dictionary of edge keys with their value set to the number of faces using each edge.
    :rtype: dict[tuple[int, int], int]
    

    Online Documentation:
    https://docs.blender.org/api/current/bpy_extras.mesh_utils.html"""
    ...

def edge_loops_from_edges(mesh, edges=None) -> Any:
    """
    Edge loops defined by edges

    Takes me.edges or a list of edges and returns the edge loops

    return a list of vertex indices.
    [ [1, 6, 7, 2], ...]

    closed loops have matching start and end values.
    

    Online Documentation:
    https://docs.blender.org/api/current/bpy_extras.mesh_utils.html"""
    ...

def mesh_linked_triangles(mesh) -> Any:
    """
    Splits the mesh into connected triangles, use this for separating cubes from
    other mesh elements within 1 mesh data-block.

    :arg mesh: the mesh used to group with.
    :type mesh: :class:`bpy.types.Mesh`
    :return: Lists of lists containing triangles.
    :rtype: list[list[:class:`bpy.types.MeshLoopTriangle`]]
    

    Online Documentation:
    https://docs.blender.org/api/current/bpy_extras.mesh_utils.html"""
    ...

def mesh_linked_uv_islands(mesh) -> Any:
    """
    Returns lists of polygon indices connected by UV islands.

    :arg mesh: the mesh used to group with.
    :type mesh: :class:`bpy.types.Mesh`
    :return: list of lists containing polygon indices
    :rtype: list[list[int]]
    

    Online Documentation:
    https://docs.blender.org/api/current/bpy_extras.mesh_utils.html"""
    ...

def ngon_tessellate(from_data, indices, fix_loops=True, debug_print=True) -> Any:
    """
    Takes a poly-line of indices (ngon) and returns a list of face
    index lists. Designed to be used for importers that need indices for an
    ngon to create from existing verts.

    :arg from_data: Either a mesh, or a list/tuple of 3D vectors.
    :type from_data: :class:`bpy.types.Mesh` | list[Sequence[float]] | tuple[Sequence[float]]
    :arg indices: a list of indices to use this list
       is the ordered closed poly-line
       to fill, and can be a subset of the data given.
    :type indices: list[int]
    :arg fix_loops: If this is enabled poly-lines
       that use loops to make multiple
       poly-lines are dealt with correctly.
    :type fix_loops: bool
    

    Online Documentation:
    https://docs.blender.org/api/current/bpy_extras.mesh_utils.html"""
    ...

def triangle_random_points(num_points, loop_triangles) -> Any:
    """
    Generates a list of random points over mesh loop triangles.

    :arg num_points: The number of random points to generate on each triangle.
    :type num_points: int
    :arg loop_triangles: Sequence of the triangles to generate points on.
    :type loop_triangles: Sequence[:class:`bpy.types.MeshLoopTriangle`]
    :return: List of random points over all triangles.
    :rtype: list[:class:`mathutils.Vector`]
    

    Online Documentation:
    https://docs.blender.org/api/current/bpy_extras.mesh_utils.html"""
    ...
