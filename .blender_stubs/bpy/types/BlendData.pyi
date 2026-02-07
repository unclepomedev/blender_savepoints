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
from .BlendDataActions import BlendDataActions
from .BlendDataAnnotations import BlendDataAnnotations
from .BlendDataArmatures import BlendDataArmatures
from .BlendDataBrushes import BlendDataBrushes
from .BlendDataCacheFiles import BlendDataCacheFiles
from .BlendDataCameras import BlendDataCameras
from .BlendDataCollections import BlendDataCollections
from .BlendDataCurves import BlendDataCurves
from .BlendDataFonts import BlendDataFonts
from .BlendDataGreasePencilsV3 import BlendDataGreasePencilsV3
from .BlendDataHairCurves import BlendDataHairCurves
from .BlendDataImages import BlendDataImages
from .BlendDataLattices import BlendDataLattices
from .BlendDataLibraries import BlendDataLibraries
from .BlendDataLights import BlendDataLights
from .BlendDataLineStyles import BlendDataLineStyles
from .BlendDataMasks import BlendDataMasks
from .BlendDataMaterials import BlendDataMaterials
from .BlendDataMeshes import BlendDataMeshes
from .BlendDataMetaBalls import BlendDataMetaBalls
from .BlendDataMovieClips import BlendDataMovieClips
from .BlendDataNodeTrees import BlendDataNodeTrees
from .BlendDataObjects import BlendDataObjects
from .BlendDataPaintCurves import BlendDataPaintCurves
from .BlendDataPalettes import BlendDataPalettes
from .BlendDataParticles import BlendDataParticles
from .BlendDataPointClouds import BlendDataPointClouds
from .BlendDataProbes import BlendDataProbes
from .BlendDataScenes import BlendDataScenes
from .BlendDataScreens import BlendDataScreens
from .BlendDataSounds import BlendDataSounds
from .BlendDataSpeakers import BlendDataSpeakers
from .BlendDataTexts import BlendDataTexts
from .BlendDataTextures import BlendDataTextures
from .BlendDataVolumes import BlendDataVolumes
from .BlendDataWindowManagers import BlendDataWindowManagers
from .BlendDataWorkSpaces import BlendDataWorkSpaces
from .BlendDataWorlds import BlendDataWorlds
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
    version: list[int]
    cameras: 'BlendDataCameras'
    scenes: 'BlendDataScenes'
    objects: 'BlendDataObjects'
    materials: 'BlendDataMaterials'
    node_groups: 'BlendDataNodeTrees'
    meshes: 'BlendDataMeshes'
    lights: 'BlendDataLights'
    libraries: 'BlendDataLibraries'
    screens: 'BlendDataScreens'
    window_managers: 'BlendDataWindowManagers'
    images: 'BlendDataImages'
    lattices: 'BlendDataLattices'
    curves: 'BlendDataCurves'
    metaballs: 'BlendDataMetaBalls'
    fonts: 'BlendDataFonts'
    textures: 'BlendDataTextures'
    brushes: 'BlendDataBrushes'
    worlds: 'BlendDataWorlds'
    collections: 'BlendDataCollections'
    shape_keys: bpy_prop_collection['Key']
    texts: 'BlendDataTexts'
    speakers: 'BlendDataSpeakers'
    sounds: 'BlendDataSounds'
    armatures: 'BlendDataArmatures'
    actions: 'BlendDataActions'
    particles: 'BlendDataParticles'
    palettes: 'BlendDataPalettes'
    annotations: 'BlendDataAnnotations'
    grease_pencils: 'BlendDataGreasePencilsV3'
    movieclips: 'BlendDataMovieClips'
    masks: 'BlendDataMasks'
    linestyles: 'BlendDataLineStyles'
    cache_files: 'BlendDataCacheFiles'
    paint_curves: 'BlendDataPaintCurves'
    workspaces: 'BlendDataWorkSpaces'
    lightprobes: 'BlendDataProbes'
    hair_curves: 'BlendDataHairCurves'
    pointclouds: 'BlendDataPointClouds'
    volumes: 'BlendDataVolumes'
    colorspace: 'BlendFileColorspace'
    def pack_linked_ids_hierarchy(self, *args, **kwargs) -> Any: ...