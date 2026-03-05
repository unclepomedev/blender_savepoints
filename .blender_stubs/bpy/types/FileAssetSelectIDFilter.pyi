# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.FileAssetSelectIDFilter.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class FileAssetSelectIDFilter(bpy_struct):

    @property
    def filter_action(self) -> bool:
        """Show Action data-blocks"""
        ...
    @filter_action.setter
    def filter_action(self, value: bool) -> None:
        ...
    @property
    def experimental_filter_armature(self) -> bool:
        """Show Armature data-blocks"""
        ...
    @experimental_filter_armature.setter
    def experimental_filter_armature(self, value: bool) -> None:
        ...
    @property
    def filter_brush(self) -> bool:
        """Show Brushes data-blocks"""
        ...
    @filter_brush.setter
    def filter_brush(self, value: bool) -> None:
        ...
    @property
    def experimental_filter_camera(self) -> bool:
        """Show Camera data-blocks"""
        ...
    @experimental_filter_camera.setter
    def experimental_filter_camera(self, value: bool) -> None:
        ...
    @property
    def experimental_filter_cachefile(self) -> bool:
        """Show Cache File data-blocks"""
        ...
    @experimental_filter_cachefile.setter
    def experimental_filter_cachefile(self, value: bool) -> None:
        ...
    @property
    def experimental_filter_curve(self) -> bool:
        """Show Curve data-blocks"""
        ...
    @experimental_filter_curve.setter
    def experimental_filter_curve(self, value: bool) -> None:
        ...
    @property
    def experimental_filter_annotations(self) -> bool:
        """Show Annotation data-blocks"""
        ...
    @experimental_filter_annotations.setter
    def experimental_filter_annotations(self, value: bool) -> None:
        ...
    @property
    def experimental_filter_grease_pencil(self) -> bool:
        """Show Grease Pencil data-blocks"""
        ...
    @experimental_filter_grease_pencil.setter
    def experimental_filter_grease_pencil(self, value: bool) -> None:
        ...
    @property
    def filter_group(self) -> bool:
        """Show Collection data-blocks"""
        ...
    @filter_group.setter
    def filter_group(self, value: bool) -> None:
        ...
    @property
    def experimental_filter_curves(self) -> bool:
        """Show/hide Curves data-blocks"""
        ...
    @experimental_filter_curves.setter
    def experimental_filter_curves(self, value: bool) -> None:
        ...
    @property
    def experimental_filter_image(self) -> bool:
        """Show Image data-blocks"""
        ...
    @experimental_filter_image.setter
    def experimental_filter_image(self, value: bool) -> None:
        ...
    @property
    def experimental_filter_light(self) -> bool:
        """Show Light data-blocks"""
        ...
    @experimental_filter_light.setter
    def experimental_filter_light(self, value: bool) -> None:
        ...
    @property
    def experimental_filter_light_probe(self) -> bool:
        """Show Light Probe data-blocks"""
        ...
    @experimental_filter_light_probe.setter
    def experimental_filter_light_probe(self, value: bool) -> None:
        ...
    @property
    def experimental_filter_linestyle(self) -> bool:
        """Show Freestyle's Line Style data-blocks"""
        ...
    @experimental_filter_linestyle.setter
    def experimental_filter_linestyle(self, value: bool) -> None:
        ...
    @property
    def experimental_filter_lattice(self) -> bool:
        """Show Lattice data-blocks"""
        ...
    @experimental_filter_lattice.setter
    def experimental_filter_lattice(self, value: bool) -> None:
        ...
    @property
    def filter_material(self) -> bool:
        """Show Material data-blocks"""
        ...
    @filter_material.setter
    def filter_material(self, value: bool) -> None:
        ...
    @property
    def experimental_filter_metaball(self) -> bool:
        """Show Metaball data-blocks"""
        ...
    @experimental_filter_metaball.setter
    def experimental_filter_metaball(self, value: bool) -> None:
        ...
    @property
    def experimental_filter_movie_clip(self) -> bool:
        """Show Movie Clip data-blocks"""
        ...
    @experimental_filter_movie_clip.setter
    def experimental_filter_movie_clip(self, value: bool) -> None:
        ...
    @property
    def experimental_filter_mesh(self) -> bool:
        """Show Mesh data-blocks"""
        ...
    @experimental_filter_mesh.setter
    def experimental_filter_mesh(self, value: bool) -> None:
        ...
    @property
    def experimental_filter_mask(self) -> bool:
        """Show Mask data-blocks"""
        ...
    @experimental_filter_mask.setter
    def experimental_filter_mask(self, value: bool) -> None:
        ...
    @property
    def filter_node_tree(self) -> bool:
        """Show Node Tree data-blocks"""
        ...
    @filter_node_tree.setter
    def filter_node_tree(self, value: bool) -> None:
        ...
    @property
    def filter_object(self) -> bool:
        """Show Object data-blocks"""
        ...
    @filter_object.setter
    def filter_object(self, value: bool) -> None:
        ...
    @property
    def experimental_filter_particle_settings(self) -> bool:
        """Show Particle Settings data-blocks"""
        ...
    @experimental_filter_particle_settings.setter
    def experimental_filter_particle_settings(self, value: bool) -> None:
        ...
    @property
    def experimental_filter_palette(self) -> bool:
        """Show Palette data-blocks"""
        ...
    @experimental_filter_palette.setter
    def experimental_filter_palette(self, value: bool) -> None:
        ...
    @property
    def experimental_filter_paint_curve(self) -> bool:
        """Show Paint Curve data-blocks"""
        ...
    @experimental_filter_paint_curve.setter
    def experimental_filter_paint_curve(self, value: bool) -> None:
        ...
    @property
    def experimental_filter_pointcloud(self) -> bool:
        """Show/hide Point Cloud data-blocks"""
        ...
    @experimental_filter_pointcloud.setter
    def experimental_filter_pointcloud(self, value: bool) -> None:
        ...
    @property
    def filter_scene(self) -> bool:
        """Show Scene data-blocks"""
        ...
    @filter_scene.setter
    def filter_scene(self, value: bool) -> None:
        ...
    @property
    def experimental_filter_speaker(self) -> bool:
        """Show Speaker data-blocks"""
        ...
    @experimental_filter_speaker.setter
    def experimental_filter_speaker(self, value: bool) -> None:
        ...
    @property
    def experimental_filter_sound(self) -> bool:
        """Show Sound data-blocks"""
        ...
    @experimental_filter_sound.setter
    def experimental_filter_sound(self, value: bool) -> None:
        ...
    @property
    def experimental_filter_texture(self) -> bool:
        """Show Texture data-blocks"""
        ...
    @experimental_filter_texture.setter
    def experimental_filter_texture(self, value: bool) -> None:
        ...
    @property
    def experimental_filter_text(self) -> bool:
        """Show Text data-blocks"""
        ...
    @experimental_filter_text.setter
    def experimental_filter_text(self, value: bool) -> None:
        ...
    @property
    def experimental_filter_font(self) -> bool:
        """Show Font data-blocks"""
        ...
    @experimental_filter_font.setter
    def experimental_filter_font(self, value: bool) -> None:
        ...
    @property
    def experimental_filter_volume(self) -> bool:
        """Show/hide Volume data-blocks"""
        ...
    @experimental_filter_volume.setter
    def experimental_filter_volume(self, value: bool) -> None:
        ...
    @property
    def filter_world(self) -> bool:
        """Show World data-blocks"""
        ...
    @filter_world.setter
    def filter_world(self, value: bool) -> None:
        ...
    @property
    def experimental_filter_work_space(self) -> bool:
        """Show workspace data-blocks"""
        ...
    @experimental_filter_work_space.setter
    def experimental_filter_work_space(self, value: bool) -> None:
        ...