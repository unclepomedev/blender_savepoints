"""
Online Documentation:
https://docs.blender.org/api/current/gpu.types.html
"""

# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


import sys
import typing
from typing import Any, Union, Callable, Iterator

class Buffer:
    """.. class:: Buffer(format, dimensions, data)

   For Python access to GPU functions requiring a pointer.

   :arg format: Format type to interpret the buffer.
      Possible values are ``FLOAT``, ``INT``, ``UINT``, ``UBYTE``, ``UINT_24_8`` & ``10_11_11_REV``.
      ``UINT_24_8`` is deprecated, use ``FLOAT`` instead.
   :type format: str
   :arg dimensions: Array describing the dimensions.
   :type dimensions: int
   :arg data: Optional data array.
   :type data: Buffer | Sequence[float] | Sequence[int]
"""
    """
    Online Documentation:
    https://docs.blender.org/api/current/gpu.types.html
    """
    def __init__(self, /, *args, **kwargs) -> Any: ...
    dimensions: Any
    def to_list(*args, **kwargs) -> Any: ...

class GPUBatch:
    """.. class:: GPUBatch(type, buf, elem=None)

   Reusable container for drawable geometry.

   :arg type: The primitive type of geometry to be drawn.
      Possible values are ``POINTS``, ``LINES``, ``TRIS``, ``LINE_STRIP``, ``LINE_LOOP``, ``TRI_STRIP``, ``TRI_FAN``, ``LINES_ADJ``, ``TRIS_ADJ`` and ``LINE_STRIP_ADJ``.
   :type type: str
   :arg buf: Vertex buffer containing all or some of the attributes required for drawing.
   :type buf: :class:`gpu.types.GPUVertBuf`
   :arg elem: An optional index buffer.
   :type elem: :class:`gpu.types.GPUIndexBuf`
"""
    """
    Online Documentation:
    https://docs.blender.org/api/current/gpu.types.html
    """
    def __init__(self, /, *args, **kwargs) -> Any: ...
    def draw(*args, **kwargs) -> Any: ...
    def draw_instanced(*args, **kwargs) -> Any: ...
    def draw_range(*args, **kwargs) -> Any: ...
    def program_set(*args, **kwargs) -> Any: ...
    def vertbuf_add(*args, **kwargs) -> Any: ...

class GPUFrameBuffer:
    """.. class:: GPUFrameBuffer(*, depth_slot=None, color_slots=None)

   This object gives access to framebuffer functionalities.
   When a 'layer' is specified in a argument, a single layer of a 3D or array texture is attached to the frame-buffer.
   For cube map textures, layer is translated into a cube map face.

   :arg depth_slot: GPUTexture to attach or a ``dict`` containing keywords: 'texture', 'layer' and 'mip'.
   :type depth_slot: :class:`gpu.types.GPUTexture` | dict[] | None
   :arg color_slots: Tuple where each item can be a GPUTexture or a ``dict`` containing keywords: 'texture', 'layer' and 'mip'.
   :type color_slots: :class:`gpu.types.GPUTexture` | dict[str, int | :class:`gpu.types.GPUTexture`] | Sequence[:class:`gpu.types.GPUTexture` | dict[str, int | :class:`gpu.types.GPUTexture`]] | None
"""
    """
    Online Documentation:
    https://docs.blender.org/api/current/gpu.types.html
    """
    def __init__(self, /, *args, **kwargs) -> Any: ...
    def bind(*args, **kwargs) -> Any: ...
    def clear(*args, **kwargs) -> Any: ...
    is_bound: Any
    def read_color(*args, **kwargs) -> Any: ...
    def read_depth(*args, **kwargs) -> Any: ...
    def viewport_get(*args, **kwargs) -> Any: ...
    def viewport_set(*args, **kwargs) -> Any: ...

class GPUIndexBuf:
    """.. class:: GPUIndexBuf(type, seq)

   Contains an index buffer.

   :arg type: The primitive type this index buffer is composed of.
      Possible values are [``POINTS``, ``LINES``, ``TRIS``, ``LINES_ADJ``, ``TRIS_ADJ``].
   :type type: str
   :arg seq: Indices this index buffer will contain.
      Whether a 1D or 2D sequence is required depends on the type.
      Optionally the sequence can support the buffer protocol.
   :type seq: Buffer | Sequence[int] | Sequence[Sequence[int]]
"""
    """
    Online Documentation:
    https://docs.blender.org/api/current/gpu.types.html
    """
    def __init__(self, /, *args, **kwargs) -> Any: ...

class GPUOffScreen:
    """.. class:: GPUOffScreen(width, height, *, format='RGBA8')

   This object gives access to off screen buffers.

   :arg width: Horizontal dimension of the buffer.
   :type width: int
   :arg height: Vertical dimension of the buffer.
   :type height: int
   :arg format: Internal data format inside GPU memory for color attachment texture. Possible values are:
      ``RGBA8``,
      ``RGBA16``,
      ``RGBA16F``,
      ``RGBA32F``.
   :type format: str
"""
    """
    Online Documentation:
    https://docs.blender.org/api/current/gpu.types.html
    """
    def __init__(self, /, *args, **kwargs) -> Any: ...
    def bind(*args, **kwargs) -> Any: ...
    def draw_view3d(*args, **kwargs) -> Any: ...
    def free(*args, **kwargs) -> Any: ...
    height: Any
    texture_color: Any
    def unbind(*args, **kwargs) -> Any: ...
    width: Any

class GPUShader:
    """
    Online Documentation:
    https://docs.blender.org/api/current/gpu.types.html
    """
    def __init__(self, /, *args, **kwargs) -> Any: ...
    def attr_from_name(*args, **kwargs) -> Any: ...
    def attrs_info_get(*args, **kwargs) -> Any: ...
    def bind(*args, **kwargs) -> Any: ...
    def format_calc(*args, **kwargs) -> Any: ...
    def image(*args, **kwargs) -> Any: ...
    name: Any
    program: Any
    def uniform_block(*args, **kwargs) -> Any: ...
    def uniform_block_from_name(*args, **kwargs) -> Any: ...
    def uniform_bool(*args, **kwargs) -> Any: ...
    def uniform_float(*args, **kwargs) -> Any: ...
    def uniform_from_name(*args, **kwargs) -> Any: ...
    def uniform_int(*args, **kwargs) -> Any: ...
    def uniform_sampler(*args, **kwargs) -> Any: ...
    def uniform_vector_float(*args, **kwargs) -> Any: ...
    def uniform_vector_int(*args, **kwargs) -> Any: ...

class GPUShaderCreateInfo:
    """.. class:: GPUShaderCreateInfo()

   Stores and describes types and variables that are used in shader sources.
"""
    """
    Online Documentation:
    https://docs.blender.org/api/current/gpu.types.html
    """
    def __init__(self, /, *args, **kwargs) -> Any: ...
    def compute_source(*args, **kwargs) -> Any: ...
    def define(*args, **kwargs) -> Any: ...
    def depth_write(*args, **kwargs) -> Any: ...
    def fragment_out(*args, **kwargs) -> Any: ...
    def fragment_source(*args, **kwargs) -> Any: ...
    def image(*args, **kwargs) -> Any: ...
    def local_group_size(*args, **kwargs) -> Any: ...
    def push_constant(*args, **kwargs) -> Any: ...
    def sampler(*args, **kwargs) -> Any: ...
    def typedef_source(*args, **kwargs) -> Any: ...
    def uniform_buf(*args, **kwargs) -> Any: ...
    def vertex_in(*args, **kwargs) -> Any: ...
    def vertex_out(*args, **kwargs) -> Any: ...
    def vertex_source(*args, **kwargs) -> Any: ...

class GPUStageInterfaceInfo:
    """.. class:: GPUStageInterfaceInfo(name)

   List of varyings between shader stages.

   :arg name: Name of the interface block.
   :type value: str
"""
    """
    Online Documentation:
    https://docs.blender.org/api/current/gpu.types.html
    """
    def __init__(self, /, *args, **kwargs) -> Any: ...
    def flat(*args, **kwargs) -> Any: ...
    name: Any
    def no_perspective(*args, **kwargs) -> Any: ...
    def smooth(*args, **kwargs) -> Any: ...

class GPUTexture:
    """.. class:: GPUTexture(size, *, layers=0, is_cubemap=False, format='RGBA8', data=None)

   This object gives access to off GPU textures.

   :arg size: Dimensions of the texture 1D, 2D, 3D or cubemap.
   :type size: int | Sequence[int]
   :arg layers: Number of layers in texture array or number of cubemaps in cubemap array
   :type layers: int
   :arg is_cubemap: Indicates the creation of a cubemap texture.
   :type is_cubemap: int
   :arg format: Internal data format inside GPU memory. Possible values are:
      ``RGBA8UI``,
      ``RGBA8I``,
      ``RGBA8``,
      ``RGBA32UI``,
      ``RGBA32I``,
      ``RGBA32F``,
      ``RGBA16UI``,
      ``RGBA16I``,
      ``RGBA16F``,
      ``RGBA16``,
      ``RG8UI``,
      ``RG8I``,
      ``RG8``,
      ``RG32UI``,
      ``RG32I``,
      ``RG32F``,
      ``RG16UI``,
      ``RG16I``,
      ``RG16F``,
      ``RG16``,
      ``R8UI``,
      ``R8I``,
      ``R8``,
      ``R32UI``,
      ``R32I``,
      ``R32F``,
      ``R16UI``,
      ``R16I``,
      ``R16F``,
      ``R16``,
      ``R11F_G11F_B10F``,
      ``DEPTH32F_STENCIL8``,
      ``DEPTH24_STENCIL8`` (deprecated, use ``DEPTH32F_STENCIL8``),
      ``SRGB8_A8``,
      ``RGB16F``,
      ``SRGB8_A8_DXT1``,
      ``SRGB8_A8_DXT3``,
      ``SRGB8_A8_DXT5``,
      ``RGBA8_DXT1``,
      ``RGBA8_DXT3``,
      ``RGBA8_DXT5``,
      ``DEPTH_COMPONENT32F``,
      ``DEPTH_COMPONENT24``, (deprecated, use ``DEPTH_COMPONENT32F``),
      ``DEPTH_COMPONENT16``.
   :type format: str
   :arg data: Buffer object to fill the texture.
   :type data: :class:`gpu.types.Buffer`
"""
    """
    Online Documentation:
    https://docs.blender.org/api/current/gpu.types.html
    """
    def __init__(self, /, *args, **kwargs) -> Any: ...
    def clear(*args, **kwargs) -> Any: ...
    format: Any
    height: Any
    def read(*args, **kwargs) -> Any: ...
    width: Any

class GPUUniformBuf:
    """.. class:: GPUUniformBuf(data)

   This object gives access to off uniform buffers.

   :arg data: Data to fill the buffer.
   :type data: object exposing buffer interface
"""
    """
    Online Documentation:
    https://docs.blender.org/api/current/gpu.types.html
    """
    def __init__(self, /, *args, **kwargs) -> Any: ...
    def update(*args, **kwargs) -> Any: ...

class GPUVertBuf:
    """.. class:: GPUVertBuf(format, len)

   Contains a VBO.

   :arg format: Vertex format.
   :type format: :class:`gpu.types.GPUVertFormat`
   :arg len: Amount of vertices that will fit into this buffer.
   :type len: int
"""
    """
    Online Documentation:
    https://docs.blender.org/api/current/gpu.types.html
    """
    def __init__(self, /, *args, **kwargs) -> Any: ...
    def attr_fill(*args, **kwargs) -> Any: ...

class GPUVertFormat:
    """.. class:: GPUVertFormat()

   This object contains information about the structure of a vertex buffer.
"""
    """
    Online Documentation:
    https://docs.blender.org/api/current/gpu.types.html
    """
    def __init__(self, /, *args, **kwargs) -> Any: ...
    def attr_add(*args, **kwargs) -> Any: ...
