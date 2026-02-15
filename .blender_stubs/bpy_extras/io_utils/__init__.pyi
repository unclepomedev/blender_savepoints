# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy_extras.io_utils.html
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
    https://docs.blender.org/api/current/bpy_extras.io_utils.html"""
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
    https://docs.blender.org/api/current/bpy_extras.io_utils.html"""
    ...

class ExportHelper:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy_extras.io_utils.html"""
    def __init__(self, /, *args, **kwargs) -> Any: ...
    def check(self, _context) -> Any: ...
    def invoke(self, context, _event) -> Any: ...

class ImportHelper:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy_extras.io_utils.html"""
    def __init__(self, /, *args, **kwargs) -> Any: ...
    def check(self, _context) -> Any: ...
    def invoke(self, context, _event) -> Any: ...
    def invoke_popup(self, context, confirm_text='') -> Any: ...

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
    https://docs.blender.org/api/current/bpy_extras.io_utils.html"""
    ...

def axis_conversion(from_forward='Y', from_up='Z', to_forward='Y', to_up='Z') -> Any:
    """
    Each argument is an axis in ['X', 'Y', 'Z', '-X', '-Y', '-Z']
    where the first 2 are a source and the second 2 are the target.
    :rtype: :class:`mathutils.Matrix`
    

    Online Documentation:
    https://docs.blender.org/api/current/bpy_extras.io_utils.html"""
    ...

def axis_conversion_ensure(operator, forward_attr, up_attr) -> Any:
    """
    Function to ensure an operator has valid axis conversion settings, intended
    to be used from :class:`bpy.types.Operator.check`.

    :arg operator: the operator to access axis attributes from.
    :type operator: :class:`bpy.types.Operator`
    :arg forward_attr: attribute storing the forward axis
    :type forward_attr: str
    :arg up_attr: attribute storing the up axis
    :type up_attr: str
    :return: True if the value was modified.
    :rtype: bool
    

    Online Documentation:
    https://docs.blender.org/api/current/bpy_extras.io_utils.html"""
    ...

def create_derived_objects(depsgraph, objects) -> Any:
    """
    This function takes a sequence of objects, returning their instances.

    :arg depsgraph: The evaluated depsgraph.
    :type depsgraph: :class:`bpy.types.Depsgraph`
    :arg objects: A sequencer of objects.
    :type objects: Sequence[:class:`bpy.types.Object`]
    :return: A dictionary where each key is an object from ``objects``,
       values are lists of (object, matrix) tuples representing instances.
    :rtype: dict[:class:`bpy.types.Object`, list[tuple[:class:`bpy.types.Object`, :class:`mathutils.Matrix`]]]
    

    Online Documentation:
    https://docs.blender.org/api/current/bpy_extras.io_utils.html"""
    ...

def data_(*args, **kwargs) -> Any:
    """.. method:: pgettext_data(msgid, msgctxt=None)

   Try to translate the given msgid (with optional msgctxt), if new data name's translation is enabled.

   .. note::
      See :func:`pgettext` notes.

   :arg msgid: The string to translate.
   :type msgid: str
   :arg msgctxt: The translation context (defaults to BLT_I18NCONTEXT_DEFAULT).
   :type msgctxt: str | None
   :return: The translated string (or ``msgid`` if no translation was found).



    Online Documentation:
    https://docs.blender.org/api/current/bpy_extras.io_utils.html"""
    ...

i18n_contexts: Any
def iface_(*args, **kwargs) -> Any:
    """.. method:: pgettext_iface(msgid, msgctxt=None)

   Try to translate the given msgid (with optional msgctxt), if labels' translation is enabled.

   .. note::
      See :func:`pgettext` notes.

   :arg msgid: The string to translate.
   :type msgid: str
   :arg msgctxt: The translation context (defaults to BLT_I18NCONTEXT_DEFAULT).
   :type msgctxt: str | None
   :return: The translated string (or msgid if no translation was found).



    Online Documentation:
    https://docs.blender.org/api/current/bpy_extras.io_utils.html"""
    ...

def orientation_helper(axis_forward='Y', axis_up='Z') -> Any:
    """
    A decorator for import/export classes, generating properties needed by the axis conversion system and IO helpers,
    with specified default values (axes).
    

    Online Documentation:
    https://docs.blender.org/api/current/bpy_extras.io_utils.html"""
    ...

def path_reference(filepath, base_src, base_dst, mode='AUTO', copy_subdir='', copy_set=None, library=None) -> Any:
    """
    Return a filepath relative to a destination directory, for use with
    exporters.

    :arg filepath: the file path to return,
       supporting blenders relative '//' prefix.
    :type filepath: str
    :arg base_src: the directory the *filepath* is relative too
       (normally the blend file).
    :type base_src: str
    :arg base_dst: the directory the *filepath* will be referenced from
       (normally the export path).
    :type base_dst: str
    :arg mode: the method used get the path in
       ['AUTO', 'ABSOLUTE', 'RELATIVE', 'MATCH', 'STRIP', 'COPY']
    :type mode: str
    :arg copy_subdir: the subdirectory of *base_dst* to use when mode='COPY'.
    :type copy_subdir: str
    :arg copy_set: collect from/to pairs when mode='COPY',
       pass to *path_reference_copy* when exporting is done.
    :type copy_set: set[tuple[str, str]]
    :arg library: The library this path is relative to.
    :type library: :class:`bpy.types.Library` | None
    :return: the new filepath.
    :rtype: str
    

    Online Documentation:
    https://docs.blender.org/api/current/bpy_extras.io_utils.html"""
    ...

def path_reference_copy(copy_set, report=<built-in function print>) -> Any:
    """
    Execute copying files of path_reference

    :arg copy_set: set of (from, to) pairs to copy.
    :type copy_set: set[tuple[str, str]]
    :arg report: function used for reporting warnings, takes a string argument.
    :type report: Callable[[str], None]
    

    Online Documentation:
    https://docs.blender.org/api/current/bpy_extras.io_utils.html"""
    ...

path_reference_mode: Any
def poll_file_object_drop(context) -> Any:
    """
    A default implementation for FileHandler poll_drop methods. Allows for both the 3D Viewport and
    the Outliner (in ViewLayer display mode) to be targets for file drag and drop.
    

    Online Documentation:
    https://docs.blender.org/api/current/bpy_extras.io_utils.html"""
    ...

def unique_name(key, name, name_dict, name_max=-1, clean_func=None, sep='.') -> Any:
    """
    Helper function for storing unique names which may have special characters
    stripped and restricted to a maximum length.

    :arg key: Unique item this name belongs to, name_dict[key] will be reused
       when available.
       This can be the object, mesh, material, etc instance itself.
       Any hashable object associated with the *name*.
    :type key: Any
    :arg name: The name used to create a unique value in *name_dict*.
    :type name: str
    :arg name_dict: This is used to cache namespace to ensure no collisions
       occur, this should be an empty dict initially and only modified by this
       function.
    :type name_dict: dict
    :arg clean_func: Function to call on *name* before creating a unique value.
    :type clean_func: function
    :arg sep: Separator to use when between the name and a number when a
       duplicate name is found.
    :type sep: str
    

    Online Documentation:
    https://docs.blender.org/api/current/bpy_extras.io_utils.html"""
    ...

def unpack_face_list(list_of_tuples) -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy_extras.io_utils.html"""
    ...

def unpack_list(list_of_tuples) -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy_extras.io_utils.html"""
    ...
