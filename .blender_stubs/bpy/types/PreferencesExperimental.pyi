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

    use_undo_legacy: bool
    """Use legacy undo (slower than the new default one, but may be more stable in some cases)"""
    override_auto_resync: bool
    """Disable library overrides automatic resync detection and process on file load (can be useful to help fixing broken files). Also see the "--disable-liboverride-auto-resync" command line option"""
    use_new_curves_tools: bool
    """Enable additional features for the new curves data block"""
    use_cycles_debug: bool
    """Enable Cycles debugging options for developers"""
    use_eevee_debug: bool
    """Enable EEVEE debugging options for developers"""
    use_sculpt_texture_paint: bool
    """Use texture painting in Sculpt Mode"""
    use_extended_asset_browser: bool
    """Enable Asset Browser editor and operators to manage regular data-blocks as assets, not just poses"""
    show_asset_debug_info: bool
    """Enable some extra fields in the Asset Browser to aid in debugging"""
    use_asset_indexing: bool
    """Disable the asset indexer, to force every asset library refresh to completely reread assets from disk"""
    use_viewport_debug: bool
    """Enable viewport debugging options for developers in the overlays pop-over"""
    write_legacy_blend_file_format: bool
    """Use file format used before Blender 5.0. This format is more limited but it may have better compatibility with tools that don't support the new format yet"""
    no_data_block_packing: bool
    """Fall-back to appending instead of packing data-blocks"""
    use_all_linked_data_direct: bool
    """Forces all linked data to be considered as directly linked. Workaround for current issues/limitations in BAT (Blender studio pipeline tool)"""
    use_shader_node_previews: bool
    """Enables previews in the shader node editor"""
    use_geometry_nodes_lists: bool
    """Enable new list types and nodes"""
    use_extensions_debug: bool
    """Extra debugging information & developer support utilities for extensions"""
    use_recompute_usercount_on_save_debug: bool
    """Recompute all ID usercounts before saving to a blendfile. Allows to work around invalid usercount handling in code that may lead to loss of data due to wrongly detected unused data-blocks"""