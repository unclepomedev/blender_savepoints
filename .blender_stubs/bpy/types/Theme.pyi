# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.Theme.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .ThemeBoneColorSet import ThemeBoneColorSet
from .ThemeClipEditor import ThemeClipEditor
from .ThemeCollectionColor import ThemeCollectionColor
from .ThemeCommon import ThemeCommon
from .ThemeConsole import ThemeConsole
from .ThemeDopeSheet import ThemeDopeSheet
from .ThemeFileBrowser import ThemeFileBrowser
from .ThemeGraphEditor import ThemeGraphEditor
from .ThemeImageEditor import ThemeImageEditor
from .ThemeInfo import ThemeInfo
from .ThemeNLAEditor import ThemeNLAEditor
from .ThemeNodeEditor import ThemeNodeEditor
from .ThemeOutliner import ThemeOutliner
from .ThemePreferences import ThemePreferences
from .ThemeProperties import ThemeProperties
from .ThemeRegions import ThemeRegions
from .ThemeSequenceEditor import ThemeSequenceEditor
from .ThemeSpreadsheet import ThemeSpreadsheet
from .ThemeStatusBar import ThemeStatusBar
from .ThemeStripColor import ThemeStripColor
from .ThemeTextEditor import ThemeTextEditor
from .ThemeTopBar import ThemeTopBar
from .ThemeUserInterface import ThemeUserInterface
from .ThemeView3D import ThemeView3D
from .bpy_prop_collection import bpy_prop_collection

class Theme(bpy_struct):

    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:
        """Name of the theme"""
        ...
    @name.setter
    def name(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def filepath(self) -> Annotated[str, "subtype='FILE_PATH'", "is_animatable=False"]:
        """The path to the preset loaded into this theme (if any)"""
        ...
    @filepath.setter
    def filepath(self, value: Annotated[str, "subtype='FILE_PATH'", "is_animatable=False"]):
        ...
    @property
    def theme_area(self) -> Literal['USER_INTERFACE', 'STYLE', 'REGIONS', 'COMMON', 'VIEW_3D', 'DOPESHEET_EDITOR', 'FILE_BROWSER', 'GRAPH_EDITOR', 'IMAGE_EDITOR', 'INFO', 'CLIP_EDITOR', 'NODE_EDITOR', 'NLA_EDITOR', 'OUTLINER', 'PREFERENCES', 'PROPERTIES', 'CONSOLE', 'SPREADSHEET', 'STATUSBAR', 'TEXT_EDITOR', 'TOPBAR', 'SEQUENCE_EDITOR', 'BONE_COLOR_SETS']:

        ...
    @theme_area.setter
    def theme_area(self, value: Literal['USER_INTERFACE', 'STYLE', 'REGIONS', 'COMMON', 'VIEW_3D', 'DOPESHEET_EDITOR', 'FILE_BROWSER', 'GRAPH_EDITOR', 'IMAGE_EDITOR', 'INFO', 'CLIP_EDITOR', 'NODE_EDITOR', 'NLA_EDITOR', 'OUTLINER', 'PREFERENCES', 'PROPERTIES', 'CONSOLE', 'SPREADSHEET', 'STATUSBAR', 'TEXT_EDITOR', 'TOPBAR', 'SEQUENCE_EDITOR', 'BONE_COLOR_SETS']):
        ...
    @property
    def user_interface(self) -> Annotated['ThemeUserInterface', "is_animatable=False"]:

        ...
    @property
    def regions(self) -> Annotated['ThemeRegions', "is_animatable=False"]:
        """Theme properties for common editor regions"""
        ...
    @property
    def common(self) -> Annotated['ThemeCommon', "is_animatable=False"]:
        """Theme properties shared by different editors"""
        ...
    @property
    def view_3d(self) -> Annotated['ThemeView3D', "is_animatable=False"]:

        ...
    @property
    def graph_editor(self) -> Annotated['ThemeGraphEditor', "is_animatable=False"]:

        ...
    @property
    def file_browser(self) -> Annotated['ThemeFileBrowser', "is_animatable=False"]:

        ...
    @property
    def nla_editor(self) -> Annotated['ThemeNLAEditor', "is_animatable=False"]:

        ...
    @property
    def dopesheet_editor(self) -> Annotated['ThemeDopeSheet', "is_animatable=False"]:

        ...
    @property
    def image_editor(self) -> Annotated['ThemeImageEditor', "is_animatable=False"]:

        ...
    @property
    def sequence_editor(self) -> Annotated['ThemeSequenceEditor', "is_animatable=False"]:

        ...
    @property
    def properties(self) -> Annotated['ThemeProperties', "is_animatable=False"]:

        ...
    @property
    def text_editor(self) -> Annotated['ThemeTextEditor', "is_animatable=False"]:

        ...
    @property
    def node_editor(self) -> Annotated['ThemeNodeEditor', "is_animatable=False"]:

        ...
    @property
    def outliner(self) -> Annotated['ThemeOutliner', "is_animatable=False"]:

        ...
    @property
    def info(self) -> Annotated['ThemeInfo', "is_animatable=False"]:

        ...
    @property
    def preferences(self) -> Annotated['ThemePreferences', "is_animatable=False"]:

        ...
    @property
    def console(self) -> Annotated['ThemeConsole', "is_animatable=False"]:

        ...
    @property
    def clip_editor(self) -> Annotated['ThemeClipEditor', "is_animatable=False"]:

        ...
    @property
    def topbar(self) -> Annotated['ThemeTopBar', "is_animatable=False"]:

        ...
    @property
    def statusbar(self) -> Annotated['ThemeStatusBar', "is_animatable=False"]:

        ...
    @property
    def spreadsheet(self) -> Annotated['ThemeSpreadsheet', "is_animatable=False"]:

        ...
    @property
    def bone_color_sets(self) -> Annotated[bpy_prop_collection['ThemeBoneColorSet'], "is_animatable=False"]:

        ...
    @property
    def collection_color(self) -> Annotated[bpy_prop_collection['ThemeCollectionColor'], "is_animatable=False"]:

        ...
    @property
    def strip_color(self) -> Annotated[bpy_prop_collection['ThemeStripColor'], "is_animatable=False"]:

        ...