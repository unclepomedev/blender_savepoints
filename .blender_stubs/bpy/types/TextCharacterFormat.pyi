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
class TextCharacterFormat(bpy_struct):
    use_bold: bool
    use_italic: bool
    use_underline: bool
    use_small_caps: bool
    material_index: int
    kerning: float