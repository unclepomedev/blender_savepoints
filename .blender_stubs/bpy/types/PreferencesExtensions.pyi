# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.PreferencesExtensions.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .UserExtensionRepo import UserExtensionRepo
from .UserExtensionRepoCollection import UserExtensionRepoCollection
from .bpy_prop_collection import bpy_prop_collection

class PreferencesExtensions(bpy_struct):

    @property
    def use_online_access_handled(self) -> bool:
        """The user has been shown the "Online Access" prompt and made a choice"""
        ...
    @use_online_access_handled.setter
    def use_online_access_handled(self, value: bool) -> None:
        ...
    @property
    def repos(self) -> Annotated['UserExtensionRepoCollection', "is_animatable=False"]:

        ...
    @property
    def active_repo(self) -> Annotated[int, "step=1"]:
        """Index of the extensions repository being edited in the Preferences UI"""
        ...
    @active_repo.setter
    def active_repo(self, value: Annotated[int, "step=1"]) -> None:
        ...