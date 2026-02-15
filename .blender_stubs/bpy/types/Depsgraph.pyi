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
from .DepsgraphObjectInstance import DepsgraphObjectInstance
from .DepsgraphUpdate import DepsgraphUpdate
from .ID import ID
from .Object import Object
from .Scene import Scene
from .ViewLayer import ViewLayer
class Depsgraph(bpy_struct):
    @property
    def mode(self) -> Literal['VIEWPORT', 'RENDER']:
        """Evaluation mode"""
        ...
    @property
    def scene(self) -> Annotated[Optional['Scene'], "is_animatable=False"]:
        """Original scene dependency graph is built for"""
        ...
    @property
    def view_layer(self) -> Annotated[Optional['ViewLayer'], "is_animatable=False"]:
        """Original view layer dependency graph is built for"""
        ...
    @property
    def scene_eval(self) -> Annotated[Optional['Scene'], "is_animatable=False"]:
        """Scene at its evaluated state"""
        ...
    @property
    def view_layer_eval(self) -> Annotated[Optional['ViewLayer'], "is_animatable=False"]:
        """View layer at its evaluated state"""
        ...
    @property
    def ids(self) -> Annotated[bpy_prop_collection['ID'], "is_animatable=False"]:
        """All evaluated data-blocks"""
        ...
    @property
    def objects(self) -> Annotated[bpy_prop_collection['Object'], "is_animatable=False"]:
        """Evaluated objects in the dependency graph"""
        ...
    @property
    def object_instances(self) -> Annotated[bpy_prop_collection['DepsgraphObjectInstance'], "is_animatable=False"]:
        """All object instances to display or render (Warning: Only use this as an iterator, never as a sequence, and do not keep any references to its items)"""
        ...
    @property
    def updates(self) -> Annotated[bpy_prop_collection['DepsgraphUpdate'], "is_animatable=False"]:
        """Updates to data-blocks"""
        ...
    def debug_relations_graphviz(self, *args, **kwargs) -> Any: ...
    def debug_stats_gnuplot(self, *args, **kwargs) -> Any: ...
    def debug_tag_update(self, *args, **kwargs) -> Any: ...
    def debug_stats(self, *args, **kwargs) -> Any: ...
    def update(self, *args, **kwargs) -> Any: ...
    def id_eval_get(self, *args, **kwargs) -> Any: ...
    def id_type_updated(self, *args, **kwargs) -> Any: ...