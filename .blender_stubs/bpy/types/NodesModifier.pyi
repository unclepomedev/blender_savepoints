# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .Modifier import Modifier
from .NodeTree import NodeTree
from .NodesModifierBake import NodesModifierBake
from .NodesModifierPanel import NodesModifierPanel
from .NodesModifierWarning import NodesModifierWarning
class NodesModifier(Modifier):
    name: str
    type: str
    show_viewport: bool
    show_render: bool
    show_in_editmode: bool
    show_on_cage: bool
    show_expanded: bool
    is_active: bool
    use_pin_to_last: bool
    is_override_data: bool
    use_apply_on_spline: bool
    execution_time: float
    persistent_uid: int
    node_group: 'NodeTree'
    bake_directory: str
    bake_target: str
    bakes: bpy_prop_collection['NodesModifierBake']
    panels: bpy_prop_collection['NodesModifierPanel']
    show_group_selector: bool
    show_manage_panel: bool
    node_warnings: bpy_prop_collection['NodesModifierWarning']
    open_output_attributes_panel: bool
    open_manage_panel: bool
    open_bake_panel: bool
    open_named_attributes_panel: bool
    open_bake_data_blocks_panel: bool
    open_warnings_panel: bool
    def bl_system_properties_get(self, *args, **kwargs) -> Any: ...