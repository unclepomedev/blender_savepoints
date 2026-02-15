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
from .Collection import Collection
from .FreestyleLineStyle import FreestyleLineStyle
class FreestyleLineSet(bpy_struct):
    linestyle: Annotated['FreestyleLineStyle', "is_animatable=False"]
    """Line style settings"""
    name: Annotated[str, "is_animatable=False"]
    """Line set name"""
    show_render: bool
    """Enable or disable this line set during stroke rendering"""
    select_by_visibility: bool
    """Select feature edges based on visibility"""
    select_by_edge_types: bool
    """Select feature edges based on edge types"""
    select_by_collection: bool
    """Select feature edges based on a collection of objects"""
    select_by_image_border: bool
    """Select feature edges by image border (less memory consumption)"""
    select_by_face_marks: bool
    """Select feature edges by face marks"""
    edge_type_negation: Literal['INCLUSIVE', 'EXCLUSIVE']
    """Specify either inclusion or exclusion of feature edges selected by edge types"""
    edge_type_combination: Literal['OR', 'AND']
    """Specify a logical combination of selection conditions on feature edge types"""
    collection: Annotated[Optional['Collection'], "is_animatable=False"]
    """A collection of objects based on which feature edges are selected"""
    collection_negation: Literal['INCLUSIVE', 'EXCLUSIVE']
    """Specify either inclusion or exclusion of feature edges belonging to a collection of objects"""
    face_mark_negation: Literal['INCLUSIVE', 'EXCLUSIVE']
    """Specify either inclusion or exclusion of feature edges selected by face marks"""
    face_mark_condition: Literal['ONE', 'BOTH']
    """Specify a feature edge selection condition based on face marks"""
    select_silhouette: bool
    """Select silhouettes (edges at the boundary of visible and hidden faces)"""
    select_border: bool
    """Select border edges (open mesh edges)"""
    select_crease: bool
    """Select crease edges (those between two faces making an angle smaller than the Crease Angle)"""
    select_ridge_valley: bool
    """Select ridges and valleys (boundary lines between convex and concave areas of surface)"""
    select_suggestive_contour: bool
    """Select suggestive contours (almost silhouette/contour edges)"""
    select_material_boundary: bool
    """Select edges at material boundaries"""
    select_contour: bool
    """Select contours (outer silhouettes of each object)"""
    select_external_contour: bool
    """Select external contours (outer silhouettes of occluding and occluded objects)"""
    select_edge_mark: bool
    """Select edge marks (edges annotated by Freestyle edge marks)"""
    exclude_silhouette: bool
    """Exclude silhouette edges"""
    exclude_border: bool
    """Exclude border edges"""
    exclude_crease: bool
    """Exclude crease edges"""
    exclude_ridge_valley: bool
    """Exclude ridges and valleys"""
    exclude_suggestive_contour: bool
    """Exclude suggestive contours"""
    exclude_material_boundary: bool
    """Exclude edges at material boundaries"""
    exclude_contour: bool
    """Exclude contours"""
    exclude_external_contour: bool
    """Exclude external contours"""
    exclude_edge_mark: bool
    """Exclude edge marks"""
    visibility: Literal['VISIBLE', 'HIDDEN', 'RANGE']
    """Determine how to use visibility for feature edge selection"""
    qi_start: Annotated[int, "subtype='UNSIGNED'", "step=1"]
    """First QI value of the QI range"""
    qi_end: Annotated[int, "subtype='UNSIGNED'", "step=1"]
    """Last QI value of the QI range"""