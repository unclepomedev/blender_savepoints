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
from .Action import Action
from .Annotation import Annotation
from .Armature import Armature
from .BlendFileColorspace import BlendFileColorspace
from .Brush import Brush
from .CacheFile import CacheFile
from .Camera import Camera
from .Collection import Collection
from .Curve import Curve
from .Curves import Curves
from .FreestyleLineStyle import FreestyleLineStyle
from .GreasePencil import GreasePencil
from .Image import Image
from .Key import Key
from .Lattice import Lattice
from .Library import Library
from .Light import Light
from .LightProbe import LightProbe
from .Mask import Mask
from .Material import Material
from .Mesh import Mesh
from .MetaBall import MetaBall
from .MovieClip import MovieClip
from .NodeTree import NodeTree
from .Object import Object
from .PaintCurve import PaintCurve
from .Palette import Palette
from .ParticleSettings import ParticleSettings
from .PointCloud import PointCloud
from .Scene import Scene
from .Screen import Screen
from .Sound import Sound
from .Speaker import Speaker
from .Text import Text
from .Texture import Texture
from .VectorFont import VectorFont
from .Volume import Volume
from .WindowManager import WindowManager
from .WorkSpace import WorkSpace
from .World import World
class BlendData(bpy_struct):
    filepath: str
    is_dirty: bool
    is_saved: bool
    use_autopack: bool
    version: int
    cameras: bpy_prop_collection['Camera']
    scenes: bpy_prop_collection['Scene']
    objects: bpy_prop_collection['Object']
    materials: bpy_prop_collection['Material']
    node_groups: bpy_prop_collection['NodeTree']
    meshes: bpy_prop_collection['Mesh']
    lights: bpy_prop_collection['Light']
    libraries: bpy_prop_collection['Library']
    screens: bpy_prop_collection['Screen']
    window_managers: bpy_prop_collection['WindowManager']
    images: bpy_prop_collection['Image']
    lattices: bpy_prop_collection['Lattice']
    curves: bpy_prop_collection['Curve']
    metaballs: bpy_prop_collection['MetaBall']
    fonts: bpy_prop_collection['VectorFont']
    textures: bpy_prop_collection['Texture']
    brushes: bpy_prop_collection['Brush']
    worlds: bpy_prop_collection['World']
    collections: bpy_prop_collection['Collection']
    shape_keys: bpy_prop_collection['Key']
    texts: bpy_prop_collection['Text']
    speakers: bpy_prop_collection['Speaker']
    sounds: bpy_prop_collection['Sound']
    armatures: bpy_prop_collection['Armature']
    actions: bpy_prop_collection['Action']
    particles: bpy_prop_collection['ParticleSettings']
    palettes: bpy_prop_collection['Palette']
    annotations: bpy_prop_collection['Annotation']
    grease_pencils: bpy_prop_collection['GreasePencil']
    movieclips: bpy_prop_collection['MovieClip']
    masks: bpy_prop_collection['Mask']
    linestyles: bpy_prop_collection['FreestyleLineStyle']
    cache_files: bpy_prop_collection['CacheFile']
    paint_curves: bpy_prop_collection['PaintCurve']
    workspaces: bpy_prop_collection['WorkSpace']
    lightprobes: bpy_prop_collection['LightProbe']
    hair_curves: bpy_prop_collection['Curves']
    pointclouds: bpy_prop_collection['PointCloud']
    volumes: bpy_prop_collection['Volume']
    colorspace: 'BlendFileColorspace'
    def pack_linked_ids_hierarchy(self, *args, **kwargs) -> Any: ...