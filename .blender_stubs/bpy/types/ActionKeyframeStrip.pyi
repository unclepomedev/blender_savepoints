# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.ActionKeyframeStrip.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .ActionStrip import ActionStrip
from .ActionChannelbag import ActionChannelbag
from .ActionChannelbags import ActionChannelbags
from .bpy_prop_collection import bpy_prop_collection

class ActionKeyframeStrip(ActionStrip):

    @property
    def type(self) -> Literal['KEYFRAME']:

        ...
    @property
    def channelbags(self) -> Annotated['ActionChannelbags', "is_animatable=False"]:

        ...
    def channelbag(self, *args, **kwargs) -> Any: ...
    def key_insert(self, *args, **kwargs) -> Any: ...