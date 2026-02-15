# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/gpu.shader.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated


def create_from_info(*args, **kwargs) -> Any:
    """.. function:: create_from_info(shader_info)

   Create shader from a GPUShaderCreateInfo.

   :arg shader_info: GPUShaderCreateInfo
   :type shader_info: :class:`gpu.types.GPUShaderCreateInfo`
   :return: Shader object corresponding to the given name.
   :rtype: :class:`gpu.types.GPUShader`


    Online Documentation:
    https://docs.blender.org/api/current/gpu.shader.html"""
    ...

def from_builtin(*args, **kwargs) -> Any:
    """.. function:: from_builtin(shader_name, *, config='DEFAULT')

   Shaders that are embedded in the blender internal code (see :ref:`built-in-shaders`).
   They all read the uniform ``mat4 ModelViewProjectionMatrix``,
   which can be edited by the :mod:`gpu.matrix` module.

   You can also choose a shader configuration that uses clip_planes by setting the ``CLIPPED`` value to the config parameter. Note that in this case you also need to manually set the value of ``mat4 ModelMatrix``.

   :arg shader_name: One of the builtin shader names.
   :type shader_name: str
   :arg config: One of these types of shader configuration:

      - ``DEFAULT``
      - ``CLIPPED``
   :type config: str
   :return: Shader object corresponding to the given name.
   :rtype: :class:`gpu.types.GPUShader`


    Online Documentation:
    https://docs.blender.org/api/current/gpu.shader.html"""
    ...

def unbind(*args, **kwargs) -> Any:
    """.. function:: unbind()

   Unbind the bound shader object.


    Online Documentation:
    https://docs.blender.org/api/current/gpu.shader.html"""
    ...
