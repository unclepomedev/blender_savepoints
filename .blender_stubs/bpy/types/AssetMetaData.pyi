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
from .AssetTag import AssetTag
class AssetMetaData(bpy_struct):
    author: str
    description: str
    copyright: str
    license: str
    tags: bpy_prop_collection['AssetTag']
    active_tag: int
    catalog_id: str
    catalog_simple_name: str