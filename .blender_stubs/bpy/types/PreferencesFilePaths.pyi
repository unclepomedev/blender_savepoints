# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.PreferencesFilePaths.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .AssetLibraryCollection import AssetLibraryCollection
from .ScriptDirectory import ScriptDirectory
from .ScriptDirectoryCollection import ScriptDirectoryCollection
from .UserAssetLibrary import UserAssetLibrary
from .bpy_prop_collection import bpy_prop_collection

class PreferencesFilePaths(bpy_struct):

    show_hidden_files_datablocks: bool
    """Show files and data-blocks that are normally hidden"""
    use_filter_files: bool
    """Enable filtering of files in the File Browser"""
    show_recent_locations: bool
    """Show Recent locations list in the File Browser"""
    show_system_bookmarks: bool
    """Show System locations list in the File Browser"""
    use_relative_paths: bool
    """Default relative path option for the file selector, when no path is defined yet"""
    use_file_compression: bool
    """Enable file compression when saving .blend files"""
    use_load_ui: bool
    """Load user interface setup when loading .blend files"""
    use_scripts_auto_execute: bool
    """Allow any .blend file to run scripts automatically (unsafe with blend files from an untrusted source)"""
    use_tabs_as_spaces: bool
    """Automatically convert all new tabs into spaces for new and loaded text files"""
    use_extension_online_access_handled: bool
    """The user has been shown the "Online Access" prompt and made a choice"""
    font_directory: Annotated[str, "subtype='DIR_PATH'", "is_animatable=False"]
    """The default directory to search for loading fonts"""
    texture_directory: Annotated[str, "subtype='DIR_PATH'", "is_animatable=False"]
    """The default directory to search for textures"""
    render_output_directory: Annotated[str, "subtype='DIR_PATH'", "is_animatable=False"]
    """The default directory for rendering output, for new scenes"""
    @property
    def script_directories(self) -> Annotated['ScriptDirectoryCollection', "is_animatable=False"]:

        ...
    i18n_branches_directory: Annotated[str, "subtype='DIR_PATH'", "is_animatable=False"]
    """The path to the '/branches' directory of your local svn-translation copy, to allow translating from the UI"""
    sound_directory: Annotated[str, "subtype='DIR_PATH'", "is_animatable=False"]
    """The default directory to search for sounds"""
    temporary_directory: Annotated[str, "subtype='DIR_PATH'", "is_animatable=False"]
    """The directory for storing temporary save files. The path must reference an existing directory or it will be ignored"""
    render_cache_directory: Annotated[str, "subtype='DIR_PATH'", "is_animatable=False"]
    """Where to cache raw render results"""
    image_editor: Annotated[str, "subtype='FILE_PATH'", "is_animatable=False"]
    """Path to an image editor"""
    text_editor: Annotated[str, "subtype='FILE_PATH'", "is_animatable=False"]
    """Command to launch the text editor, either a full path or a command in $PATH.
Use the internal editor when left blank"""
    text_editor_args: Annotated[str, "is_animatable=False"]
    """Defines the specific format of the arguments with which the text editor opens files. The supported expansions are as follows:

$filepath The absolute path of the file.
$line The line to open at (Optional).
$column The column to open from the beginning of the line (Optional).
$line0 & column0 start at zero.
Example: -f $filepath -l $line -c $column"""
    animation_player: Annotated[str, "subtype='FILE_PATH'", "is_animatable=False"]
    """Path to a custom animation/frame sequence player"""
    animation_player_preset: Literal['INTERNAL', 'DJV', 'FRAMECYCLER', 'RV', 'MPLAYER', 'CUSTOM']
    """Preset configs for external animation players"""
    save_version: Annotated[int, "step=1"]
    """The number of old versions to maintain in the current directory, when manually saving"""
    use_auto_save_temporary_files: bool
    """Automatic saving of temporary files in temp directory, uses process ID.
Warning: Sculpt and edit mode data won't be saved"""
    auto_save_time: Annotated[int, "step=1"]
    """The time (in minutes) to wait between automatic temporary saves"""
    recent_files: Annotated[int, "step=1"]
    """Maximum number of recently opened files to remember"""
    file_preview_type: Literal['NONE', 'AUTO', 'SCREENSHOT', 'CAMERA']
    """What type of blend preview to create"""
    @property
    def asset_libraries(self) -> Annotated['AssetLibraryCollection', "is_animatable=False"]:

        ...
    active_asset_library: Annotated[int, "step=1"]
    """Index of the asset library being edited in the Preferences UI"""