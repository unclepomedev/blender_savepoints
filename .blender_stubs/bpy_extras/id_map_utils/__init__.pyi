# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy_extras.id_map_utils.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated


def get_all_referenced_ids(id, ref_map) -> Any:
    """Return a set of IDs directly or indirectly referenced by id.

    Online Documentation:
    https://docs.blender.org/api/current/bpy_extras.id_map_utils.html"""
    ...

def get_id_reference_map() -> Any:
    """Return a dictionary of direct data-block references for every data-block in the blend file.

    Online Documentation:
    https://docs.blender.org/api/current/bpy_extras.id_map_utils.html"""
    ...

def recursive_get_referenced_ids(ref_map, id, referenced_ids, visited) -> Any:
    """Recursively populate referenced_ids with IDs referenced by id.

    Online Documentation:
    https://docs.blender.org/api/current/bpy_extras.id_map_utils.html"""
    ...
