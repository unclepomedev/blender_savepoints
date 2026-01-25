# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .Space import Space
from .Text import Text
class SpaceTextEditor(Space):
    type: str
    show_locked_time: bool
    show_region_header: bool
    show_region_footer: bool
    show_region_ui: bool
    text: 'Text'
    show_word_wrap: bool
    show_line_numbers: bool
    show_syntax_highlight: bool
    show_line_highlight: bool
    tab_width: int
    font_size: int
    show_margin: bool
    margin_column: int
    top: int
    visible_lines: int
    use_overwrite: bool
    use_live_edit: bool
    use_find_all: bool
    use_find_wrap: bool
    use_match_case: bool
    find_text: str
    replace_text: str
    def is_syntax_highlight_supported(self, *args, **kwargs) -> Any: ...
    def region_location_from_cursor(self, *args, **kwargs) -> Any: ...