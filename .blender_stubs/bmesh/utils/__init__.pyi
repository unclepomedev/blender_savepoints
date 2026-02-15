# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bmesh.utils.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated


def edge_rotate(*args, **kwargs) -> Any:
    """.. method:: edge_rotate(edge, ccw=False)

   Rotate the edge and return the newly created edge.
   If rotating the edge fails, None will be returned.

   :arg edge: The edge to rotate.
   :type edge: :class:`bmesh.types.BMEdge`
   :arg ccw: When True the edge will be rotated counter clockwise.
   :type ccw: bool
   :return: The newly rotated edge.
   :rtype: :class:`bmesh.types.BMEdge`


    Online Documentation:
    https://docs.blender.org/api/current/bmesh.utils.html"""
    ...

def edge_split(*args, **kwargs) -> Any:
    """.. method:: edge_split(edge, vert, fac)

   Split an edge, return the newly created data.

   :arg edge: The edge to split.
   :type edge: :class:`bmesh.types.BMEdge`
   :arg vert: One of the verts on the edge, defines the split direction.
   :type vert: :class:`bmesh.types.BMVert`
   :arg fac: The point on the edge where the new vert will be created [0 - 1].
   :type fac: float
   :return: The newly created (edge, vert) pair.
   :rtype: tuple[:class:`bmesh.types.BMEdge`, :class:`bmesh.types.BMVert`]


    Online Documentation:
    https://docs.blender.org/api/current/bmesh.utils.html"""
    ...

def face_flip(*args, **kwargs) -> Any:
    """.. method:: face_flip(faces)

   Flip the faces direction.

   :arg face: Face to flip.
   :type face: :class:`bmesh.types.BMFace`


    Online Documentation:
    https://docs.blender.org/api/current/bmesh.utils.html"""
    ...

def face_join(*args, **kwargs) -> Any:
    """.. method:: face_join(faces, remove=True)

   Joins a sequence of faces.

   :arg faces: Sequence of faces.
   :type faces: :class:`bmesh.types.BMFace`
   :arg remove: Remove the edges and vertices between the faces.
   :type remove: bool
   :return: The newly created face or None on failure.
   :rtype: :class:`bmesh.types.BMFace`


    Online Documentation:
    https://docs.blender.org/api/current/bmesh.utils.html"""
    ...

def face_split(*args, **kwargs) -> Any:
    """.. method:: face_split(face, vert_a, vert_b, *, coords=(), use_exist=True, example=None)

   Face split with optional intermediate points.

   :arg face: The face to cut.
   :type face: :class:`bmesh.types.BMFace`
   :arg vert_a: First vertex to cut in the face (face must contain the vert).
   :type vert_a: :class:`bmesh.types.BMVert`
   :arg vert_b: Second vertex to cut in the face (face must contain the vert).
   :type vert_b: :class:`bmesh.types.BMVert`
   :arg coords: Optional sequence of 3D points in between *vert_a* and *vert_b*.
   :type coords: Sequence[Sequence[float]]
   :arg use_exist: .Use an existing edge if it exists (Only used when *coords* argument is empty or omitted)
   :type use_exist: bool
   :arg example: Newly created edge will copy settings from this one.
   :type example: :class:`bmesh.types.BMEdge`
   :return: The newly created face or None on failure.
   :rtype: tuple[:class:`bmesh.types.BMFace`, :class:`bmesh.types.BMLoop`]


    Online Documentation:
    https://docs.blender.org/api/current/bmesh.utils.html"""
    ...

def face_split_edgenet(*args, **kwargs) -> Any:
    """.. method:: face_split_edgenet(face, edgenet)

   Splits a face into any number of regions defined by an edgenet.

   :arg face: The face to split.
   :type face: :class:`bmesh.types.BMFace`
   :arg face: The face to split.
   :type face: :class:`bmesh.types.BMFace`
   :arg edgenet: Sequence of edges.
   :type edgenet: Sequence[:class:`bmesh.types.BMEdge`]
   :return: The newly created faces.
   :rtype: tuple[:class:`bmesh.types.BMFace`, ...]

   .. note::

      Regions defined by edges need to connect to the face, otherwise they're ignored as loose edges.


    Online Documentation:
    https://docs.blender.org/api/current/bmesh.utils.html"""
    ...

def face_vert_separate(*args, **kwargs) -> Any:
    """.. method:: face_vert_separate(face, vert)

   Rip a vertex in a face away and add a new vertex.

   :arg face: The face to separate.
   :type face: :class:`bmesh.types.BMFace`
   :arg vert: A vertex in the face to separate.
   :type vert: :class:`bmesh.types.BMVert`
   :return vert: The newly created vertex or None on failure.
   :rtype vert: :class:`bmesh.types.BMVert`

   .. note::

      This is the same as loop_separate, and has only been added for convenience.


    Online Documentation:
    https://docs.blender.org/api/current/bmesh.utils.html"""
    ...

def loop_separate(*args, **kwargs) -> Any:
    """.. method:: loop_separate(loop)

   Rip a vertex in a face away and add a new vertex.

   :arg loop: The loop to separate.
   :type loop: :class:`bmesh.types.BMLoop`
   :return vert: The newly created vertex or None on failure.
   :rtype vert: :class:`bmesh.types.BMVert`


    Online Documentation:
    https://docs.blender.org/api/current/bmesh.utils.html"""
    ...

def uv_select_check(*args, **kwargs) -> Any:
    """.. method:: uv_select_check(bm, /, *, sync=True, flush=False, contiguous=False)

   Split an edge, return the newly created data.

   :arg sync: Check the data is properly synchronized between UV's and the underlying mesh. Failure to synchronize with the mesh selection may cause tools not to behave properly.
   :type sync: bool
   :arg flush: Check the selection has been properly flushed between elements (based on the current :class:`BMesh.select_mode`).
   :type flush: bool
   :arg contiguous: Check connected UV's and edges have a matching selection state.
   :type contiguous: bool
   :return: An error dictionary or None when there are no errors found.
   :rtype: dict[str, int] | None


    Online Documentation:
    https://docs.blender.org/api/current/bmesh.utils.html"""
    ...

def vert_collapse_edge(*args, **kwargs) -> Any:
    """.. method:: vert_collapse_edge(vert, edge)

   Collapse a vertex into an edge.

   :arg vert: The vert that will be collapsed.
   :type vert: :class:`bmesh.types.BMVert`
   :arg edge: The edge to collapse into.
   :type edge: :class:`bmesh.types.BMEdge`
   :return: The resulting edge from the collapse operation.
   :rtype: :class:`bmesh.types.BMEdge`


    Online Documentation:
    https://docs.blender.org/api/current/bmesh.utils.html"""
    ...

def vert_collapse_faces(*args, **kwargs) -> Any:
    """.. method:: vert_collapse_faces(vert, edge, fac, join_faces)

   Collapses a vertex that has only two manifold edges onto a vertex it shares an edge with.

   :arg vert: The vert that will be collapsed.
   :type vert: :class:`bmesh.types.BMVert`
   :arg edge: The edge to collapse into.
   :type edge: :class:`bmesh.types.BMEdge`
   :arg fac: The factor to use when merging customdata [0 - 1].
   :type fac: float
   :arg join_faces: When true the faces around the vertex will be joined otherwise collapse the vertex by merging the 2 edges this vertex connects to into one.
   :type join_faces: bool
   :return: The resulting edge from the collapse operation.
   :rtype: :class:`bmesh.types.BMEdge`


    Online Documentation:
    https://docs.blender.org/api/current/bmesh.utils.html"""
    ...

def vert_dissolve(*args, **kwargs) -> Any:
    """.. method:: vert_dissolve(vert)

   Dissolve this vertex (will be removed).

   :arg vert: The vert to be dissolved.
   :type vert: :class:`bmesh.types.BMVert`
   :return: True when the vertex dissolve is successful.
   :rtype: bool


    Online Documentation:
    https://docs.blender.org/api/current/bmesh.utils.html"""
    ...

def vert_separate(*args, **kwargs) -> Any:
    """.. method:: vert_separate(vert, edges)

   Separate this vertex at every edge.

   :arg vert: The vert to be separated.
   :type vert: :class:`bmesh.types.BMVert`
   :arg edges: The edges to separated.
   :type edges: :class:`bmesh.types.BMEdge`
   :return: The newly separated verts (including the vertex passed).
   :rtype: tuple[:class:`bmesh.types.BMVert`, ...]


    Online Documentation:
    https://docs.blender.org/api/current/bmesh.utils.html"""
    ...

def vert_splice(*args, **kwargs) -> Any:
    """.. method:: vert_splice(vert, vert_target)

   Splice vert into vert_target.

   :arg vert: The vertex to be removed.
   :type vert: :class:`bmesh.types.BMVert`
   :arg vert_target: The vertex to use.
   :type vert_target: :class:`bmesh.types.BMVert`

   .. note:: The verts mustn't share an edge or face.


    Online Documentation:
    https://docs.blender.org/api/current/bmesh.utils.html"""
    ...
