# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.FileSelectIDFilter.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class FileSelectIDFilter(bpy_struct):

    @property
    def filter_action(self) -> bool:
        """Show Action data-blocks"""
        ...
    @filter_action.setter
    def filter_action(self, value: bool) -> None:
        ...
    @property
    def filter_armature(self) -> bool:
        """Show Armature data-blocks"""
        ...
    @filter_armature.setter
    def filter_armature(self, value: bool) -> None:
        ...
    @property
    def filter_brush(self) -> bool:
        """Show Brushes data-blocks"""
        ...
    @filter_brush.setter
    def filter_brush(self, value: bool) -> None:
        ...
    @property
    def filter_camera(self) -> bool:
        """Show Camera data-blocks"""
        ...
    @filter_camera.setter
    def filter_camera(self, value: bool) -> None:
        ...
    @property
    def filter_cachefile(self) -> bool:
        """Show Cache File data-blocks"""
        ...
    @filter_cachefile.setter
    def filter_cachefile(self, value: bool) -> None:
        ...
    @property
    def filter_curve(self) -> bool:
        """Show Curve data-blocks"""
        ...
    @filter_curve.setter
    def filter_curve(self, value: bool) -> None:
        ...
    @property
    def filter_annotations(self) -> bool:
        """Show Annotation data-blocks"""
        ...
    @filter_annotations.setter
    def filter_annotations(self, value: bool) -> None:
        ...
    @property
    def filter_grease_pencil(self) -> bool:
        """Show Grease Pencil data-blocks"""
        ...
    @filter_grease_pencil.setter
    def filter_grease_pencil(self, value: bool) -> None:
        ...
    @property
    def filter_group(self) -> bool:
        """Show Collection data-blocks"""
        ...
    @filter_group.setter
    def filter_group(self, value: bool) -> None:
        ...
    @property
    def filter_curves(self) -> bool:
        """Show/hide Curves data-blocks"""
        ...
    @filter_curves.setter
    def filter_curves(self, value: bool) -> None:
        ...
    @property
    def filter_image(self) -> bool:
        """Show Image data-blocks"""
        ...
    @filter_image.setter
    def filter_image(self, value: bool) -> None:
        ...
    @property
    def filter_light(self) -> bool:
        """Show Light data-blocks"""
        ...
    @filter_light.setter
    def filter_light(self, value: bool) -> None:
        ...
    @property
    def filter_light_probe(self) -> bool:
        """Show Light Probe data-blocks"""
        ...
    @filter_light_probe.setter
    def filter_light_probe(self, value: bool) -> None:
        ...
    @property
    def filter_linestyle(self) -> bool:
        """Show Freestyle's Line Style data-blocks"""
        ...
    @filter_linestyle.setter
    def filter_linestyle(self, value: bool) -> None:
        ...
    @property
    def filter_lattice(self) -> bool:
        """Show Lattice data-blocks"""
        ...
    @filter_lattice.setter
    def filter_lattice(self, value: bool) -> None:
        ...
    @property
    def filter_material(self) -> bool:
        """Show Material data-blocks"""
        ...
    @filter_material.setter
    def filter_material(self, value: bool) -> None:
        ...
    @property
    def filter_metaball(self) -> bool:
        """Show Metaball data-blocks"""
        ...
    @filter_metaball.setter
    def filter_metaball(self, value: bool) -> None:
        ...
    @property
    def filter_movie_clip(self) -> bool:
        """Show Movie Clip data-blocks"""
        ...
    @filter_movie_clip.setter
    def filter_movie_clip(self, value: bool) -> None:
        ...
    @property
    def filter_mesh(self) -> bool:
        """Show Mesh data-blocks"""
        ...
    @filter_mesh.setter
    def filter_mesh(self, value: bool) -> None:
        ...
    @property
    def filter_mask(self) -> bool:
        """Show Mask data-blocks"""
        ...
    @filter_mask.setter
    def filter_mask(self, value: bool) -> None:
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
    def filter_particle_settings(self) -> bool:
        """Show Particle Settings data-blocks"""
        ...
    @filter_particle_settings.setter
    def filter_particle_settings(self, value: bool) -> None:
        ...
    @property
    def filter_palette(self) -> bool:
        """Show Palette data-blocks"""
        ...
    @filter_palette.setter
    def filter_palette(self, value: bool) -> None:
        ...
    @property
    def filter_paint_curve(self) -> bool:
        """Show Paint Curve data-blocks"""
        ...
    @filter_paint_curve.setter
    def filter_paint_curve(self, value: bool) -> None:
        ...
    @property
    def filter_pointcloud(self) -> bool:
        """Show/hide Point Cloud data-blocks"""
        ...
    @filter_pointcloud.setter
    def filter_pointcloud(self, value: bool) -> None:
        ...
    @property
    def filter_scene(self) -> bool:
        """Show Scene data-blocks"""
        ...
    @filter_scene.setter
    def filter_scene(self, value: bool) -> None:
        ...
    @property
    def filter_speaker(self) -> bool:
        """Show Speaker data-blocks"""
        ...
    @filter_speaker.setter
    def filter_speaker(self, value: bool) -> None:
        ...
    @property
    def filter_sound(self) -> bool:
        """Show Sound data-blocks"""
        ...
    @filter_sound.setter
    def filter_sound(self, value: bool) -> None:
        ...
    @property
    def filter_texture(self) -> bool:
        """Show Texture data-blocks"""
        ...
    @filter_texture.setter
    def filter_texture(self, value: bool) -> None:
        ...
    @property
    def filter_text(self) -> bool:
        """Show Text data-blocks"""
        ...
    @filter_text.setter
    def filter_text(self, value: bool) -> None:
        ...
    @property
    def filter_font(self) -> bool:
        """Show Font data-blocks"""
        ...
    @filter_font.setter
    def filter_font(self, value: bool) -> None:
        ...
    @property
    def filter_volume(self) -> bool:
        """Show/hide Volume data-blocks"""
        ...
    @filter_volume.setter
    def filter_volume(self, value: bool) -> None:
        ...
    @property
    def filter_world(self) -> bool:
        """Show World data-blocks"""
        ...
    @filter_world.setter
    def filter_world(self, value: bool) -> None:
        ...
    @property
    def filter_work_space(self) -> bool:
        """Show workspace data-blocks"""
        ...
    @filter_work_space.setter
    def filter_work_space(self, value: bool) -> None:
        ...
    @property
    def category_scene(self) -> bool:
        """Show scenes"""
        ...
    @category_scene.setter
    def category_scene(self, value: bool) -> None:
        ...
    @property
    def category_animation(self) -> bool:
        """Show animation data"""
        ...
    @category_animation.setter
    def category_animation(self, value: bool) -> None:
        ...
    @property
    def category_object(self) -> bool:
        """Show objects and collections"""
        ...
    @category_object.setter
    def category_object(self, value: bool) -> None:
        ...
    @property
    def category_geometry(self) -> bool:
        """Show meshes, curves, lattice, armatures and metaballs data"""
        ...
    @category_geometry.setter
    def category_geometry(self, value: bool) -> None:
        ...
    @property
    def category_shading(self) -> bool:
        """Show materials, node-trees, textures and Freestyle's line-styles"""
        ...
    @category_shading.setter
    def category_shading(self, value: bool) -> None:
        ...
    @property
    def category_image(self) -> bool:
        """Show images, movie clips, sounds and masks"""
        ...
    @category_image.setter
    def category_image(self, value: bool) -> None:
        ...
    @property
    def category_environment(self) -> bool:
        """Show worlds, lights, cameras and speakers"""
        ...
    @category_environment.setter
    def category_environment(self, value: bool) -> None:
        ...
    @property
    def category_misc(self) -> bool:
        """Show other data types"""
        ...
    @category_misc.setter
    def category_misc(self, value: bool) -> None:
        ...