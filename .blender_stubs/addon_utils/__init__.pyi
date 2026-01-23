# Blender Probe Generated Stub for Blender 5.1.0 Alpha
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


import sys
import typing
from typing import Any, Union, Callable, Iterator

addons_fake_modules: Any
def check(module_name) -> Any:
    ...

def check_extension(module_name) -> Any:
    ...

def disable(module_name, *, default_set=False, refresh_handled=False, handle_error=None) -> Any:
    ...

def disable_all() -> Any:
    ...

def enable(module_name, *, default_set=False, persistent=False, refresh_handled=False, handle_error=None) -> Any:
    ...

error_duplicates: Any
error_encoding = False
def extensions_refresh(ensure_wheels=True, addon_modules_pending=None, handle_error=None) -> Any:
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
    ...

def stale_pending_remove_paths(path_base, paths) -> Any:
    ...

def stale_pending_stage_paths(path_base, paths) -> Any:
    ...
