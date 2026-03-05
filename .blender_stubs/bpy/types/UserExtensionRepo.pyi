# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.UserExtensionRepo.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class UserExtensionRepo(bpy_struct):

    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:
        """Unique repository name"""
        ...
    @name.setter
    def name(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def module(self) -> Annotated[str, "is_animatable=False"]:
        """Unique module identifier"""
        ...
    @module.setter
    def module(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def custom_directory(self) -> Annotated[str, "subtype='DIR_PATH'", "is_animatable=False"]:
        """The local directory containing extensions"""
        ...
    @custom_directory.setter
    def custom_directory(self, value: Annotated[str, "subtype='DIR_PATH'", "is_animatable=False"]):
        ...
    @property
    def directory(self) -> Annotated[str, "subtype='DIR_PATH'", "is_animatable=False"]:
        """The local directory containing extensions"""
        ...
    @property
    def remote_url(self) -> Annotated[str, "is_animatable=False"]:
        """Remote URL to the extension repository, the file-system may be referenced using the file URI scheme: "file://" """
        ...
    @remote_url.setter
    def remote_url(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def access_token(self) -> Annotated[str, "subtype='PASSWORD'", "is_animatable=False"]:
        """Personal access token, may be required by some repositories"""
        ...
    @access_token.setter
    def access_token(self, value: Annotated[str, "subtype='PASSWORD'", "is_animatable=False"]):
        ...
    @property
    def source(self) -> Literal['USER', 'SYSTEM']:
        """Select if the repository is in a user managed or system provided directory"""
        ...
    @source.setter
    def source(self, value: Literal['USER', 'SYSTEM']):
        ...
    @property
    def use_cache(self) -> bool:
        """Downloaded package files are deleted after installation"""
        ...
    @use_cache.setter
    def use_cache(self, value: bool):
        ...
    @property
    def enabled(self) -> bool:
        """Enable the repository"""
        ...
    @enabled.setter
    def enabled(self, value: bool):
        ...
    @property
    def use_sync_on_startup(self) -> bool:
        """Allow Blender to check for updates upon launch"""
        ...
    @use_sync_on_startup.setter
    def use_sync_on_startup(self, value: bool):
        ...
    @property
    def use_access_token(self) -> bool:
        """Repository requires an access token"""
        ...
    @use_access_token.setter
    def use_access_token(self, value: bool):
        ...
    @property
    def use_custom_directory(self) -> bool:
        """Manually set the path for extensions to be stored. When disabled a user's extensions directory is created."""
        ...
    @use_custom_directory.setter
    def use_custom_directory(self, value: bool):
        ...
    @property
    def use_remote_url(self) -> bool:
        """Synchronize the repository with a remote URL"""
        ...
    @use_remote_url.setter
    def use_remote_url(self, value: bool):
        ...