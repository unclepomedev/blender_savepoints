"""
Online Documentation:
https://docs.blender.org/api/current/bpy.utils.html
"""

# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


import sys
import typing
from typing import Any, Union, Callable, Iterator

def app_template_paths(*, path=None) -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html
    """
    ...

def blend_paths(*args, **kwargs) -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html
    """
    ...

def escape_identifier(*args, **kwargs) -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html
    """
    ...

def execfile(filepath, *, mod=None) -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html
    """
    ...

def expose_bundled_modules() -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html
    """
    ...

def extension_path_user(package, *, path='', create=False) -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html
    """
    ...

def flip_name(*args, **kwargs) -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html
    """
    ...

def is_path_builtin(path) -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html
    """
    ...

def is_path_extension(path) -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html
    """
    ...

def keyconfig_init() -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html
    """
    ...

def keyconfig_set(filepath, *, report=None) -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html
    """
    ...

def load_scripts(*, reload_scripts=False, refresh_scripts=False, extensions=True) -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html
    """
    ...

def load_scripts_extensions(*, reload_scripts=False) -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html
    """
    ...

def make_rna_paths(struct_name, prop_name, enum_name) -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html
    """
    ...

def manual_language_code(default='en') -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html
    """
    ...

def manual_map() -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html
    """
    ...

def modules_from_path(path, loaded_modules) -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html
    """
    ...

def preset_find(name, preset_path, *, display_name=False, ext='.py') -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html
    """
    ...

def preset_paths(subdir) -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html
    """
    ...

def refresh_script_paths() -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html
    """
    ...

def register_class(*args, **kwargs) -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html
    """
    ...

def register_classes_factory(classes) -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html
    """
    ...

def register_cli_command(*args, **kwargs) -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html
    """
    ...

def register_manual_map(manual_hook) -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html
    """
    ...

def register_preset_path(path) -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html
    """
    ...

def register_submodule_factory(module_name, submodule_names) -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html
    """
    ...

def register_tool(tool_cls, *, after=None, separator=False, group=False) -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html
    """
    ...

def resource_path(*args, **kwargs) -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html
    """
    ...

def script_path_user() -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html
    """
    ...

def script_paths(*, subdir=None, user_pref=True, check_all=False, use_user=True, use_system_environment=True) -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html
    """
    ...

def script_paths_pref() -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html
    """
    ...

def script_paths_system_environment() -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html
    """
    ...

def smpte_from_frame(frame, *, fps=None, fps_base=None) -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html
    """
    ...

def smpte_from_seconds(time, *, fps=None, fps_base=None) -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html
    """
    ...

def system_resource(*args, **kwargs) -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html
    """
    ...

def time_from_frame(frame, *, fps=None, fps_base=None) -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html
    """
    ...

def time_to_frame(time, *, fps=None, fps_base=None) -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html
    """
    ...

def unescape_identifier(*args, **kwargs) -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html
    """
    ...

def unregister_class(*args, **kwargs) -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html
    """
    ...

def unregister_cli_command(*args, **kwargs) -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html
    """
    ...

def unregister_manual_map(manual_hook) -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html
    """
    ...

def unregister_preset_path(path) -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html
    """
    ...

def unregister_tool(tool_cls) -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html
    """
    ...

def user_resource(resource_type, *, path='', create=False) -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.html
    """
    ...

from . import previews as previews
# Documentation: https://docs.blender.org/api/current/bpy.utils.previews.html
from . import toolsystem as toolsystem
# Documentation: https://docs.blender.org/api/current/bpy.utils.toolsystem.html
from . import units as units
# Documentation: https://docs.blender.org/api/current/bpy.utils.units.html