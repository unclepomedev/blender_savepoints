# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
from .AssetTag import AssetTag
from .AssetTags import AssetTags
class AssetMetaData(bpy_struct):
    author: Annotated[str, "is_animatable=False"]
    """Name of the creator of the asset"""
    description: Annotated[str, "is_animatable=False"]
    """A description of the asset to be displayed for the user"""
    copyright: Annotated[str, "is_animatable=False"]
    """Copyright notice for this asset. An empty copyright notice does not necessarily indicate that this is copyright-free. Contact the author if any clarification is needed."""
    license: Annotated[str, "is_animatable=False"]
    """The type of license this asset is distributed under. An empty license name does not necessarily indicate that this is free of licensing terms. Contact the author if any clarification is needed."""
    @property
    def tags(self) -> Annotated['AssetTags', "is_animatable=False"]:
        """Custom tags (name tokens) for the asset, used for filtering and general asset management"""
        ...
    active_tag: Annotated[int, "step=1", "is_animatable=False"]
    """Index of the tag set for editing"""
    catalog_id: Annotated[str, "is_animatable=False"]
    """Identifier for the asset's catalog, used by Blender to look up the asset's catalog path. Must be a UUID according to RFC4122."""
    @property
    def catalog_simple_name(self) -> Annotated[str, "is_animatable=False"]:
        """Simple name of the asset's catalog, for debugging and data recovery purposes"""
        ...