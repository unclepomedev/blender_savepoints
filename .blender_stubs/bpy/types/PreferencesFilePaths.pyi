# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
from .ScriptDirectory import ScriptDirectory
from .UserAssetLibrary import UserAssetLibrary
class PreferencesFilePaths(bpy_struct):
    show_hidden_files_datablocks: bool
    use_filter_files: bool
    show_recent_locations: bool
    show_system_bookmarks: bool
    use_relative_paths: bool
    use_file_compression: bool
    use_load_ui: bool
    use_scripts_auto_execute: bool
    use_tabs_as_spaces: bool
    use_extension_online_access_handled: bool
    font_directory: str
    texture_directory: str
    render_output_directory: str
    script_directories: bpy_prop_collection['ScriptDirectory']
    i18n_branches_directory: str
    sound_directory: str
    temporary_directory: str
    render_cache_directory: str
    image_editor: str
    text_editor: str
    text_editor_args: str
    animation_player: str
    animation_player_preset: str
    save_version: int
    use_auto_save_temporary_files: bool
    auto_save_time: int
    recent_files: int
    file_preview_type: str
    asset_libraries: bpy_prop_collection['UserAssetLibrary']
    active_asset_library: int