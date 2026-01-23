# Blender Probe Generated Stub for Blender 5.1.0 Alpha
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
from .ID import ID
from .IDOverrideLibraryProperty import IDOverrideLibraryProperty
class IDOverrideLibrary(bpy_struct):
    reference: 'ID'
    hierarchy_root: 'ID'
    is_in_hierarchy: bool
    is_system_override: bool
    properties: bpy_prop_collection['IDOverrideLibraryProperty']
    def operations_update(self, *args, **kwargs) -> Any: ...
    def reset(self, *args, **kwargs) -> Any: ...
    def destroy(self, *args, **kwargs) -> Any: ...
    def resync(self, *args, **kwargs) -> Any: ...