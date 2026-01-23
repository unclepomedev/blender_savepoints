# Blender Probe Generated Stub for Blender 5.1.0 Alpha
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
class UserExtensionRepo(bpy_struct):
    name: str
    module: str
    custom_directory: str
    directory: str
    remote_url: str
    access_token: str
    source: str
    use_cache: bool
    enabled: bool
    use_sync_on_startup: bool
    use_access_token: bool
    use_custom_directory: bool
    use_remote_url: bool