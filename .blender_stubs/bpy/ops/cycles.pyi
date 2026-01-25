# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import typing
import bpy
from typing import Any, Optional, Union

def denoise_animation(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, input_filepath: str = ..., output_filepath: str = ...) -> set[str]:
    """Denoise rendered animation sequence using current scene and view layer settings. Requires denoising data passes and output to OpenEXR multilayer files"""
    ...

def merge_images(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, input_filepath1: str = ..., input_filepath2: str = ..., output_filepath: str = ...) -> set[str]:
    """Combine OpenEXR multi-layer images rendered with different sample ranges into one image with reduced noise"""
    ...

def use_shading_nodes(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Enable nodes on a light"""
    ...
