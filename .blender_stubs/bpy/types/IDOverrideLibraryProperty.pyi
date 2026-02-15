# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.IDOverrideLibraryProperty.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .IDOverrideLibraryPropertyOperation import IDOverrideLibraryPropertyOperation
from .IDOverrideLibraryPropertyOperations import IDOverrideLibraryPropertyOperations
from .bpy_prop_collection import bpy_prop_collection

class IDOverrideLibraryProperty(bpy_struct):

    @property
    def rna_path(self) -> Annotated[str, "is_animatable=False"]:
        """RNA path leading to that property, from owning ID"""
        ...
    @property
    def operations(self) -> Annotated['IDOverrideLibraryPropertyOperations', "is_animatable=False"]:
        """List of overriding operations for a property"""
        ...