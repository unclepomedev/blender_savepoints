# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
class PreferencesKeymap(bpy_struct):
    show_ui_keyconfig: bool
    active_keyconfig: Annotated[str, "subtype='DIR_PATH'", "is_animatable=False"]
    """The name of the active key configuration"""