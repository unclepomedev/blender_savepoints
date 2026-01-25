# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .Property import Property
from .Struct import Struct
class FloatProperty(Property):
    name: str
    identifier: str
    description: str
    translation_context: str
    type: str
    subtype: str
    srna: 'Struct'
    unit: str
    icon: str
    is_readonly: bool
    is_animatable: bool
    is_overridable: bool
    is_required: bool
    is_argument_optional: bool
    is_never_none: bool
    is_hidden: bool
    is_skip_save: bool
    is_skip_preset: bool
    is_output: bool
    is_registered: bool
    is_registered_optional: bool
    is_runtime: bool
    is_enum_flag: bool
    is_library_editable: bool
    is_path_output: bool
    is_path_supports_blend_relative: bool
    is_path_supports_templates: bool
    is_deprecated: bool
    deprecated_note: str
    deprecated_version: list[int]
    deprecated_removal_version: list[int]
    tags: set[str]
    default: float
    default_array: list[float]
    array_length: int
    array_dimensions: list[int]
    is_array: bool
    hard_min: float
    hard_max: float
    soft_min: float
    soft_max: float
    step: float
    precision: int