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
    @property
    def show_locked_time(self) -> bool:
        """Synchronize the visible timeline range with other time-based editors"""
        ...
    @show_locked_time.setter
    def show_locked_time(self, value: bool):
        ...
    @property
    def show_region_header(self) -> bool:

        ...
    @show_region_header.setter
    def show_region_header(self, value: bool):
        ...
    @property
    def show_region_footer(self) -> bool:

        ...
    @show_region_footer.setter
    def show_region_footer(self, value: bool):
        ...
    @property
    def show_region_ui(self) -> bool:

        ...
    @show_region_ui.setter
    def show_region_ui(self, value: bool):
        ...
    @property
    def text(self) -> Annotated[Optional['Text'], "is_animatable=False"]:
        """Text displayed and edited in this space"""
        ...
    @text.setter
    def text(self, value: Annotated[Optional['Text'], "is_animatable=False"]):
        ...
    @property
    def show_word_wrap(self) -> bool:
        """Wrap words if there is not enough horizontal space"""
        ...
    @show_word_wrap.setter
    def show_word_wrap(self, value: bool):
        ...
    @property
    def show_line_numbers(self) -> bool:
        """Show line numbers next to the text"""
        ...
    @show_line_numbers.setter
    def show_line_numbers(self, value: bool):
        ...
    @property
    def show_syntax_highlight(self) -> bool:
        """Syntax highlight for scripting"""
        ...
    @show_syntax_highlight.setter
    def show_syntax_highlight(self, value: bool):
        ...
    @property
    def show_line_highlight(self) -> bool:
        """Highlight the current line"""
        ...
    @show_line_highlight.setter
    def show_line_highlight(self, value: bool):
        ...
    @property
    def tab_width(self) -> Annotated[int, "step=1"]:
        """Number of spaces to display tabs with"""
        ...
    @tab_width.setter
    def tab_width(self, value: Annotated[int, "step=1"]):
        ...
    @property
    def font_size(self) -> Annotated[int, "step=1"]:
        """Font size to use for displaying the text"""
        ...
    @font_size.setter
    def font_size(self, value: Annotated[int, "step=1"]):
        ...
    @property
    def show_margin(self) -> bool:
        """Show right margin"""
        ...
    @show_margin.setter
    def show_margin(self, value: bool):
        ...
    @property
    def margin_column(self) -> Annotated[int, "step=1"]:
        """Column number to show right margin at"""
        ...
    @margin_column.setter
    def margin_column(self, value: Annotated[int, "step=1"]):
        ...
    @property
    def top(self) -> Annotated[int, "step=1"]:
        """Top line visible"""
        ...
    @top.setter
    def top(self, value: Annotated[int, "step=1"]):
        ...
    @property
    def visible_lines(self) -> Annotated[int, "step=1"]:
        """Amount of lines that can be visible in current editor"""
        ...
    @property
    def use_overwrite(self) -> bool:
        """Overwrite characters when typing rather than inserting them"""
        ...
    @use_overwrite.setter
    def use_overwrite(self, value: bool):
        ...
    @property
    def use_live_edit(self) -> bool:
        """Run Python while editing"""
        ...
    @use_live_edit.setter
    def use_live_edit(self, value: bool):
        ...
    @property
    def use_find_all(self) -> bool:
        """Search in all text data-blocks, instead of only the active one"""
        ...
    @use_find_all.setter
    def use_find_all(self, value: bool):
        ...
    @property
    def use_find_wrap(self) -> bool:
        """Search again from the start of the file when reaching the end"""
        ...
    @use_find_wrap.setter
    def use_find_wrap(self, value: bool):
        ...
    @property
    def use_match_case(self) -> bool:
        """Search string is sensitive to uppercase and lowercase letters"""
        ...
    @use_match_case.setter
    def use_match_case(self, value: bool):
        ...
    @property
    def find_text(self) -> Annotated[str, "is_animatable=False"]:
        """Text to search for with the find tool"""
        ...
    @find_text.setter
    def find_text(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def replace_text(self) -> Annotated[str, "is_animatable=False"]:
        """Text to replace selected text with using the replace tool"""
        ...
    @replace_text.setter
    def replace_text(self, value: Annotated[str, "is_animatable=False"]):
        ...
    def is_syntax_highlight_supported(self, *args, **kwargs) -> Any: ...
    def region_location_from_cursor(self, *args, **kwargs) -> Any: ...