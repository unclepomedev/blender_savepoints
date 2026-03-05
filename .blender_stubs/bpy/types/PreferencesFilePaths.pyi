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

    @property
    def show_hidden_files_datablocks(self) -> bool:
        """Show files and data-blocks that are normally hidden"""
        ...
    @show_hidden_files_datablocks.setter
    def show_hidden_files_datablocks(self, value: bool) -> None:
        ...
    @property
    def use_filter_files(self) -> bool:
        """Enable filtering of files in the File Browser"""
        ...
    @use_filter_files.setter
    def use_filter_files(self, value: bool) -> None:
        ...
    @property
    def show_recent_locations(self) -> bool:
        """Show Recent locations list in the File Browser"""
        ...
    @show_recent_locations.setter
    def show_recent_locations(self, value: bool) -> None:
        ...
    @property
    def show_system_bookmarks(self) -> bool:
        """Show System locations list in the File Browser"""
        ...
    @show_system_bookmarks.setter
    def show_system_bookmarks(self, value: bool) -> None:
        ...
    @property
    def use_relative_paths(self) -> bool:
        """Default relative path option for the file selector, when no path is defined yet"""
        ...
    @use_relative_paths.setter
    def use_relative_paths(self, value: bool) -> None:
        ...
    @property
    def use_file_compression(self) -> bool:
        """Enable file compression when saving .blend files"""
        ...
    @use_file_compression.setter
    def use_file_compression(self, value: bool) -> None:
        ...
    @property
    def use_load_ui(self) -> bool:
        """Load user interface setup when loading .blend files"""
        ...
    @use_load_ui.setter
    def use_load_ui(self, value: bool) -> None:
        ...
    @property
    def use_scripts_auto_execute(self) -> bool:
        """Allow any .blend file to run scripts automatically (unsafe with blend files from an untrusted source)"""
        ...
    @use_scripts_auto_execute.setter
    def use_scripts_auto_execute(self, value: bool) -> None:
        ...
    @property
    def use_tabs_as_spaces(self) -> bool:
        """Automatically convert all new tabs into spaces for new and loaded text files"""
        ...
    @use_tabs_as_spaces.setter
    def use_tabs_as_spaces(self, value: bool) -> None:
        ...
    @property
    def use_extension_online_access_handled(self) -> bool:
        """The user has been shown the "Online Access" prompt and made a choice"""
        ...
    @use_extension_online_access_handled.setter
    def use_extension_online_access_handled(self, value: bool) -> None:
        ...
    @property
    def font_directory(self) -> Annotated[str, "subtype='DIR_PATH'", "is_animatable=False"]:
        """The default directory to search for loading fonts"""
        ...
    @font_directory.setter
    def font_directory(self, value: Annotated[str, "subtype='DIR_PATH'", "is_animatable=False"]) -> None:
        ...
    @property
    def texture_directory(self) -> Annotated[str, "subtype='DIR_PATH'", "is_animatable=False"]:
        """The default directory to search for textures"""
        ...
    @texture_directory.setter
    def texture_directory(self, value: Annotated[str, "subtype='DIR_PATH'", "is_animatable=False"]) -> None:
        ...
    @property
    def render_output_directory(self) -> Annotated[str, "subtype='DIR_PATH'", "is_animatable=False"]:
        """The default directory for rendering output, for new scenes"""
        ...
    @render_output_directory.setter
    def render_output_directory(self, value: Annotated[str, "subtype='DIR_PATH'", "is_animatable=False"]) -> None:
        ...
    @property
    def script_directories(self) -> Annotated['ScriptDirectoryCollection', "is_animatable=False"]:

        ...
    @property
    def i18n_branches_directory(self) -> Annotated[str, "subtype='DIR_PATH'", "is_animatable=False"]:
        """The path to the '/branches' directory of your local svn-translation copy, to allow translating from the UI"""
        ...
    @i18n_branches_directory.setter
    def i18n_branches_directory(self, value: Annotated[str, "subtype='DIR_PATH'", "is_animatable=False"]) -> None:
        ...
    @property
    def sound_directory(self) -> Annotated[str, "subtype='DIR_PATH'", "is_animatable=False"]:
        """The default directory to search for sounds"""
        ...
    @sound_directory.setter
    def sound_directory(self, value: Annotated[str, "subtype='DIR_PATH'", "is_animatable=False"]) -> None:
        ...
    @property
    def temporary_directory(self) -> Annotated[str, "subtype='DIR_PATH'", "is_animatable=False"]:
        """The directory for storing temporary save files. The path must reference an existing directory or it will be ignored"""
        ...
    @temporary_directory.setter
    def temporary_directory(self, value: Annotated[str, "subtype='DIR_PATH'", "is_animatable=False"]) -> None:
        ...
    @property
    def render_cache_directory(self) -> Annotated[str, "subtype='DIR_PATH'", "is_animatable=False"]:
        """Where to cache raw render results"""
        ...
    @render_cache_directory.setter
    def render_cache_directory(self, value: Annotated[str, "subtype='DIR_PATH'", "is_animatable=False"]) -> None:
        ...
    @property
    def image_editor(self) -> Annotated[str, "subtype='FILE_PATH'", "is_animatable=False"]:
        """Path to an image editor"""
        ...
    @image_editor.setter
    def image_editor(self, value: Annotated[str, "subtype='FILE_PATH'", "is_animatable=False"]) -> None:
        ...
    @property
    def text_editor(self) -> Annotated[str, "subtype='FILE_PATH'", "is_animatable=False"]:
        """Command to launch the text editor, either a full path or a command in $PATH.
Use the internal editor when left blank"""
        ...
    @text_editor.setter
    def text_editor(self, value: Annotated[str, "subtype='FILE_PATH'", "is_animatable=False"]) -> None:
        ...
    @property
    def text_editor_args(self) -> Annotated[str, "is_animatable=False"]:
        """Defines the specific format of the arguments with which the text editor opens files. The supported expansions are as follows:

$filepath The absolute path of the file.
$line The line to open at (Optional).
$column The column to open from the beginning of the line (Optional).
$line0 & column0 start at zero.
Example: -f $filepath -l $line -c $column"""
        ...
    @text_editor_args.setter
    def text_editor_args(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def animation_player(self) -> Annotated[str, "subtype='FILE_PATH'", "is_animatable=False"]:
        """Path to a custom animation/frame sequence player"""
        ...
    @animation_player.setter
    def animation_player(self, value: Annotated[str, "subtype='FILE_PATH'", "is_animatable=False"]) -> None:
        ...
    @property
    def animation_player_preset(self) -> Literal['INTERNAL', 'DJV', 'FRAMECYCLER', 'RV', 'MPLAYER', 'CUSTOM']:
        """Preset configs for external animation players"""
        ...
    @animation_player_preset.setter
    def animation_player_preset(self, value: Literal['INTERNAL', 'DJV', 'FRAMECYCLER', 'RV', 'MPLAYER', 'CUSTOM']) -> None:
        ...
    @property
    def save_version(self) -> Annotated[int, "step=1"]:
        """The number of old versions to maintain in the current directory, when manually saving"""
        ...
    @save_version.setter
    def save_version(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def use_auto_save_temporary_files(self) -> bool:
        """Automatic saving of temporary files in temp directory, uses process ID.
Warning: Sculpt and edit mode data won't be saved"""
        ...
    @use_auto_save_temporary_files.setter
    def use_auto_save_temporary_files(self, value: bool) -> None:
        ...
    @property
    def auto_save_time(self) -> Annotated[int, "step=1"]:
        """The time (in minutes) to wait between automatic temporary saves"""
        ...
    @auto_save_time.setter
    def auto_save_time(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def recent_files(self) -> Annotated[int, "step=1"]:
        """Maximum number of recently opened files to remember"""
        ...
    @recent_files.setter
    def recent_files(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def file_preview_type(self) -> Literal['NONE', 'AUTO', 'SCREENSHOT', 'CAMERA']:
        """What type of blend preview to create"""
        ...
    @file_preview_type.setter
    def file_preview_type(self, value: Literal['NONE', 'AUTO', 'SCREENSHOT', 'CAMERA']) -> None:
        ...
    @property
    def asset_libraries(self) -> Annotated['AssetLibraryCollection', "is_animatable=False"]:

        ...
    @property
    def active_asset_library(self) -> Annotated[int, "step=1"]:
        """Index of the asset library being edited in the Preferences UI"""
        ...
    @active_asset_library.setter
    def active_asset_library(self, value: Annotated[int, "step=1"]) -> None:
        ...