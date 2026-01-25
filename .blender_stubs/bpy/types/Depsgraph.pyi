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
from .DepsgraphObjectInstance import DepsgraphObjectInstance
from .DepsgraphUpdate import DepsgraphUpdate
from .ID import ID
from .Object import Object
from .Scene import Scene
from .ViewLayer import ViewLayer
class Depsgraph(bpy_struct):
    mode: str
    scene: 'Scene'
    view_layer: 'ViewLayer'
    scene_eval: 'Scene'
    view_layer_eval: 'ViewLayer'
    ids: bpy_prop_collection['ID']
    objects: bpy_prop_collection['Object']
    object_instances: bpy_prop_collection['DepsgraphObjectInstance']
    updates: bpy_prop_collection['DepsgraphUpdate']
    def debug_relations_graphviz(self, *args, **kwargs) -> Any: ...
    def debug_stats_gnuplot(self, *args, **kwargs) -> Any: ...
    def debug_tag_update(self, *args, **kwargs) -> Any: ...
    def debug_stats(self, *args, **kwargs) -> Any: ...
    def update(self, *args, **kwargs) -> Any: ...
    def id_eval_get(self, *args, **kwargs) -> Any: ...
    def id_type_updated(self, *args, **kwargs) -> Any: ...