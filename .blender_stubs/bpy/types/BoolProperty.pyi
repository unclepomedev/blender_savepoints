# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated
from .bpy_prop_collection import bpy_prop_collection

from .Property import Property
from .Struct import Struct
class BoolProperty(Property):
    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:
        """Human readable name"""
        ...
    @property
    def identifier(self) -> Annotated[str, "is_animatable=False"]:
        """Unique name used in the code and scripting"""
        ...
    @property
    def description(self) -> Annotated[str, "is_animatable=False"]:
        """Description of the property for tooltips"""
        ...
    @property
    def translation_context(self) -> Annotated[str, "is_animatable=False"]:
        """Translation context of the property's name"""
        ...
    @property
    def type(self) -> Literal['BOOLEAN', 'INT', 'FLOAT', 'STRING', 'ENUM', 'POINTER', 'COLLECTION']:
        """Data type of the property"""
        ...
    @property
    def subtype(self) -> Literal['NONE', 'FILE_PATH', 'DIR_PATH', 'FILE_NAME', 'BYTE_STRING', 'PASSWORD', 'PIXEL', 'PIXEL_DIAMETER', 'UNSIGNED', 'PERCENTAGE', 'FACTOR', 'ANGLE', 'TIME', 'TIME_ABSOLUTE', 'DISTANCE', 'DISTANCE_DIAMETER', 'DISTANCE_CAMERA', 'POWER', 'TEMPERATURE', 'WAVELENGTH', 'COLOR_TEMPERATURE', 'FREQUENCY', 'COLOR', 'TRANSLATION', 'DIRECTION', 'VELOCITY', 'ACCELERATION', 'MATRIX', 'EULER', 'QUATERNION', 'AXISANGLE', 'XYZ', 'XYZ_LENGTH', 'COLOR_GAMMA', 'COORDINATES', 'LAYER', 'LAYER_MEMBER']:
        """Semantic interpretation of the property"""
        ...
    @property
    def srna(self) -> Annotated[Optional['Struct'], "is_animatable=False"]:
        """Struct definition used for properties assigned to this item"""
        ...
    @property
    def unit(self) -> Literal['NONE', 'LENGTH', 'AREA', 'VOLUME', 'ROTATION', 'TIME', 'TIME_ABSOLUTE', 'VELOCITY', 'ACCELERATION', 'MASS', 'CAMERA', 'POWER', 'TEMPERATURE', 'WAVELENGTH', 'COLOR_TEMPERATURE', 'FREQUENCY']:
        """Type of units for this property"""
        ...
    @property
    def icon(self) -> str:
        """Icon of the item"""
        ...
    @property
    def is_readonly(self) -> bool:
        """Property is editable through RNA"""
        ...
    @property
    def is_animatable(self) -> bool:
        """Property is animatable through RNA"""
        ...
    @property
    def is_overridable(self) -> bool:
        """Property is overridable through RNA"""
        ...
    @property
    def is_required(self) -> bool:
        """False when this property is an optional argument in an RNA function"""
        ...
    @property
    def is_argument_optional(self) -> bool:
        """True when the property is optional in a Python function implementing an RNA function"""
        ...
    @property
    def is_never_none(self) -> bool:
        """True when this value cannot be set to None"""
        ...
    @property
    def is_hidden(self) -> bool:
        """True when the property is hidden"""
        ...
    @property
    def is_skip_save(self) -> bool:
        """True when the property uses ghost values"""
        ...
    @property
    def is_skip_preset(self) -> bool:
        """True when the property is not saved in presets"""
        ...
    @property
    def is_output(self) -> bool:
        """True when this property is an output value from an RNA function"""
        ...
    @property
    def is_registered(self) -> bool:
        """Property is registered as part of type registration"""
        ...
    @property
    def is_registered_optional(self) -> bool:
        """Property is optionally registered as part of type registration"""
        ...
    @property
    def is_runtime(self) -> bool:
        """Property has been dynamically created at runtime"""
        ...
    @property
    def is_enum_flag(self) -> bool:
        """True when multiple enums"""
        ...
    @property
    def is_library_editable(self) -> bool:
        """Property is editable from linked instances (changes not saved)"""
        ...
    @property
    def is_path_output(self) -> bool:
        """Property is a filename, filepath or directory output"""
        ...
    @property
    def is_path_supports_blend_relative(self) -> bool:
        """Property is a path which supports the "//" prefix, signifying the location as relative to the ".blend" file's directory"""
        ...
    @property
    def is_path_supports_templates(self) -> bool:
        """Property is a path which supports the "{variable_name}" variable expression syntax, which substitutes the value of the referenced variable in place of the expression"""
        ...
    @property
    def is_deprecated(self) -> bool:
        """The property is deprecated"""
        ...
    @property
    def deprecated_note(self) -> Annotated[str, "is_animatable=False"]:
        """A note regarding deprecation"""
        ...
    @property
    def deprecated_version(self) -> Annotated[list[int], "step=1"]:
        """The Blender version this was deprecated"""
        ...
    @property
    def deprecated_removal_version(self) -> Annotated[list[int], "step=1"]:
        """The Blender version this is expected to be removed"""
        ...
    @property
    def tags(self) -> set[str]:
        """Subset of tags (defined in parent struct) that are set for this property"""
        ...
    @property
    def default(self) -> bool:
        """Default value for this number"""
        ...
    @property
    def default_array(self) -> list[bool]:
        """Default value for this array"""
        ...
    @property
    def array_length(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Maximum length of the array, 0 means unlimited"""
        ...
    @property
    def array_dimensions(self) -> Annotated[list[int], "subtype='UNSIGNED'", "step=1"]:
        """Length of each dimension of the array"""
        ...
    @property
    def is_array(self) -> bool:
        ...