# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.SpaceTextEditor.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .Space import Space
from .Text import Text

class SpaceTextEditor(Space):

    @property
    def type(self) -> Literal['EMPTY', 'VIEW_3D', 'IMAGE_EDITOR', 'NODE_EDITOR', 'SEQUENCE_EDITOR', 'CLIP_EDITOR', 'DOPESHEET_EDITOR', 'GRAPH_EDITOR', 'NLA_EDITOR', 'TEXT_EDITOR', 'CONSOLE', 'INFO', 'TOPBAR', 'STATUSBAR', 'OUTLINER', 'PROPERTIES', 'FILE_BROWSER', 'SPREADSHEET', 'PREFERENCES']:
        """Space data type"""
        ...
    show_locked_time: bool
    """Synchronize the visible timeline range with other time-based editors"""
    show_region_header: bool

    show_region_footer: bool

    show_region_ui: bool

    text: Annotated[Optional['Text'], "is_animatable=False"]
    """Text displayed and edited in this space"""
    show_word_wrap: bool
    """Wrap words if there is not enough horizontal space"""
    show_line_numbers: bool
    """Show line numbers next to the text"""
    show_syntax_highlight: bool
    """Syntax highlight for scripting"""
    show_line_highlight: bool
    """Highlight the current line"""
    tab_width: Annotated[int, "step=1"]
    """Number of spaces to display tabs with"""
    font_size: Annotated[int, "step=1"]
    """Font size to use for displaying the text"""
    show_margin: bool
    """Show right margin"""
    margin_column: Annotated[int, "step=1"]
    """Column number to show right margin at"""
    top: Annotated[int, "step=1"]
    """Top line visible"""
    @property
    def visible_lines(self) -> Annotated[int, "step=1"]:
        """Amount of lines that can be visible in current editor"""
        ...
    use_overwrite: bool
    """Overwrite characters when typing rather than inserting them"""
    use_live_edit: bool
    """Run Python while editing"""
    use_find_all: bool
    """Search in all text data-blocks, instead of only the active one"""
    use_find_wrap: bool
    """Search again from the start of the file when reaching the end"""
    use_match_case: bool
    """Search string is sensitive to uppercase and lowercase letters"""
    find_text: Annotated[str, "is_animatable=False"]
    """Text to search for with the find tool"""
    replace_text: Annotated[str, "is_animatable=False"]
    """Text to replace selected text with using the replace tool"""
    def is_syntax_highlight_supported(self, *args, **kwargs) -> Any: ...
    def region_location_from_cursor(self, *args, **kwargs) -> Any: ...