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

    filter_action: bool
    """Show Action data-blocks"""
    experimental_filter_armature: bool
    """Show Armature data-blocks"""
    filter_brush: bool
    """Show Brushes data-blocks"""
    experimental_filter_camera: bool
    """Show Camera data-blocks"""
    experimental_filter_cachefile: bool
    """Show Cache File data-blocks"""
    experimental_filter_curve: bool
    """Show Curve data-blocks"""
    experimental_filter_annotations: bool
    """Show Annotation data-blocks"""
    experimental_filter_grease_pencil: bool
    """Show Grease Pencil data-blocks"""
    filter_group: bool
    """Show Collection data-blocks"""
    experimental_filter_curves: bool
    """Show/hide Curves data-blocks"""
    experimental_filter_image: bool
    """Show Image data-blocks"""
    experimental_filter_light: bool
    """Show Light data-blocks"""
    experimental_filter_light_probe: bool
    """Show Light Probe data-blocks"""
    experimental_filter_linestyle: bool
    """Show Freestyle's Line Style data-blocks"""
    experimental_filter_lattice: bool
    """Show Lattice data-blocks"""
    filter_material: bool
    """Show Material data-blocks"""
    experimental_filter_metaball: bool
    """Show Metaball data-blocks"""
    experimental_filter_movie_clip: bool
    """Show Movie Clip data-blocks"""
    experimental_filter_mesh: bool
    """Show Mesh data-blocks"""
    experimental_filter_mask: bool
    """Show Mask data-blocks"""
    filter_node_tree: bool
    """Show Node Tree data-blocks"""
    filter_object: bool
    """Show Object data-blocks"""
    experimental_filter_particle_settings: bool
    """Show Particle Settings data-blocks"""
    experimental_filter_palette: bool
    """Show Palette data-blocks"""
    experimental_filter_paint_curve: bool
    """Show Paint Curve data-blocks"""
    experimental_filter_pointcloud: bool
    """Show/hide Point Cloud data-blocks"""
    filter_scene: bool
    """Show Scene data-blocks"""
    experimental_filter_speaker: bool
    """Show Speaker data-blocks"""
    experimental_filter_sound: bool
    """Show Sound data-blocks"""
    experimental_filter_texture: bool
    """Show Texture data-blocks"""
    experimental_filter_text: bool
    """Show Text data-blocks"""
    experimental_filter_font: bool
    """Show Font data-blocks"""
    experimental_filter_volume: bool
    """Show/hide Volume data-blocks"""
    filter_world: bool
    """Show World data-blocks"""
    experimental_filter_work_space: bool
    """Show workspace data-blocks"""