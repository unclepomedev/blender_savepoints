# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.SpaceOutliner.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .Space import Space

class SpaceOutliner(Space):

    @property
    def type(self) -> Literal['EMPTY', 'VIEW_3D', 'IMAGE_EDITOR', 'NODE_EDITOR', 'SEQUENCE_EDITOR', 'CLIP_EDITOR', 'DOPESHEET_EDITOR', 'GRAPH_EDITOR', 'NLA_EDITOR', 'TEXT_EDITOR', 'CONSOLE', 'INFO', 'TOPBAR', 'STATUSBAR', 'OUTLINER', 'PROPERTIES', 'FILE_BROWSER', 'SPREADSHEET', 'PREFERENCES']:
        """Space data type"""
        ...
    @property
    def show_locked_time(self) -> bool:
        """Synchronize the visible timeline range with other time-based editors"""
        ...
    @show_locked_time.setter
    def show_locked_time(self, value: bool):
        ...
    @property
    def show_region_header(self) -> bool:

        ...
    @show_region_header.setter
    def show_region_header(self, value: bool):
        ...
    @property
    def display_mode(self) -> Literal['SCENES', 'VIEW_LAYER', 'SEQUENCE', 'LIBRARIES', 'DATA_API', 'LIBRARY_OVERRIDES', 'ORPHAN_DATA']:
        """Type of information to display"""
        ...
    @display_mode.setter
    def display_mode(self, value: Literal['SCENES', 'VIEW_LAYER', 'SEQUENCE', 'LIBRARIES', 'DATA_API', 'LIBRARY_OVERRIDES', 'ORPHAN_DATA']):
        ...
    @property
    def lib_override_view_mode(self) -> Literal['PROPERTIES', 'HIERARCHIES']:
        """Choose different visualizations of library override data"""
        ...
    @lib_override_view_mode.setter
    def lib_override_view_mode(self, value: Literal['PROPERTIES', 'HIERARCHIES']):
        ...
    @property
    def filter_text(self) -> Annotated[str, "is_animatable=False"]:
        """Live search filtering string"""
        ...
    @filter_text.setter
    def filter_text(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def use_filter_case_sensitive(self) -> bool:
        """Only use case sensitive matches of search string"""
        ...
    @use_filter_case_sensitive.setter
    def use_filter_case_sensitive(self, value: bool):
        ...
    @property
    def use_filter_complete(self) -> bool:
        """Only use complete matches of search string"""
        ...
    @use_filter_complete.setter
    def use_filter_complete(self, value: bool):
        ...
    @property
    def use_sort_alpha(self) -> bool:

        ...
    @use_sort_alpha.setter
    def use_sort_alpha(self, value: bool):
        ...
    @property
    def use_sync_select(self) -> bool:
        """Sync outliner selection with other editors"""
        ...
    @use_sync_select.setter
    def use_sync_select(self, value: bool):
        ...
    @property
    def show_mode_column(self) -> bool:
        """Show the mode column for mode toggle and activation"""
        ...
    @show_mode_column.setter
    def show_mode_column(self, value: bool):
        ...
    @property
    def show_restrict_column_enable(self) -> bool:
        """Exclude from view layer"""
        ...
    @show_restrict_column_enable.setter
    def show_restrict_column_enable(self, value: bool):
        ...
    @property
    def show_restrict_column_select(self) -> bool:
        """Selectable"""
        ...
    @show_restrict_column_select.setter
    def show_restrict_column_select(self, value: bool):
        ...
    @property
    def show_restrict_column_hide(self) -> bool:
        """Temporarily hide in viewport"""
        ...
    @show_restrict_column_hide.setter
    def show_restrict_column_hide(self, value: bool):
        ...
    @property
    def show_restrict_column_viewport(self) -> bool:
        """Globally disable in viewports"""
        ...
    @show_restrict_column_viewport.setter
    def show_restrict_column_viewport(self, value: bool):
        ...
    @property
    def show_restrict_column_render(self) -> bool:
        """Globally disable in renders"""
        ...
    @show_restrict_column_render.setter
    def show_restrict_column_render(self, value: bool):
        ...
    @property
    def show_restrict_column_holdout(self) -> bool:
        """Holdout"""
        ...
    @show_restrict_column_holdout.setter
    def show_restrict_column_holdout(self, value: bool):
        ...
    @property
    def show_restrict_column_indirect_only(self) -> bool:
        """Indirect only"""
        ...
    @show_restrict_column_indirect_only.setter
    def show_restrict_column_indirect_only(self, value: bool):
        ...
    @property
    def use_filter_object(self) -> bool:
        """Show objects"""
        ...
    @use_filter_object.setter
    def use_filter_object(self, value: bool):
        ...
    @property
    def use_filter_object_content(self) -> bool:
        """Show what is inside the objects elements"""
        ...
    @use_filter_object_content.setter
    def use_filter_object_content(self, value: bool):
        ...
    @property
    def use_filter_children(self) -> bool:
        """Show children"""
        ...
    @use_filter_children.setter
    def use_filter_children(self, value: bool):
        ...
    @property
    def use_filter_collection(self) -> bool:
        """Show collections"""
        ...
    @use_filter_collection.setter
    def use_filter_collection(self, value: bool):
        ...
    @property
    def use_filter_view_layers(self) -> bool:
        """Show all the view layers"""
        ...
    @use_filter_view_layers.setter
    def use_filter_view_layers(self, value: bool):
        ...
    @property
    def filter_state(self) -> Literal['ALL', 'VISIBLE', 'SELECTED', 'ACTIVE', 'SELECTABLE']:

        ...
    @filter_state.setter
    def filter_state(self, value: Literal['ALL', 'VISIBLE', 'SELECTED', 'ACTIVE', 'SELECTABLE']):
        ...
    @property
    def filter_invert(self) -> bool:
        """Invert the object state filter"""
        ...
    @filter_invert.setter
    def filter_invert(self, value: bool):
        ...
    @property
    def use_filter_object_mesh(self) -> bool:
        """Show mesh objects"""
        ...
    @use_filter_object_mesh.setter
    def use_filter_object_mesh(self, value: bool):
        ...
    @property
    def use_filter_object_armature(self) -> bool:
        """Show armature objects"""
        ...
    @use_filter_object_armature.setter
    def use_filter_object_armature(self, value: bool):
        ...
    @property
    def use_filter_object_empty(self) -> bool:
        """Show empty objects"""
        ...
    @use_filter_object_empty.setter
    def use_filter_object_empty(self, value: bool):
        ...
    @property
    def use_filter_object_light(self) -> bool:
        """Show light objects"""
        ...
    @use_filter_object_light.setter
    def use_filter_object_light(self, value: bool):
        ...
    @property
    def use_filter_object_camera(self) -> bool:
        """Show camera objects"""
        ...
    @use_filter_object_camera.setter
    def use_filter_object_camera(self, value: bool):
        ...
    @property
    def use_filter_object_grease_pencil(self) -> bool:
        """Show Grease Pencil objects"""
        ...
    @use_filter_object_grease_pencil.setter
    def use_filter_object_grease_pencil(self, value: bool):
        ...
    @property
    def use_filter_object_others(self) -> bool:
        """Show curves, lattices, light probes, fonts, ..."""
        ...
    @use_filter_object_others.setter
    def use_filter_object_others(self, value: bool):
        ...
    @property
    def use_filter_id_type(self) -> bool:
        """Show only data-blocks of one type"""
        ...
    @use_filter_id_type.setter
    def use_filter_id_type(self, value: bool):
        ...
    @property
    def filter_id_type(self) -> Literal['ACTION', 'ARMATURE', 'BRUSH', 'CACHEFILE', 'CAMERA', 'COLLECTION', 'CURVE', 'CURVES', 'FONT', 'GREASEPENCIL', 'GREASEPENCIL_V3', 'IMAGE', 'KEY', 'LATTICE', 'LIBRARY', 'LIGHT', 'LIGHT_PROBE', 'LINESTYLE', 'MASK', 'MATERIAL', 'MESH', 'META', 'MOVIECLIP', 'NODETREE', 'OBJECT', 'PAINTCURVE', 'PALETTE', 'PARTICLE', 'POINTCLOUD', 'SCENE', 'SCREEN', 'SOUND', 'SPEAKER', 'TEXT', 'TEXTURE', 'VOLUME', 'WINDOWMANAGER', 'WORKSPACE', 'WORLD']:
        """Data-block type to show"""
        ...
    @filter_id_type.setter
    def filter_id_type(self, value: Literal['ACTION', 'ARMATURE', 'BRUSH', 'CACHEFILE', 'CAMERA', 'COLLECTION', 'CURVE', 'CURVES', 'FONT', 'GREASEPENCIL', 'GREASEPENCIL_V3', 'IMAGE', 'KEY', 'LATTICE', 'LIBRARY', 'LIGHT', 'LIGHT_PROBE', 'LINESTYLE', 'MASK', 'MATERIAL', 'MESH', 'META', 'MOVIECLIP', 'NODETREE', 'OBJECT', 'PAINTCURVE', 'PALETTE', 'PARTICLE', 'POINTCLOUD', 'SCENE', 'SCREEN', 'SOUND', 'SPEAKER', 'TEXT', 'TEXTURE', 'VOLUME', 'WINDOWMANAGER', 'WORKSPACE', 'WORLD']):
        ...
    @property
    def use_filter_lib_override_system(self) -> bool:
        """For libraries with overrides created, show the overridden values that are defined/controlled automatically (e.g. to make users of an overridden data-block point to the override data, not the original linked data)"""
        ...
    @use_filter_lib_override_system.setter
    def use_filter_lib_override_system(self, value: bool):
        ...