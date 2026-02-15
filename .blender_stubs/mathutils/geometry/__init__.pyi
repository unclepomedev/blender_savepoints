# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/mathutils.geometry.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated


def area_tri(*args, **kwargs) -> Any:
    """.. function:: area_tri(v1, v2, v3, /)

   Returns the area size of the 2D or 3D triangle defined.

   :arg v1: Point1
   :type v1: :class:`mathutils.Vector`
   :arg v2: Point2
   :type v2: :class:`mathutils.Vector`
   :arg v3: Point3
   :type v3: :class:`mathutils.Vector`
   :rtype: float


    Online Documentation:
    https://docs.blender.org/api/current/mathutils.geometry.html"""
    ...

def barycentric_transform(*args, **kwargs) -> Any:
    """.. function:: barycentric_transform(point, tri_a1, tri_a2, tri_a3, tri_b1, tri_b2, tri_b3, /)

   Return a transformed point, the transformation is defined by 2 triangles.

   :arg point: The point to transform.
   :type point: :class:`mathutils.Vector`
   :arg tri_a1: source triangle vertex.
   :type tri_a1: :class:`mathutils.Vector`
   :arg tri_a2: source triangle vertex.
   :type tri_a2: :class:`mathutils.Vector`
   :arg tri_a3: source triangle vertex.
   :type tri_a3: :class:`mathutils.Vector`
   :arg tri_b1: target triangle vertex.
   :type tri_b1: :class:`mathutils.Vector`
   :arg tri_b2: target triangle vertex.
   :type tri_b2: :class:`mathutils.Vector`
   :arg tri_b3: target triangle vertex.
   :type tri_b3: :class:`mathutils.Vector`
   :return: The transformed point
   :rtype: :class:`mathutils.Vector`


    Online Documentation:
    https://docs.blender.org/api/current/mathutils.geometry.html"""
    ...

def box_fit_2d(*args, **kwargs) -> Any:
    """.. function:: box_fit_2d(points, /)

   Returns an angle that best fits the points to an axis aligned rectangle

   :arg points: Sequence of 2D points.
   :type points: Sequence[Sequence[float]]
   :return: angle
   :rtype: float


    Online Documentation:
    https://docs.blender.org/api/current/mathutils.geometry.html"""
    ...

def box_pack_2d(*args, **kwargs) -> Any:
    """.. function:: box_pack_2d(boxes, /)

   Returns a tuple with the width and height of the packed bounding box.

   :arg boxes: list of boxes, each box is a list where the first 4 items are [X, Y, width, height, ...] other items are ignored. The X & Y values in this list are modified to set the packed positions.
   :type boxes: list[list[float]]
   :return: The width and height of the packed bounding box.
   :rtype: tuple[float, float]


    Online Documentation:
    https://docs.blender.org/api/current/mathutils.geometry.html"""
    ...

def closest_point_on_tri(*args, **kwargs) -> Any:
    """.. function:: closest_point_on_tri(pt, tri_p1, tri_p2, tri_p3, /)

   Takes 4 vectors: one is the point and the next 3 define the triangle.

   :arg pt: Point
   :type pt: :class:`mathutils.Vector`
   :arg tri_p1: First point of the triangle
   :type tri_p1: :class:`mathutils.Vector`
   :arg tri_p2: Second point of the triangle
   :type tri_p2: :class:`mathutils.Vector`
   :arg tri_p3: Third point of the triangle
   :type tri_p3: :class:`mathutils.Vector`
   :return: The closest point of the triangle.
   :rtype: :class:`mathutils.Vector`


    Online Documentation:
    https://docs.blender.org/api/current/mathutils.geometry.html"""
    ...

def convex_hull_2d(*args, **kwargs) -> Any:
    """.. function:: convex_hull_2d(points)

   Returns a list of indices into the list given

   :arg points: Sequence of 2D points.
   :type points: Sequence[Sequence[float]]
   :return: a list of indices
   :rtype: list[int]


    Online Documentation:
    https://docs.blender.org/api/current/mathutils.geometry.html"""
    ...

def delaunay_2d_cdt(*args, **kwargs) -> Any:
    """.. function:: delaunay_2d_cdt(vert_coords, edges, faces, output_type, epsilon, need_ids=True, /)

   Computes the Constrained Delaunay Triangulation of a set of vertices,
   with edges and faces that must appear in the triangulation.
   Some triangles may be eaten away, or combined with other triangles,
   according to output type.
   The returned verts may be in a different order from input verts, may be moved
   slightly, and may be merged with other nearby verts.
   The three returned orig lists give, for each of verts, edges, and faces, the list of
   input element indices corresponding to the positionally same output element.
   For edges, the orig indices start with the input edges and then continue
   with the edges implied by each of the faces (n of them for an n-gon).
   If the need_ids argument is supplied, and False, then the code skips the preparation
   of the orig arrays, which may save some time.

   :arg vert_coords: Vertex coordinates (2d)
   :type vert_coords: Sequence[:class:`mathutils.Vector`]
   :arg edges: Edges, as pairs of indices in ``vert_coords``
   :type edges: Sequence[Sequence[int, int]]
   :arg faces: Faces, each sublist is a face, as indices in ``vert_coords`` (CCW oriented).
   :type faces: Sequence[Sequence[int]]
   :arg output_type: What output looks like. 0 => triangles with convex hull. 1 => triangles inside constraints. 2 => the input constraints, intersected. 3 => like 2 but detect holes and omit them from output. 4 => like 2 but with extra edges to make valid BMesh faces. 5 => like 4 but detect holes and omit them from output.
   :type output_type: int
   :arg epsilon: For nearness tests; should not be zero
   :type epsilon: float
   :arg need_ids: are the orig output arrays needed?
   :type need_ids: bool
   :return: Output tuple, (vert_coords, edges, faces, orig_verts, orig_edges, orig_faces)
   :rtype: tuple[list[:class:`mathutils.Vector`], list[tuple[int, int]], list[list[int]], list[list[int]], list[list[int]], list[list[int]]]


    Online Documentation:
    https://docs.blender.org/api/current/mathutils.geometry.html"""
    ...

def distance_point_to_plane(*args, **kwargs) -> Any:
    """.. function:: distance_point_to_plane(pt, plane_co, plane_no, /)

   Returns the signed distance between a point and a plane    (negative when below the normal).

   :arg pt: Point
   :type pt: :class:`mathutils.Vector`
   :arg plane_co: A point on the plane
   :type plane_co: :class:`mathutils.Vector`
   :arg plane_no: The direction the plane is facing
   :type plane_no: :class:`mathutils.Vector`
   :rtype: float


    Online Documentation:
    https://docs.blender.org/api/current/mathutils.geometry.html"""
    ...

def interpolate_bezier(*args, **kwargs) -> Any:
    """.. function:: interpolate_bezier(knot1, handle1, handle2, knot2, resolution, /)

   Interpolate a bezier spline segment.

   :arg knot1: First bezier spline point.
   :type knot1: :class:`mathutils.Vector`
   :arg handle1: First bezier spline handle.
   :type handle1: :class:`mathutils.Vector`
   :arg handle2: Second bezier spline handle.
   :type handle2: :class:`mathutils.Vector`
   :arg knot2: Second bezier spline point.
   :type knot2: :class:`mathutils.Vector`
   :arg resolution: Number of points to return.
   :type resolution: int
   :return: The interpolated points.
   :rtype: list[:class:`mathutils.Vector`]


    Online Documentation:
    https://docs.blender.org/api/current/mathutils.geometry.html"""
    ...

def intersect_line_line(*args, **kwargs) -> Any:
    """.. function:: intersect_line_line(v1, v2, v3, v4, /)

   Returns a tuple with the points on each line respectively closest to the other.

   :arg v1: First point of the first line
   :type v1: :class:`mathutils.Vector`
   :arg v2: Second point of the first line
   :type v2: :class:`mathutils.Vector`
   :arg v3: First point of the second line
   :type v3: :class:`mathutils.Vector`
   :arg v4: Second point of the second line
   :type v4: :class:`mathutils.Vector`
   :return: The intersection on each line or None when the lines are co-linear.
   :rtype: tuple[:class:`mathutils.Vector`, :class:`mathutils.Vector`] | None


    Online Documentation:
    https://docs.blender.org/api/current/mathutils.geometry.html"""
    ...

def intersect_line_line_2d(*args, **kwargs) -> Any:
    """.. function:: intersect_line_line_2d(lineA_p1, lineA_p2, lineB_p1, lineB_p2, /)

   Takes 2 segments (defined by 4 vectors) and returns a vector for their point of intersection or None.

   .. warning:: Despite its name, this function works on segments, and not on lines.

   :arg lineA_p1: First point of the first line
   :type lineA_p1: :class:`mathutils.Vector`
   :arg lineA_p2: Second point of the first line
   :type lineA_p2: :class:`mathutils.Vector`
   :arg lineB_p1: First point of the second line
   :type lineB_p1: :class:`mathutils.Vector`
   :arg lineB_p2: Second point of the second line
   :type lineB_p2: :class:`mathutils.Vector`
   :return: The point of intersection or None when not found
   :rtype: :class:`mathutils.Vector` | None


    Online Documentation:
    https://docs.blender.org/api/current/mathutils.geometry.html"""
    ...

def intersect_line_plane(*args, **kwargs) -> Any:
    """.. function:: intersect_line_plane(line_a, line_b, plane_co, plane_no, no_flip=False, /)

   Calculate the intersection between a line (as 2 vectors) and a plane.
   Returns a vector for the intersection or None.

   :arg line_a: First point of the first line
   :type line_a: :class:`mathutils.Vector`
   :arg line_b: Second point of the first line
   :type line_b: :class:`mathutils.Vector`
   :arg plane_co: A point on the plane
   :type plane_co: :class:`mathutils.Vector`
   :arg plane_no: The direction the plane is facing
   :type plane_no: :class:`mathutils.Vector`
   :arg no_flip: Not implemented
   :type no_flip: bool
   :return: The point of intersection or None when not found
   :rtype: :class:`mathutils.Vector` | None


    Online Documentation:
    https://docs.blender.org/api/current/mathutils.geometry.html"""
    ...

def intersect_line_sphere(*args, **kwargs) -> Any:
    """.. function:: intersect_line_sphere(line_a, line_b, sphere_co, sphere_radius, clip=True, /)

   Takes a line (as 2 points) and a sphere (as a point and a radius) and
   returns the intersection

   :arg line_a: First point of the line
   :type line_a: :class:`mathutils.Vector`
   :arg line_b: Second point of the line
   :type line_b: :class:`mathutils.Vector`
   :arg sphere_co: The center of the sphere
   :type sphere_co: :class:`mathutils.Vector`
   :arg sphere_radius: Radius of the sphere
   :type sphere_radius: float
   :arg clip: When False, don't restrict the intersection to the area of the sphere.
   :type clip: bool
   :return: The intersection points as a pair of vectors or None when there is no intersection
   :rtype: tuple[:class:`mathutils.Vector` | None, :class:`mathutils.Vector` | None]


    Online Documentation:
    https://docs.blender.org/api/current/mathutils.geometry.html"""
    ...

def intersect_line_sphere_2d(*args, **kwargs) -> Any:
    """.. function:: intersect_line_sphere_2d(line_a, line_b, sphere_co, sphere_radius, clip=True, /)

   Takes a line (as 2 points) and a sphere (as a point and a radius) and
   returns the intersection

   :arg line_a: First point of the line
   :type line_a: :class:`mathutils.Vector`
   :arg line_b: Second point of the line
   :type line_b: :class:`mathutils.Vector`
   :arg sphere_co: The center of the sphere
   :type sphere_co: :class:`mathutils.Vector`
   :arg sphere_radius: Radius of the sphere
   :type sphere_radius: float
   :arg clip: When False, don't restrict the intersection to the area of the sphere.
   :type clip: bool
   :return: The intersection points as a pair of vectors or None when there is no intersection
   :rtype: tuple[:class:`mathutils.Vector` | None, :class:`mathutils.Vector` | None]


    Online Documentation:
    https://docs.blender.org/api/current/mathutils.geometry.html"""
    ...

def intersect_plane_plane(*args, **kwargs) -> Any:
    """.. function:: intersect_plane_plane(plane_a_co, plane_a_no, plane_b_co, plane_b_no, /)

   Return the intersection between two planes

   :arg plane_a_co: Point on the first plane
   :type plane_a_co: :class:`mathutils.Vector`
   :arg plane_a_no: Normal of the first plane
   :type plane_a_no: :class:`mathutils.Vector`
   :arg plane_b_co: Point on the second plane
   :type plane_b_co: :class:`mathutils.Vector`
   :arg plane_b_no: Normal of the second plane
   :type plane_b_no: :class:`mathutils.Vector`
   :return: The line of the intersection represented as a point and a vector or None if the intersection can't be calculated
   :rtype: tuple[:class:`mathutils.Vector`, :class:`mathutils.Vector`] | tuple[None, None]


    Online Documentation:
    https://docs.blender.org/api/current/mathutils.geometry.html"""
    ...

def intersect_point_line(*args, **kwargs) -> Any:
    """.. function:: intersect_point_line(pt, line_p1, line_p2, /)

   Takes a point and a line and returns the closest point on the line and its distance from the first point of the line as a percentage of the length of the line.

   :arg pt: Point
   :type pt: :class:`mathutils.Vector`
   :arg line_p1: First point of the line
   :type line_p1: :class:`mathutils.Vector`
   :arg line_p2: Second point of the line
   :type line_p2: :class:`mathutils.Vector`
   :rtype: tuple[:class:`mathutils.Vector`, float]


    Online Documentation:
    https://docs.blender.org/api/current/mathutils.geometry.html"""
    ...

def intersect_point_line_segment(*args, **kwargs) -> Any:
    """.. function:: intersect_point_line_segment(pt, seg_p1, seg_p2, /)

   Takes a point and a segment and returns the closest point on the segment and the distance to the segment.

   :arg pt: Point
   :type pt: :class:`mathutils.Vector`
   :arg seg_p1: First point of the segment
   :type seg_p1: :class:`mathutils.Vector`
   :arg seg_p2: Second point of the segment
   :type seg_p2: :class:`mathutils.Vector`
   :rtype: tuple[:class:`mathutils.Vector`, float]


    Online Documentation:
    https://docs.blender.org/api/current/mathutils.geometry.html"""
    ...

def intersect_point_quad_2d(*args, **kwargs) -> Any:
    """.. function:: intersect_point_quad_2d(pt, quad_p1, quad_p2, quad_p3, quad_p4, /)

   Takes 5 vectors (using only the x and y coordinates): one is the point and the next 4 define the quad,
   only the x and y are used from the vectors. Returns 1 if the point is within the quad, otherwise 0.
   Works only with convex quads without singular edges.

   :arg pt: Point
   :type pt: :class:`mathutils.Vector`
   :arg quad_p1: First point of the quad
   :type quad_p1: :class:`mathutils.Vector`
   :arg quad_p2: Second point of the quad
   :type quad_p2: :class:`mathutils.Vector`
   :arg quad_p3: Third point of the quad
   :type quad_p3: :class:`mathutils.Vector`
   :arg quad_p4: Fourth point of the quad
   :type quad_p4: :class:`mathutils.Vector`
   :rtype: int


    Online Documentation:
    https://docs.blender.org/api/current/mathutils.geometry.html"""
    ...

def intersect_point_tri(*args, **kwargs) -> Any:
    """.. function:: intersect_point_tri(pt, tri_p1, tri_p2, tri_p3, /)

   Takes 4 vectors: one is the point and the next 3 define the triangle. Projects the point onto the triangle plane and checks if it is within the triangle.

   :arg pt: Point
   :type pt: :class:`mathutils.Vector`
   :arg tri_p1: First point of the triangle
   :type tri_p1: :class:`mathutils.Vector`
   :arg tri_p2: Second point of the triangle
   :type tri_p2: :class:`mathutils.Vector`
   :arg tri_p3: Third point of the triangle
   :type tri_p3: :class:`mathutils.Vector`
   :return: Point on the triangles plane or None if its outside the triangle
   :rtype: :class:`mathutils.Vector` | None


    Online Documentation:
    https://docs.blender.org/api/current/mathutils.geometry.html"""
    ...

def intersect_point_tri_2d(*args, **kwargs) -> Any:
    """.. function:: intersect_point_tri_2d(pt, tri_p1, tri_p2, tri_p3, /)

   Takes 4 vectors (using only the x and y coordinates): one is the point and the next 3 define the triangle. Returns 1 if the point is within the triangle, otherwise 0.

   :arg pt: Point
   :type pt: :class:`mathutils.Vector`
   :arg tri_p1: First point of the triangle
   :type tri_p1: :class:`mathutils.Vector`
   :arg tri_p2: Second point of the triangle
   :type tri_p2: :class:`mathutils.Vector`
   :arg tri_p3: Third point of the triangle
   :type tri_p3: :class:`mathutils.Vector`
   :rtype: int


    Online Documentation:
    https://docs.blender.org/api/current/mathutils.geometry.html"""
    ...

def intersect_ray_tri(*args, **kwargs) -> Any:
    """.. function:: intersect_ray_tri(v1, v2, v3, ray, orig, clip=True, /)

   Returns the intersection between a ray and a triangle, if possible, returns None otherwise.

   :arg v1: Point1
   :type v1: :class:`mathutils.Vector`
   :arg v2: Point2
   :type v2: :class:`mathutils.Vector`
   :arg v3: Point3
   :type v3: :class:`mathutils.Vector`
   :arg ray: Direction of the projection
   :type ray: :class:`mathutils.Vector`
   :arg orig: Origin
   :type orig: :class:`mathutils.Vector`
   :arg clip: When False, don't restrict the intersection to the area of the triangle, use the infinite plane defined by the triangle.
   :type clip: bool
   :return: The point of intersection or None if no intersection is found
   :rtype: :class:`mathutils.Vector` | None


    Online Documentation:
    https://docs.blender.org/api/current/mathutils.geometry.html"""
    ...

def intersect_sphere_sphere_2d(*args, **kwargs) -> Any:
    """.. function:: intersect_sphere_sphere_2d(p_a, radius_a, p_b, radius_b, /)

   Returns 2 points on between intersecting circles.

   :arg p_a: Center of the first circle
   :type p_a: :class:`mathutils.Vector`
   :arg radius_a: Radius of the first circle
   :type radius_a: float
   :arg p_b: Center of the second circle
   :type p_b: :class:`mathutils.Vector`
   :arg radius_b: Radius of the second circle
   :type radius_b: float
   :return: 2 points on between intersecting circles or None when there is no intersection.
   :rtype: tuple[:class:`mathutils.Vector`, :class:`mathutils.Vector`] | tuple[None, None]


    Online Documentation:
    https://docs.blender.org/api/current/mathutils.geometry.html"""
    ...

def intersect_tri_tri_2d(*args, **kwargs) -> Any:
    """.. function:: intersect_tri_tri_2d(tri_a1, tri_a2, tri_a3, tri_b1, tri_b2, tri_b3, /)

   Check if two 2D triangles intersect.

   :rtype: bool


    Online Documentation:
    https://docs.blender.org/api/current/mathutils.geometry.html"""
    ...

def normal(*args, **kwargs) -> Any:
    """.. function:: normal(*vectors)

   Returns the normal of a 3D polygon.

   :arg vectors: 3 or more vectors to calculate normals.
   :type vectors: Sequence[Sequence[float]]
   :rtype: :class:`mathutils.Vector`


    Online Documentation:
    https://docs.blender.org/api/current/mathutils.geometry.html"""
    ...

def points_in_planes(*args, **kwargs) -> Any:
    """.. function:: points_in_planes(planes, epsilon_coplanar=1e-4, epsilon_isect=1e-6, /)

   Returns a list of points inside all planes given and a list of index values for the planes used.

   :arg planes: List of planes (4D vectors).
   :type planes: list[:class:`mathutils.Vector`]
   :arg epsilon_coplanar: Epsilon value for interpreting plane pairs as co-plannar.
   :type epsilon_coplanar: float
   :arg epsilon_isect: Epsilon value for intersection.
   :type epsilon_isect: float
   :return: Two lists, once containing the 3D coordinates inside the planes, another containing the plane indices used.
   :rtype: tuple[list[:class:`mathutils.Vector`], list[int]]


    Online Documentation:
    https://docs.blender.org/api/current/mathutils.geometry.html"""
    ...

def tessellate_polygon(*args, **kwargs) -> Any:
    """.. function:: tessellate_polygon(polylines, /)

   Takes a list of polylines (each point a pair or triplet of numbers) and returns the point indices for a polyline filled with triangles. Does not handle degenerate geometry (such as zero-length lines due to consecutive identical points).

   :arg polylines: Polygons where each polygon is a sequence of 2D or 3D points.
   :type polylines: Sequence[Sequence[Sequence[float]]]   :return: A list of triangles.
   :rtype: list[tuple[int, int, int]]


    Online Documentation:
    https://docs.blender.org/api/current/mathutils.geometry.html"""
    ...

def volume_tetrahedron(*args, **kwargs) -> Any:
    """.. function:: volume_tetrahedron(v1, v2, v3, v4, /)

   Return the volume formed by a tetrahedron (points can be in any order).

   :arg v1: Point1
   :type v1: :class:`mathutils.Vector`
   :arg v2: Point2
   :type v2: :class:`mathutils.Vector`
   :arg v3: Point3
   :type v3: :class:`mathutils.Vector`
   :arg v4: Point4
   :type v4: :class:`mathutils.Vector`
   :rtype: float


    Online Documentation:
    https://docs.blender.org/api/current/mathutils.geometry.html"""
    ...
