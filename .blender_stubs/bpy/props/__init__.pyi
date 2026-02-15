# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.props.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated


def BoolProperty(*args, **kwargs) -> Any:
    """.. function:: BoolProperty(*, name="", description="", translation_context="*", default=False, options={'ANIMATABLE'}, override=set(), tags=set(), subtype='NONE', update=None, get=None, set=None, get_transform=None, set_transform=None)

   Returns a new boolean property definition.

   :arg name: Name used in the user interface.
   :type name: str
   :arg description: Text used for the tooltip and api documentation.
   :type description: str
   :arg translation_context: Text used as context to disambiguate translations.
   :type translation_context: str
   :arg options: Enumerator in :ref:`rna_enum_property_flag_items`.
   :type options: set[str]
   :arg override: Enumerator in :ref:`rna_enum_property_override_flag_items`.
   :type override: set[str]
   :arg tags: Enumerator of tags that are defined by parent class.
   :type tags: set[str]
   :arg subtype: Enumerator in :ref:`rna_enum_property_subtype_number_items`.
   :type subtype: str
   :arg update: Function to be called when this value is modified,
      This function must take 2 values (self, context) and return None.
      *Warning* there are no safety checks to avoid infinite recursion.
   :type update: Callable[[:class:`bpy.types.bpy_struct`, :class:`bpy.types.Context`], None]
   :arg get: Function to be called when this value is 'read', and the default,
      system-defined storage is not used for this property.
      This function must take 1 value (self) and return the value of the property.

      .. note:: Defining this callback without a matching ``set`` one will make the property read-only (even if ``READ_ONLY`` option is not set).
   :type get: Callable[[:class:`bpy.types.bpy_struct`], bool]
   :arg set: Function to be called when this value is 'written', and the default,
      system-defined storage is not used for this property.
      This function must take 2 values (self, value) and return None.

      .. note:: Defining this callback without a matching ``get`` one is invalid.
   :type set: Callable[[:class:`bpy.types.bpy_struct`, bool], None]
   :arg get_transform: Function to be called when this value is 'read',
      if some additional processing must be performed on the stored value.
      This function must take three arguments (self, the stored value,
      and a boolean indicating if the property is currently set),
      and return the final, transformed value of the property.

      .. note:: The callback is responsible to ensure that value limits of the property (min/max, length...) are respected. Otherwise a ValueError exception is raised.

   :type get_transform: Callable[[:class:`bpy.types.bpy_struct`, bool, bool], bool]
   :arg set_transform: Function to be called when this value is 'written',
      if some additional processing must be performed on the given value before storing it.
      This function must take four arguments (self, the given value to store,
      the currently stored value ('raw' value, without any ``get_transform`` applied to it),
      and a boolean indicating if the property is currently set),
      and return the final, transformed value of the property.

      .. note:: The callback is responsible to ensure that value limits (min/max, length...) are respected. Otherwise a ValueError exception is raised.

   :type set_transform: Callable[[:class:`bpy.types.bpy_struct`, bool, bool, bool], bool]


    Online Documentation:
    https://docs.blender.org/api/current/bpy.props.html"""
    ...

def BoolVectorProperty(*args, **kwargs) -> Any:
    """.. function:: BoolVectorProperty(*, name="", description="", translation_context="*", default=(False, False, False), options={'ANIMATABLE'}, override=set(), tags=set(), subtype='NONE', size=3, update=None, get=None, set=None, get_transform=None, set_transform=None)

   Returns a new vector boolean property definition.

   :arg name: Name used in the user interface.
   :type name: str
   :arg description: Text used for the tooltip and api documentation.
   :type description: str
   :arg translation_context: Text used as context to disambiguate translations.
   :type translation_context: str
   :arg default: sequence of booleans the length of *size*.
   :type default: Sequence[bool]
   :arg options: Enumerator in :ref:`rna_enum_property_flag_items`.
   :type options: set[str]
   :arg override: Enumerator in :ref:`rna_enum_property_override_flag_items`.
   :type override: set[str]
   :arg tags: Enumerator of tags that are defined by parent class.
   :type tags: set[str]
   :arg subtype: Enumerator in :ref:`rna_enum_property_subtype_number_array_items`.
   :type subtype: str
   :arg size: Vector dimensions in [1, 32]. An int sequence can be used to define multi-dimension arrays.
   :type size: int | Sequence[int]
   :arg update: Function to be called when this value is modified,
      This function must take 2 values (self, context) and return None.
      *Warning* there are no safety checks to avoid infinite recursion.
   :type update: Callable[[:class:`bpy.types.bpy_struct`, :class:`bpy.types.Context`], None]
   :arg get: Function to be called when this value is 'read', and the default,
      system-defined storage is not used for this property.
      This function must take 1 value (self) and return the value of the property.

      .. note:: Defining this callback without a matching ``set`` one will make the property read-only (even if ``READ_ONLY`` option is not set).
   :type get: Callable[[:class:`bpy.types.bpy_struct`], Sequence[bool]]
   :arg set: Function to be called when this value is 'written', and the default,
      system-defined storage is not used for this property.
      This function must take 2 values (self, value) and return None.

      .. note:: Defining this callback without a matching ``get`` one is invalid.
   :type set: Callable[[:class:`bpy.types.bpy_struct`, tuple[bool, ...]], None]
   :arg get_transform: Function to be called when this value is 'read',
      if some additional processing must be performed on the stored value.
      This function must take three arguments (self, the stored value,
      and a boolean indicating if the property is currently set),
      and return the final, transformed value of the property.

      .. note:: The callback is responsible to ensure that value limits of the property (min/max, length...) are respected. Otherwise a ValueError exception is raised.

   :type get_transform: Callable[[:class:`bpy.types.bpy_struct`, Sequence[bool], bool], Sequence[bool]]
   :arg set_transform: Function to be called when this value is 'written',
      if some additional processing must be performed on the given value before storing it.
      This function must take four arguments (self, the given value to store,
      the currently stored value ('raw' value, without any ``get_transform`` applied to it),
      and a boolean indicating if the property is currently set),
      and return the final, transformed value of the property.

      .. note:: The callback is responsible to ensure that value limits (min/max, length...) are respected. Otherwise a ValueError exception is raised.

   :type set_transform: Callable[[:class:`bpy.types.bpy_struct`, Sequence[bool], Sequence[bool], bool], Sequence[bool]]


    Online Documentation:
    https://docs.blender.org/api/current/bpy.props.html"""
    ...

def CollectionProperty(*args, **kwargs) -> Any:
    """.. function:: CollectionProperty(type, *, name="", description="", translation_context="*", options={'ANIMATABLE'}, override=set(), tags=set())

   Returns a new collection property definition.

   :arg type: A subclass of a property group.
   :type type: type[:class:`bpy.types.PropertyGroup`]
   :arg name: Name used in the user interface.
   :type name: str
   :arg description: Text used for the tooltip and api documentation.
   :type description: str
   :arg translation_context: Text used as context to disambiguate translations.
   :type translation_context: str
   :arg options: Enumerator in :ref:`rna_enum_property_flag_items`.
   :type options: set[str]
   :arg override: Enumerator in :ref:`rna_enum_property_override_flag_collection_items`.
   :type override: set[str]
   :arg tags: Enumerator of tags that are defined by parent class.
   :type tags: set[str]


    Online Documentation:
    https://docs.blender.org/api/current/bpy.props.html"""
    ...

def EnumProperty(*args, **kwargs) -> Any:
    """.. function:: EnumProperty(items, *, name="", description="", translation_context="*", default=None, options={'ANIMATABLE'}, override=set(), tags=set(), update=None, get=None, set=None, get_transform=None, set_transform=None)

   Returns a new enumerator property definition.

   :arg items: sequence of enum items formatted:
      ``[(identifier, name, description, icon, number), ...]``.

      The first three elements of the tuples are mandatory.

      :identifier: The identifier is used for Python access.
         An empty identifier means that the item is a separator
      :name: Name for the interface.
      :description: Used for documentation and tooltips.
      :icon: An icon string identifier or integer icon value
         (e.g. returned by :class:`bpy.types.UILayout.icon`)
      :number: Unique value used as the identifier for this item (stored in file data).
         Use when the identifier may need to change. If the *ENUM_FLAG* option is used,
         the values are bit-masks and should be powers of two.

      When an item only contains 4 items they define ``(identifier, name, description, number)``.

      Separators may be added using either None (nameless separator),
      or a regular item tuple with an empty identifier string, in which case the name,
      if non-empty, will be displayed in the UI above the separator line.
      For dynamic values a callback can be passed which returns a list in
      the same format as the static list.
      This function must take 2 arguments ``(self, context)``, **context may be None**.

      .. warning::

         There is a known bug with using a callback,
         Python must keep a reference to the strings returned by the callback or Blender
         will misbehave or even crash.
   :type items: Iterable[tuple[str, str, str] | tuple[str, str, str, int] | tuple[str, str, str, int, int] | None] | Callable[[:class:`bpy.types.bpy_struct`, :class:`bpy.types.Context` | None], Iterable[tuple[str, str, str] | tuple[str, str, str, int] | tuple[str, str, str, int, int] | None]]
   :arg name: Name used in the user interface.
   :type name: str
   :arg description: Text used for the tooltip and api documentation.
   :type description: str
   :arg translation_context: Text used as context to disambiguate translations.
   :type translation_context: str
   :arg default: The default value for this enum, a string from the identifiers used in *items*, or integer matching an item number.
      If the *ENUM_FLAG* option is used this must be a set of such string identifiers instead.
      WARNING: Strings cannot be specified for dynamic enums
      (i.e. if a callback function is given as *items* parameter).
   :type default: str | int | set[str]
   :arg options: Enumerator in :ref:`rna_enum_property_flag_enum_items`.
   :type options: set[str]
   :arg override: Enumerator in :ref:`rna_enum_property_override_flag_items`.
   :type override: set[str]
   :arg tags: Enumerator of tags that are defined by parent class.
   :type tags: set[str]
   :arg update: Function to be called when this value is modified,
      This function must take 2 values (self, context) and return None.
      *Warning* there are no safety checks to avoid infinite recursion.
   :type update: Callable[[:class:`bpy.types.bpy_struct`, :class:`bpy.types.Context`], None]
   :arg get: Function to be called when this value is 'read', and the default,
      system-defined storage is not used for this property.
      This function must take 1 value (self) and return the value of the property.

      .. note:: Defining this callback without a matching ``set`` one will make the property read-only (even if ``READ_ONLY`` option is not set).
   :type get: Callable[[:class:`bpy.types.bpy_struct`], int]
   :arg set: Function to be called when this value is 'written', and the default,
      system-defined storage is not used for this property.
      This function must take 2 values (self, value) and return None.

      .. note:: Defining this callback without a matching ``get`` one is invalid.
   :type set: Callable[[:class:`bpy.types.bpy_struct`, int], None]
   :arg get_transform: Function to be called when this value is 'read',
      if some additional processing must be performed on the stored value.
      This function must take three arguments (self, the stored value,
      and a boolean indicating if the property is currently set),
      and return the final, transformed value of the property.

      .. note:: The callback is responsible to ensure that value limits of the property (min/max, length...) are respected. Otherwise a ValueError exception is raised.

   :type get_transform: Callable[[:class:`bpy.types.bpy_struct`, int, bool], int]
   :arg set_transform: Function to be called when this value is 'written',
      if some additional processing must be performed on the given value before storing it.
      This function must take four arguments (self, the given value to store,
      the currently stored value ('raw' value, without any ``get_transform`` applied to it),
      and a boolean indicating if the property is currently set),
      and return the final, transformed value of the property.

      .. note:: The callback is responsible to ensure that value limits (min/max, length...) are respected. Otherwise a ValueError exception is raised.

   :type set_transform: Callable[[:class:`bpy.types.bpy_struct`, int, int, bool], int]


    Online Documentation:
    https://docs.blender.org/api/current/bpy.props.html"""
    ...

def FloatProperty(*args, **kwargs) -> Any:
    """.. function:: FloatProperty(*, name="", description="", translation_context="*", default=0.0, min=-3.402823e+38, max=3.402823e+38, soft_min=-3.402823e+38, soft_max=3.402823e+38, step=3, precision=2, options={'ANIMATABLE'}, override=set(), tags=set(), subtype='NONE', unit='NONE', update=None, get=None, set=None, get_transform=None, set_transform=None)

   Returns a new float (single precision) property definition.

   :arg name: Name used in the user interface.
   :type name: str
   :arg description: Text used for the tooltip and api documentation.
   :type description: str
   :arg translation_context: Text used as context to disambiguate translations.
   :type translation_context: str
   :arg min: Hard minimum, trying to assign a value below will silently assign this minimum instead.
   :type min: float
   :arg max: Hard maximum, trying to assign a value above will silently assign this maximum instead.
   :type max: float
   :arg soft_min: Soft minimum (>= *min*), user won't be able to drag the widget below this value in the UI.
   :type soft_min: float
   :arg soft_max: Soft maximum (<= *max*), user won't be able to drag the widget above this value in the UI.
   :type soft_max: float
   :arg step: Step of increment/decrement in UI, in [1, 100], defaults to 3 (WARNING: actual value is /100).
   :type step: int
   :arg precision: Maximum number of decimal digits to display, in [0, 6]. Fraction is automatically hidden for exact integer values of fields with unit 'NONE' or 'TIME' (frame count) and step divisible by 100.
   :type precision: int
   :arg options: Enumerator in :ref:`rna_enum_property_flag_items`.
   :type options: set[str]
   :arg override: Enumerator in :ref:`rna_enum_property_override_flag_items`.
   :type override: set[str]
   :arg tags: Enumerator of tags that are defined by parent class.
   :type tags: set[str]
   :arg subtype: Enumerator in :ref:`rna_enum_property_subtype_number_items`.
   :type subtype: str
   :arg unit: Enumerator in :ref:`rna_enum_property_unit_items`.
   :type unit: str
   :arg update: Function to be called when this value is modified,
      This function must take 2 values (self, context) and return None.
      *Warning* there are no safety checks to avoid infinite recursion.
   :type update: Callable[[:class:`bpy.types.bpy_struct`, :class:`bpy.types.Context`], None]
   :arg get: Function to be called when this value is 'read', and the default,
      system-defined storage is not used for this property.
      This function must take 1 value (self) and return the value of the property.

      .. note:: Defining this callback without a matching ``set`` one will make the property read-only (even if ``READ_ONLY`` option is not set).
   :type get: Callable[[:class:`bpy.types.bpy_struct`], float]
   :arg set: Function to be called when this value is 'written', and the default,
      system-defined storage is not used for this property.
      This function must take 2 values (self, value) and return None.

      .. note:: Defining this callback without a matching ``get`` one is invalid.
   :type set: Callable[[:class:`bpy.types.bpy_struct`, float], None]
   :arg get_transform: Function to be called when this value is 'read',
      if some additional processing must be performed on the stored value.
      This function must take three arguments (self, the stored value,
      and a boolean indicating if the property is currently set),
      and return the final, transformed value of the property.

      .. note:: The callback is responsible to ensure that value limits of the property (min/max, length...) are respected. Otherwise a ValueError exception is raised.

   :type get_transform: Callable[[:class:`bpy.types.bpy_struct`, float, bool], float]
   :arg set_transform: Function to be called when this value is 'written',
      if some additional processing must be performed on the given value before storing it.
      This function must take four arguments (self, the given value to store,
      the currently stored value ('raw' value, without any ``get_transform`` applied to it),
      and a boolean indicating if the property is currently set),
      and return the final, transformed value of the property.

      .. note:: The callback is responsible to ensure that value limits (min/max, length...) are respected. Otherwise a ValueError exception is raised.

   :type set_transform: Callable[[:class:`bpy.types.bpy_struct`, float, float, bool], float]


    Online Documentation:
    https://docs.blender.org/api/current/bpy.props.html"""
    ...

def FloatVectorProperty(*args, **kwargs) -> Any:
    """.. function:: FloatVectorProperty(*, name="", description="", translation_context="*", default=(0.0, 0.0, 0.0), min=sys.float_info.min, max=sys.float_info.max, soft_min=sys.float_info.min, soft_max=sys.float_info.max, step=3, precision=2, options={'ANIMATABLE'}, override=set(), tags=set(), subtype='NONE', unit='NONE', size=3, update=None, get=None, set=None)

   Returns a new vector float property definition.

   :arg name: Name used in the user interface.
   :type name: str
   :arg description: Text used for the tooltip and api documentation.
   :type description: str
   :arg translation_context: Text used as context to disambiguate translations.
   :type translation_context: str
   :arg default: Sequence of floats the length of *size*.
   :type default: Sequence[float]
   :arg min: Hard minimum, trying to assign a value below will silently assign this minimum instead.
   :type min: float
   :arg max: Hard maximum, trying to assign a value above will silently assign this maximum instead.
   :type max: float
   :arg soft_min: Soft minimum (>= *min*), user won't be able to drag the widget below this value in the UI.
   :type soft_min: float
   :arg soft_max: Soft maximum (<= *max*), user won't be able to drag the widget above this value in the UI.
   :type soft_max: float
   :arg options: Enumerator in :ref:`rna_enum_property_flag_items`.
   :type options: set[str]
   :arg override: Enumerator in :ref:`rna_enum_property_override_flag_items`.
   :type override: set[str]
   :arg tags: Enumerator of tags that are defined by parent class.
   :type tags: set[str]
   :arg step: Step of increment/decrement in UI, in [1, 100], defaults to 3 (WARNING: actual value is /100).
   :type step: int
   :arg precision: Maximum number of decimal digits to display, in [0, 6]. Fraction is automatically hidden for exact integer values of fields with unit 'NONE' or 'TIME' (frame count) and step divisible by 100.
   :type precision: int
   :arg subtype: Enumerator in :ref:`rna_enum_property_subtype_number_array_items`.
   :type subtype: str
   :arg unit: Enumerator in :ref:`rna_enum_property_unit_items`.
   :type unit: str
   :arg size: Vector dimensions in [1, 32]. An int sequence can be used to define multi-dimension arrays.
   :type size: int | Sequence[int]
   :arg update: Function to be called when this value is modified,
      This function must take 2 values (self, context) and return None.
      *Warning* there are no safety checks to avoid infinite recursion.
   :type update: Callable[[:class:`bpy.types.bpy_struct`, :class:`bpy.types.Context`], None]
   :arg get: Function to be called when this value is 'read', and the default,
      system-defined storage is not used for this property.
      This function must take 1 value (self) and return the value of the property.

      .. note:: Defining this callback without a matching ``set`` one will make the property read-only (even if ``READ_ONLY`` option is not set).
   :type get: Callable[[:class:`bpy.types.bpy_struct`], Sequence[float]]
   :arg set: Function to be called when this value is 'written', and the default,
      system-defined storage is not used for this property.
      This function must take 2 values (self, value) and return None.

      .. note:: Defining this callback without a matching ``get`` one is invalid.
   :type set: Callable[[:class:`bpy.types.bpy_struct`, tuple[float, ...]], None]
   :arg get_transform: Function to be called when this value is 'read',
      if some additional processing must be performed on the stored value.
      This function must take three arguments (self, the stored value,
      and a boolean indicating if the property is currently set),
      and return the final, transformed value of the property.

      .. note:: The callback is responsible to ensure that value limits of the property (min/max, length...) are respected. Otherwise a ValueError exception is raised.

   :type get_transform: Callable[[:class:`bpy.types.bpy_struct`, Sequence[float], bool], Sequence[float]]
   :arg set_transform: Function to be called when this value is 'written',
      if some additional processing must be performed on the given value before storing it.
      This function must take four arguments (self, the given value to store,
      the currently stored value ('raw' value, without any ``get_transform`` applied to it),
      and a boolean indicating if the property is currently set),
      and return the final, transformed value of the property.

      .. note:: The callback is responsible to ensure that value limits (min/max, length...) are respected. Otherwise a ValueError exception is raised.

   :type set_transform: Callable[[:class:`bpy.types.bpy_struct`, Sequence[float], Sequence[float], bool], Sequence[float]]


    Online Documentation:
    https://docs.blender.org/api/current/bpy.props.html"""
    ...

def IntProperty(*args, **kwargs) -> Any:
    """.. function:: IntProperty(*, name="", description="", translation_context="*", default=0, min=-2**31, max=2**31-1, soft_min=-2**31, soft_max=2**31-1, step=1, options={'ANIMATABLE'}, override=set(), tags=set(), subtype='NONE', update=None, get=None, set=None, get_transform=None, set_transform=None)

   Returns a new int property definition.

   :arg name: Name used in the user interface.
   :type name: str
   :arg description: Text used for the tooltip and api documentation.
   :type description: str
   :arg translation_context: Text used as context to disambiguate translations.
   :type translation_context: str
   :arg min: Hard minimum, trying to assign a value below will silently assign this minimum instead.
   :type min: int
   :arg max: Hard maximum, trying to assign a value above will silently assign this maximum instead.
   :type max: int
   :arg soft_min: Soft minimum (>= *min*), user won't be able to drag the widget below this value in the UI.
   :type soft_min: int
   :arg soft_max: Soft maximum (<= *max*), user won't be able to drag the widget above this value in the UI.
   :type soft_max: int
   :arg step: Step of increment/decrement in UI, in [1, 100], defaults to 1 (WARNING: unused currently!).
   :type step: int
   :arg options: Enumerator in :ref:`rna_enum_property_flag_items`.
   :type options: set[str]
   :arg override: Enumerator in :ref:`rna_enum_property_override_flag_items`.
   :type override: set[str]
   :arg tags: Enumerator of tags that are defined by parent class.
   :type tags: set[str]
   :arg subtype: Enumerator in :ref:`rna_enum_property_subtype_number_items`.
   :type subtype: str
   :arg update: Function to be called when this value is modified,
      This function must take 2 values (self, context) and return None.
      *Warning* there are no safety checks to avoid infinite recursion.
   :type update: Callable[[:class:`bpy.types.bpy_struct`, :class:`bpy.types.Context`], None]
   :arg get: Function to be called when this value is 'read', and the default,
      system-defined storage is not used for this property.
      This function must take 1 value (self) and return the value of the property.

      .. note:: Defining this callback without a matching ``set`` one will make the property read-only (even if ``READ_ONLY`` option is not set).
   :type get: Callable[[:class:`bpy.types.bpy_struct`], int]
   :arg set: Function to be called when this value is 'written', and the default,
      system-defined storage is not used for this property.
      This function must take 2 values (self, value) and return None.

      .. note:: Defining this callback without a matching ``get`` one is invalid.
   :type set: Callable[[:class:`bpy.types.bpy_struct`, int], None]
   :arg get_transform: Function to be called when this value is 'read',
      if some additional processing must be performed on the stored value.
      This function must take three arguments (self, the stored value,
      and a boolean indicating if the property is currently set),
      and return the final, transformed value of the property.

      .. note:: The callback is responsible to ensure that value limits of the property (min/max, length...) are respected. Otherwise a ValueError exception is raised.

   :type get_transform: Callable[[:class:`bpy.types.bpy_struct`, int, bool], int]
   :arg set_transform: Function to be called when this value is 'written',
      if some additional processing must be performed on the given value before storing it.
      This function must take four arguments (self, the given value to store,
      the currently stored value ('raw' value, without any ``get_transform`` applied to it),
      and a boolean indicating if the property is currently set),
      and return the final, transformed value of the property.

      .. note:: The callback is responsible to ensure that value limits (min/max, length...) are respected. Otherwise a ValueError exception is raised.

   :type set_transform: Callable[[:class:`bpy.types.bpy_struct`, int, int, bool], int]


    Online Documentation:
    https://docs.blender.org/api/current/bpy.props.html"""
    ...

def IntVectorProperty(*args, **kwargs) -> Any:
    """.. function:: IntVectorProperty(*, name="", description="", translation_context="*", default=(0, 0, 0), min=-2**31, max=2**31-1, soft_min=-2**31, soft_max=2**31-1, step=1, options={'ANIMATABLE'}, override=set(), tags=set(), subtype='NONE', size=3, update=None, get=None, set=None, get_transform=None, set_transform=None)

   Returns a new vector int property definition.

   :arg name: Name used in the user interface.
   :type name: str
   :arg description: Text used for the tooltip and api documentation.
   :type description: str
   :arg translation_context: Text used as context to disambiguate translations.
   :type translation_context: str
   :arg default: sequence of ints the length of *size*.
   :type default: Sequence[int]
   :arg min: Hard minimum, trying to assign a value below will silently assign this minimum instead.
   :type min: int
   :arg max: Hard maximum, trying to assign a value above will silently assign this maximum instead.
   :type max: int
   :arg soft_min: Soft minimum (>= *min*), user won't be able to drag the widget below this value in the UI.
   :type soft_min: int
   :arg soft_max: Soft maximum (<= *max*), user won't be able to drag the widget above this value in the UI.
   :type soft_max: int
   :arg step: Step of increment/decrement in UI, in [1, 100], defaults to 1 (WARNING: unused currently!).
   :type step: int
   :arg options: Enumerator in :ref:`rna_enum_property_flag_items`.
   :type options: set[str]
   :arg override: Enumerator in :ref:`rna_enum_property_override_flag_items`.
   :type override: set[str]
   :arg tags: Enumerator of tags that are defined by parent class.
   :type tags: set[str]
   :arg subtype: Enumerator in :ref:`rna_enum_property_subtype_number_array_items`.
   :type subtype: str
   :arg size: Vector dimensions in [1, 32]. An int sequence can be used to define multi-dimension arrays.
   :type size: int | Sequence[int]
   :arg update: Function to be called when this value is modified,
      This function must take 2 values (self, context) and return None.
      *Warning* there are no safety checks to avoid infinite recursion.
   :type update: Callable[[:class:`bpy.types.bpy_struct`, :class:`bpy.types.Context`], None]
   :arg get: Function to be called when this value is 'read', and the default,
      system-defined storage is not used for this property.
      This function must take 1 value (self) and return the value of the property.

      .. note:: Defining this callback without a matching ``set`` one will make the property read-only (even if ``READ_ONLY`` option is not set).
   :type get: Callable[[:class:`bpy.types.bpy_struct`], Sequence[int]]
   :arg set: Function to be called when this value is 'written', and the default,
      system-defined storage is not used for this property.
      This function must take 2 values (self, value) and return None.

      .. note:: Defining this callback without a matching ``get`` one is invalid.
   :type set: Callable[[:class:`bpy.types.bpy_struct`, tuple[int, ...]], None]
   :arg get_transform: Function to be called when this value is 'read',
      if some additional processing must be performed on the stored value.
      This function must take three arguments (self, the stored value,
      and a boolean indicating if the property is currently set),
      and return the final, transformed value of the property.

      .. note:: The callback is responsible to ensure that value limits of the property (min/max, length...) are respected. Otherwise a ValueError exception is raised.

   :type get_transform: Callable[[:class:`bpy.types.bpy_struct`, Sequence[int], bool], Sequence[int]]
   :arg set_transform: Function to be called when this value is 'written',
      if some additional processing must be performed on the given value before storing it.
      This function must take four arguments (self, the given value to store,
      the currently stored value ('raw' value, without any ``get_transform`` applied to it),
      and a boolean indicating if the property is currently set),
      and return the final, transformed value of the property.

      .. note:: The callback is responsible to ensure that value limits (min/max, length...) are respected. Otherwise a ValueError exception is raised.

   :type set_transform: Callable[[:class:`bpy.types.bpy_struct`, Sequence[int], Sequence[int], bool], Sequence[int]]


    Online Documentation:
    https://docs.blender.org/api/current/bpy.props.html"""
    ...

def PointerProperty(*args, **kwargs) -> Any:
    """.. function:: PointerProperty(type, *, name="", description="", translation_context="*", options={'ANIMATABLE'}, override=set(), tags=set(), poll=None, update=None)

   Returns a new pointer property definition.

   :arg type: A subclass of a property group or ID types.
   :type type: type[:class:`bpy.types.PropertyGroup` | :class:`bpy.types.ID`]
   :arg name: Name used in the user interface.
   :type name: str
   :arg description: Text used for the tooltip and api documentation.
   :type description: str
   :arg translation_context: Text used as context to disambiguate translations.
   :type translation_context: str
   :arg options: Enumerator in :ref:`rna_enum_property_flag_items`.
   :type options: set[str]
   :arg override: Enumerator in :ref:`rna_enum_property_override_flag_items`.
   :type override: set[str]
   :arg tags: Enumerator of tags that are defined by parent class.
   :type tags: set[str]
   :arg poll: Function that determines whether an item is valid for this property.
      The function must take 2 values (self, object) and return a boolean.

      .. note:: The return value will be checked only when assigning an item from the UI, but it is still possible to assign an "invalid" item to the property directly.

   :type poll: Callable[[:class:`bpy.types.bpy_struct`, :class:`bpy.types.ID`], bool]
   :arg update: Function to be called when this value is modified,
      This function must take 2 values (self, context) and return None.
      *Warning* there are no safety checks to avoid infinite recursion.
   :type update: Callable[[:class:`bpy.types.bpy_struct`, :class:`bpy.types.Context`], None]

.. note:: Pointer properties do not support storing references to embedded IDs (e.g. :class:`bpy.types.Scene.collection`, :class:`bpy.types.Material.node_tree`).
   These should exclusively be referenced and accessed through their owner ID (e.g. the scene or material).


    Online Documentation:
    https://docs.blender.org/api/current/bpy.props.html"""
    ...

def RemoveProperty(*args, **kwargs) -> Any:
    """.. function:: RemoveProperty(cls, attr)

   Removes a dynamically defined property.

   :arg cls: The class containing the property (must be a positional argument).
   :type cls: type
   :arg attr: Property name (must be passed as a keyword).
   :type attr: str

.. note:: Typically this function doesn't need to be accessed directly.
   Instead use ``del cls.attr``


    Online Documentation:
    https://docs.blender.org/api/current/bpy.props.html"""
    ...

def StringProperty(*args, **kwargs) -> Any:
    """.. function:: StringProperty(*, name="", description="", translation_context="*", default="", maxlen=0, options={'ANIMATABLE'}, override=set(), tags=set(), subtype='NONE', update=None, get=None, set=None, get_transform=None, set_transform=None, search=None, search_options={'SUGGESTION'})

   Returns a new string property definition.

   :arg name: Name used in the user interface.
   :type name: str
   :arg description: Text used for the tooltip and api documentation.
   :type description: str
   :arg translation_context: Text used as context to disambiguate translations.
   :type translation_context: str
   :arg default: initializer string.
   :type default: str
   :arg maxlen: maximum length of the string.
   :type maxlen: int
   :arg options: Enumerator in :ref:`rna_enum_property_flag_items`.
   :type options: set[str]
   :arg override: Enumerator in :ref:`rna_enum_property_override_flag_items`.
   :type override: set[str]
   :arg tags: Enumerator of tags that are defined by parent class.
   :type tags: set[str]
   :arg subtype: Enumerator in :ref:`rna_enum_property_subtype_string_items`.
   :type subtype: str
   :arg update: Function to be called when this value is modified,
      This function must take 2 values (self, context) and return None.
      *Warning* there are no safety checks to avoid infinite recursion.
   :type update: Callable[[:class:`bpy.types.bpy_struct`, :class:`bpy.types.Context`], None]
   :arg get: Function to be called when this value is 'read', and the default,
      system-defined storage is not used for this property.
      This function must take 1 value (self) and return the value of the property.

      .. note:: Defining this callback without a matching ``set`` one will make the property read-only (even if ``READ_ONLY`` option is not set).
   :type get: Callable[[:class:`bpy.types.bpy_struct`], str]
   :arg set: Function to be called when this value is 'written', and the default,
      system-defined storage is not used for this property.
      This function must take 2 values (self, value) and return None.

      .. note:: Defining this callback without a matching ``get`` one is invalid.
   :type set: Callable[[:class:`bpy.types.bpy_struct`, str], None]
   :arg get_transform: Function to be called when this value is 'read',
      if some additional processing must be performed on the stored value.
      This function must take three arguments (self, the stored value,
      and a boolean indicating if the property is currently set),
      and return the final, transformed value of the property.

      .. note:: The callback is responsible to ensure that value limits of the property (min/max, length...) are respected. Otherwise a ValueError exception is raised.

   :type get_transform: Callable[[:class:`bpy.types.bpy_struct`, str, bool], str]
   :arg set_transform: Function to be called when this value is 'written',
      if some additional processing must be performed on the given value before storing it.
      This function must take four arguments (self, the given value to store,
      the currently stored value ('raw' value, without any ``get_transform`` applied to it),
      and a boolean indicating if the property is currently set),
      and return the final, transformed value of the property.

      .. note:: The callback is responsible to ensure that value limits (min/max, length...) are respected. Otherwise a ValueError exception is raised.

   :type set_transform: Callable[[:class:`bpy.types.bpy_struct`, str, str, bool], str]
   :arg search: Function to be called to show candidates for this string (shown in the UI).
      This function must take 3 values (self, context, edit_text)
      and return a sequence, iterator or generator where each item must be:

      - A single string (representing a candidate to display).
      - A tuple-pair of strings, where the first is a candidate and the second
        is additional information about the candidate.
   :type search: Callable[[:class:`bpy.types.bpy_struct`, :class:`bpy.types.Context`, str], Iterable[str | tuple[str, str]]]
   :arg search_options: Set of strings in:

      - 'SORT' sorts the resulting items.
      - 'SUGGESTION' lets the user enter values not found in search candidates.
        **WARNING** disabling this flag causes the search callback to run on redraw,
        so only disable this flag if it's not likely to cause performance issues.

   :type search_options: set[str]


    Online Documentation:
    https://docs.blender.org/api/current/bpy.props.html"""
    ...
