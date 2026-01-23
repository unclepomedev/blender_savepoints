"""
Online Documentation:
https://docs.blender.org/api/current/bpy_extras.node_shader_utils.html
"""

# Blender Probe Generated Stub for Blender 5.1.0 Alpha
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
    https://docs.blender.org/api/current/bpy_extras.node_shader_utils.html
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

class PrincipledBSDFWrapper:
    """
    Hard coded shader setup, based in Principled BSDF.
    Should cover most common cases on import, and gives a basic nodal shaders support for export.
    Supports basic: diffuse/spec/reflect/transparency/normal, with texturing.
    """
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy_extras.node_shader_utils.html
    """
    def __init__(self, material, is_readonly=True) -> Any: ...
    alpha: Any
    def alpha_get(self) -> Any: ...
    def alpha_set(self, value) -> Any: ...
    alpha_texture: Any
    def alpha_texture_get(self) -> Any: ...
    base_color: Any
    def base_color_get(self) -> Any: ...
    def base_color_set(self, color) -> Any: ...
    base_color_texture: Any
    def base_color_texture_get(self) -> Any: ...
    emission_color: Any
    def emission_color_get(self) -> Any: ...
    def emission_color_set(self, color) -> Any: ...
    emission_color_texture: Any
    def emission_color_texture_get(self) -> Any: ...
    emission_strength: Any
    def emission_strength_get(self) -> Any: ...
    def emission_strength_set(self, value) -> Any: ...
    emission_strength_texture: Any
    def emission_strength_texture_get(self) -> Any: ...
    ior: Any
    def ior_get(self) -> Any: ...
    def ior_set(self, value) -> Any: ...
    ior_texture: Any
    def ior_texture_get(self) -> Any: ...
    is_readonly: Any
    material: Any
    metallic: Any
    def metallic_get(self) -> Any: ...
    def metallic_set(self, value) -> Any: ...
    metallic_texture: Any
    def metallic_texture_get(self) -> Any: ...
    node_normalmap: Any
    def node_normalmap_get(self) -> Any: ...
    node_out: Any
    node_principled_bsdf: Any
    node_texcoords: Any
    def node_texcoords_get(self) -> Any: ...
    normalmap_strength: Any
    def normalmap_strength_get(self) -> Any: ...
    def normalmap_strength_set(self, value) -> Any: ...
    normalmap_texture: Any
    def normalmap_texture_get(self) -> Any: ...
    roughness: Any
    def roughness_get(self) -> Any: ...
    def roughness_set(self, value) -> Any: ...
    roughness_texture: Any
    def roughness_texture_get(self) -> Any: ...
    specular: Any
    def specular_get(self) -> Any: ...
    def specular_set(self, value) -> Any: ...
    specular_texture: Any
    def specular_texture_get(self) -> Any: ...
    specular_tint: Any
    def specular_tint_get(self) -> Any: ...
    def specular_tint_set(self, color) -> Any: ...
    specular_tint_texture: Any
    def specular_tint_texture_get(self) -> Any: ...
    transmission: Any
    def transmission_get(self) -> Any: ...
    def transmission_set(self, value) -> Any: ...
    transmission_texture: Any
    def transmission_texture_get(self) -> Any: ...
    def update(self) -> Any: ...

class ShaderImageTextureWrapper:
    """
    Generic 'image texture'-like wrapper, handling image node, some mapping (texture coordinates transformations),
    and texture coordinates source.
    """
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy_extras.node_shader_utils.html
    """
    def __init__(self, owner_shader: bpy_extras.node_shader_utils.ShaderWrapper, node_dst, socket_dst, grid_row_diff=0, use_alpha=False, colorspace_is_data=Ellipsis, colorspace_name=Ellipsis) -> Any: ...
    colorspace_is_data: Any
    colorspace_name: Any
    def copy_from(self, tex) -> Any: ...
    def copy_mapping_from(self, tex) -> Any: ...
    extension: Any
    def extension_get(self) -> Any: ...
    def extension_set(self, extension) -> Any: ...
    grid_row_diff: Any
    def has_mapping_node(self) -> Any: ...
    image: Any
    def image_get(self) -> Any: ...
    def image_set(self, image) -> Any: ...
    is_readonly: Any
    node_dst: Any
    node_image: Any
    def node_image_get(self) -> Any: ...
    node_mapping: Any
    def node_mapping_get(self) -> Any: ...
    owner_shader: Any
    projection: Any
    def projection_get(self) -> Any: ...
    def projection_set(self, projection) -> Any: ...
    rotation: Any
    def rotation_get(self) -> Any: ...
    def rotation_set(self, rotation) -> Any: ...
    scale: Any
    def scale_get(self) -> Any: ...
    def scale_set(self, scale) -> Any: ...
    socket_dst: Any
    texcoords: Any
    def texcoords_get(self) -> Any: ...
    def texcoords_set(self, texcoords) -> Any: ...
    translation: Any
    def translation_get(self) -> Any: ...
    def translation_set(self, translation) -> Any: ...
    use_alpha: Any

class ShaderWrapper:
    """
    Base class with minimal common ground for all types of shader interfaces we may want/need to implement.
    """
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy_extras.node_shader_utils.html
    """
    def __init__(self, material, is_readonly=True) -> Any: ...
    is_readonly: Any
    material: Any
    node_out: Any
    node_texcoords: Any
    def node_texcoords_get(self) -> Any: ...
    def update(self) -> Any: ...

class Vector:
    """.. class:: Vector(seq=(0.0, 0.0, 0.0), /)

   This object gives access to Vectors in Blender.

   :arg seq: Components of the vector, must be a sequence of at least two.
   :type seq: Sequence[float]
"""
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy_extras.node_shader_utils.html
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

def node_input_value_get(node, input, default_value=None) -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy_extras.node_shader_utils.html
    """
    ...

def node_input_value_set(node, input, value) -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy_extras.node_shader_utils.html
    """
    ...

def rgb_to_rgba(rgb) -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy_extras.node_shader_utils.html
    """
    ...

def rgba_to_rgb(rgba) -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy_extras.node_shader_utils.html
    """
    ...

def values_clamp(val, minv, maxv) -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy_extras.node_shader_utils.html
    """
    ...
