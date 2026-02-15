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
class AssetWeakReference(bpy_struct):
    @property
    def asset_library_type(self) -> Annotated[Literal['ALL', 'LOCAL', 'ESSENTIALS', 'CUSTOM'], "is_animatable=False"]:
        ...
    @property
    def asset_library_identifier(self) -> Annotated[str, "is_animatable=False"]:
        ...
    @property
    def relative_asset_identifier(self) -> Annotated[str, "is_animatable=False"]:
        ...