# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.FileAssetSelectParams.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .FileSelectParams import FileSelectParams
from .FileAssetSelectIDFilter import FileAssetSelectIDFilter
from .FileSelectIDFilter import FileSelectIDFilter

class FileAssetSelectParams(FileSelectParams):

    @property
    def title(self) -> Annotated[str, "is_animatable=False"]:
        """Title for the file browser"""
        ...
    @property
    def directory(self) -> Annotated[str, "subtype='BYTE_STRING'", "is_animatable=False"]:
        """Directory displayed in the file browser"""
        ...
    @directory.setter
    def directory(self, value: Annotated[str, "subtype='BYTE_STRING'", "is_animatable=False"]) -> None:
        ...
    @property
    def filename(self) -> Annotated[str, "subtype='FILE_NAME'", "is_animatable=False"]:
        """Active file in the file browser"""
        ...
    @filename.setter
    def filename(self, value: Annotated[str, "subtype='FILE_NAME'", "is_animatable=False"]) -> None:
        ...
    @property
    def use_library_browsing(self) -> bool:
        """Whether we may browse Blender files' content or not"""
        ...
    @property
    def display_type(self) -> Literal['LIST_VERTICAL', 'LIST_HORIZONTAL', 'THUMBNAIL']:
        """Display mode for the file list"""
        ...
    @display_type.setter
    def display_type(self, value: Literal['LIST_VERTICAL', 'LIST_HORIZONTAL', 'THUMBNAIL']) -> None:
        ...
    @property
    def recursion_level(self) -> Literal['NONE', 'BLEND', 'ALL_1', 'ALL_2', 'ALL_3']:
        """Numbers of dirtree levels to show simultaneously"""
        ...
    @recursion_level.setter
    def recursion_level(self, value: Literal['NONE', 'BLEND', 'ALL_1', 'ALL_2', 'ALL_3']) -> None:
        ...
    @property
    def show_details_size(self) -> bool:
        """Show a column listing the size of each file"""
        ...
    @show_details_size.setter
    def show_details_size(self, value: bool) -> None:
        ...
    @property
    def show_details_datetime(self) -> bool:
        """Show a column listing the date and time of modification for each file"""
        ...
    @show_details_datetime.setter
    def show_details_datetime(self, value: bool) -> None:
        ...
    @property
    def use_filter(self) -> bool:
        """Enable filtering of files"""
        ...
    @use_filter.setter
    def use_filter(self, value: bool) -> None:
        ...
    @property
    def show_hidden(self) -> bool:
        """Show hidden dot files"""
        ...
    @show_hidden.setter
    def show_hidden(self, value: bool) -> None:
        ...
    @property
    def sort_method(self) -> Literal['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE', 'ASSET_CATALOG']:

        ...
    @sort_method.setter
    def sort_method(self, value: Literal['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE', 'ASSET_CATALOG']) -> None:
        ...
    @property
    def use_sort_invert(self) -> bool:
        """Sort items descending, from highest value to lowest"""
        ...
    @use_sort_invert.setter
    def use_sort_invert(self, value: bool) -> None:
        ...
    @property
    def use_filter_image(self) -> bool:
        """Show image files"""
        ...
    @use_filter_image.setter
    def use_filter_image(self, value: bool) -> None:
        ...
    @property
    def use_filter_blender(self) -> bool:
        """Show .blend files"""
        ...
    @use_filter_blender.setter
    def use_filter_blender(self, value: bool) -> None:
        ...
    @property
    def use_filter_backup(self) -> bool:
        """Show .blend1, .blend2, etc. files"""
        ...
    @use_filter_backup.setter
    def use_filter_backup(self, value: bool) -> None:
        ...
    @property
    def use_filter_movie(self) -> bool:
        """Show movie files"""
        ...
    @use_filter_movie.setter
    def use_filter_movie(self, value: bool) -> None:
        ...
    @property
    def use_filter_script(self) -> bool:
        """Show script files"""
        ...
    @use_filter_script.setter
    def use_filter_script(self, value: bool) -> None:
        ...
    @property
    def use_filter_font(self) -> bool:
        """Show font files"""
        ...
    @use_filter_font.setter
    def use_filter_font(self, value: bool) -> None:
        ...
    @property
    def use_filter_sound(self) -> bool:
        """Show sound files"""
        ...
    @use_filter_sound.setter
    def use_filter_sound(self, value: bool) -> None:
        ...
    @property
    def use_filter_text(self) -> bool:
        """Show text files"""
        ...
    @use_filter_text.setter
    def use_filter_text(self, value: bool) -> None:
        ...
    @property
    def use_filter_volume(self) -> bool:
        """Show 3D volume files"""
        ...
    @use_filter_volume.setter
    def use_filter_volume(self, value: bool) -> None:
        ...
    @property
    def use_filter_folder(self) -> bool:
        """Show folders"""
        ...
    @use_filter_folder.setter
    def use_filter_folder(self, value: bool) -> None:
        ...
    @property
    def use_filter_blendid(self) -> bool:
        """Show .blend files items (objects, materials, etc.)"""
        ...
    @use_filter_blendid.setter
    def use_filter_blendid(self, value: bool) -> None:
        ...
    @property
    def use_filter_asset_only(self) -> bool:
        """Hide .blend files items that are not data-blocks with asset metadata"""
        ...
    @use_filter_asset_only.setter
    def use_filter_asset_only(self, value: bool) -> None:
        ...
    @property
    def filter_id(self) -> Annotated['FileSelectIDFilter', "is_animatable=False"]:
        """Which ID types to show/hide, when browsing a library"""
        ...
    @property
    def filter_glob(self) -> Annotated[str, "is_animatable=False"]:
        """UNIX shell-like filename patterns matching, supports wildcards ('*') and list of patterns separated by ';'"""
        ...
    @filter_glob.setter
    def filter_glob(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def filter_search(self) -> Annotated[str, "is_animatable=False"]:
        """Filter by name or tag, supports '*' wildcard"""
        ...
    @filter_search.setter
    def filter_search(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def display_size(self) -> Annotated[int, "step=1"]:
        """Change the size of thumbnails"""
        ...
    @display_size.setter
    def display_size(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def display_size_discrete(self) -> Literal['TINY', 'SMALL', 'NORMAL', 'BIG', 'LARGE']:
        """Change the size of thumbnails in discrete steps"""
        ...
    @display_size_discrete.setter
    def display_size_discrete(self, value: Literal['TINY', 'SMALL', 'NORMAL', 'BIG', 'LARGE']) -> None:
        ...
    @property
    def list_display_size(self) -> Annotated[int, "step=1"]:
        """Change the size of thumbnails in list views"""
        ...
    @list_display_size.setter
    def list_display_size(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def list_column_size(self) -> Annotated[int, "step=1"]:
        """The width of columns in horizontal list views"""
        ...
    @list_column_size.setter
    def list_column_size(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def asset_library_reference(self) -> Literal['ALL', 'LOCAL', 'ESSENTIALS', 'CUSTOM']:

        ...
    @asset_library_reference.setter
    def asset_library_reference(self, value: Literal['ALL', 'LOCAL', 'ESSENTIALS', 'CUSTOM']) -> None:
        ...
    @property
    def catalog_id(self) -> Annotated[str, "is_animatable=False"]:
        """The UUID of the catalog shown in the browser"""
        ...
    @catalog_id.setter
    def catalog_id(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def filter_asset_id(self) -> Annotated['FileAssetSelectIDFilter', "is_animatable=False"]:
        """Which asset types to show/hide, when browsing an asset library"""
        ...
    @property
    def import_method(self) -> Literal['FOLLOW_PREFS', 'LINK', 'APPEND', 'APPEND_REUSE', 'PACK']:
        """Determine how the asset will be imported"""
        ...
    @import_method.setter
    def import_method(self, value: Literal['FOLLOW_PREFS', 'LINK', 'APPEND', 'APPEND_REUSE', 'PACK']) -> None:
        ...
    @property
    def instance_collections_on_link(self) -> bool:
        """Create instances for collections when linking, rather than adding them directly to the scene"""
        ...
    @instance_collections_on_link.setter
    def instance_collections_on_link(self, value: bool) -> None:
        ...
    @property
    def instance_collections_on_append(self) -> bool:
        """Create instances for collections when appending, rather than adding them directly to the scene"""
        ...
    @instance_collections_on_append.setter
    def instance_collections_on_append(self, value: bool) -> None:
        ...