# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.KeyConfigurations.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .KeyConfig import KeyConfig

class KeyConfigurations(bpy_struct):

    active: Annotated[Optional['KeyConfig'], "is_animatable=False"]
    """Active key configuration (preset)"""
    @property
    def default(self) -> Annotated[Optional['KeyConfig'], "subtype=''", "unit='MASS'", "is_animatable=False"]:
        """Default builtin key configuration"""
        ...
    @property
    def addon(self) -> Annotated[Optional['KeyConfig'], "subtype=''", "unit='MASS'", "is_animatable=False"]:
        """Key configuration that can be extended by add-ons, and is added to the active configuration when handling events"""
        ...
    @property
    def user(self) -> Annotated[Optional['KeyConfig'], "subtype=''", "unit='MASS'", "is_animatable=False"]:
        """Final key configuration that combines keymaps from the active and add-on configurations, and can be edited by the user"""
        ...
    def new(self, *args, **kwargs) -> Any: ...
    def remove(self, *args, **kwargs) -> Any: ...
    def find_item_from_operator(self, *args, **kwargs) -> Any: ...
    def update(self, *args, **kwargs) -> Any: ...
    def __contains__(self, key: Union[str, int]) -> bool: ...
    def __iter__(self) -> Iterator['KeyConfig']: ...
    def __getitem__(self, key: Union[str, int]) -> 'KeyConfig': ...
    def __len__(self) -> int: ...
    # --- Injected Methods ---
    addon: Any
    user: Any
    active: Any