# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.path.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated


def abspath(path, *, start=None, library=None) -> Any:
    """
    Returns the absolute path relative to the current blend file
    using the "//" prefix.

    :arg start: Relative to this path,
       when not set the current filename is used.
    :type start: str | bytes
    :arg library: The library this path is from. This is only included for
       convenience, when the library is not None its path replaces *start*.
    :type library: :class:`bpy.types.Library`
    :return: The absolute path.
    :rtype: str
    

    Online Documentation:
    https://docs.blender.org/api/current/bpy.path.html"""
    ...

def basename(path) -> Any:
    """
    Equivalent to ``os.path.basename``, but skips a "//" prefix.

    Use for Windows compatibility.

    :return: The base name of the given path.
    :rtype: str
    

    Online Documentation:
    https://docs.blender.org/api/current/bpy.path.html"""
    ...

def clean_name(name, *, replace='_') -> Any:
    """
    Returns a name with characters replaced that
    may cause problems under various circumstances,
    such as writing to a file.

    All characters besides A-Z/a-z, 0-9 are replaced with "_"
    or the *replace* argument if defined.

    :arg name: The path name.
    :type name: str | bytes
    :arg replace: The replacement for non-valid characters.
    :type replace: str
    :return: The cleaned name.
    :rtype: str
    

    Online Documentation:
    https://docs.blender.org/api/current/bpy.path.html"""
    ...

def display_name(name, *, has_ext=True, title_case=True) -> Any:
    """
    Creates a display string from name to be used menus and the user interface.
    Intended for use with filenames and module names.

    :arg name: The name to be used for displaying the user interface.
    :type name: str
    :arg has_ext: Remove file extension from name.
    :type has_ext: bool
    :arg title_case: Convert lowercase names to title case.
    :type title_case: bool
    :return: The display string.
    :rtype: str
    

    Online Documentation:
    https://docs.blender.org/api/current/bpy.path.html"""
    ...

def display_name_from_filepath(name) -> Any:
    """
    Returns the path stripped of directory and extension,
    ensured to be utf8 compatible.

    :arg name: The file path to convert.
    :type name: str
    :return: The display name.
    :rtype: str
    

    Online Documentation:
    https://docs.blender.org/api/current/bpy.path.html"""
    ...

def display_name_to_filepath(name) -> Any:
    """
    Performs the reverse of display_name using literal versions of characters
    which aren't supported in a filepath.

    :arg name: The display name to convert.
    :type name: str
    :return: The file path.
    :rtype: str
    

    Online Documentation:
    https://docs.blender.org/api/current/bpy.path.html"""
    ...

def ensure_ext(filepath, ext, *, case_sensitive=False) -> Any:
    """
    Return the path with the extension added if it is not already set.

    :arg filepath: The file path.
    :type filepath: str
    :arg ext: The extension to check for, can be a compound extension. Should
              start with a dot, such as ``.blend`` or ``.tar.gz``.
    :type ext: str
    :arg case_sensitive: Check for matching case when comparing extensions.
    :type case_sensitive: bool
    :return: The file path with the given extension.
    :rtype: str
    

    Online Documentation:
    https://docs.blender.org/api/current/bpy.path.html"""
    ...

extensions_audio: Any
extensions_image: Any
extensions_movie: Any
def is_subdir(path, directory) -> Any:
    """
    Returns true if *path* in a subdirectory of *directory*.
    Both paths must be absolute.

    :arg path: An absolute path.
    :type path: str | bytes
    :return: Whether or not the path is a subdirectory.
    :rtype: bool
    

    Online Documentation:
    https://docs.blender.org/api/current/bpy.path.html"""
    ...

def module_names(path, *, recursive=False, package='') -> Any:
    """
    Return a list of modules which can be imported from *path*.

    :arg path: a directory to scan.
    :type path: str
    :arg recursive: Also return submodule names for packages.
    :type recursive: bool
    :arg package: Optional string, used as the prefix for module names (without the trailing ".").
    :type package: str
    :return: a list of string pairs (module_name, module_file).
    :rtype: list[tuple[str, str]]
    

    Online Documentation:
    https://docs.blender.org/api/current/bpy.path.html"""
    ...

def native_pathsep(path) -> Any:
    """
    Replace the path separator with the systems native ``os.sep``.

    :arg path: The path to replace.
    :type path: str
    :return: The path with system native separators.
    :rtype: str
    

    Online Documentation:
    https://docs.blender.org/api/current/bpy.path.html"""
    ...

def reduce_dirs(dirs) -> Any:
    """
    Given a sequence of directories, remove duplicates and
    any directories nested in one of the other paths.
    (Useful for recursive path searching).

    :arg dirs: Sequence of directory paths.
    :type dirs: Sequence[str]
    :return: A unique list of paths.
    :rtype: list[str]
    

    Online Documentation:
    https://docs.blender.org/api/current/bpy.path.html"""
    ...

def relpath(path, *, start=None) -> Any:
    """
    Returns the path relative to the current blend file using the "//" prefix.

    :arg path: An absolute path.
    :type path: str | bytes
    :arg start: Relative to this path,
       when not set the current filename is used.
    :type start: str | bytes
    :return: The relative path.
    :rtype: str
    

    Online Documentation:
    https://docs.blender.org/api/current/bpy.path.html"""
    ...

def resolve_ncase(path) -> Any:
    """
    Resolve a case insensitive path on a case sensitive system,
    returning a string with the path if found else return the original path.

    :arg path: The path name to resolve.
    :type path: str
    :return: The resolved path.
    :rtype: str
    

    Online Documentation:
    https://docs.blender.org/api/current/bpy.path.html"""
    ...
