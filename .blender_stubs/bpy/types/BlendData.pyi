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
    @property
    def filepath(self) -> Annotated[str, "subtype='FILE_PATH'", "is_animatable=False"]:
        """Path to the .blend file"""
        ...
    @property
    def is_dirty(self) -> bool:
        """Have recent edits been saved to disk"""
        ...
    @property
    def is_saved(self) -> bool:
        """Has the current session been saved to disk as a .blend file"""
        ...
    use_autopack: bool
    """Automatically pack all external data into .blend file"""
    @property
    def version(self) -> Annotated[list[int], "subtype='XYZ'", "step=1"]:
        """File format version the .blend file was saved with"""
        ...
    @property
    def cameras(self) -> Annotated['BlendDataCameras', "is_animatable=False"]:
        """Camera data-blocks"""
        ...
    @property
    def scenes(self) -> Annotated['BlendDataScenes', "is_animatable=False"]:
        """Scene data-blocks"""
        ...
    @property
    def objects(self) -> Annotated['BlendDataObjects', "is_animatable=False"]:
        """Object data-blocks"""
        ...
    @property
    def materials(self) -> Annotated['BlendDataMaterials', "is_animatable=False"]:
        """Material data-blocks"""
        ...
    @property
    def node_groups(self) -> Annotated['BlendDataNodeTrees', "is_animatable=False"]:
        """Node group data-blocks"""
        ...
    @property
    def meshes(self) -> Annotated['BlendDataMeshes', "is_animatable=False"]:
        """Mesh data-blocks"""
        ...
    @property
    def lights(self) -> Annotated['BlendDataLights', "is_animatable=False"]:
        """Light data-blocks"""
        ...
    @property
    def libraries(self) -> Annotated['BlendDataLibraries', "is_animatable=False"]:
        """Library data-blocks"""
        ...
    @property
    def screens(self) -> Annotated['BlendDataScreens', "is_animatable=False"]:
        """Screen data-blocks"""
        ...
    @property
    def window_managers(self) -> Annotated['BlendDataWindowManagers', "is_animatable=False"]:
        """Window manager data-blocks"""
        ...
    @property
    def images(self) -> Annotated['BlendDataImages', "is_animatable=False"]:
        """Image data-blocks"""
        ...
    @property
    def lattices(self) -> Annotated['BlendDataLattices', "is_animatable=False"]:
        """Lattice data-blocks"""
        ...
    @property
    def curves(self) -> Annotated['BlendDataCurves', "is_animatable=False"]:
        """Curve data-blocks"""
        ...
    @property
    def metaballs(self) -> Annotated['BlendDataMetaBalls', "is_animatable=False"]:
        """Metaball data-blocks"""
        ...
    @property
    def fonts(self) -> Annotated['BlendDataFonts', "is_animatable=False"]:
        """Vector font data-blocks"""
        ...
    @property
    def textures(self) -> Annotated['BlendDataTextures', "is_animatable=False"]:
        """Texture data-blocks"""
        ...
    @property
    def brushes(self) -> Annotated['BlendDataBrushes', "is_animatable=False"]:
        """Brush data-blocks"""
        ...
    @property
    def worlds(self) -> Annotated['BlendDataWorlds', "is_animatable=False"]:
        """World data-blocks"""
        ...
    @property
    def collections(self) -> Annotated['BlendDataCollections', "is_animatable=False"]:
        """Collection data-blocks"""
        ...
    @property
    def shape_keys(self) -> Annotated[bpy_prop_collection['Key'], "is_animatable=False"]:
        """Shape Key data-blocks"""
        ...
    @property
    def texts(self) -> Annotated['BlendDataTexts', "is_animatable=False"]:
        """Text data-blocks"""
        ...
    @property
    def speakers(self) -> Annotated['BlendDataSpeakers', "is_animatable=False"]:
        """Speaker data-blocks"""
        ...
    @property
    def sounds(self) -> Annotated['BlendDataSounds', "is_animatable=False"]:
        """Sound data-blocks"""
        ...
    @property
    def armatures(self) -> Annotated['BlendDataArmatures', "is_animatable=False"]:
        """Armature data-blocks"""
        ...
    @property
    def actions(self) -> Annotated['BlendDataActions', "is_animatable=False"]:
        """Action data-blocks"""
        ...
    @property
    def particles(self) -> Annotated['BlendDataParticles', "is_animatable=False"]:
        """Particle data-blocks"""
        ...
    @property
    def palettes(self) -> Annotated['BlendDataPalettes', "is_animatable=False"]:
        """Palette data-blocks"""
        ...
    @property
    def annotations(self) -> Annotated['BlendDataAnnotations', "is_animatable=False"]:
        """Annotation data-blocks (legacy Grease Pencil)"""
        ...
    @property
    def grease_pencils(self) -> Annotated['BlendDataGreasePencilsV3', "is_animatable=False"]:
        """Grease Pencil data-blocks"""
        ...
    @property
    def movieclips(self) -> Annotated['BlendDataMovieClips', "is_animatable=False"]:
        """Movie Clip data-blocks"""
        ...
    @property
    def masks(self) -> Annotated['BlendDataMasks', "is_animatable=False"]:
        """Masks data-blocks"""
        ...
    @property
    def linestyles(self) -> Annotated['BlendDataLineStyles', "is_animatable=False"]:
        """Line Style data-blocks"""
        ...
    @property
    def cache_files(self) -> Annotated['BlendDataCacheFiles', "is_animatable=False"]:
        """Cache Files data-blocks"""
        ...
    @property
    def paint_curves(self) -> Annotated['BlendDataPaintCurves', "is_animatable=False"]:
        """Paint Curves data-blocks"""
        ...
    @property
    def workspaces(self) -> Annotated['BlendDataWorkSpaces', "is_animatable=False"]:
        """Workspace data-blocks"""
        ...
    @property
    def lightprobes(self) -> Annotated['BlendDataProbes', "is_animatable=False"]:
        """Light Probe data-blocks"""
        ...
    @property
    def hair_curves(self) -> Annotated['BlendDataHairCurves', "is_animatable=False"]:
        """Hair curve data-blocks"""
        ...
    @property
    def pointclouds(self) -> Annotated['BlendDataPointClouds', "is_animatable=False"]:
        """Point cloud data-blocks"""
        ...
    @property
    def volumes(self) -> Annotated['BlendDataVolumes', "is_animatable=False"]:
        """Volume data-blocks"""
        ...
    @property
    def colorspace(self) -> Annotated['BlendFileColorspace', "is_animatable=False"]:
        """Information about the color space used for data-blocks in a blend file"""
        ...
    def pack_linked_ids_hierarchy(self, *args, **kwargs) -> Any: ...