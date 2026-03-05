# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.PreferencesExperimental.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class PreferencesExperimental(bpy_struct):

    @property
    def use_undo_legacy(self) -> bool:
        """Use legacy undo (slower than the new default one, but may be more stable in some cases)"""
        ...
    @use_undo_legacy.setter
    def use_undo_legacy(self, value: bool) -> None:
        ...
    @property
    def override_auto_resync(self) -> bool:
        """Disable library overrides automatic resync detection and process on file load (can be useful to help fixing broken files). Also see the "--disable-liboverride-auto-resync" command line option"""
        ...
    @override_auto_resync.setter
    def override_auto_resync(self, value: bool) -> None:
        ...
    @property
    def use_new_curves_tools(self) -> bool:
        """Enable additional features for the new curves data block"""
        ...
    @use_new_curves_tools.setter
    def use_new_curves_tools(self, value: bool) -> None:
        ...
    @property
    def use_cycles_debug(self) -> bool:
        """Enable Cycles debugging options for developers"""
        ...
    @use_cycles_debug.setter
    def use_cycles_debug(self, value: bool) -> None:
        ...
    @property
    def use_eevee_debug(self) -> bool:
        """Enable EEVEE debugging options for developers"""
        ...
    @use_eevee_debug.setter
    def use_eevee_debug(self, value: bool) -> None:
        ...
    @property
    def use_sculpt_texture_paint(self) -> bool:
        """Use texture painting in Sculpt Mode"""
        ...
    @use_sculpt_texture_paint.setter
    def use_sculpt_texture_paint(self, value: bool) -> None:
        ...
    @property
    def use_extended_asset_browser(self) -> bool:
        """Enable Asset Browser editor and operators to manage regular data-blocks as assets, not just poses"""
        ...
    @use_extended_asset_browser.setter
    def use_extended_asset_browser(self, value: bool) -> None:
        ...
    @property
    def show_asset_debug_info(self) -> bool:
        """Enable some extra fields in the Asset Browser to aid in debugging"""
        ...
    @show_asset_debug_info.setter
    def show_asset_debug_info(self, value: bool) -> None:
        ...
    @property
    def use_asset_indexing(self) -> bool:
        """Disable the asset indexer, to force every asset library refresh to completely reread assets from disk"""
        ...
    @use_asset_indexing.setter
    def use_asset_indexing(self, value: bool) -> None:
        ...
    @property
    def use_viewport_debug(self) -> bool:
        """Enable viewport debugging options for developers in the overlays pop-over"""
        ...
    @use_viewport_debug.setter
    def use_viewport_debug(self, value: bool) -> None:
        ...
    @property
    def write_legacy_blend_file_format(self) -> bool:
        """Use file format used before Blender 5.0. This format is more limited but it may have better compatibility with tools that don't support the new format yet"""
        ...
    @write_legacy_blend_file_format.setter
    def write_legacy_blend_file_format(self, value: bool) -> None:
        ...
    @property
    def no_data_block_packing(self) -> bool:
        """Fall-back to appending instead of packing data-blocks"""
        ...
    @no_data_block_packing.setter
    def no_data_block_packing(self, value: bool) -> None:
        ...
    @property
    def use_all_linked_data_direct(self) -> bool:
        """Forces all linked data to be considered as directly linked. Workaround for current issues/limitations in BAT (Blender studio pipeline tool)"""
        ...
    @use_all_linked_data_direct.setter
    def use_all_linked_data_direct(self, value: bool) -> None:
        ...
    @property
    def use_shader_node_previews(self) -> bool:
        """Enables previews in the shader node editor"""
        ...
    @use_shader_node_previews.setter
    def use_shader_node_previews(self, value: bool) -> None:
        ...
    @property
    def use_geometry_nodes_lists(self) -> bool:
        """Enable new list types and nodes"""
        ...
    @use_geometry_nodes_lists.setter
    def use_geometry_nodes_lists(self, value: bool) -> None:
        ...
    @property
    def use_extensions_debug(self) -> bool:
        """Extra debugging information & developer support utilities for extensions"""
        ...
    @use_extensions_debug.setter
    def use_extensions_debug(self, value: bool) -> None:
        ...
    @property
    def use_recompute_usercount_on_save_debug(self) -> bool:
        """Recompute all ID usercounts before saving to a blendfile. Allows to work around invalid usercount handling in code that may lead to loss of data due to wrongly detected unused data-blocks"""
        ...
    @use_recompute_usercount_on_save_debug.setter
    def use_recompute_usercount_on_save_debug(self, value: bool) -> None:
        ...