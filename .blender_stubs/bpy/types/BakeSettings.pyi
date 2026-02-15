# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.BakeSettings.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .ImageFormatSettings import ImageFormatSettings
from .Object import Object

class BakeSettings(bpy_struct):

    type: Annotated[Literal['NORMALS', 'DISPLACEMENT', 'VECTOR_DISPLACEMENT'], "is_animatable=False"]
    """Choose shading information to bake into the image"""
    cage_object: Annotated[Optional['Object'], "is_animatable=False"]
    """Object to use as cage instead of calculating the cage from the active object with cage extrusion"""
    filepath: Annotated[str, "subtype='FILE_PATH'", "is_animatable=False"]
    """Image filepath to use when saving externally"""
    width: Annotated[int, "subtype='PIXEL'", "step=1", "is_animatable=False"]
    """Horizontal dimension of the baking map"""
    height: Annotated[int, "subtype='PIXEL'", "step=1", "is_animatable=False"]
    """Vertical dimension of the baking map"""
    margin: Annotated[int, "subtype='PIXEL'", "step=1", "is_animatable=False"]
    """Extends the baked result as a post process filter"""
    margin_type: Annotated[Literal['ADJACENT_FACES', 'EXTEND'], "is_animatable=False"]
    """Algorithm to extend the baked result"""
    max_ray_distance: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=1.0", "precision=3", "is_animatable=False"]
    """The maximum ray distance for matching points between the active and selected objects. If zero, there is no limit."""
    cage_extrusion: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=1.0", "precision=3", "is_animatable=False"]
    """Inflate the active object by the specified distance for baking. This helps matching to points nearer to the outside of the selected object meshes."""
    normal_space: Annotated[Literal['OBJECT', 'TANGENT'], "is_animatable=False"]
    """Choose normal space for baking"""
    normal_r: Annotated[Literal['POS_X', 'POS_Y', 'POS_Z', 'NEG_X', 'NEG_Y', 'NEG_Z'], "is_animatable=False"]
    """Axis to bake in red channel"""
    normal_g: Annotated[Literal['POS_X', 'POS_Y', 'POS_Z', 'NEG_X', 'NEG_Y', 'NEG_Z'], "is_animatable=False"]
    """Axis to bake in green channel"""
    normal_b: Annotated[Literal['POS_X', 'POS_Y', 'POS_Z', 'NEG_X', 'NEG_Y', 'NEG_Z'], "is_animatable=False"]
    """Axis to bake in blue channel"""
    @property
    def image_settings(self) -> Annotated['ImageFormatSettings', "is_animatable=False"]:

        ...
    target: Annotated[Literal['IMAGE_TEXTURES', 'VERTEX_COLORS'], "is_animatable=False"]
    """Where to output the baked map"""
    save_mode: Annotated[Literal['INTERNAL', 'EXTERNAL'], "is_animatable=False"]
    """Where to save baked image textures"""
    view_from: Annotated[Literal['ABOVE_SURFACE', 'ACTIVE_CAMERA'], "is_animatable=False"]
    """Source of reflection ray directions"""
    use_selected_to_active: Annotated[bool, "is_animatable=False"]
    """Bake shading on the surface of selected objects to the active object"""
    use_clear: Annotated[bool, "is_animatable=False"]
    """Clear Images before baking (internal only)"""
    use_split_materials: Annotated[bool, "is_animatable=False"]
    """Split external images per material (external only)"""
    use_automatic_name: Annotated[bool, "is_animatable=False"]
    """Automatically name the output file with the pass type (external only)"""
    use_cage: Annotated[bool, "is_animatable=False"]
    """Cast rays to active object from a cage"""
    use_pass_emit: Annotated[bool, "is_animatable=False"]
    """Add emission contribution"""
    use_pass_direct: Annotated[bool, "is_animatable=False"]
    """Add direct lighting contribution"""
    use_pass_indirect: Annotated[bool, "is_animatable=False"]
    """Add indirect lighting contribution"""
    use_pass_color: Annotated[bool, "is_animatable=False"]
    """Color the pass"""
    use_pass_diffuse: Annotated[bool, "is_animatable=False"]
    """Add diffuse contribution"""
    use_pass_glossy: Annotated[bool, "is_animatable=False"]
    """Add glossy contribution"""
    use_pass_transmission: Annotated[bool, "is_animatable=False"]
    """Add transmission contribution"""
    @property
    def pass_filter(self) -> Annotated[set[str], "is_animatable=False"]:
        """Passes to include in the active baking pass"""
        ...
    use_multires: Annotated[bool, "is_animatable=False"]
    """Bake directly from multires object"""
    use_lores_mesh: Annotated[bool, "is_animatable=False"]
    """Calculate heights against unsubdivided low resolution mesh"""
    displacement_space: Annotated[Literal['OBJECT', 'TANGENT'], "is_animatable=False"]
    """Choose displacement space for baking"""