# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/gpu.capabilities.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated


def compute_shader_support_get(*args, **kwargs) -> Any:
    """.. function:: compute_shader_support_get()

   Are compute shaders supported.

   :return: True when supported, False when not supported.
   :rtype: bool


    Online Documentation:
    https://docs.blender.org/api/current/gpu.capabilities.html"""
    ...

def extensions_get(*args, **kwargs) -> Any:
    """.. function:: extensions_get()

   Get supported extensions in the current context.

   :return: Extensions.
   :rtype: tuple[str]


    Online Documentation:
    https://docs.blender.org/api/current/gpu.capabilities.html"""
    ...

def hdr_support_get(*args, **kwargs) -> Any:
    """.. function:: hdr_support_get()

  Return whether GPU backend supports High Dynamic range for viewport.

   :return: HDR support available.
   :rtype: bool


    Online Documentation:
    https://docs.blender.org/api/current/gpu.capabilities.html"""
    ...

def max_batch_indices_get(*args, **kwargs) -> Any:
    """.. function:: max_batch_indices_get()

   Get maximum number of vertex array indices.

   :return: Number of indices.
   :rtype: int


    Online Documentation:
    https://docs.blender.org/api/current/gpu.capabilities.html"""
    ...

def max_batch_vertices_get(*args, **kwargs) -> Any:
    """.. function:: max_batch_vertices_get()

   Get maximum number of vertex array vertices.

   :return: Number of vertices.
   :rtype: int


    Online Documentation:
    https://docs.blender.org/api/current/gpu.capabilities.html"""
    ...

def max_images_get(*args, **kwargs) -> Any:
    """.. function:: max_images_get()

   Get maximum supported number of image units.

   :return: Number of image units.
   :rtype: int


    Online Documentation:
    https://docs.blender.org/api/current/gpu.capabilities.html"""
    ...

def max_texture_layers_get(*args, **kwargs) -> Any:
    """.. function:: max_texture_layers_get()

   Get maximum number of layers in texture.

   :return: Number of layers.
   :rtype: int


    Online Documentation:
    https://docs.blender.org/api/current/gpu.capabilities.html"""
    ...

def max_texture_size_get(*args, **kwargs) -> Any:
    """.. function:: max_texture_size_get()

   Get estimated maximum texture size to be able to handle.

   :return: Texture size.
   :rtype: int


    Online Documentation:
    https://docs.blender.org/api/current/gpu.capabilities.html"""
    ...

def max_textures_frag_get(*args, **kwargs) -> Any:
    """.. function:: max_textures_frag_get()

   Get maximum supported texture image units used for
   accessing texture maps from the fragment shader.

   :return: Texture image units.
   :rtype: int


    Online Documentation:
    https://docs.blender.org/api/current/gpu.capabilities.html"""
    ...

def max_textures_geom_get(*args, **kwargs) -> Any:
    """.. function:: max_textures_geom_get()

   Get maximum supported texture image units used for
   accessing texture maps from the geometry shader.

   :return: Texture image units.
   :rtype: int


    Online Documentation:
    https://docs.blender.org/api/current/gpu.capabilities.html"""
    ...

def max_textures_get(*args, **kwargs) -> Any:
    """.. function:: max_textures_get()

   Get maximum supported texture image units used for
   accessing texture maps from the vertex shader and the
   fragment processor.

   :return: Texture image units.
   :rtype: int


    Online Documentation:
    https://docs.blender.org/api/current/gpu.capabilities.html"""
    ...

def max_textures_vert_get(*args, **kwargs) -> Any:
    """.. function:: max_textures_vert_get()

   Get maximum supported texture image units used for
   accessing texture maps from the vertex shader.

   :return: Texture image units.
   :rtype: int


    Online Documentation:
    https://docs.blender.org/api/current/gpu.capabilities.html"""
    ...

def max_uniforms_frag_get(*args, **kwargs) -> Any:
    """.. function:: max_uniforms_frag_get()

   Get maximum number of values held in uniform variable
   storage for a fragment shader.

   :return: Number of values.
   :rtype: int


    Online Documentation:
    https://docs.blender.org/api/current/gpu.capabilities.html"""
    ...

def max_uniforms_vert_get(*args, **kwargs) -> Any:
    """.. function:: max_uniforms_vert_get()

   Get maximum number of values held in uniform variable
   storage for a vertex shader.

   :return: Number of values.
   :rtype: int


    Online Documentation:
    https://docs.blender.org/api/current/gpu.capabilities.html"""
    ...

def max_varying_floats_get(*args, **kwargs) -> Any:
    """.. function:: max_varying_floats_get()

   Get maximum number of varying variables used by
   vertex and fragment shaders.

   :return: Number of variables.
   :rtype: int


    Online Documentation:
    https://docs.blender.org/api/current/gpu.capabilities.html"""
    ...

def max_vertex_attribs_get(*args, **kwargs) -> Any:
    """.. function:: max_vertex_attribs_get()

   Get maximum number of vertex attributes accessible to
   a vertex shader.

   :return: Number of attributes.
   :rtype: int


    Online Documentation:
    https://docs.blender.org/api/current/gpu.capabilities.html"""
    ...

def max_work_group_count_get(*args, **kwargs) -> Any:
    """.. function:: max_work_group_count_get(index)

   Get maximum number of work groups that may be dispatched to a compute shader.

   :arg index: Index of the dimension.
   :type index: int
   :return: Maximum number of work groups for the queried dimension.
   :rtype: int


    Online Documentation:
    https://docs.blender.org/api/current/gpu.capabilities.html"""
    ...

def max_work_group_size_get(*args, **kwargs) -> Any:
    """.. function:: max_work_group_size_get(index)

   Get maximum size of a work group that may be dispatched to a compute shader.

   :arg index: Index of the dimension.
   :type index: int
   :return: Maximum size of a work group for the queried dimension.
   :rtype: int


    Online Documentation:
    https://docs.blender.org/api/current/gpu.capabilities.html"""
    ...

def shader_image_load_store_support_get(*args, **kwargs) -> Any:
    """.. function:: shader_image_load_store_support_get()

   Is image load/store supported.

   :return: True when supported, False when not supported.
   :rtype: bool


    Online Documentation:
    https://docs.blender.org/api/current/gpu.capabilities.html"""
    ...
