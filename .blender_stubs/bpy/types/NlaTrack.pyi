# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.NlaTrack.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .NlaStrip import NlaStrip
from .NlaStrips import NlaStrips
from .bpy_prop_collection import bpy_prop_collection

class NlaTrack(bpy_struct):

    @property
    def strips(self) -> Annotated['NlaStrips', "is_animatable=False"]:
        """NLA Strips on this NLA-track"""
        ...
    @property
    def is_override_data(self) -> bool:
        """In a local override data, whether this NLA track comes from the linked reference data, or is local to the override"""
        ...
    name: Annotated[str, "is_animatable=False"]

    @property
    def active(self) -> bool:
        """NLA Track is active"""
        ...
    is_solo: bool
    """NLA Track is evaluated itself (i.e. active Action and all other NLA Tracks in the same AnimData block are disabled)"""
    select: bool
    """NLA Track is selected"""
    mute: bool
    """Disable NLA Track evaluation"""
    lock: bool
    """NLA Track is locked"""