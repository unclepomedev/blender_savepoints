# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.FreestyleLineSet.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .Collection import Collection
from .FreestyleLineStyle import FreestyleLineStyle

class FreestyleLineSet(bpy_struct):

    @property
    def linestyle(self) -> Annotated['FreestyleLineStyle', "is_animatable=False"]:
        """Line style settings"""
        ...
    @linestyle.setter
    def linestyle(self, value: Annotated['FreestyleLineStyle', "is_animatable=False"]) -> None:
        ...
    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:
        """Line set name"""
        ...
    @name.setter
    def name(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def show_render(self) -> bool:
        """Enable or disable this line set during stroke rendering"""
        ...
    @show_render.setter
    def show_render(self, value: bool) -> None:
        ...
    @property
    def select_by_visibility(self) -> bool:
        """Select feature edges based on visibility"""
        ...
    @select_by_visibility.setter
    def select_by_visibility(self, value: bool) -> None:
        ...
    @property
    def select_by_edge_types(self) -> bool:
        """Select feature edges based on edge types"""
        ...
    @select_by_edge_types.setter
    def select_by_edge_types(self, value: bool) -> None:
        ...
    @property
    def select_by_collection(self) -> bool:
        """Select feature edges based on a collection of objects"""
        ...
    @select_by_collection.setter
    def select_by_collection(self, value: bool) -> None:
        ...
    @property
    def select_by_image_border(self) -> bool:
        """Select feature edges by image border (less memory consumption)"""
        ...
    @select_by_image_border.setter
    def select_by_image_border(self, value: bool) -> None:
        ...
    @property
    def select_by_face_marks(self) -> bool:
        """Select feature edges by face marks"""
        ...
    @select_by_face_marks.setter
    def select_by_face_marks(self, value: bool) -> None:
        ...
    @property
    def edge_type_negation(self) -> Literal['INCLUSIVE', 'EXCLUSIVE']:
        """Specify either inclusion or exclusion of feature edges selected by edge types"""
        ...
    @edge_type_negation.setter
    def edge_type_negation(self, value: Literal['INCLUSIVE', 'EXCLUSIVE']) -> None:
        ...
    @property
    def edge_type_combination(self) -> Literal['OR', 'AND']:
        """Specify a logical combination of selection conditions on feature edge types"""
        ...
    @edge_type_combination.setter
    def edge_type_combination(self, value: Literal['OR', 'AND']) -> None:
        ...
    @property
    def collection(self) -> Annotated[Optional['Collection'], "is_animatable=False"]:
        """A collection of objects based on which feature edges are selected"""
        ...
    @collection.setter
    def collection(self, value: Annotated[Optional['Collection'], "is_animatable=False"]) -> None:
        ...
    @property
    def collection_negation(self) -> Literal['INCLUSIVE', 'EXCLUSIVE']:
        """Specify either inclusion or exclusion of feature edges belonging to a collection of objects"""
        ...
    @collection_negation.setter
    def collection_negation(self, value: Literal['INCLUSIVE', 'EXCLUSIVE']) -> None:
        ...
    @property
    def face_mark_negation(self) -> Literal['INCLUSIVE', 'EXCLUSIVE']:
        """Specify either inclusion or exclusion of feature edges selected by face marks"""
        ...
    @face_mark_negation.setter
    def face_mark_negation(self, value: Literal['INCLUSIVE', 'EXCLUSIVE']) -> None:
        ...
    @property
    def face_mark_condition(self) -> Literal['ONE', 'BOTH']:
        """Specify a feature edge selection condition based on face marks"""
        ...
    @face_mark_condition.setter
    def face_mark_condition(self, value: Literal['ONE', 'BOTH']) -> None:
        ...
    @property
    def select_silhouette(self) -> bool:
        """Select silhouettes (edges at the boundary of visible and hidden faces)"""
        ...
    @select_silhouette.setter
    def select_silhouette(self, value: bool) -> None:
        ...
    @property
    def select_border(self) -> bool:
        """Select border edges (open mesh edges)"""
        ...
    @select_border.setter
    def select_border(self, value: bool) -> None:
        ...
    @property
    def select_crease(self) -> bool:
        """Select crease edges (those between two faces making an angle smaller than the Crease Angle)"""
        ...
    @select_crease.setter
    def select_crease(self, value: bool) -> None:
        ...
    @property
    def select_ridge_valley(self) -> bool:
        """Select ridges and valleys (boundary lines between convex and concave areas of surface)"""
        ...
    @select_ridge_valley.setter
    def select_ridge_valley(self, value: bool) -> None:
        ...
    @property
    def select_suggestive_contour(self) -> bool:
        """Select suggestive contours (almost silhouette/contour edges)"""
        ...
    @select_suggestive_contour.setter
    def select_suggestive_contour(self, value: bool) -> None:
        ...
    @property
    def select_material_boundary(self) -> bool:
        """Select edges at material boundaries"""
        ...
    @select_material_boundary.setter
    def select_material_boundary(self, value: bool) -> None:
        ...
    @property
    def select_contour(self) -> bool:
        """Select contours (outer silhouettes of each object)"""
        ...
    @select_contour.setter
    def select_contour(self, value: bool) -> None:
        ...
    @property
    def select_external_contour(self) -> bool:
        """Select external contours (outer silhouettes of occluding and occluded objects)"""
        ...
    @select_external_contour.setter
    def select_external_contour(self, value: bool) -> None:
        ...
    @property
    def select_edge_mark(self) -> bool:
        """Select edge marks (edges annotated by Freestyle edge marks)"""
        ...
    @select_edge_mark.setter
    def select_edge_mark(self, value: bool) -> None:
        ...
    @property
    def exclude_silhouette(self) -> bool:
        """Exclude silhouette edges"""
        ...
    @exclude_silhouette.setter
    def exclude_silhouette(self, value: bool) -> None:
        ...
    @property
    def exclude_border(self) -> bool:
        """Exclude border edges"""
        ...
    @exclude_border.setter
    def exclude_border(self, value: bool) -> None:
        ...
    @property
    def exclude_crease(self) -> bool:
        """Exclude crease edges"""
        ...
    @exclude_crease.setter
    def exclude_crease(self, value: bool) -> None:
        ...
    @property
    def exclude_ridge_valley(self) -> bool:
        """Exclude ridges and valleys"""
        ...
    @exclude_ridge_valley.setter
    def exclude_ridge_valley(self, value: bool) -> None:
        ...
    @property
    def exclude_suggestive_contour(self) -> bool:
        """Exclude suggestive contours"""
        ...
    @exclude_suggestive_contour.setter
    def exclude_suggestive_contour(self, value: bool) -> None:
        ...
    @property
    def exclude_material_boundary(self) -> bool:
        """Exclude edges at material boundaries"""
        ...
    @exclude_material_boundary.setter
    def exclude_material_boundary(self, value: bool) -> None:
        ...
    @property
    def exclude_contour(self) -> bool:
        """Exclude contours"""
        ...
    @exclude_contour.setter
    def exclude_contour(self, value: bool) -> None:
        ...
    @property
    def exclude_external_contour(self) -> bool:
        """Exclude external contours"""
        ...
    @exclude_external_contour.setter
    def exclude_external_contour(self, value: bool) -> None:
        ...
    @property
    def exclude_edge_mark(self) -> bool:
        """Exclude edge marks"""
        ...
    @exclude_edge_mark.setter
    def exclude_edge_mark(self, value: bool) -> None:
        ...
    @property
    def visibility(self) -> Literal['VISIBLE', 'HIDDEN', 'RANGE']:
        """Determine how to use visibility for feature edge selection"""
        ...
    @visibility.setter
    def visibility(self, value: Literal['VISIBLE', 'HIDDEN', 'RANGE']) -> None:
        ...
    @property
    def qi_start(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """First QI value of the QI range"""
        ...
    @qi_start.setter
    def qi_start(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1"]) -> None:
        ...
    @property
    def qi_end(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Last QI value of the QI range"""
        ...
    @qi_end.setter
    def qi_end(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1"]) -> None:
        ...