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
from .Collection import Collection
from .FreestyleLineStyle import FreestyleLineStyle
class FreestyleLineSet(bpy_struct):
    linestyle: 'FreestyleLineStyle'
    name: str
    show_render: bool
    select_by_visibility: bool
    select_by_edge_types: bool
    select_by_collection: bool
    select_by_image_border: bool
    select_by_face_marks: bool
    edge_type_negation: str
    edge_type_combination: str
    collection: 'Collection'
    collection_negation: str
    face_mark_negation: str
    face_mark_condition: str
    select_silhouette: bool
    select_border: bool
    select_crease: bool
    select_ridge_valley: bool
    select_suggestive_contour: bool
    select_material_boundary: bool
    select_contour: bool
    select_external_contour: bool
    select_edge_mark: bool
    exclude_silhouette: bool
    exclude_border: bool
    exclude_crease: bool
    exclude_ridge_valley: bool
    exclude_suggestive_contour: bool
    exclude_material_boundary: bool
    exclude_contour: bool
    exclude_external_contour: bool
    exclude_edge_mark: bool
    visibility: str
    qi_start: int
    qi_end: int