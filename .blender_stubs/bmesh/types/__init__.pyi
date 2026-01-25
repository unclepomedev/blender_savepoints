"""
Online Documentation:
https://docs.blender.org/api/current/bmesh.types.html
"""

# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


import sys
import typing
from typing import Any, Union, Callable, Iterator

class BMDeformVert:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bmesh.types.html
    """
    def __init__(self, /, *args, **kwargs) -> Any: ...
    def clear(*args, **kwargs) -> Any: ...
    def get(*args, **kwargs) -> Any: ...
    def items(*args, **kwargs) -> Any: ...
    def keys(*args, **kwargs) -> Any: ...
    def values(*args, **kwargs) -> Any: ...

class BMEdge:
    """The BMesh edge connecting 2 verts
"""
    """
    Online Documentation:
    https://docs.blender.org/api/current/bmesh.types.html
    """
    def __init__(self, /, *args, **kwargs) -> Any: ...
    def calc_face_angle(*args, **kwargs) -> Any: ...
    def calc_face_angle_signed(*args, **kwargs) -> Any: ...
    def calc_length(*args, **kwargs) -> Any: ...
    def calc_tangent(*args, **kwargs) -> Any: ...
    def copy_from(*args, **kwargs) -> Any: ...
    hide: Any
    def hide_set(*args, **kwargs) -> Any: ...
    index: Any
    is_boundary: Any
    is_contiguous: Any
    is_convex: Any
    is_manifold: Any
    is_valid: Any
    is_wire: Any
    link_faces: Any
    link_loops: Any
    def normal_update(*args, **kwargs) -> Any: ...
    def other_vert(*args, **kwargs) -> Any: ...
    seam: Any
    select: Any
    def select_set(*args, **kwargs) -> Any: ...
    smooth: Any
    tag: Any
    verts: Any

class BMEdgeSeq:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bmesh.types.html
    """
    def __init__(self, /, *args, **kwargs) -> Any: ...
    def ensure_lookup_table(*args, **kwargs) -> Any: ...
    def get(*args, **kwargs) -> Any: ...
    def index_update(*args, **kwargs) -> Any: ...
    layers: Any
    def new(*args, **kwargs) -> Any: ...
    def remove(*args, **kwargs) -> Any: ...
    def sort(*args, **kwargs) -> Any: ...

class BMEditSelIter:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bmesh.types.html
    """
    def __init__(self, /, *args, **kwargs) -> Any: ...

class BMEditSelSeq:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bmesh.types.html
    """
    def __init__(self, /, *args, **kwargs) -> Any: ...
    active: Any
    def add(*args, **kwargs) -> Any: ...
    def clear(*args, **kwargs) -> Any: ...
    def discard(*args, **kwargs) -> Any: ...
    def remove(*args, **kwargs) -> Any: ...
    def validate(*args, **kwargs) -> Any: ...

class BMElemSeq:
    """General sequence type used for accessing any sequence of
:class:`bmesh.types.BMVert`, :class:`bmesh.types.BMEdge`, :class:`bmesh.types.BMFace`, :class:`bmesh.types.BMLoop`.

When accessed via :class:`bmesh.types.BMesh.verts`, :class:`bmesh.types.BMesh.edges`, :class:`bmesh.types.BMesh.faces`
there are also functions to create/remove items.
"""
    """
    Online Documentation:
    https://docs.blender.org/api/current/bmesh.types.html
    """
    def __init__(self, /, *args, **kwargs) -> Any: ...
    def index_update(*args, **kwargs) -> Any: ...

class BMFace:
    """The BMesh face with 3 or more sides
"""
    """
    Online Documentation:
    https://docs.blender.org/api/current/bmesh.types.html
    """
    def __init__(self, /, *args, **kwargs) -> Any: ...
    def calc_area(*args, **kwargs) -> Any: ...
    def calc_center_bounds(*args, **kwargs) -> Any: ...
    def calc_center_median(*args, **kwargs) -> Any: ...
    def calc_center_median_weighted(*args, **kwargs) -> Any: ...
    def calc_perimeter(*args, **kwargs) -> Any: ...
    def calc_tangent_edge(*args, **kwargs) -> Any: ...
    def calc_tangent_edge_diagonal(*args, **kwargs) -> Any: ...
    def calc_tangent_edge_pair(*args, **kwargs) -> Any: ...
    def calc_tangent_vert_diagonal(*args, **kwargs) -> Any: ...
    def copy(*args, **kwargs) -> Any: ...
    def copy_from(*args, **kwargs) -> Any: ...
    def copy_from_face_interp(*args, **kwargs) -> Any: ...
    edges: Any
    hide: Any
    def hide_set(*args, **kwargs) -> Any: ...
    index: Any
    is_valid: Any
    loops: Any
    material_index: Any
    normal: Any
    def normal_flip(*args, **kwargs) -> Any: ...
    def normal_update(*args, **kwargs) -> Any: ...
    select: Any
    def select_set(*args, **kwargs) -> Any: ...
    smooth: Any
    tag: Any
    uv_select: Any
    def uv_select_set(*args, **kwargs) -> Any: ...
    verts: Any

class BMFaceSeq:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bmesh.types.html
    """
    def __init__(self, /, *args, **kwargs) -> Any: ...
    active: Any
    def ensure_lookup_table(*args, **kwargs) -> Any: ...
    def get(*args, **kwargs) -> Any: ...
    def index_update(*args, **kwargs) -> Any: ...
    layers: Any
    def new(*args, **kwargs) -> Any: ...
    def remove(*args, **kwargs) -> Any: ...
    def sort(*args, **kwargs) -> Any: ...

class BMIter:
    """Internal BMesh type for looping over verts/faces/edges,
used for iterating over :class:`bmesh.types.BMElemSeq` types.
"""
    """
    Online Documentation:
    https://docs.blender.org/api/current/bmesh.types.html
    """
    def __init__(self, /, *args, **kwargs) -> Any: ...

class BMLayerAccessEdge:
    """Exposes custom-data layer attributes.
"""
    """
    Online Documentation:
    https://docs.blender.org/api/current/bmesh.types.html
    """
    def __init__(self, /, *args, **kwargs) -> Any: ...
    bool: Any
    color: Any
    float: Any
    float_color: Any
    float_vector: Any
    int: Any
    string: Any

class BMLayerAccessFace:
    """Exposes custom-data layer attributes.
"""
    """
    Online Documentation:
    https://docs.blender.org/api/current/bmesh.types.html
    """
    def __init__(self, /, *args, **kwargs) -> Any: ...
    bool: Any
    color: Any
    float: Any
    float_color: Any
    float_vector: Any
    int: Any
    string: Any

class BMLayerAccessLoop:
    """Exposes custom-data layer attributes.
"""
    """
    Online Documentation:
    https://docs.blender.org/api/current/bmesh.types.html
    """
    def __init__(self, /, *args, **kwargs) -> Any: ...
    bool: Any
    color: Any
    float: Any
    float_color: Any
    float_vector: Any
    int: Any
    string: Any
    uv: Any

class BMLayerAccessVert:
    """Exposes custom-data layer attributes.
"""
    """
    Online Documentation:
    https://docs.blender.org/api/current/bmesh.types.html
    """
    def __init__(self, /, *args, **kwargs) -> Any: ...
    bool: Any
    color: Any
    deform: Any
    float: Any
    float_color: Any
    float_vector: Any
    int: Any
    shape: Any
    skin: Any
    string: Any

class BMLayerCollection:
    """Gives access to a collection of custom-data layers of the same type and behaves like Python dictionaries, except for the ability to do list like index access.
"""
    """
    Online Documentation:
    https://docs.blender.org/api/current/bmesh.types.html
    """
    def __init__(self, /, *args, **kwargs) -> Any: ...
    active: Any
    def get(*args, **kwargs) -> Any: ...
    is_singleton: Any
    def items(*args, **kwargs) -> Any: ...
    def keys(*args, **kwargs) -> Any: ...
    def new(*args, **kwargs) -> Any: ...
    def remove(*args, **kwargs) -> Any: ...
    def values(*args, **kwargs) -> Any: ...
    def verify(*args, **kwargs) -> Any: ...

class BMLayerItem:
    """Exposes a single custom data layer, their main purpose is for use as item accessors to custom-data when used with vert/edge/face/loop data.
"""
    """
    Online Documentation:
    https://docs.blender.org/api/current/bmesh.types.html
    """
    def __init__(self, /, *args, **kwargs) -> Any: ...
    def copy_from(*args, **kwargs) -> Any: ...
    name: Any

class BMLoop:
    """This is normally accessed from :class:`bmesh.types.BMFace.loops` where each face loop represents a corner of the face.
"""
    """
    Online Documentation:
    https://docs.blender.org/api/current/bmesh.types.html
    """
    def __init__(self, /, *args, **kwargs) -> Any: ...
    def calc_angle(*args, **kwargs) -> Any: ...
    def calc_normal(*args, **kwargs) -> Any: ...
    def calc_tangent(*args, **kwargs) -> Any: ...
    def copy_from(*args, **kwargs) -> Any: ...
    def copy_from_face_interp(*args, **kwargs) -> Any: ...
    edge: Any
    face: Any
    index: Any
    is_convex: Any
    is_valid: Any
    link_loop_next: Any
    link_loop_prev: Any
    link_loop_radial_next: Any
    link_loop_radial_prev: Any
    link_loops: Any
    tag: Any
    uv_select_edge: Any
    def uv_select_edge_set(*args, **kwargs) -> Any: ...
    uv_select_vert: Any
    def uv_select_vert_set(*args, **kwargs) -> Any: ...
    vert: Any

class BMLoopSeq:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bmesh.types.html
    """
    def __init__(self, /, *args, **kwargs) -> Any: ...
    layers: Any

class BMLoopUV:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bmesh.types.html
    """
    def __init__(self, /, *args, **kwargs) -> Any: ...
    pin_uv: Any
    uv: Any

class BMVert:
    """The BMesh vertex type
"""
    """
    Online Documentation:
    https://docs.blender.org/api/current/bmesh.types.html
    """
    def __init__(self, /, *args, **kwargs) -> Any: ...
    def calc_edge_angle(*args, **kwargs) -> Any: ...
    def calc_shell_factor(*args, **kwargs) -> Any: ...
    co: Any
    def copy_from(*args, **kwargs) -> Any: ...
    def copy_from_face_interp(*args, **kwargs) -> Any: ...
    def copy_from_vert_interp(*args, **kwargs) -> Any: ...
    hide: Any
    def hide_set(*args, **kwargs) -> Any: ...
    index: Any
    is_boundary: Any
    is_manifold: Any
    is_valid: Any
    is_wire: Any
    link_edges: Any
    link_faces: Any
    link_loops: Any
    normal: Any
    def normal_update(*args, **kwargs) -> Any: ...
    select: Any
    def select_set(*args, **kwargs) -> Any: ...
    tag: Any

class BMVertSeq:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bmesh.types.html
    """
    def __init__(self, /, *args, **kwargs) -> Any: ...
    def ensure_lookup_table(*args, **kwargs) -> Any: ...
    def index_update(*args, **kwargs) -> Any: ...
    layers: Any
    def new(*args, **kwargs) -> Any: ...
    def remove(*args, **kwargs) -> Any: ...
    def sort(*args, **kwargs) -> Any: ...

class BMesh:
    """The BMesh data structure
"""
    """
    Online Documentation:
    https://docs.blender.org/api/current/bmesh.types.html
    """
    def __init__(self, /, *args, **kwargs) -> Any: ...
    def calc_loop_triangles(*args, **kwargs) -> Any: ...
    def calc_volume(*args, **kwargs) -> Any: ...
    def clear(*args, **kwargs) -> Any: ...
    def copy(*args, **kwargs) -> Any: ...
    edges: Any
    faces: Any
    def free(*args, **kwargs) -> Any: ...
    def from_mesh(*args, **kwargs) -> Any: ...
    def from_object(*args, **kwargs) -> Any: ...
    is_valid: Any
    is_wrapped: Any
    loops: Any
    def normal_update(*args, **kwargs) -> Any: ...
    def select_flush(*args, **kwargs) -> Any: ...
    def select_flush_mode(*args, **kwargs) -> Any: ...
    select_history: Any
    select_mode: Any
    def to_mesh(*args, **kwargs) -> Any: ...
    def transform(*args, **kwargs) -> Any: ...
    def uv_select_flush(*args, **kwargs) -> Any: ...
    def uv_select_flush_mode(*args, **kwargs) -> Any: ...
    def uv_select_flush_shared(*args, **kwargs) -> Any: ...
    def uv_select_foreach_set(*args, **kwargs) -> Any: ...
    def uv_select_foreach_set_from_mesh(*args, **kwargs) -> Any: ...
    def uv_select_sync_from_mesh(*args, **kwargs) -> Any: ...
    def uv_select_sync_to_mesh(*args, **kwargs) -> Any: ...
    uv_select_sync_valid: Any
    verts: Any
