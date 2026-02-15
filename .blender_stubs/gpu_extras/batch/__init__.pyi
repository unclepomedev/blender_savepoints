# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/gpu_extras.batch.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated


def batch_for_shader(shader, type, content, *, indices=None) -> Any:
    """
    Return a batch already configured and compatible with the shader.

    :arg shader: shader for which a compatible format will be computed.
    :type shader: :class:`gpu.types.GPUShader`
    :arg type: "'POINTS', 'LINES', 'TRIS' or 'LINES_ADJ'".
    :type type: str
    :arg content: Maps the name of the shader attribute with the data to fill the vertex buffer.
       For the dictionary values see documentation for :class:`gpu.types.GPUVertBuf.attr_fill` data argument.
    :type content: dict[str, Buffer | Sequence[float] | Sequence[int] | Sequence[Sequence[float]] | Sequence[Sequence[int]]]
    :return: compatible batch
    :rtype: :class:`gpu.types.GPUBatch`
    

    Online Documentation:
    https://docs.blender.org/api/current/gpu_extras.batch.html"""
    ...
