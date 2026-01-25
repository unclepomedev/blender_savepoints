# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
from .Image import Image
from .ImageUser import ImageUser
from .MovieClip import MovieClip
from .MovieClipUser import MovieClipUser
class CameraBackgroundImage(bpy_struct):
    is_override_data: bool
    source: str
    image: 'Image'
    clip: 'MovieClip'
    image_user: 'ImageUser'
    clip_user: 'MovieClipUser'
    offset: list[float]
    scale: float
    rotation: float
    use_flip_x: bool
    use_flip_y: bool
    alpha: float
    show_expanded: bool
    use_camera_clip: bool
    show_background_image: bool
    show_on_foreground: bool
    display_depth: str
    frame_method: str