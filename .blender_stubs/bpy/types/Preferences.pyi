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
from .Addon import Addon
from .Addons import Addons
from .PathCompare import PathCompare
from .PathCompareCollection import PathCompareCollection
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
from .StudioLights import StudioLights
from .Theme import Theme
from .ThemeStyle import ThemeStyle
class Preferences(bpy_struct):
    active_section: Literal['INTERFACE', 'VIEWPORT', 'LIGHTS', 'EDITING', 'ANIMATION', 'EXTENSIONS', 'ADDONS', 'THEMES', 'INPUT', 'NAVIGATION', 'KEYMAP', 'SYSTEM', 'SAVE_LOAD', 'FILE_PATHS', 'DEVELOPER_TOOLS', 'EXPERIMENTAL']
    """Preferences"""
    app_template: Annotated[str, "is_animatable=False"]
    @property
    def themes(self) -> Annotated[bpy_prop_collection['Theme'], "is_animatable=False"]:
        ...
    @property
    def ui_styles(self) -> Annotated[bpy_prop_collection['ThemeStyle'], "is_animatable=False"]:
        ...
    @property
    def addons(self) -> Annotated['Addons', "is_animatable=False"]:
        ...
    @property
    def autoexec_paths(self) -> Annotated['PathCompareCollection', "is_animatable=False"]:
        ...
    use_recent_searches: bool
    """Sort the recently searched items at the top"""
    @property
    def view(self) -> Annotated['PreferencesView', "is_animatable=False"]:
        """Preferences related to viewing data"""
        ...
    @property
    def edit(self) -> Annotated['PreferencesEdit', "is_animatable=False"]:
        """Settings for interacting with Blender data"""
        ...
    @property
    def inputs(self) -> Annotated['PreferencesInput', "is_animatable=False"]:
        """Settings for input devices"""
        ...
    @property
    def keymap(self) -> Annotated['PreferencesKeymap', "is_animatable=False"]:
        """Shortcut setup for keyboards and other input devices"""
        ...
    @property
    def filepaths(self) -> Annotated['PreferencesFilePaths', "is_animatable=False"]:
        """Default paths for external files"""
        ...
    @property
    def extensions(self) -> Annotated['PreferencesExtensions', "is_animatable=False"]:
        """Settings for extensions"""
        ...
    @property
    def system(self) -> Annotated['PreferencesSystem', "is_animatable=False"]:
        """Graphics driver and operating system settings"""
        ...
    @property
    def apps(self) -> Annotated['PreferencesApps', "is_animatable=False"]:
        """Preferences that work only for apps"""
        ...
    @property
    def experimental(self) -> Annotated['PreferencesExperimental', "is_animatable=False"]:
        """Settings for features that are still early in their development stage"""
        ...
    @property
    def version(self) -> Annotated[list[int], "subtype='XYZ'", "step=1"]:
        """Version of Blender the userpref.blend was saved with"""
        ...
    @property
    def studio_lights(self) -> Annotated['StudioLights', "is_animatable=False"]:
        ...
    use_preferences_save: bool
    """Save preferences on exit when modified (unless factory settings have been loaded)"""
    is_dirty: bool
    """Preferences have changed"""