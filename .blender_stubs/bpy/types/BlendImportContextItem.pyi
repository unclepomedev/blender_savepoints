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
from .BlendImportContextLibrary import BlendImportContextLibrary
from .ID import ID
from .Library import Library
class BlendImportContextItem(bpy_struct):
    name: str
    id_type: str
    source_libraries: bpy_prop_collection['BlendImportContextLibrary']
    append_action: str
    import_info: set[str]
    id: 'ID'
    source_library: 'Library'
    library_override_id: 'ID'
    reusable_local_id: 'ID'