# Blender Probe Generated Stub for Blender 5.1.0 Alpha
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
from .Addon import Addon
from .PathCompare import PathCompare
from .PreferencesApps import PreferencesApps
from .PreferencesEdit import PreferencesEdit
from .PreferencesExperimental import PreferencesExperimental
from .PreferencesExtensions import PreferencesExtensions
from .PreferencesFilePaths import PreferencesFilePaths
from .PreferencesInput import PreferencesInput
from .PreferencesKeymap import PreferencesKeymap
from .PreferencesSystem import PreferencesSystem
from .PreferencesView import PreferencesView
from .StudioLight import StudioLight
from .Theme import Theme
from .ThemeStyle import ThemeStyle
class Preferences(bpy_struct):
    active_section: str
    app_template: str
    themes: bpy_prop_collection['Theme']
    ui_styles: bpy_prop_collection['ThemeStyle']
    addons: bpy_prop_collection['Addon']
    autoexec_paths: bpy_prop_collection['PathCompare']
    use_recent_searches: bool
    show_hidden_ids: bool
    view: 'PreferencesView'
    edit: 'PreferencesEdit'
    inputs: 'PreferencesInput'
    keymap: 'PreferencesKeymap'
    filepaths: 'PreferencesFilePaths'
    extensions: 'PreferencesExtensions'
    system: 'PreferencesSystem'
    apps: 'PreferencesApps'
    experimental: 'PreferencesExperimental'
    version: int
    studio_lights: bpy_prop_collection['StudioLight']
    use_preferences_save: bool
    is_dirty: bool