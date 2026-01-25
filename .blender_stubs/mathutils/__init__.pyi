"""
Online Documentation:
https://docs.blender.org/api/current/mathutils.html
"""

# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


import sys
import typing
from typing import Any, Union, Callable, Iterator

class Color:
    """.. class:: Color(rgb=(0.0, 0.0, 0.0), /)

   This object gives access to Colors in Blender.

   Most colors returned by Blender APIs are in scene linear color space, as defined by    the OpenColorIO configuration. The notable exception is user interface theming colors,    which are in sRGB color space.

   :arg rgb: (red, green, blue) color values where (0, 0, 0) is black & (1, 1, 1) is white.
   :type rgb: Sequence[float]
"""
    """
    Online Documentation:
    https://docs.blender.org/api/current/mathutils.html
    """
    def __init__(self, /, *args, **kwargs) -> Any: ...
    b: Any
    def copy(*args, **kwargs) -> Any: ...
    def freeze(*args, **kwargs) -> Any: ...
    def from_aces_to_scene_linear(*args, **kwargs) -> Any: ...
    def from_acescg_to_scene_linear(*args, **kwargs) -> Any: ...
    def from_rec2020_linear_to_scene_linear(*args, **kwargs) -> Any: ...
    def from_rec709_linear_to_scene_linear(*args, **kwargs) -> Any: ...
    def from_scene_linear_to_aces(*args, **kwargs) -> Any: ...
    def from_scene_linear_to_acescg(*args, **kwargs) -> Any: ...
    def from_scene_linear_to_rec2020_linear(*args, **kwargs) -> Any: ...
    def from_scene_linear_to_rec709_linear(*args, **kwargs) -> Any: ...
    def from_scene_linear_to_srgb(*args, **kwargs) -> Any: ...
    def from_scene_linear_to_xyz_d65(*args, **kwargs) -> Any: ...
    def from_srgb_to_scene_linear(*args, **kwargs) -> Any: ...
    def from_xyz_d65_to_scene_linear(*args, **kwargs) -> Any: ...
    g: Any
    h: Any
    hsv: Any
    is_frozen: Any
    is_valid: Any
    is_wrapped: Any
    owner: Any
    r: Any
    s: Any
    v: Any

class Euler:
    """.. class:: Euler(angles=(0.0, 0.0, 0.0), order='XYZ', /)

   This object gives access to Eulers in Blender.

   .. seealso:: `Euler angles <https://en.wikipedia.org/wiki/Euler_angles>`__ on Wikipedia.

   :arg angles: (X, Y, Z) angles in radians.
   :type angles: Sequence[float]
   :arg order: Euler rotation order.
   :type order: Literal['XYZ', 'XZY', 'YXZ', 'YZX', 'ZXY', 'ZYX']
"""
    """
    Online Documentation:
    https://docs.blender.org/api/current/mathutils.html
    """
    def __init__(self, /, *args, **kwargs) -> Any: ...
    def copy(*args, **kwargs) -> Any: ...
    def freeze(*args, **kwargs) -> Any: ...
    is_frozen: Any
    is_valid: Any
    is_wrapped: Any
    def make_compatible(*args, **kwargs) -> Any: ...
    order: Any
    owner: Any
    def rotate(*args, **kwargs) -> Any: ...
    def rotate_axis(*args, **kwargs) -> Any: ...
    def to_matrix(*args, **kwargs) -> Any: ...
    def to_quaternion(*args, **kwargs) -> Any: ...
    x: Any
    y: Any
    z: Any
    def zero(*args, **kwargs) -> Any: ...

class Matrix:
    """.. class:: Matrix(rows=Matrix.Identity(4), /)

   This object gives access to Matrices in Blender, supporting square and rectangular
   matrices from 2x2 up to 4x4.

   :arg rows: Sequence of rows.
   :type rows: Sequence[Sequence[float]]
"""
    """
    Online Documentation:
    https://docs.blender.org/api/current/mathutils.html
    """
    def Diagonal(*args, **kwargs) -> Any: ...
    def Identity(*args, **kwargs) -> Any: ...
    def LocRotScale(*args, **kwargs) -> Any: ...
    def OrthoProjection(*args, **kwargs) -> Any: ...
    def Rotation(*args, **kwargs) -> Any: ...
    def Scale(*args, **kwargs) -> Any: ...
    def Shear(*args, **kwargs) -> Any: ...
    def Translation(*args, **kwargs) -> Any: ...
    def __init__(self, /, *args, **kwargs) -> Any: ...
    def adjugate(*args, **kwargs) -> Any: ...
    def adjugated(*args, **kwargs) -> Any: ...
    col: Any
    def copy(*args, **kwargs) -> Any: ...
    def decompose(*args, **kwargs) -> Any: ...
    def determinant(*args, **kwargs) -> Any: ...
    def freeze(*args, **kwargs) -> Any: ...
    def identity(*args, **kwargs) -> Any: ...
    def invert(*args, **kwargs) -> Any: ...
    def invert_safe(*args, **kwargs) -> Any: ...
    def inverted(*args, **kwargs) -> Any: ...
    def inverted_safe(*args, **kwargs) -> Any: ...
    is_frozen: Any
    is_identity: Any
    is_negative: Any
    is_orthogonal: Any
    is_orthogonal_axis_vectors: Any
    is_valid: Any
    is_wrapped: Any
    def lerp(*args, **kwargs) -> Any: ...
    median_scale: Any
    def normalize(*args, **kwargs) -> Any: ...
    def normalized(*args, **kwargs) -> Any: ...
    owner: Any
    def resize_4x4(*args, **kwargs) -> Any: ...
    def rotate(*args, **kwargs) -> Any: ...
    row: Any
    def to_2x2(*args, **kwargs) -> Any: ...
    def to_3x3(*args, **kwargs) -> Any: ...
    def to_4x4(*args, **kwargs) -> Any: ...
    def to_euler(*args, **kwargs) -> Any: ...
    def to_quaternion(*args, **kwargs) -> Any: ...
    def to_scale(*args, **kwargs) -> Any: ...
    def to_translation(*args, **kwargs) -> Any: ...
    translation: Any
    def transpose(*args, **kwargs) -> Any: ...
    def transposed(*args, **kwargs) -> Any: ...
    def zero(*args, **kwargs) -> Any: ...

class Quaternion:
    """.. class:: Quaternion(seq=(1.0, 0.0, 0.0, 0.0), angle=0.0, /)

   This object gives access to Quaternions in Blender.

   :arg seq: size 3 or 4
   :type seq: :class:`Vector`
   :arg angle: rotation angle, in radians
   :type angle: float

   The constructor takes arguments in various forms:

   (), *no args*
      Create an identity quaternion
   (*wxyz*)
      Create a quaternion from a ``(w, x, y, z)`` vector.
   (*exponential_map*)
      Create a quaternion from a 3d exponential map vector.

      .. seealso:: :meth:`to_exponential_map`
   (*axis, angle*)
      Create a quaternion representing a rotation of *angle* radians over *axis*.

      .. seealso:: :meth:`to_axis_angle`
"""
    """
    Online Documentation:
    https://docs.blender.org/api/current/mathutils.html
    """
    def __init__(self, /, *args, **kwargs) -> Any: ...
    angle: Any
    axis: Any
    def conjugate(*args, **kwargs) -> Any: ...
    def conjugated(*args, **kwargs) -> Any: ...
    def copy(*args, **kwargs) -> Any: ...
    def cross(*args, **kwargs) -> Any: ...
    def dot(*args, **kwargs) -> Any: ...
    def freeze(*args, **kwargs) -> Any: ...
    def identity(*args, **kwargs) -> Any: ...
    def invert(*args, **kwargs) -> Any: ...
    def inverted(*args, **kwargs) -> Any: ...
    is_frozen: Any
    is_valid: Any
    is_wrapped: Any
    magnitude: Any
    def make_compatible(*args, **kwargs) -> Any: ...
    def negate(*args, **kwargs) -> Any: ...
    def normalize(*args, **kwargs) -> Any: ...
    def normalized(*args, **kwargs) -> Any: ...
    owner: Any
    def rotate(*args, **kwargs) -> Any: ...
    def rotation_difference(*args, **kwargs) -> Any: ...
    def slerp(*args, **kwargs) -> Any: ...
    def to_axis_angle(*args, **kwargs) -> Any: ...
    def to_euler(*args, **kwargs) -> Any: ...
    def to_exponential_map(*args, **kwargs) -> Any: ...
    def to_matrix(*args, **kwargs) -> Any: ...
    def to_swing_twist(*args, **kwargs) -> Any: ...
    w: Any
    x: Any
    y: Any
    z: Any

class Vector:
    """.. class:: Vector(seq=(0.0, 0.0, 0.0), /)

   This object gives access to Vectors in Blender.

   :arg seq: Components of the vector, must be a sequence of at least two.
   :type seq: Sequence[float]
"""
    """
    Online Documentation:
    https://docs.blender.org/api/current/mathutils.html
    """
    def Fill(*args, **kwargs) -> Any: ...
    def Linspace(*args, **kwargs) -> Any: ...
    def Range(*args, **kwargs) -> Any: ...
    def Repeat(*args, **kwargs) -> Any: ...
    def __init__(self, /, *args, **kwargs) -> Any: ...
    def angle(*args, **kwargs) -> Any: ...
    def angle_signed(*args, **kwargs) -> Any: ...
    def copy(*args, **kwargs) -> Any: ...
    def cross(*args, **kwargs) -> Any: ...
    def dot(*args, **kwargs) -> Any: ...
    def freeze(*args, **kwargs) -> Any: ...
    is_frozen: Any
    is_valid: Any
    is_wrapped: Any
    length: Any
    length_squared: Any
    def lerp(*args, **kwargs) -> Any: ...
    magnitude: Any
    def negate(*args, **kwargs) -> Any: ...
    def normalize(*args, **kwargs) -> Any: ...
    def normalized(*args, **kwargs) -> Any: ...
    def orthogonal(*args, **kwargs) -> Any: ...
    owner: Any
    def project(*args, **kwargs) -> Any: ...
    def reflect(*args, **kwargs) -> Any: ...
    def resize(*args, **kwargs) -> Any: ...
    def resize_2d(*args, **kwargs) -> Any: ...
    def resize_3d(*args, **kwargs) -> Any: ...
    def resize_4d(*args, **kwargs) -> Any: ...
    def resized(*args, **kwargs) -> Any: ...
    def rotate(*args, **kwargs) -> Any: ...
    def rotation_difference(*args, **kwargs) -> Any: ...
    def slerp(*args, **kwargs) -> Any: ...
    def to_2d(*args, **kwargs) -> Any: ...
    def to_3d(*args, **kwargs) -> Any: ...
    def to_4d(*args, **kwargs) -> Any: ...
    def to_track_quat(*args, **kwargs) -> Any: ...
    def to_tuple(*args, **kwargs) -> Any: ...
    w: Any
    ww: Any
    www: Any
    wwww: Any
    wwwx: Any
    wwwy: Any
    wwwz: Any
    wwx: Any
    wwxw: Any
    wwxx: Any
    wwxy: Any
    wwxz: Any
    wwy: Any
    wwyw: Any
    wwyx: Any
    wwyy: Any
    wwyz: Any
    wwz: Any
    wwzw: Any
    wwzx: Any
    wwzy: Any
    wwzz: Any
    wx: Any
    wxw: Any
    wxww: Any
    wxwx: Any
    wxwy: Any
    wxwz: Any
    wxx: Any
    wxxw: Any
    wxxx: Any
    wxxy: Any
    wxxz: Any
    wxy: Any
    wxyw: Any
    wxyx: Any
    wxyy: Any
    wxyz: Any
    wxz: Any
    wxzw: Any
    wxzx: Any
    wxzy: Any
    wxzz: Any
    wy: Any
    wyw: Any
    wyww: Any
    wywx: Any
    wywy: Any
    wywz: Any
    wyx: Any
    wyxw: Any
    wyxx: Any
    wyxy: Any
    wyxz: Any
    wyy: Any
    wyyw: Any
    wyyx: Any
    wyyy: Any
    wyyz: Any
    wyz: Any
    wyzw: Any
    wyzx: Any
    wyzy: Any
    wyzz: Any
    wz: Any
    wzw: Any
    wzww: Any
    wzwx: Any
    wzwy: Any
    wzwz: Any
    wzx: Any
    wzxw: Any
    wzxx: Any
    wzxy: Any
    wzxz: Any
    wzy: Any
    wzyw: Any
    wzyx: Any
    wzyy: Any
    wzyz: Any
    wzz: Any
    wzzw: Any
    wzzx: Any
    wzzy: Any
    wzzz: Any
    x: Any
    xw: Any
    xww: Any
    xwww: Any
    xwwx: Any
    xwwy: Any
    xwwz: Any
    xwx: Any
    xwxw: Any
    xwxx: Any
    xwxy: Any
    xwxz: Any
    xwy: Any
    xwyw: Any
    xwyx: Any
    xwyy: Any
    xwyz: Any
    xwz: Any
    xwzw: Any
    xwzx: Any
    xwzy: Any
    xwzz: Any
    xx: Any
    xxw: Any
    xxww: Any
    xxwx: Any
    xxwy: Any
    xxwz: Any
    xxx: Any
    xxxw: Any
    xxxx: Any
    xxxy: Any
    xxxz: Any
    xxy: Any
    xxyw: Any
    xxyx: Any
    xxyy: Any
    xxyz: Any
    xxz: Any
    xxzw: Any
    xxzx: Any
    xxzy: Any
    xxzz: Any
    xy: Any
    xyw: Any
    xyww: Any
    xywx: Any
    xywy: Any
    xywz: Any
    xyx: Any
    xyxw: Any
    xyxx: Any
    xyxy: Any
    xyxz: Any
    xyy: Any
    xyyw: Any
    xyyx: Any
    xyyy: Any
    xyyz: Any
    xyz: Any
    xyzw: Any
    xyzx: Any
    xyzy: Any
    xyzz: Any
    xz: Any
    xzw: Any
    xzww: Any
    xzwx: Any
    xzwy: Any
    xzwz: Any
    xzx: Any
    xzxw: Any
    xzxx: Any
    xzxy: Any
    xzxz: Any
    xzy: Any
    xzyw: Any
    xzyx: Any
    xzyy: Any
    xzyz: Any
    xzz: Any
    xzzw: Any
    xzzx: Any
    xzzy: Any
    xzzz: Any
    y: Any
    yw: Any
    yww: Any
    ywww: Any
    ywwx: Any
    ywwy: Any
    ywwz: Any
    ywx: Any
    ywxw: Any
    ywxx: Any
    ywxy: Any
    ywxz: Any
    ywy: Any
    ywyw: Any
    ywyx: Any
    ywyy: Any
    ywyz: Any
    ywz: Any
    ywzw: Any
    ywzx: Any
    ywzy: Any
    ywzz: Any
    yx: Any
    yxw: Any
    yxww: Any
    yxwx: Any
    yxwy: Any
    yxwz: Any
    yxx: Any
    yxxw: Any
    yxxx: Any
    yxxy: Any
    yxxz: Any
    yxy: Any
    yxyw: Any
    yxyx: Any
    yxyy: Any
    yxyz: Any
    yxz: Any
    yxzw: Any
    yxzx: Any
    yxzy: Any
    yxzz: Any
    yy: Any
    yyw: Any
    yyww: Any
    yywx: Any
    yywy: Any
    yywz: Any
    yyx: Any
    yyxw: Any
    yyxx: Any
    yyxy: Any
    yyxz: Any
    yyy: Any
    yyyw: Any
    yyyx: Any
    yyyy: Any
    yyyz: Any
    yyz: Any
    yyzw: Any
    yyzx: Any
    yyzy: Any
    yyzz: Any
    yz: Any
    yzw: Any
    yzww: Any
    yzwx: Any
    yzwy: Any
    yzwz: Any
    yzx: Any
    yzxw: Any
    yzxx: Any
    yzxy: Any
    yzxz: Any
    yzy: Any
    yzyw: Any
    yzyx: Any
    yzyy: Any
    yzyz: Any
    yzz: Any
    yzzw: Any
    yzzx: Any
    yzzy: Any
    yzzz: Any
    z: Any
    def zero(*args, **kwargs) -> Any: ...
    zw: Any
    zww: Any
    zwww: Any
    zwwx: Any
    zwwy: Any
    zwwz: Any
    zwx: Any
    zwxw: Any
    zwxx: Any
    zwxy: Any
    zwxz: Any
    zwy: Any
    zwyw: Any
    zwyx: Any
    zwyy: Any
    zwyz: Any
    zwz: Any
    zwzw: Any
    zwzx: Any
    zwzy: Any
    zwzz: Any
    zx: Any
    zxw: Any
    zxww: Any
    zxwx: Any
    zxwy: Any
    zxwz: Any
    zxx: Any
    zxxw: Any
    zxxx: Any
    zxxy: Any
    zxxz: Any
    zxy: Any
    zxyw: Any
    zxyx: Any
    zxyy: Any
    zxyz: Any
    zxz: Any
    zxzw: Any
    zxzx: Any
    zxzy: Any
    zxzz: Any
    zy: Any
    zyw: Any
    zyww: Any
    zywx: Any
    zywy: Any
    zywz: Any
    zyx: Any
    zyxw: Any
    zyxx: Any
    zyxy: Any
    zyxz: Any
    zyy: Any
    zyyw: Any
    zyyx: Any
    zyyy: Any
    zyyz: Any
    zyz: Any
    zyzw: Any
    zyzx: Any
    zyzy: Any
    zyzz: Any
    zz: Any
    zzw: Any
    zzww: Any
    zzwx: Any
    zzwy: Any
    zzwz: Any
    zzx: Any
    zzxw: Any
    zzxx: Any
    zzxy: Any
    zzxz: Any
    zzy: Any
    zzyw: Any
    zzyx: Any
    zzyy: Any
    zzyz: Any
    zzz: Any
    zzzw: Any
    zzzx: Any
    zzzy: Any
    zzzz: Any

from . import bvhtree as bvhtree
# Documentation: https://docs.blender.org/api/current/mathutils.bvhtree.html
from . import geometry as geometry
# Documentation: https://docs.blender.org/api/current/mathutils.geometry.html
from . import interpolate as interpolate
# Documentation: https://docs.blender.org/api/current/mathutils.interpolate.html
from . import kdtree as kdtree
# Documentation: https://docs.blender.org/api/current/mathutils.kdtree.html
from . import noise as noise
# Documentation: https://docs.blender.org/api/current/mathutils.noise.html