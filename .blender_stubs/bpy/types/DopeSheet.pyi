# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.DopeSheet.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .Collection import Collection
from .ID import ID

class DopeSheet(bpy_struct):

    @property
    def source(self) -> Annotated[Optional['ID'], "is_animatable=False"]:
        """ID-Block representing source data, usually ID_SCE (i.e. Scene)"""
        ...
    @property
    def show_datablock_filters(self) -> bool:
        """Show options for whether channels related to certain types of data are included"""
        ...
    @show_datablock_filters.setter
    def show_datablock_filters(self, value: bool) -> None:
        ...
    @property
    def show_only_selected(self) -> bool:
        """Only include channels relating to selected objects and data"""
        ...
    @show_only_selected.setter
    def show_only_selected(self, value: bool) -> None:
        ...
    @property
    def show_only_slot_of_active_object(self) -> bool:
        """Only show the slot of the active Object. Otherwise show all the Action's Slots"""
        ...
    @show_only_slot_of_active_object.setter
    def show_only_slot_of_active_object(self, value: bool) -> None:
        ...
    @property
    def show_hidden(self) -> bool:
        """Include channels from objects/bone that are not visible"""
        ...
    @show_hidden.setter
    def show_hidden(self, value: bool) -> None:
        ...
    @property
    def use_datablock_sort(self) -> bool:
        """Alphabetically sorts data-blocks - mainly objects in the scene (disable to increase viewport speed)"""
        ...
    @use_datablock_sort.setter
    def use_datablock_sort(self, value: bool) -> None:
        ...
    @property
    def use_filter_invert(self) -> bool:
        """Invert filter search"""
        ...
    @use_filter_invert.setter
    def use_filter_invert(self, value: bool) -> None:
        ...
    @property
    def show_only_errors(self) -> bool:
        """Only include F-Curves and drivers that are disabled or have errors"""
        ...
    @show_only_errors.setter
    def show_only_errors(self, value: bool) -> None:
        ...
    @property
    def filter_collection(self) -> Annotated[Optional['Collection'], "is_animatable=False"]:
        """Collection that included object should be a member of"""
        ...
    @filter_collection.setter
    def filter_collection(self, value: Annotated[Optional['Collection'], "is_animatable=False"]) -> None:
        ...
    @property
    def filter_fcurve_name(self) -> Annotated[str, "is_animatable=False"]:
        """F-Curve live filtering string"""
        ...
    @filter_fcurve_name.setter
    def filter_fcurve_name(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def filter_text(self) -> Annotated[str, "is_animatable=False"]:
        """Live filtering string"""
        ...
    @filter_text.setter
    def filter_text(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def use_multi_word_filter(self) -> bool:
        """Perform fuzzy/multi-word matching.
Warning: May be slow"""
        ...
    @use_multi_word_filter.setter
    def use_multi_word_filter(self, value: bool) -> None:
        ...
    @property
    def show_missing_nla(self) -> bool:
        """Include animation data-blocks with no NLA data (NLA editor only)"""
        ...
    @show_missing_nla.setter
    def show_missing_nla(self, value: bool) -> None:
        ...
    @property
    def show_summary(self) -> bool:
        """Display an additional 'summary' line (Dope Sheet editors only)"""
        ...
    @show_summary.setter
    def show_summary(self, value: bool) -> None:
        ...
    @property
    def show_expanded_summary(self) -> bool:
        """Collapse summary when shown, so all other channels get hidden (Dope Sheet editors only)"""
        ...
    @show_expanded_summary.setter
    def show_expanded_summary(self, value: bool) -> None:
        ...
    @property
    def show_transforms(self) -> bool:
        """Include visualization of object-level animation data (mostly transforms)"""
        ...
    @show_transforms.setter
    def show_transforms(self, value: bool) -> None:
        ...
    @property
    def show_shapekeys(self) -> bool:
        """Include visualization of shape key related animation data"""
        ...
    @show_shapekeys.setter
    def show_shapekeys(self, value: bool) -> None:
        ...
    @property
    def show_modifiers(self) -> bool:
        """Include visualization of animation data related to data-blocks linked to modifiers"""
        ...
    @show_modifiers.setter
    def show_modifiers(self, value: bool) -> None:
        ...
    @property
    def show_meshes(self) -> bool:
        """Include visualization of mesh related animation data"""
        ...
    @show_meshes.setter
    def show_meshes(self, value: bool) -> None:
        ...
    @property
    def show_lattices(self) -> bool:
        """Include visualization of lattice related animation data"""
        ...
    @show_lattices.setter
    def show_lattices(self, value: bool) -> None:
        ...
    @property
    def show_cameras(self) -> bool:
        """Include visualization of camera related animation data"""
        ...
    @show_cameras.setter
    def show_cameras(self, value: bool) -> None:
        ...
    @property
    def show_materials(self) -> bool:
        """Include visualization of material related animation data"""
        ...
    @show_materials.setter
    def show_materials(self, value: bool) -> None:
        ...
    @property
    def show_lights(self) -> bool:
        """Include visualization of light related animation data"""
        ...
    @show_lights.setter
    def show_lights(self, value: bool) -> None:
        ...
    @property
    def show_linestyles(self) -> bool:
        """Include visualization of Line Style related Animation data"""
        ...
    @show_linestyles.setter
    def show_linestyles(self, value: bool) -> None:
        ...
    @property
    def show_textures(self) -> bool:
        """Include visualization of texture related animation data"""
        ...
    @show_textures.setter
    def show_textures(self, value: bool) -> None:
        ...
    @property
    def show_curves(self) -> bool:
        """Include visualization of curve related animation data"""
        ...
    @show_curves.setter
    def show_curves(self, value: bool) -> None:
        ...
    @property
    def show_worlds(self) -> bool:
        """Include visualization of world related animation data"""
        ...
    @show_worlds.setter
    def show_worlds(self, value: bool) -> None:
        ...
    @property
    def show_scenes(self) -> bool:
        """Include visualization of scene related animation data"""
        ...
    @show_scenes.setter
    def show_scenes(self, value: bool) -> None:
        ...
    @property
    def show_particles(self) -> bool:
        """Include visualization of particle related animation data"""
        ...
    @show_particles.setter
    def show_particles(self, value: bool) -> None:
        ...
    @property
    def show_metaballs(self) -> bool:
        """Include visualization of metaball related animation data"""
        ...
    @show_metaballs.setter
    def show_metaballs(self, value: bool) -> None:
        ...
    @property
    def show_armatures(self) -> bool:
        """Include visualization of armature related animation data"""
        ...
    @show_armatures.setter
    def show_armatures(self, value: bool) -> None:
        ...
    @property
    def show_nodes(self) -> bool:
        """Include visualization of node related animation data"""
        ...
    @show_nodes.setter
    def show_nodes(self, value: bool) -> None:
        ...
    @property
    def show_speakers(self) -> bool:
        """Include visualization of speaker related animation data"""
        ...
    @show_speakers.setter
    def show_speakers(self, value: bool) -> None:
        ...
    @property
    def show_cache_files(self) -> bool:
        """Include visualization of cache file related animation data"""
        ...
    @show_cache_files.setter
    def show_cache_files(self, value: bool) -> None:
        ...
    @property
    def show_hair_curves(self) -> bool:
        """Include visualization of hair related animation data"""
        ...
    @show_hair_curves.setter
    def show_hair_curves(self, value: bool) -> None:
        ...
    @property
    def show_pointclouds(self) -> bool:
        """Include visualization of point cloud related animation data"""
        ...
    @show_pointclouds.setter
    def show_pointclouds(self, value: bool) -> None:
        ...
    @property
    def show_volumes(self) -> bool:
        """Include visualization of volume related animation data"""
        ...
    @show_volumes.setter
    def show_volumes(self, value: bool) -> None:
        ...
    @property
    def show_lightprobes(self) -> bool:
        """Include visualization of lightprobe related animation data"""
        ...
    @show_lightprobes.setter
    def show_lightprobes(self, value: bool) -> None:
        ...
    @property
    def show_gpencil(self) -> bool:
        """Include visualization of Grease Pencil related animation data and frames"""
        ...
    @show_gpencil.setter
    def show_gpencil(self, value: bool) -> None:
        ...
    @property
    def show_movieclips(self) -> bool:
        """Include visualization of movie clip related animation data"""
        ...
    @show_movieclips.setter
    def show_movieclips(self, value: bool) -> None:
        ...
    @property
    def show_driver_fallback_as_error(self) -> bool:
        """Include drivers that relied on any fallback values for their evaluation in the Only Show Errors filter, even if the driver evaluation succeeded"""
        ...
    @show_driver_fallback_as_error.setter
    def show_driver_fallback_as_error(self, value: bool) -> None:
        ...