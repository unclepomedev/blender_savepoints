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
from .Collection import Collection
from .ID import ID
class DopeSheet(bpy_struct):
    source: 'ID'
    show_datablock_filters: bool
    show_only_selected: bool
    show_only_slot_of_active_object: bool
    show_hidden: bool
    use_datablock_sort: bool
    use_filter_invert: bool
    show_only_errors: bool
    filter_collection: 'Collection'
    filter_fcurve_name: str
    filter_text: str
    use_multi_word_filter: bool
    show_missing_nla: bool
    show_summary: bool
    show_expanded_summary: bool
    show_transforms: bool
    show_shapekeys: bool
    show_modifiers: bool
    show_meshes: bool
    show_lattices: bool
    show_cameras: bool
    show_materials: bool
    show_lights: bool
    show_linestyles: bool
    show_textures: bool
    show_curves: bool
    show_worlds: bool
    show_scenes: bool
    show_particles: bool
    show_metaballs: bool
    show_armatures: bool
    show_nodes: bool
    show_speakers: bool
    show_cache_files: bool
    show_hair_curves: bool
    show_pointclouds: bool
    show_volumes: bool
    show_lightprobes: bool
    show_gpencil: bool
    show_movieclips: bool
    show_driver_fallback_as_error: bool