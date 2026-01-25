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
class Theme(bpy_struct):
    name: str
    filepath: str
    theme_area: str
    user_interface: 'ThemeUserInterface'
    regions: 'ThemeRegions'
    common: 'ThemeCommon'
    view_3d: 'ThemeView3D'
    graph_editor: 'ThemeGraphEditor'
    file_browser: 'ThemeFileBrowser'
    nla_editor: 'ThemeNLAEditor'
    dopesheet_editor: 'ThemeDopeSheet'
    image_editor: 'ThemeImageEditor'
    sequence_editor: 'ThemeSequenceEditor'
    properties: 'ThemeProperties'
    text_editor: 'ThemeTextEditor'
    node_editor: 'ThemeNodeEditor'
    outliner: 'ThemeOutliner'
    info: 'ThemeInfo'
    preferences: 'ThemePreferences'
    console: 'ThemeConsole'
    clip_editor: 'ThemeClipEditor'
    topbar: 'ThemeTopBar'
    statusbar: 'ThemeStatusBar'
    spreadsheet: 'ThemeSpreadsheet'
    bone_color_sets: bpy_prop_collection['ThemeBoneColorSet']
    collection_color: bpy_prop_collection['ThemeCollectionColor']
    strip_color: bpy_prop_collection['ThemeStripColor']