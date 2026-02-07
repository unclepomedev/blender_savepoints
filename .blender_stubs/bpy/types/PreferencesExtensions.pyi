# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
from .UserExtensionRepo import UserExtensionRepo
from .UserExtensionRepoCollection import UserExtensionRepoCollection
class PreferencesExtensions(bpy_struct):
    use_online_access_handled: bool
    repos: 'UserExtensionRepoCollection'
    active_repo: int