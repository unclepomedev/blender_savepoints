# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .FileSelectParams import FileSelectParams
from .FileAssetSelectIDFilter import FileAssetSelectIDFilter
from .FileSelectIDFilter import FileSelectIDFilter
class FileAssetSelectParams(FileSelectParams):
    title: str
    directory: str
    filename: str
    use_library_browsing: bool
    display_type: str
    recursion_level: str
    show_details_size: bool
    show_details_datetime: bool
    use_filter: bool
    show_hidden: bool
    sort_method: str
    use_sort_invert: bool
    use_filter_image: bool
    use_filter_blender: bool
    use_filter_backup: bool
    use_filter_movie: bool
    use_filter_script: bool
    use_filter_font: bool
    use_filter_sound: bool
    use_filter_text: bool
    use_filter_volume: bool
    use_filter_folder: bool
    use_filter_blendid: bool
    use_filter_asset_only: bool
    filter_id: 'FileSelectIDFilter'
    filter_glob: str
    filter_search: str
    display_size: int
    display_size_discrete: str
    list_display_size: int
    list_column_size: int
    asset_library_reference: str
    catalog_id: str
    filter_asset_id: 'FileAssetSelectIDFilter'
    import_method: str
    instance_collections_on_link: bool
    instance_collections_on_append: bool