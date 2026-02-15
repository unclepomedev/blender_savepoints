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
from .Collection import Collection
from .ID import ID
class DopeSheet(bpy_struct):
    @property
    def source(self) -> Annotated[Optional['ID'], "is_animatable=False"]:
        """ID-Block representing source data, usually ID_SCE (i.e. Scene)"""
        ...
    show_datablock_filters: bool
    """Show options for whether channels related to certain types of data are included"""
    show_only_selected: bool
    """Only include channels relating to selected objects and data"""
    show_only_slot_of_active_object: bool
    """Only show the slot of the active Object. Otherwise show all the Action's Slots"""
    show_hidden: bool
    """Include channels from objects/bone that are not visible"""
    use_datablock_sort: bool
    """Alphabetically sorts data-blocks - mainly objects in the scene (disable to increase viewport speed)"""
    use_filter_invert: bool
    """Invert filter search"""
    show_only_errors: bool
    """Only include F-Curves and drivers that are disabled or have errors"""
    filter_collection: Annotated[Optional['Collection'], "is_animatable=False"]
    """Collection that included object should be a member of"""
    filter_fcurve_name: Annotated[str, "is_animatable=False"]
    """F-Curve live filtering string"""
    filter_text: Annotated[str, "is_animatable=False"]
    """Live filtering string"""
    use_multi_word_filter: bool
    """Perform fuzzy/multi-word matching.
Warning: May be slow"""
    show_missing_nla: bool
    """Include animation data-blocks with no NLA data (NLA editor only)"""
    show_summary: bool
    """Display an additional 'summary' line (Dope Sheet editors only)"""
    show_expanded_summary: bool
    """Collapse summary when shown, so all other channels get hidden (Dope Sheet editors only)"""
    show_transforms: bool
    """Include visualization of object-level animation data (mostly transforms)"""
    show_shapekeys: bool
    """Include visualization of shape key related animation data"""
    show_modifiers: bool
    """Include visualization of animation data related to data-blocks linked to modifiers"""
    show_meshes: bool
    """Include visualization of mesh related animation data"""
    show_lattices: bool
    """Include visualization of lattice related animation data"""
    show_cameras: bool
    """Include visualization of camera related animation data"""
    show_materials: bool
    """Include visualization of material related animation data"""
    show_lights: bool
    """Include visualization of light related animation data"""
    show_linestyles: bool
    """Include visualization of Line Style related Animation data"""
    show_textures: bool
    """Include visualization of texture related animation data"""
    show_curves: bool
    """Include visualization of curve related animation data"""
    show_worlds: bool
    """Include visualization of world related animation data"""
    show_scenes: bool
    """Include visualization of scene related animation data"""
    show_particles: bool
    """Include visualization of particle related animation data"""
    show_metaballs: bool
    """Include visualization of metaball related animation data"""
    show_armatures: bool
    """Include visualization of armature related animation data"""
    show_nodes: bool
    """Include visualization of node related animation data"""
    show_speakers: bool
    """Include visualization of speaker related animation data"""
    show_cache_files: bool
    """Include visualization of cache file related animation data"""
    show_hair_curves: bool
    """Include visualization of hair related animation data"""
    show_pointclouds: bool
    """Include visualization of point cloud related animation data"""
    show_volumes: bool
    """Include visualization of volume related animation data"""
    show_lightprobes: bool
    """Include visualization of lightprobe related animation data"""
    show_gpencil: bool
    """Include visualization of Grease Pencil related animation data and frames"""
    show_movieclips: bool
    """Include visualization of movie clip related animation data"""
    show_driver_fallback_as_error: bool
    """Include drivers that relied on any fallback values for their evaluation in the Only Show Errors filter, even if the driver evaluation succeeded"""