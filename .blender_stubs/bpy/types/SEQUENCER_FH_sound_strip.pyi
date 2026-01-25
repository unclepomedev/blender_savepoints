# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .FileHandler import FileHandler
from .SequencerFileHandlerBase import SequencerFileHandlerBase
class SEQUENCER_FH_sound_strip(FileHandler, SequencerFileHandlerBase):
    bl_idname: str
    bl_import_operator: str
    bl_export_operator: str
    bl_label: str
    bl_file_extensions: str
    def poll_drop(self, *args, **kwargs) -> Any: ...