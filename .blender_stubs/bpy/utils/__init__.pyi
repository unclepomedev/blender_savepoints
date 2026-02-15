# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.utils.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated


def app_template_paths(*, path=None) -> Any:
    """
    Returns valid application template paths.

    :arg path: Optional subdir.
    :type path: str
    :return: App template paths.
    :rtype: Iterator[str]
    

    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html"""
    ...

def blend_paths(*args, **kwargs) -> Any:
    """.. function:: blend_paths(*, absolute=False, packed=False, local=False)

   Returns a list of paths to external files referenced by the loaded .blend file.

   :arg absolute: When true the paths returned are made absolute.
   :type absolute: bool
   :arg packed: When true skip file paths for packed data.
   :type packed: bool
   :arg local: When true skip linked library paths.
   :type local: bool
   :return: path list.
   :rtype: list[str]


    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html"""
    ...

def escape_identifier(*args, **kwargs) -> Any:
    """.. function:: escape_identifier(string)

   Simple string escaping function used for animation paths.

   :arg string: text
   :type string: str
   :return: The escaped string.
   :rtype: str


    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html"""
    ...

def execfile(filepath, *, mod=None) -> Any:
    """
    Execute a file path as a Python script.

    :arg filepath: Path of the script to execute.
    :type filepath: str
    :arg mod: Optional cached module, the result of a previous execution.
    :type mod: ModuleType | None
    :return: The module which can be passed back in as ``mod``.
    :rtype: ModuleType
    

    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html"""
    ...

def expose_bundled_modules() -> Any:
    """
    For Blender as a Python module, add bundled VFX library python bindings
    to ``sys.path``. These may be used instead of dedicated packages, to ensure
    the libraries are compatible with Blender.
    

    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html"""
    ...

def extension_path_user(package, *, path='', create=False) -> Any:
    """
    Return a user writable directory associated with an extension.

    .. note::

       This allows each extension to have its own user directory to store files.

       The location of the extension it self is not a suitable place to store files
       because it is cleared each upgrade and the users may not have write permissions
       to the repository (typically "System" repositories).

    :arg package: The ``__package__`` of the extension.
    :type package: str
    :arg path: Optional subdirectory.
    :type path: str
    :arg create: Treat the path as a directory and create it if its not existing.
    :type create: bool
    :return: a path.
    :rtype: str
    

    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html"""
    ...

def flip_name(*args, **kwargs) -> Any:
    """.. function:: flip_name(name, *, strip_digits=False)

   Flip a name between left/right sides, useful for 
   mirroring bone names.

   :arg name: Bone name to flip.
   :type name: str
   :arg strip_digits: Whether to remove ``.###`` suffix.
   :type strip_digits: bool
   :return: The flipped name.
   :rtype: str


    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html"""
    ...

def is_path_builtin(path) -> Any:
    """
    Returns True if the path is one of the built-in paths used by Blender.

    :arg path: Path you want to check if it is in the built-in settings directory
    :type path: str
    :rtype: bool
    

    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html"""
    ...

def is_path_extension(path) -> Any:
    """
    Returns True if the path is from an extensions repository.

    :arg path: Path to check if it is within an extension repository.
    :type path: str
    :rtype: bool
    

    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html"""
    ...

def keyconfig_init() -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html"""
    ...

def keyconfig_set(filepath, *, report=None) -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html"""
    ...

def load_scripts(*, reload_scripts=False, refresh_scripts=False, extensions=True) -> Any:
    """
    Load scripts and run each modules register function.

    :arg reload_scripts: Causes all scripts to have their unregister method
       called before loading.
    :type reload_scripts: bool
    :arg refresh_scripts: only load scripts which are not already loaded
       as modules.
    :type refresh_scripts: bool
    :arg extensions: Loads additional scripts (add-ons & app-templates).
    :type extensions: bool
    

    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html"""
    ...

def load_scripts_extensions(*, reload_scripts=False) -> Any:
    """
    Load extensions scripts (add-ons and app-templates)

    :arg reload_scripts: Causes all scripts to have their unregister method
       called before loading.
    :type reload_scripts: bool
    

    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html"""
    ...

def make_rna_paths(struct_name, prop_name, enum_name) -> Any:
    """
    Create RNA "paths" from given names.

    :arg struct_name: Name of a RNA struct (like e.g. "Scene").
    :type struct_name: str
    :arg prop_name: Name of a RNA struct's property.
    :type prop_name: str
    :arg enum_name: Name of a RNA enum identifier.
    :type enum_name: str
    :return: A triple of three "RNA paths"
       (most_complete_path, "struct.prop", "struct.prop:'enum'").
       If no enum_name is given, the third element will always be void.
    :rtype: tuple[str, str, str]
    

    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html"""
    ...

def manual_language_code(default='en') -> Any:
    """
    :return:
       The language code used for user manual URL component based on the current language user-preference,
       falling back to the ``default`` when unavailable.
    :rtype: str
    

    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html"""
    ...

def manual_map() -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html"""
    ...

def modules_from_path(path, loaded_modules) -> Any:
    """
    Load all modules in a path and return them as a list.

    :arg path: this path is scanned for scripts and packages.
    :type path: str
    :arg loaded_modules: already loaded module names, files matching these
       names will be ignored.
    :type loaded_modules: set[ModuleType]
    :return: all loaded modules.
    :rtype: list[ModuleType]
    

    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html"""
    ...

def preset_find(name, preset_path, *, display_name=False, ext='.py') -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html"""
    ...

def preset_paths(subdir) -> Any:
    """
    Returns a list of paths for a specific preset.

    :arg subdir: preset subdirectory (must not be an absolute path).
    :type subdir: str
    :return: Script paths.
    :rtype: list[str]
    

    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html"""
    ...

def refresh_script_paths() -> Any:
    """
    Run this after creating new script paths to update sys.path
    

    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html"""
    ...

def register_class(*args, **kwargs) -> Any:
    """.. function:: register_class(cls)

   Register a subclass of a Blender type class.

   :arg cls: Registerable Blender class type.
   :type cls: type[:class:`bpy.types.Panel` | :class:`bpy.types.UIList` | :class:`bpy.types.Menu` | :class:`bpy.types.Header` | :class:`bpy.types.Operator` | :class:`bpy.types.KeyingSetInfo` | :class:`bpy.types.RenderEngine` | :class:`bpy.types.AssetShelf` | :class:`bpy.types.FileHandler` | :class:`bpy.types.PropertyGroup` | :class:`bpy.types.AddonPreferences` | :class:`bpy.types.NodeTree` | :class:`bpy.types.Node` | :class:`bpy.types.NodeSocket`]

   :raises ValueError:
      if the class is not a subclass of a registerable blender class.

   .. note::

      If the class has a *register* class method it will be called
      before registration.


    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html"""
    ...

def register_classes_factory(classes) -> Any:
    """
    Utility function to create register and unregister functions
    which simply registers and unregisters a sequence of classes.
    

    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html"""
    ...

def register_cli_command(*args, **kwargs) -> Any:
    """.. method:: register_cli_command(id, execute)

   Register a command, accessible via the (``-c`` / ``--command``) command-line argument.

   :arg id: The command identifier (must pass an ``str.isidentifier`` check).

      If the ``id`` is already registered, a warning is printed and the command is inaccessible to prevent accidents invoking the wrong command.
   :type id: str
   :arg execute: Callback, taking a single list of strings and returns an int.
      The arguments are built from all command-line arguments following the command id.
      The return value should be 0 for success, 1 on failure (specific error codes from the ``os`` module can also be used).
   :type execute: callable
   :return: The command handle which can be passed to :func:`unregister_cli_command`.

      This uses Python's capsule type however the result should be considered an opaque handle only used for unregistering.
   :rtype: capsule


    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html"""
    ...

def register_manual_map(manual_hook) -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html"""
    ...

def register_preset_path(path) -> Any:
    """
    Register a preset search path.

    :arg path: preset directory (must be an absolute path).

       This path must contain a "presets" subdirectory which will typically contain presets for add-ons.

       You may call ``bpy.utils.register_preset_path(os.path.dirname(__file__))`` from an add-ons ``__init__.py`` file.
       When the ``__init__.py`` is in the same location as a ``presets`` directory.
       For example an operators preset would be located under: ``presets/operator/{operator.id}/``
       where ``operator.id`` is the ``bl_idname`` of the operator.
    :type path: str
    :return: success
    :rtype: bool
    

    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html"""
    ...

def register_submodule_factory(module_name, submodule_names) -> Any:
    """
    Utility function to create register and unregister functions
    which simply load submodules,
    calling their register & unregister functions.

    .. note::

       Modules are registered in the order given,
       unregistered in reverse order.

    :arg module_name: The module name, typically ``__name__``.
    :type module_name: str
    :arg submodule_names: List of submodule names to load and unload.
    :type submodule_names: list[str]
    :return: register and unregister functions.
    :rtype: tuple[Callable[[], None], Callable[[], None]]
    

    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html"""
    ...

def register_tool(tool_cls, *, after=None, separator=False, group=False) -> Any:
    """
    Register a tool in the toolbar.

    :arg tool_cls: A tool subclass.
    :type tool_cls: type[:class:`bpy.types.WorkSpaceTool`]
    :arg after: Optional identifiers this tool will be added after.
    :type after: Sequence[str] | set[str] | None
    :arg separator: When true, add a separator before this tool.
    :type separator: bool
    :arg group: When true, add a new nested group of tools.
    :type group: bool
    

    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html"""
    ...

def resource_path(*args, **kwargs) -> Any:
    """.. function:: resource_path(type, *, major=bpy.app.version[0], minor=bpy.app.version[1])

   Return the base path for storing system files.

   :arg type: string in ['USER', 'LOCAL', 'SYSTEM'].
   :type type: str
   :arg major: major version, defaults to current.
   :type major: int
   :arg minor: minor version, defaults to current.
   :type minor: str
   :return: the resource path (not necessarily existing).
   :rtype: str


    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html"""
    ...

def script_path_user() -> Any:
    """returns the env var and falls back to home dir or None

    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html"""
    ...

def script_paths(*, subdir=None, user_pref=True, check_all=False, use_user=True, use_system_environment=True) -> Any:
    """
    Returns a list of valid script paths.

    :arg subdir: Optional subdir.
    :type subdir: str
    :arg user_pref: Include the user preference script paths.
    :type user_pref: bool
    :arg check_all: Include local, user and system paths rather just the paths Blender uses.
    :type check_all: bool
    :arg use_user: Include user paths
    :type use_user: bool
    :arg use_system_environment: Include BLENDER_SYSTEM_SCRIPTS variable path
    :type use_system_environment: bool
    :return: script paths.
    :rtype: list[str]
    

    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html"""
    ...

def script_paths_pref() -> Any:
    """Returns a list of user preference script directories.

    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html"""
    ...

def script_paths_system_environment() -> Any:
    """Returns a list of system script directories from environment variables.

    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html"""
    ...

def smpte_from_frame(frame, *, fps=None, fps_base=None) -> Any:
    """
    Returns an SMPTE formatted string from the *frame*:
    ``HH:MM:SS:FF``.

    If *fps* and *fps_base* are not given the current scene is used.

    :arg frame: frame number.
    :type frame: int | float
    :return: the frame string.
    :rtype: str
    

    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html"""
    ...

def smpte_from_seconds(time, *, fps=None, fps_base=None) -> Any:
    """
    Returns an SMPTE formatted string from the *time*:
    ``HH:MM:SS:FF``.

    If *fps* and *fps_base* are not given the current scene is used.

    :arg time: time in seconds.
    :type time: int | float | datetime.timedelta
    :return: the frame string.
    :rtype: str
    

    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html"""
    ...

def system_resource(*args, **kwargs) -> Any:
    """.. function:: system_resource(type, *, path="")

   Return a system resource path.

   :arg type: string in ['DATAFILES', 'SCRIPTS', 'EXTENSIONS', 'PYTHON'].
   :type type: str
   :arg path: Optional subdirectory.
   :type path: str | bytes


    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html"""
    ...

def time_from_frame(frame, *, fps=None, fps_base=None) -> Any:
    """
    Returns the time from a frame number .

    If *fps* and *fps_base* are not given the current scene is used.

    :arg frame: number.
    :type frame: int | float
    :return: the time in seconds.
    :rtype: datetime.timedelta
    

    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html"""
    ...

def time_to_frame(time, *, fps=None, fps_base=None) -> Any:
    """
    Returns a float frame number from a time given in seconds or
    as a datetime.timedelta object.

    If *fps* and *fps_base* are not given the current scene is used.

    :arg time: time in seconds.
    :type time: float | int | datetime.timedelta
    :return: The frame.
    :rtype: float | int | datetime.timedelta
    

    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html"""
    ...

def unescape_identifier(*args, **kwargs) -> Any:
    """.. function:: unescape_identifier(string)

   Simple string un-escape function used for animation paths.
   This performs the reverse of :func:`escape_identifier`.

   :arg string: text
   :type string: str
   :return: The un-escaped string.
   :rtype: str


    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html"""
    ...

def unregister_class(*args, **kwargs) -> Any:
    """.. function:: unregister_class(cls)

   Unload the Python class from blender.

   :arg cls: Blender type class, 
      see :mod:`bpy.utils.register_class` for classes which can 
      be registered.
   :type cls: type[:class:`bpy.types.Panel` | :class:`bpy.types.UIList` | :class:`bpy.types.Menu` | :class:`bpy.types.Header` | :class:`bpy.types.Operator` | :class:`bpy.types.KeyingSetInfo` | :class:`bpy.types.RenderEngine` | :class:`bpy.types.AssetShelf` | :class:`bpy.types.FileHandler` | :class:`bpy.types.PropertyGroup` | :class:`bpy.types.AddonPreferences` | :class:`bpy.types.NodeTree` | :class:`bpy.types.Node` | :class:`bpy.types.NodeSocket`]

   .. note::

      If the class has an *unregister* class method it will be called
      before unregistering.


    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html"""
    ...

def unregister_cli_command(*args, **kwargs) -> Any:
    """.. method:: unregister_cli_command(handle)

   Unregister a CLI command.

   :arg handle: The return value of :func:`register_cli_command`.
   :type handle: capsule


    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html"""
    ...

def unregister_manual_map(manual_hook) -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html"""
    ...

def unregister_preset_path(path) -> Any:
    """
    Unregister a preset search path.

    :arg path: preset directory (must be an absolute path).

       This must match the registered path exactly.
    :type path: str
    :return: success
    :rtype: bool
    

    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html"""
    ...

def unregister_tool(tool_cls) -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html"""
    ...

def user_resource(resource_type, *, path='', create=False) -> Any:
    """
    Return a user resource path (normally from the users home directory).

    :arg resource_type: Resource type in ['DATAFILES', 'CONFIG', 'SCRIPTS', 'EXTENSIONS'].
    :type resource_type: str
    :arg path: Optional subdirectory.
    :type path: str
    :arg create: Treat the path as a directory and create it if its not existing.
    :type create: bool
    :return: a path.
    :rtype: str
    

    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html"""
    ...

from . import previews as previews
# Documentation: https://docs.blender.org/api/current/bpy.utils.previews.html
from . import toolsystem as toolsystem
# Documentation: https://docs.blender.org/api/current/bpy.utils.toolsystem.html
from . import units as units
# Documentation: https://docs.blender.org/api/current/bpy.utils.units.html