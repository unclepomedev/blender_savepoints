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
class FileSelectIDFilter(bpy_struct):
    filter_action: bool
    """Show Action data-blocks"""
    filter_armature: bool
    """Show Armature data-blocks"""
    filter_brush: bool
    """Show Brushes data-blocks"""
    filter_camera: bool
    """Show Camera data-blocks"""
    filter_cachefile: bool
    """Show Cache File data-blocks"""
    filter_curve: bool
    """Show Curve data-blocks"""
    filter_annotations: bool
    """Show Annotation data-blocks"""
    filter_grease_pencil: bool
    """Show Grease Pencil data-blocks"""
    filter_group: bool
    """Show Collection data-blocks"""
    filter_curves: bool
    """Show/hide Curves data-blocks"""
    filter_image: bool
    """Show Image data-blocks"""
    filter_light: bool
    """Show Light data-blocks"""
    filter_light_probe: bool
    """Show Light Probe data-blocks"""
    filter_linestyle: bool
    """Show Freestyle's Line Style data-blocks"""
    filter_lattice: bool
    """Show Lattice data-blocks"""
    filter_material: bool
    """Show Material data-blocks"""
    filter_metaball: bool
    """Show Metaball data-blocks"""
    filter_movie_clip: bool
    """Show Movie Clip data-blocks"""
    filter_mesh: bool
    """Show Mesh data-blocks"""
    filter_mask: bool
    """Show Mask data-blocks"""
    filter_node_tree: bool
    """Show Node Tree data-blocks"""
    filter_object: bool
    """Show Object data-blocks"""
    filter_particle_settings: bool
    """Show Particle Settings data-blocks"""
    filter_palette: bool
    """Show Palette data-blocks"""
    filter_paint_curve: bool
    """Show Paint Curve data-blocks"""
    filter_pointcloud: bool
    """Show/hide Point Cloud data-blocks"""
    filter_scene: bool
    """Show Scene data-blocks"""
    filter_speaker: bool
    """Show Speaker data-blocks"""
    filter_sound: bool
    """Show Sound data-blocks"""
    filter_texture: bool
    """Show Texture data-blocks"""
    filter_text: bool
    """Show Text data-blocks"""
    filter_font: bool
    """Show Font data-blocks"""
    filter_volume: bool
    """Show/hide Volume data-blocks"""
    filter_world: bool
    """Show World data-blocks"""
    filter_work_space: bool
    """Show workspace data-blocks"""
    category_scene: bool
    """Show scenes"""
    category_animation: bool
    """Show animation data"""
    category_object: bool
    """Show objects and collections"""
    category_geometry: bool
    """Show meshes, curves, lattice, armatures and metaballs data"""
    category_shading: bool
    """Show materials, node-trees, textures and Freestyle's line-styles"""
    category_image: bool
    """Show images, movie clips, sounds and masks"""
    category_environment: bool
    """Show worlds, lights, cameras and speakers"""
    category_misc: bool
    """Show other data types"""