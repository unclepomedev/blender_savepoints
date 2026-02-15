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

    name: Annotated[str, "is_animatable=False"]
    """Unique repository name"""
    module: Annotated[str, "is_animatable=False"]
    """Unique module identifier"""
    custom_directory: Annotated[str, "subtype='DIR_PATH'", "is_animatable=False"]
    """The local directory containing extensions"""
    @property
    def directory(self) -> Annotated[str, "subtype='DIR_PATH'", "is_animatable=False"]:
        """The local directory containing extensions"""
        ...
    remote_url: Annotated[str, "is_animatable=False"]
    """Remote URL to the extension repository, the file-system may be referenced using the file URI scheme: "file://" """
    access_token: Annotated[str, "subtype='PASSWORD'", "is_animatable=False"]
    """Personal access token, may be required by some repositories"""
    source: Literal['USER', 'SYSTEM']
    """Select if the repository is in a user managed or system provided directory"""
    use_cache: bool
    """Downloaded package files are deleted after installation"""
    enabled: bool
    """Enable the repository"""
    use_sync_on_startup: bool
    """Allow Blender to check for updates upon launch"""
    use_access_token: bool
    """Repository requires an access token"""
    use_custom_directory: bool
    """Manually set the path for extensions to be stored. When disabled a user's extensions directory is created."""
    use_remote_url: bool
    """Synchronize the repository with a remote URL"""