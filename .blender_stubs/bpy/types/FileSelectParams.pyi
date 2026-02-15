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
from .FileSelectIDFilter import FileSelectIDFilter
class FileSelectParams(bpy_struct):
    @property
    def title(self) -> Annotated[str, "is_animatable=False"]:
        """Title for the file browser"""
        ...
    directory: Annotated[str, "subtype='BYTE_STRING'", "is_animatable=False"]
    """Directory displayed in the file browser"""
    filename: Annotated[str, "subtype='FILE_NAME'", "is_animatable=False"]
    """Active file in the file browser"""
    @property
    def use_library_browsing(self) -> bool:
        """Whether we may browse Blender files' content or not"""
        ...
    display_type: Literal['LIST_VERTICAL', 'LIST_HORIZONTAL', 'THUMBNAIL']
    """Display mode for the file list"""
    recursion_level: Literal['NONE', 'BLEND', 'ALL_1', 'ALL_2', 'ALL_3']
    """Numbers of dirtree levels to show simultaneously"""
    show_details_size: bool
    """Show a column listing the size of each file"""
    show_details_datetime: bool
    """Show a column listing the date and time of modification for each file"""
    use_filter: bool
    """Enable filtering of files"""
    show_hidden: bool
    """Show hidden dot files"""
    sort_method: Literal['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE', 'ASSET_CATALOG']
    use_sort_invert: bool
    """Sort items descending, from highest value to lowest"""
    use_filter_image: bool
    """Show image files"""
    use_filter_blender: bool
    """Show .blend files"""
    use_filter_backup: bool
    """Show .blend1, .blend2, etc. files"""
    use_filter_movie: bool
    """Show movie files"""
    use_filter_script: bool
    """Show script files"""
    use_filter_font: bool
    """Show font files"""
    use_filter_sound: bool
    """Show sound files"""
    use_filter_text: bool
    """Show text files"""
    use_filter_volume: bool
    """Show 3D volume files"""
    use_filter_folder: bool
    """Show folders"""
    use_filter_blendid: bool
    """Show .blend files items (objects, materials, etc.)"""
    use_filter_asset_only: bool
    """Hide .blend files items that are not data-blocks with asset metadata"""
    @property
    def filter_id(self) -> Annotated['FileSelectIDFilter', "is_animatable=False"]:
        """Which ID types to show/hide, when browsing a library"""
        ...
    filter_glob: Annotated[str, "is_animatable=False"]
    """UNIX shell-like filename patterns matching, supports wildcards ('*') and list of patterns separated by ';'"""
    filter_search: Annotated[str, "is_animatable=False"]
    """Filter by name or tag, supports '*' wildcard"""
    display_size: Annotated[int, "step=1"]
    """Change the size of thumbnails"""
    display_size_discrete: Literal['TINY', 'SMALL', 'NORMAL', 'BIG', 'LARGE']
    """Change the size of thumbnails in discrete steps"""
    list_display_size: Annotated[int, "step=1"]
    """Change the size of thumbnails in list views"""
    list_column_size: Annotated[int, "step=1"]
    """The width of columns in horizontal list views"""