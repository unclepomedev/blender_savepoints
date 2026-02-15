# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy_extras.object_utils.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated


class AddObjectHelper:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy_extras.object_utils.html"""
    def __init__(self, /, *args, **kwargs) -> Any: ...
    def align_update_callback(self, _context) -> Any: ...
    def poll(context) -> Any: ...

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
    https://docs.blender.org/api/current/bpy_extras.object_utils.html"""
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
    https://docs.blender.org/api/current/bpy_extras.object_utils.html"""
    ...

def add_object_align_init(context, operator) -> Any:
    """
    Return a matrix using the operator settings and view context.

    :arg context: The context to use.
    :type context: :class:`bpy.types.Context`
    :arg operator: The operator, checked for location and rotation properties.
    :type operator: :class:`bpy.types.Operator`
    :return: the matrix from the context and settings.
    :rtype: :class:`mathutils.Matrix`
    

    Online Documentation:
    https://docs.blender.org/api/current/bpy_extras.object_utils.html"""
    ...

annotations: Any
def object_add_grid_scale(context) -> Any:
    """
    Return scale which should be applied on object
    data to align it to grid scale
    

    Online Documentation:
    https://docs.blender.org/api/current/bpy_extras.object_utils.html"""
    ...

def object_add_grid_scale_apply_operator(operator, context) -> Any:
    """
    Scale an operators distance values by the grid size.
    

    Online Documentation:
    https://docs.blender.org/api/current/bpy_extras.object_utils.html"""
    ...

def object_data_add(context, obdata, operator=None, name=None) -> Any:
    """
    Add an object using the view context and preference to initialize the
    location, rotation and layer.

    :arg context: The context to use.
    :type context: :class:`bpy.types.Context`
    :arg obdata: Valid object data to used for the new object or None.
    :type obdata: :class:`bpy.types.ID` | None
    :arg operator: The operator, checked for location and rotation properties.
    :type operator: :class:`bpy.types.Operator`
    :arg name: Optional name
    :type name: str
    :return: the newly created object in the scene.
    :rtype: :class:`bpy.types.Object`
    

    Online Documentation:
    https://docs.blender.org/api/current/bpy_extras.object_utils.html"""
    ...

def object_report_if_active_shape_key_is_locked(obj, operator) -> Any:
    """
    Checks if the active shape key of the specified object is locked, and reports an error if so.

    If the object has no shape keys, there is nothing to lock, and the function returns False.

    :arg obj: Object to check.
    :type obj: :class:`bpy.types.Object`
    :arg operator: Currently running operator to report the error through. Use None to suppress emitting the message.
    :type operator: :class:`bpy.types.Operator`
    :return: True if the shape key was locked.
    

    Online Documentation:
    https://docs.blender.org/api/current/bpy_extras.object_utils.html"""
    ...

def world_to_camera_view(scene, obj, coord) -> Any:
    """
    Returns the camera space coords for a 3d point.
    (also known as: normalized device coordinates - NDC).

    Where (0, 0) is the bottom left and (1, 1)
    is the top right of the camera frame.
    values outside 0-1 are also supported.
    A negative 'z' value means the point is behind the camera.

    Takes shift-x/y, lens angle and sensor size into account
    as well as perspective/ortho projections.

    :arg scene: Scene to use for frame size.
    :type scene: :class:`bpy.types.Scene`
    :arg obj: Camera object.
    :type obj: :class:`bpy.types.Object`
    :arg coord: World space location.
    :type coord: :class:`mathutils.Vector`
    :return: a vector where X and Y map to the view plane and
       Z is the depth on the view axis.
    :rtype: :class:`mathutils.Vector`
    

    Online Documentation:
    https://docs.blender.org/api/current/bpy_extras.object_utils.html"""
    ...
