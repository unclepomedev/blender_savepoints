# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated
from .bpy_prop_collection import bpy_prop_collection

from .Space import Space
class SpaceOutliner(Space):
    @property
    def type(self) -> Literal['EMPTY', 'VIEW_3D', 'IMAGE_EDITOR', 'NODE_EDITOR', 'SEQUENCE_EDITOR', 'CLIP_EDITOR', 'DOPESHEET_EDITOR', 'GRAPH_EDITOR', 'NLA_EDITOR', 'TEXT_EDITOR', 'CONSOLE', 'INFO', 'TOPBAR', 'STATUSBAR', 'OUTLINER', 'PROPERTIES', 'FILE_BROWSER', 'SPREADSHEET', 'PREFERENCES']:
        """Space data type"""
        ...
    show_locked_time: bool
    """Synchronize the visible timeline range with other time-based editors"""
    show_region_header: bool
    display_mode: Literal['SCENES', 'VIEW_LAYER', 'SEQUENCE', 'LIBRARIES', 'DATA_API', 'LIBRARY_OVERRIDES', 'ORPHAN_DATA']
    """Type of information to display"""
    lib_override_view_mode: Literal['PROPERTIES', 'HIERARCHIES']
    """Choose different visualizations of library override data"""
    filter_text: Annotated[str, "is_animatable=False"]
    """Live search filtering string"""
    use_filter_case_sensitive: bool
    """Only use case sensitive matches of search string"""
    use_filter_complete: bool
    """Only use complete matches of search string"""
    use_sort_alpha: bool
    use_sync_select: bool
    """Sync outliner selection with other editors"""
    show_mode_column: bool
    """Show the mode column for mode toggle and activation"""
    show_restrict_column_enable: bool
    """Exclude from view layer"""
    show_restrict_column_select: bool
    """Selectable"""
    show_restrict_column_hide: bool
    """Temporarily hide in viewport"""
    show_restrict_column_viewport: bool
    """Globally disable in viewports"""
    show_restrict_column_render: bool
    """Globally disable in renders"""
    show_restrict_column_holdout: bool
    """Holdout"""
    show_restrict_column_indirect_only: bool
    """Indirect only"""
    use_filter_object: bool
    """Show objects"""
    use_filter_object_content: bool
    """Show what is inside the objects elements"""
    use_filter_children: bool
    """Show children"""
    use_filter_collection: bool
    """Show collections"""
    use_filter_view_layers: bool
    """Show all the view layers"""
    filter_state: Literal['ALL', 'VISIBLE', 'SELECTED', 'ACTIVE', 'SELECTABLE']
    filter_invert: bool
    """Invert the object state filter"""
    use_filter_object_mesh: bool
    """Show mesh objects"""
    use_filter_object_armature: bool
    """Show armature objects"""
    use_filter_object_empty: bool
    """Show empty objects"""
    use_filter_object_light: bool
    """Show light objects"""
    use_filter_object_camera: bool
    """Show camera objects"""
    use_filter_object_grease_pencil: bool
    """Show Grease Pencil objects"""
    use_filter_object_others: bool
    """Show curves, lattices, light probes, fonts, ..."""
    use_filter_id_type: bool
    """Show only data-blocks of one type"""
    filter_id_type: Literal['ACTION', 'ARMATURE', 'BRUSH', 'CACHEFILE', 'CAMERA', 'COLLECTION', 'CURVE', 'CURVES', 'FONT', 'GREASEPENCIL', 'GREASEPENCIL_V3', 'IMAGE', 'KEY', 'LATTICE', 'LIBRARY', 'LIGHT', 'LIGHT_PROBE', 'LINESTYLE', 'MASK', 'MATERIAL', 'MESH', 'META', 'MOVIECLIP', 'NODETREE', 'OBJECT', 'PAINTCURVE', 'PALETTE', 'PARTICLE', 'POINTCLOUD', 'SCENE', 'SCREEN', 'SOUND', 'SPEAKER', 'TEXT', 'TEXTURE', 'VOLUME', 'WINDOWMANAGER', 'WORKSPACE', 'WORLD']
    """Data-block type to show"""
    use_filter_lib_override_system: bool
    """For libraries with overrides created, show the overridden values that are defined/controlled automatically (e.g. to make users of an overridden data-block point to the override data, not the original linked data)"""