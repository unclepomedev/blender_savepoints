# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name




import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated


addons_fake_modules: Any
def check(module_name) -> Any:
    """
    Returns the loaded state of the addon.

    :arg module_name: The name of the addon and module.
    :type module_name: str
    :return: (loaded_default, loaded_state)
    :rtype: tuple[bool, bool]
    """
    ...

def check_extension(module_name) -> Any:
    """
    Return true if the module is an extension.
    """
    ...

def disable(module_name, *, default_set=False, refresh_handled=False, handle_error=None) -> Any:
    """
    Disables an addon by name.

    :arg module_name: The name of the addon and module.
    :type module_name: str
    :arg default_set: Set the user-preference.
    :type default_set: bool
    :arg handle_error: Called in the case of an error, taking an exception argument.
    :type handle_error: Callable[[Exception], None] | None
    """
    ...

def disable_all() -> Any:
    ...

def enable(module_name, *, default_set=False, persistent=False, refresh_handled=False, handle_error=None) -> Any:
    """
    Enables an addon by name.

    :arg module_name: the name of the addon and module.
    :type module_name: str
    :arg default_set: Set the user-preference.
    :type default_set: bool
    :arg persistent: Ensure the addon is enabled for the entire session (after loading new files).
    :type persistent: bool
    :arg refresh_handled: When true, :func:`extensions_refresh` must have been called with ``module_name``
       included in ``addon_modules_pending``.
       This should be used to avoid many calls to refresh extensions when enabling multiple add-ons at once.
    :type refresh_handled: bool
    :arg handle_error: Called in the case of an error, taking an exception argument.
    :type handle_error: Callable[[Exception], None] | None
    :return: the loaded module or None on failure.
    :rtype: ModuleType
    """
    ...

error_duplicates: Any
error_encoding = False
def extensions_refresh(ensure_wheels=True, addon_modules_pending=None, handle_error=None) -> Any:
    """
    Ensure data relating to extensions is up to date.
    This should be called after extensions on the file-system have changed.

    :arg ensure_wheels: When true, refresh installed wheels with wheels used by extensions.
    :type ensure_wheels: bool
    :arg addon_modules_pending: Refresh these add-ons by listing their package names, as if they are enabled.
       This is needed so wheels can be setup before the add-on is enabled.
    :type addon_modules_pending: Sequence[str] | None
    :arg handle_error: Called in the case of an error, taking an exception argument.
    :type handle_error: Callable[[Exception], None] | None
    """
    ...

def module_bl_info(mod, *, info_basis=None) -> Any:
    ...

def modules(*, module_cache={}, refresh=True) -> Any:
    ...

def modules_refresh(*, module_cache={}) -> Any:
    ...

def paths() -> Any:
    ...

def reset_all(*, reload_scripts=False) -> Any:
    """
    Sets the addon state based on the user preferences.
    """
    ...

def stale_pending_remove_paths(path_base, paths) -> Any:
    ...

def stale_pending_stage_paths(path_base, paths) -> Any:
    ...
