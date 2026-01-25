# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .Attribute import Attribute
from .FloatColorAttributeValue import FloatColorAttributeValue
class FloatColorAttribute(Attribute):
    name: str
    data_type: str
    storage_type: str
    domain: str
    is_internal: bool
    is_required: bool
    data: bpy_prop_collection['FloatColorAttributeValue']