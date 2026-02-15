# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.IDOverrideLibrary.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .ID import ID
from .IDOverrideLibraryProperties import IDOverrideLibraryProperties
from .IDOverrideLibraryProperty import IDOverrideLibraryProperty
from .bpy_prop_collection import bpy_prop_collection

class IDOverrideLibrary(bpy_struct):

    @property
    def reference(self) -> Annotated[Optional['ID'], "is_animatable=False"]:
        """Linked ID used as reference by this override"""
        ...
    @property
    def hierarchy_root(self) -> Annotated[Optional['ID'], "is_animatable=False"]:
        """Library override ID used as root of the override hierarchy this ID is a member of"""
        ...
    is_in_hierarchy: bool
    """Whether this library override is defined as part of a library hierarchy, or as a single, isolated and autonomous override"""
    is_system_override: bool
    """Whether this library override exists only for the override hierarchy, or if it is actually editable by the user"""
    @property
    def properties(self) -> Annotated['IDOverrideLibraryProperties', "is_animatable=False"]:
        """List of overridden properties"""
        ...
    def operations_update(self, *args, **kwargs) -> Any: ...
    def reset(self, *args, **kwargs) -> Any: ...
    def destroy(self, *args, **kwargs) -> Any: ...
    def resync(self, *args, **kwargs) -> Any: ...