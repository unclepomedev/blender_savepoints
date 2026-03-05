# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.Brush.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .ID import ID
from .AssetMetaData import AssetMetaData
from .BrushCapabilities import BrushCapabilities
from .BrushCapabilitiesImagePaint import BrushCapabilitiesImagePaint
from .BrushCapabilitiesSculpt import BrushCapabilitiesSculpt
from .BrushCapabilitiesVertexPaint import BrushCapabilitiesVertexPaint
from .BrushCapabilitiesWeightPaint import BrushCapabilitiesWeightPaint
from .BrushCurvesSculptSettings import BrushCurvesSculptSettings
from .BrushGpencilSettings import BrushGpencilSettings
from .BrushTextureSlot import BrushTextureSlot
from .ColorRamp import ColorRamp
from .CurveMapping import CurveMapping
from .IDOverrideLibrary import IDOverrideLibrary
from .ImagePreview import ImagePreview
from .Library import Library
from .LibraryWeakReference import LibraryWeakReference
from .PaintCurve import PaintCurve
from .Texture import Texture

class Brush(ID):

    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:
        """Unique data-block ID name (within a same type and library)"""
        ...
    @name.setter
    def name(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def name_full(self) -> Annotated[str, "is_animatable=False"]:
        """Unique data-block ID name, including library one if any"""
        ...
    @property
    def id_type(self) -> Literal['ACTION', 'ARMATURE', 'BRUSH', 'CACHEFILE', 'CAMERA', 'COLLECTION', 'CURVE', 'CURVES', 'FONT', 'GREASEPENCIL', 'GREASEPENCIL_V3', 'IMAGE', 'KEY', 'LATTICE', 'LIBRARY', 'LIGHT', 'LIGHT_PROBE', 'LINESTYLE', 'MASK', 'MATERIAL', 'MESH', 'META', 'MOVIECLIP', 'NODETREE', 'OBJECT', 'PAINTCURVE', 'PALETTE', 'PARTICLE', 'POINTCLOUD', 'SCENE', 'SCREEN', 'SOUND', 'SPEAKER', 'TEXT', 'TEXTURE', 'VOLUME', 'WINDOWMANAGER', 'WORKSPACE', 'WORLD']:
        """Type identifier of this data-block"""
        ...
    @property
    def session_uid(self) -> Annotated[int, "step=1"]:
        """A session-wide unique identifier for the data block that remains the same across renames and internal reallocations, unchanged when reloading the file"""
        ...
    @property
    def is_evaluated(self) -> bool:
        """Whether this ID is runtime-only, evaluated data-block, or actual data from .blend file"""
        ...
    @property
    def original(self) -> Annotated[Optional['ID'], "is_animatable=False"]:
        """Actual data-block from .blend file (Main database) that generated that evaluated one"""
        ...
    @property
    def users(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Number of times this data-block is referenced"""
        ...
    @property
    def use_fake_user(self) -> bool:
        """Save this data-block even if it has no users"""
        ...
    @use_fake_user.setter
    def use_fake_user(self, value: bool):
        ...
    @property
    def use_extra_user(self) -> bool:
        """Indicates whether an extra user is set or not (mainly for internal/debug usages)"""
        ...
    @use_extra_user.setter
    def use_extra_user(self, value: bool):
        ...
    @property
    def is_embedded_data(self) -> bool:
        """This data-block is not an independent one, but is actually a sub-data of another ID (typical example: root node trees or master collections)"""
        ...
    @property
    def is_linked_packed(self) -> bool:
        """This data-block is linked and packed into the .blend file"""
        ...
    @property
    def is_missing(self) -> bool:
        """This data-block is a place-holder for missing linked data (i.e. it is [an override of] a linked data that could not be found anymore)"""
        ...
    @property
    def is_runtime_data(self) -> bool:
        """This data-block is runtime data, i.e. it won't be saved in .blend file. Note that e.g. evaluated IDs are always runtime, so this value is only editable for data-blocks in Main data-base."""
        ...
    @is_runtime_data.setter
    def is_runtime_data(self, value: bool):
        ...
    @property
    def is_editable(self) -> bool:
        """This data-block is editable in the user interface. Linked data-blocks are not editable, except if they were loaded as editable assets."""
        ...
    @property
    def tag(self) -> bool:
        """Tools can use this to tag data for their own purposes (initial state is undefined)"""
        ...
    @tag.setter
    def tag(self, value: bool):
        ...
    @property
    def is_library_indirect(self) -> bool:
        """Is this ID block linked indirectly"""
        ...
    @property
    def library(self) -> Annotated[Optional['Library'], "is_animatable=False"]:
        """Library file the data-block is linked from"""
        ...
    @property
    def library_weak_reference(self) -> Annotated[Optional['LibraryWeakReference'], "is_animatable=False"]:
        """Weak reference to a data-block in another library .blend file (used to re-use already appended data instead of appending new copies)"""
        ...
    @property
    def asset_data(self) -> Annotated[Optional['AssetMetaData'], "is_animatable=False"]:
        """Additional data for an asset data-block"""
        ...
    @asset_data.setter
    def asset_data(self, value: Annotated[Optional['AssetMetaData'], "is_animatable=False"]):
        ...
    @property
    def override_library(self) -> Annotated[Optional['IDOverrideLibrary'], "is_animatable=False"]:
        """Library override data"""
        ...
    @property
    def preview(self) -> Annotated[Optional['ImagePreview'], "is_animatable=False"]:
        """Preview image and icon of this data-block (always None if not supported for this type of data)"""
        ...
    @property
    def has_unsaved_changes(self) -> bool:
        """Indicates that there are any user visible changes since the brush has been imported or read from the file"""
        ...
    @property
    def blend(self) -> Literal['MIX', 'DARKEN', 'MUL', 'COLORBURN', 'LINEARBURN', 'LIGHTEN', 'SCREEN', 'COLORDODGE', 'ADD', 'OVERLAY', 'SOFTLIGHT', 'HARDLIGHT', 'VIVIDLIGHT', 'LINEARLIGHT', 'PINLIGHT', 'DIFFERENCE', 'EXCLUSION', 'SUB', 'HUE', 'SATURATION', 'COLOR', 'LUMINOSITY', 'ERASE_ALPHA', 'ADD_ALPHA']:
        """Brush blending mode"""
        ...
    @blend.setter
    def blend(self, value: Literal['MIX', 'DARKEN', 'MUL', 'COLORBURN', 'LINEARBURN', 'LIGHTEN', 'SCREEN', 'COLORDODGE', 'ADD', 'OVERLAY', 'SOFTLIGHT', 'HARDLIGHT', 'VIVIDLIGHT', 'LINEARLIGHT', 'PINLIGHT', 'DIFFERENCE', 'EXCLUSION', 'SUB', 'HUE', 'SATURATION', 'COLOR', 'LUMINOSITY', 'ERASE_ALPHA', 'ADD_ALPHA']):
        ...
    @property
    def sculpt_brush_type(self) -> Literal['DRAW', 'DRAW_SHARP', 'CLAY', 'CLAY_STRIPS', 'CLAY_THUMB', 'LAYER', 'INFLATE', 'BLOB', 'CREASE', 'SMOOTH', 'PLANE', 'MULTIPLANE_SCRAPE', 'PINCH', 'GRAB', 'ELASTIC_DEFORM', 'SNAKE_HOOK', 'THUMB', 'POSE', 'NUDGE', 'ROTATE', 'TOPOLOGY', 'BOUNDARY', 'CLOTH', 'SIMPLIFY', 'MASK', 'DRAW_FACE_SETS', 'DISPLACEMENT_ERASER', 'DISPLACEMENT_SMEAR', 'PAINT', 'SMEAR']:

        ...
    @sculpt_brush_type.setter
    def sculpt_brush_type(self, value: Literal['DRAW', 'DRAW_SHARP', 'CLAY', 'CLAY_STRIPS', 'CLAY_THUMB', 'LAYER', 'INFLATE', 'BLOB', 'CREASE', 'SMOOTH', 'PLANE', 'MULTIPLANE_SCRAPE', 'PINCH', 'GRAB', 'ELASTIC_DEFORM', 'SNAKE_HOOK', 'THUMB', 'POSE', 'NUDGE', 'ROTATE', 'TOPOLOGY', 'BOUNDARY', 'CLOTH', 'SIMPLIFY', 'MASK', 'DRAW_FACE_SETS', 'DISPLACEMENT_ERASER', 'DISPLACEMENT_SMEAR', 'PAINT', 'SMEAR']):
        ...
    @property
    def vertex_brush_type(self) -> Literal['DRAW', 'BLUR', 'AVERAGE', 'SMEAR']:

        ...
    @vertex_brush_type.setter
    def vertex_brush_type(self, value: Literal['DRAW', 'BLUR', 'AVERAGE', 'SMEAR']):
        ...
    @property
    def weight_brush_type(self) -> Literal['DRAW', 'BLUR', 'AVERAGE', 'SMEAR']:

        ...
    @weight_brush_type.setter
    def weight_brush_type(self, value: Literal['DRAW', 'BLUR', 'AVERAGE', 'SMEAR']):
        ...
    @property
    def image_brush_type(self) -> Literal['DRAW', 'SOFTEN', 'SMEAR', 'CLONE', 'FILL', 'MASK']:

        ...
    @image_brush_type.setter
    def image_brush_type(self, value: Literal['DRAW', 'SOFTEN', 'SMEAR', 'CLONE', 'FILL', 'MASK']):
        ...
    @property
    def gpencil_brush_type(self) -> Annotated[Literal['DRAW', 'FILL', 'ERASE', 'TINT'], "is_animatable=False"]:

        ...
    @gpencil_brush_type.setter
    def gpencil_brush_type(self, value: Annotated[Literal['DRAW', 'FILL', 'ERASE', 'TINT'], "is_animatable=False"]):
        ...
    @property
    def gpencil_vertex_brush_type(self) -> Annotated[Literal['DRAW', 'BLUR', 'AVERAGE', 'SMEAR', 'REPLACE'], "is_animatable=False"]:

        ...
    @gpencil_vertex_brush_type.setter
    def gpencil_vertex_brush_type(self, value: Annotated[Literal['DRAW', 'BLUR', 'AVERAGE', 'SMEAR', 'REPLACE'], "is_animatable=False"]):
        ...
    @property
    def gpencil_sculpt_brush_type(self) -> Annotated[Literal['SMOOTH', 'THICKNESS', 'STRENGTH', 'RANDOMIZE', 'GRAB', 'PUSH', 'TWIST', 'PINCH', 'CLONE'], "is_animatable=False"]:

        ...
    @gpencil_sculpt_brush_type.setter
    def gpencil_sculpt_brush_type(self, value: Annotated[Literal['SMOOTH', 'THICKNESS', 'STRENGTH', 'RANDOMIZE', 'GRAB', 'PUSH', 'TWIST', 'PINCH', 'CLONE'], "is_animatable=False"]):
        ...
    @property
    def gpencil_weight_brush_type(self) -> Annotated[Literal['WEIGHT', 'BLUR', 'AVERAGE', 'SMEAR'], "is_animatable=False"]:

        ...
    @gpencil_weight_brush_type.setter
    def gpencil_weight_brush_type(self, value: Annotated[Literal['WEIGHT', 'BLUR', 'AVERAGE', 'SMEAR'], "is_animatable=False"]):
        ...
    @property
    def curves_sculpt_brush_type(self) -> Annotated[Literal['SELECTION_PAINT', 'ADD', 'DELETE', 'DENSITY', 'COMB', 'SNAKE_HOOK', 'GROW_SHRINK', 'PINCH', 'PUFF', 'SMOOTH', 'SLIDE'], "is_animatable=False"]:

        ...
    @curves_sculpt_brush_type.setter
    def curves_sculpt_brush_type(self, value: Annotated[Literal['SELECTION_PAINT', 'ADD', 'DELETE', 'DENSITY', 'COMB', 'SNAKE_HOOK', 'GROW_SHRINK', 'PINCH', 'PUFF', 'SMOOTH', 'SLIDE'], "is_animatable=False"]):
        ...
    @property
    def direction(self) -> Literal['ADD', 'SUBTRACT']:

        ...
    @direction.setter
    def direction(self, value: Literal['ADD', 'SUBTRACT']):
        ...
    @property
    def stroke_method(self) -> Literal['DOTS', 'DRAG_DOT', 'SPACE', 'AIRBRUSH', 'ANCHORED', 'LINE', 'CURVE']:

        ...
    @stroke_method.setter
    def stroke_method(self, value: Literal['DOTS', 'DRAG_DOT', 'SPACE', 'AIRBRUSH', 'ANCHORED', 'LINE', 'CURVE']):
        ...
    @property
    def sculpt_plane(self) -> Literal['AREA', 'VIEW', 'X', 'Y', 'Z']:

        ...
    @sculpt_plane.setter
    def sculpt_plane(self, value: Literal['AREA', 'VIEW', 'X', 'Y', 'Z']):
        ...
    @property
    def mask_tool(self) -> Literal['DRAW', 'SMOOTH']:

        ...
    @mask_tool.setter
    def mask_tool(self, value: Literal['DRAW', 'SMOOTH']):
        ...
    @property
    def curve_distance_falloff_preset(self) -> Literal['CUSTOM', 'SMOOTH', 'SMOOTHER', 'SPHERE', 'ROOT', 'SHARP', 'LIN', 'POW4', 'INVSQUARE', 'CONSTANT']:

        ...
    @curve_distance_falloff_preset.setter
    def curve_distance_falloff_preset(self, value: Literal['CUSTOM', 'SMOOTH', 'SMOOTHER', 'SPHERE', 'ROOT', 'SHARP', 'LIN', 'POW4', 'INVSQUARE', 'CONSTANT']):
        ...
    @property
    def deform_target(self) -> Literal['GEOMETRY', 'CLOTH_SIM']:
        """How the deformation of the brush will affect the object"""
        ...
    @deform_target.setter
    def deform_target(self, value: Literal['GEOMETRY', 'CLOTH_SIM']):
        ...
    @property
    def elastic_deform_type(self) -> Literal['GRAB', 'GRAB_BISCALE', 'GRAB_TRISCALE', 'SCALE', 'TWIST']:
        """Deformation type that is used in the brush"""
        ...
    @elastic_deform_type.setter
    def elastic_deform_type(self, value: Literal['GRAB', 'GRAB_BISCALE', 'GRAB_TRISCALE', 'SCALE', 'TWIST']):
        ...
    @property
    def snake_hook_deform_type(self) -> Literal['FALLOFF', 'ELASTIC']:
        """Deformation type that is used in the brush"""
        ...
    @snake_hook_deform_type.setter
    def snake_hook_deform_type(self, value: Literal['FALLOFF', 'ELASTIC']):
        ...
    @property
    def plane_inversion_mode(self) -> Literal['INVERT_DISPLACEMENT', 'SWAP_DEPTH_AND_HEIGHT']:
        """Inversion Mode"""
        ...
    @plane_inversion_mode.setter
    def plane_inversion_mode(self, value: Literal['INVERT_DISPLACEMENT', 'SWAP_DEPTH_AND_HEIGHT']):
        ...
    @property
    def cloth_deform_type(self) -> Literal['DRAG', 'PUSH', 'PINCH_POINT', 'PINCH_PERPENDICULAR', 'INFLATE', 'GRAB', 'EXPAND', 'SNAKE_HOOK']:
        """Deformation type that is used in the brush"""
        ...
    @cloth_deform_type.setter
    def cloth_deform_type(self, value: Literal['DRAG', 'PUSH', 'PINCH_POINT', 'PINCH_PERPENDICULAR', 'INFLATE', 'GRAB', 'EXPAND', 'SNAKE_HOOK']):
        ...
    @property
    def cloth_force_falloff_type(self) -> Literal['RADIAL', 'PLANE']:
        """Shape used in the brush to apply force to the cloth"""
        ...
    @cloth_force_falloff_type.setter
    def cloth_force_falloff_type(self, value: Literal['RADIAL', 'PLANE']):
        ...
    @property
    def cloth_simulation_area_type(self) -> Literal['LOCAL', 'GLOBAL', 'DYNAMIC']:
        """Part of the mesh that is going to be simulated when the stroke is active"""
        ...
    @cloth_simulation_area_type.setter
    def cloth_simulation_area_type(self, value: Literal['LOCAL', 'GLOBAL', 'DYNAMIC']):
        ...
    @property
    def boundary_falloff_type(self) -> Literal['CONSTANT', 'RADIUS', 'LOOP', 'LOOP_INVERT']:
        """How the brush falloff is applied across the boundary"""
        ...
    @boundary_falloff_type.setter
    def boundary_falloff_type(self, value: Literal['CONSTANT', 'RADIUS', 'LOOP', 'LOOP_INVERT']):
        ...
    @property
    def smooth_deform_type(self) -> Literal['LAPLACIAN', 'SURFACE']:
        """Deformation type that is used in the brush"""
        ...
    @smooth_deform_type.setter
    def smooth_deform_type(self, value: Literal['LAPLACIAN', 'SURFACE']):
        ...
    @property
    def smear_deform_type(self) -> Literal['DRAG', 'PINCH', 'EXPAND']:
        """Deformation type that is used in the brush"""
        ...
    @smear_deform_type.setter
    def smear_deform_type(self, value: Literal['DRAG', 'PINCH', 'EXPAND']):
        ...
    @property
    def slide_deform_type(self) -> Literal['DRAG', 'PINCH', 'EXPAND']:
        """Deformation type that is used in the brush"""
        ...
    @slide_deform_type.setter
    def slide_deform_type(self, value: Literal['DRAG', 'PINCH', 'EXPAND']):
        ...
    @property
    def boundary_deform_type(self) -> Literal['BEND', 'EXPAND', 'INFLATE', 'GRAB', 'TWIST', 'SMOOTH']:
        """Deformation type that is used in the brush"""
        ...
    @boundary_deform_type.setter
    def boundary_deform_type(self, value: Literal['BEND', 'EXPAND', 'INFLATE', 'GRAB', 'TWIST', 'SMOOTH']):
        ...
    @property
    def pose_deform_type(self) -> Literal['ROTATE_TWIST', 'SCALE_TRANSLATE', 'SQUASH_STRETCH']:
        """Deformation type that is used in the brush"""
        ...
    @pose_deform_type.setter
    def pose_deform_type(self, value: Literal['ROTATE_TWIST', 'SCALE_TRANSLATE', 'SQUASH_STRETCH']):
        ...
    @property
    def pose_origin_type(self) -> Literal['TOPOLOGY', 'FACE_SETS', 'FACE_SETS_FK']:
        """Method to set the rotation origins for the segments of the brush"""
        ...
    @pose_origin_type.setter
    def pose_origin_type(self, value: Literal['TOPOLOGY', 'FACE_SETS', 'FACE_SETS_FK']):
        ...
    @property
    def jitter_unit(self) -> Literal['VIEW', 'BRUSH']:
        """Jitter in screen space or relative to brush size"""
        ...
    @jitter_unit.setter
    def jitter_unit(self, value: Literal['VIEW', 'BRUSH']):
        ...
    @property
    def falloff_shape(self) -> Literal['SPHERE', 'PROJECTED']:
        """Use projected or spherical falloff"""
        ...
    @falloff_shape.setter
    def falloff_shape(self, value: Literal['SPHERE', 'PROJECTED']):
        ...
    @property
    def size(self) -> Annotated[int, "subtype='PIXEL_DIAMETER'", "step=1"]:
        """Diameter of the brush in pixels"""
        ...
    @size.setter
    def size(self, value: Annotated[int, "subtype='PIXEL_DIAMETER'", "step=1"]):
        ...
    @property
    def unprojected_size(self) -> Annotated[float, "subtype='DISTANCE_DIAMETER'", "unit='LENGTH'", "step=1.0", "precision=-1"]:
        """Diameter of brush in Blender units"""
        ...
    @unprojected_size.setter
    def unprojected_size(self, value: Annotated[float, "subtype='DISTANCE_DIAMETER'", "unit='LENGTH'", "step=1.0", "precision=-1"]):
        ...
    @property
    def input_samples(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Number of input samples to average together to smooth the brush stroke"""
        ...
    @input_samples.setter
    def input_samples(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1"]):
        ...
    @property
    def jitter(self) -> Annotated[float, "step=0.10000000149011612", "precision=4"]:
        """Jitter the position of the brush while painting"""
        ...
    @jitter.setter
    def jitter(self, value: Annotated[float, "step=0.10000000149011612", "precision=4"]):
        ...
    @property
    def jitter_absolute(self) -> Annotated[int, "subtype='PIXEL'", "step=1"]:
        """Jitter the position of the brush in pixels while painting"""
        ...
    @jitter_absolute.setter
    def jitter_absolute(self, value: Annotated[int, "subtype='PIXEL'", "step=1"]):
        ...
    @property
    def spacing(self) -> Annotated[int, "subtype='PERCENTAGE'", "step=5"]:
        """Spacing between brush daubs as a percentage of brush diameter"""
        ...
    @spacing.setter
    def spacing(self, value: Annotated[int, "subtype='PERCENTAGE'", "step=5"]):
        ...
    @property
    def grad_spacing(self) -> Annotated[int, "subtype='PIXEL'", "step=5"]:
        """Spacing before brush gradient goes full circle"""
        ...
    @grad_spacing.setter
    def grad_spacing(self, value: Annotated[int, "subtype='PIXEL'", "step=5"]):
        ...
    @property
    def use_color_jitter(self) -> Annotated[bool, "is_animatable=False"]:
        """Jitter brush color"""
        ...
    @use_color_jitter.setter
    def use_color_jitter(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def hue_jitter(self) -> Annotated[float, "step=0.05000000074505806", "precision=2"]:
        """Color jitter effect on hue"""
        ...
    @hue_jitter.setter
    def hue_jitter(self, value: Annotated[float, "step=0.05000000074505806", "precision=2"]):
        ...
    @property
    def saturation_jitter(self) -> Annotated[float, "step=0.05000000074505806", "precision=2"]:
        """Color jitter effect on saturation"""
        ...
    @saturation_jitter.setter
    def saturation_jitter(self, value: Annotated[float, "step=0.05000000074505806", "precision=2"]):
        ...
    @property
    def value_jitter(self) -> Annotated[float, "step=0.05000000074505806", "precision=2"]:
        """Color jitter effect on value"""
        ...
    @value_jitter.setter
    def value_jitter(self, value: Annotated[float, "step=0.05000000074505806", "precision=2"]):
        ...
    @property
    def use_stroke_random_hue(self) -> Annotated[bool, "is_animatable=False"]:
        """Use randomness at stroke level"""
        ...
    @use_stroke_random_hue.setter
    def use_stroke_random_hue(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_stroke_random_sat(self) -> Annotated[bool, "is_animatable=False"]:
        """Use randomness at stroke level"""
        ...
    @use_stroke_random_sat.setter
    def use_stroke_random_sat(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_stroke_random_val(self) -> Annotated[bool, "is_animatable=False"]:
        """Use randomness at stroke level"""
        ...
    @use_stroke_random_val.setter
    def use_stroke_random_val(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_random_press_hue(self) -> Annotated[bool, "is_animatable=False"]:
        """Use pressure to modulate randomness"""
        ...
    @use_random_press_hue.setter
    def use_random_press_hue(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_random_press_sat(self) -> Annotated[bool, "is_animatable=False"]:
        """Use pressure to modulate randomness"""
        ...
    @use_random_press_sat.setter
    def use_random_press_sat(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_random_press_val(self) -> Annotated[bool, "is_animatable=False"]:
        """Use pressure to modulate randomness"""
        ...
    @use_random_press_val.setter
    def use_random_press_val(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def curve_random_hue(self) -> Annotated[Optional['CurveMapping'], "is_animatable=False"]:
        """Curve used for modulating effect"""
        ...
    @property
    def curve_random_saturation(self) -> Annotated[Optional['CurveMapping'], "is_animatable=False"]:
        """Curve used for modulating effect"""
        ...
    @property
    def curve_random_value(self) -> Annotated[Optional['CurveMapping'], "is_animatable=False"]:
        """Curve used for modulating effect"""
        ...
    @property
    def curve_size(self) -> Annotated[Optional['CurveMapping'], "is_animatable=False"]:
        """Curve used to map pressure to brush size"""
        ...
    @property
    def curve_strength(self) -> Annotated[Optional['CurveMapping'], "is_animatable=False"]:
        """Curve used to map pressure to brush strength"""
        ...
    @property
    def curve_jitter(self) -> Annotated[Optional['CurveMapping'], "is_animatable=False"]:
        """Curve used to map pressure to brush jitter"""
        ...
    @property
    def smooth_stroke_radius(self) -> Annotated[int, "subtype='PIXEL'", "step=1"]:
        """Minimum distance from last point before stroke continues"""
        ...
    @smooth_stroke_radius.setter
    def smooth_stroke_radius(self, value: Annotated[int, "subtype='PIXEL'", "step=1"]):
        ...
    @property
    def smooth_stroke_factor(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Higher values give a smoother stroke"""
        ...
    @smooth_stroke_factor.setter
    def smooth_stroke_factor(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def rate(self) -> Annotated[float, "step=1.0", "precision=3"]:
        """Interval between paints for Airbrush"""
        ...
    @rate.setter
    def rate(self, value: Annotated[float, "step=1.0", "precision=3"]):
        ...
    @property
    def color(self) -> Annotated[list[float], "subtype='COLOR'", "step=0.0010000000474974513", "precision=3"]:

        ...
    @color.setter
    def color(self, value: Annotated[list[float], "subtype='COLOR'", "step=0.0010000000474974513", "precision=3"]):
        ...
    @property
    def secondary_color(self) -> Annotated[list[float], "subtype='COLOR'", "step=0.0010000000474974513", "precision=3"]:

        ...
    @secondary_color.setter
    def secondary_color(self, value: Annotated[list[float], "subtype='COLOR'", "step=0.0010000000474974513", "precision=3"]):
        ...
    @property
    def weight(self) -> Annotated[float, "subtype='FACTOR'", "step=0.0010000000474974513", "precision=3"]:
        """Vertex weight when brush is applied"""
        ...
    @weight.setter
    def weight(self, value: Annotated[float, "subtype='FACTOR'", "step=0.0010000000474974513", "precision=3"]):
        ...
    @property
    def strength(self) -> Annotated[float, "subtype='FACTOR'", "step=0.0010000000474974513", "precision=3"]:
        """How powerful the effect of the brush is when applied"""
        ...
    @strength.setter
    def strength(self, value: Annotated[float, "subtype='FACTOR'", "step=0.0010000000474974513", "precision=3"]):
        ...
    @property
    def flow(self) -> Annotated[float, "subtype='FACTOR'", "step=0.0010000000474974513", "precision=3"]:
        """Amount of paint that is applied per stroke sample"""
        ...
    @flow.setter
    def flow(self, value: Annotated[float, "subtype='FACTOR'", "step=0.0010000000474974513", "precision=3"]):
        ...
    @property
    def wet_mix(self) -> Annotated[float, "subtype='FACTOR'", "step=0.0010000000474974513", "precision=3"]:
        """Amount of paint that is picked from the surface into the brush color"""
        ...
    @wet_mix.setter
    def wet_mix(self, value: Annotated[float, "subtype='FACTOR'", "step=0.0010000000474974513", "precision=3"]):
        ...
    @property
    def wet_persistence(self) -> Annotated[float, "subtype='FACTOR'", "step=0.0010000000474974513", "precision=3"]:
        """Amount of wet paint that stays in the brush after applying paint to the surface"""
        ...
    @wet_persistence.setter
    def wet_persistence(self, value: Annotated[float, "subtype='FACTOR'", "step=0.0010000000474974513", "precision=3"]):
        ...
    @property
    def density(self) -> Annotated[float, "subtype='FACTOR'", "step=0.0010000000474974513", "precision=3"]:
        """Amount of random elements that are going to be affected by the brush"""
        ...
    @density.setter
    def density(self, value: Annotated[float, "subtype='FACTOR'", "step=0.0010000000474974513", "precision=3"]):
        ...
    @property
    def tip_scale_x(self) -> Annotated[float, "subtype='FACTOR'", "step=0.0010000000474974513", "precision=3"]:
        """Scale of the brush tip in the X axis"""
        ...
    @tip_scale_x.setter
    def tip_scale_x(self, value: Annotated[float, "subtype='FACTOR'", "step=0.0010000000474974513", "precision=3"]):
        ...
    @property
    def use_hardness_pressure(self) -> Annotated[bool, "is_animatable=False"]:
        """Use pressure to modulate hardness"""
        ...
    @use_hardness_pressure.setter
    def use_hardness_pressure(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def invert_hardness_pressure(self) -> Annotated[bool, "is_animatable=False"]:
        """Invert the modulation of pressure in hardness"""
        ...
    @invert_hardness_pressure.setter
    def invert_hardness_pressure(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_flow_pressure(self) -> Annotated[bool, "is_animatable=False"]:
        """Use pressure to modulate flow"""
        ...
    @use_flow_pressure.setter
    def use_flow_pressure(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def invert_flow_pressure(self) -> Annotated[bool, "is_animatable=False"]:
        """Invert the modulation of pressure in flow"""
        ...
    @invert_flow_pressure.setter
    def invert_flow_pressure(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_wet_mix_pressure(self) -> Annotated[bool, "is_animatable=False"]:
        """Use pressure to modulate wet mix"""
        ...
    @use_wet_mix_pressure.setter
    def use_wet_mix_pressure(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def invert_wet_mix_pressure(self) -> Annotated[bool, "is_animatable=False"]:
        """Invert the modulation of pressure in wet mix"""
        ...
    @invert_wet_mix_pressure.setter
    def invert_wet_mix_pressure(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_wet_persistence_pressure(self) -> Annotated[bool, "is_animatable=False"]:
        """Use pressure to modulate wet persistence"""
        ...
    @use_wet_persistence_pressure.setter
    def use_wet_persistence_pressure(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def invert_wet_persistence_pressure(self) -> Annotated[bool, "is_animatable=False"]:
        """Invert the modulation of pressure in wet persistence"""
        ...
    @invert_wet_persistence_pressure.setter
    def invert_wet_persistence_pressure(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_density_pressure(self) -> Annotated[bool, "is_animatable=False"]:
        """Use pressure to modulate density"""
        ...
    @use_density_pressure.setter
    def use_density_pressure(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def invert_density_pressure(self) -> Annotated[bool, "is_animatable=False"]:
        """Invert the modulation of pressure in density"""
        ...
    @invert_density_pressure.setter
    def invert_density_pressure(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def dash_ratio(self) -> Annotated[float, "subtype='FACTOR'", "step=0.0010000000474974513", "precision=3"]:
        """Ratio of samples in a cycle that the brush is enabled"""
        ...
    @dash_ratio.setter
    def dash_ratio(self, value: Annotated[float, "subtype='FACTOR'", "step=0.0010000000474974513", "precision=3"]):
        ...
    @property
    def dash_samples(self) -> Annotated[int, "subtype='UNSIGNED'", "step=5"]:
        """Length of a dash cycle measured in stroke samples"""
        ...
    @dash_samples.setter
    def dash_samples(self, value: Annotated[int, "subtype='UNSIGNED'", "step=5"]):
        ...
    @property
    def plane_offset(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.0010000000474974513", "precision=3"]:
        """Adjust plane on which the brush acts towards or away from the object surface"""
        ...
    @plane_offset.setter
    def plane_offset(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.0010000000474974513", "precision=3"]):
        ...
    @property
    def plane_trim(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]:
        """If a vertex is further away from offset plane than this, then it is not affected"""
        ...
    @plane_trim.setter
    def plane_trim(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]):
        ...
    @property
    def height(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=1.0", "precision=3"]:
        """Affectable height of brush (i.e. the layer height for the layer tool)"""
        ...
    @height.setter
    def height(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=1.0", "precision=3"]):
        ...
    @property
    def plane_depth(self) -> Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=3"]:
        """The maximum distance below the plane for affected vertices. Increasing the depth affects vertices farther below the plane."""
        ...
    @plane_depth.setter
    def plane_depth(self, value: Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=3"]):
        ...
    @property
    def plane_height(self) -> Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=3"]:
        """The maximum distance above the plane for affected vertices. Increasing the height affects vertices farther above the plane."""
        ...
    @plane_height.setter
    def plane_height(self, value: Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=3"]):
        ...
    @property
    def stabilize_normal(self) -> Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=3"]:
        """Stabilize the orientation of the brush plane."""
        ...
    @stabilize_normal.setter
    def stabilize_normal(self, value: Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=3"]):
        ...
    @property
    def stabilize_plane(self) -> Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=3"]:
        """Stabilize the center of the brush plane."""
        ...
    @stabilize_plane.setter
    def stabilize_plane(self, value: Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=3"]):
        ...
    @property
    def texture_sample_bias(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]:
        """Value added to texture samples"""
        ...
    @texture_sample_bias.setter
    def texture_sample_bias(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]):
        ...
    @property
    def use_color_as_displacement(self) -> bool:
        """Handle each pixel color as individual vector for displacement (area plane mapping only)"""
        ...
    @use_color_as_displacement.setter
    def use_color_as_displacement(self, value: bool):
        ...
    @property
    def normal_weight(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """How much grab will pull vertices out of surface during a grab"""
        ...
    @normal_weight.setter
    def normal_weight(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def elastic_deform_volume_preservation(self) -> Annotated[float, "step=0.009999999776482582", "precision=3"]:
        """Poisson ratio for elastic deformation. Higher values preserve volume more, but also lead to more bulging."""
        ...
    @elastic_deform_volume_preservation.setter
    def elastic_deform_volume_preservation(self, value: Annotated[float, "step=0.009999999776482582", "precision=3"]):
        ...
    @property
    def rake_factor(self) -> Annotated[float, "subtype='FACTOR'", "step=0.0010000000474974513", "precision=3"]:
        """How much grab will follow cursor rotation"""
        ...
    @rake_factor.setter
    def rake_factor(self, value: Annotated[float, "subtype='FACTOR'", "step=0.0010000000474974513", "precision=3"]):
        ...
    @property
    def crease_pinch_factor(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """How much the crease brush pinches"""
        ...
    @crease_pinch_factor.setter
    def crease_pinch_factor(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def pose_offset(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Offset of the pose origin in relation to the brush radius"""
        ...
    @pose_offset.setter
    def pose_offset(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def disconnected_distance_max(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]:
        """Maximum distance to search for disconnected loose parts in the mesh"""
        ...
    @disconnected_distance_max.setter
    def disconnected_distance_max(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]):
        ...
    @property
    def boundary_offset(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Offset of the boundary origin in relation to the brush radius"""
        ...
    @boundary_offset.setter
    def boundary_offset(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def surface_smooth_shape_preservation(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """How much of the original shape is preserved when smoothing"""
        ...
    @surface_smooth_shape_preservation.setter
    def surface_smooth_shape_preservation(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def surface_smooth_current_vertex(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """How much the position of each individual vertex influences the final result"""
        ...
    @surface_smooth_current_vertex.setter
    def surface_smooth_current_vertex(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def surface_smooth_iterations(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Number of smoothing iterations per brush step"""
        ...
    @surface_smooth_iterations.setter
    def surface_smooth_iterations(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1"]):
        ...
    @property
    def multiplane_scrape_angle(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Angle between the planes of the crease"""
        ...
    @multiplane_scrape_angle.setter
    def multiplane_scrape_angle(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def pose_smooth_iterations(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Smooth iterations applied after calculating the pose factor of each vertex"""
        ...
    @pose_smooth_iterations.setter
    def pose_smooth_iterations(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1"]):
        ...
    @property
    def pose_ik_segments(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Number of segments of the inverse kinematics chain that will deform the mesh"""
        ...
    @pose_ik_segments.setter
    def pose_ik_segments(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1"]):
        ...
    @property
    def tip_roundness(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Roundness of the brush tip"""
        ...
    @tip_roundness.setter
    def tip_roundness(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def cloth_mass(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Mass of each simulation particle"""
        ...
    @cloth_mass.setter
    def cloth_mass(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def cloth_damping(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """How much the applied forces are propagated through the cloth"""
        ...
    @cloth_damping.setter
    def cloth_damping(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def cloth_sim_limit(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Factor added relative to the size of the radius to limit the cloth simulation effects"""
        ...
    @cloth_sim_limit.setter
    def cloth_sim_limit(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def cloth_sim_falloff(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Area to apply deformation falloff to the effects of the simulation"""
        ...
    @cloth_sim_falloff.setter
    def cloth_sim_falloff(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def cloth_constraint_softbody_strength(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """How much the cloth preserves the original shape, acting as a soft body"""
        ...
    @cloth_constraint_softbody_strength.setter
    def cloth_constraint_softbody_strength(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def hardness(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """How close the brush falloff starts from the edge of the brush"""
        ...
    @hardness.setter
    def hardness(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def automasking_boundary_edges_propagation_steps(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Distance where boundary edge automasking is going to protect vertices from the fully masked edge"""
        ...
    @automasking_boundary_edges_propagation_steps.setter
    def automasking_boundary_edges_propagation_steps(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1"]):
        ...
    @property
    def auto_smooth_factor(self) -> Annotated[float, "subtype='FACTOR'", "step=0.0010000000474974513", "precision=3"]:
        """Amount of smoothing to automatically apply to each stroke"""
        ...
    @auto_smooth_factor.setter
    def auto_smooth_factor(self, value: Annotated[float, "subtype='FACTOR'", "step=0.0010000000474974513", "precision=3"]):
        ...
    @property
    def topology_rake_factor(self) -> Annotated[float, "subtype='FACTOR'", "step=0.0010000000474974513", "precision=3"]:
        """Automatically align edges to the brush direction to generate cleaner topology and define sharp features. Best used on low-poly meshes as it has a performance impact."""
        ...
    @topology_rake_factor.setter
    def topology_rake_factor(self, value: Annotated[float, "subtype='FACTOR'", "step=0.0010000000474974513", "precision=3"]):
        ...
    @property
    def tilt_strength_factor(self) -> Annotated[float, "subtype='FACTOR'", "step=0.0010000000474974513", "precision=3"]:
        """How much the tilt of the pen will affect the brush. Negative values indicate inverting the tilt directions."""
        ...
    @tilt_strength_factor.setter
    def tilt_strength_factor(self, value: Annotated[float, "subtype='FACTOR'", "step=0.0010000000474974513", "precision=3"]):
        ...
    @property
    def normal_radius_factor(self) -> Annotated[float, "subtype='FACTOR'", "step=0.0010000000474974513", "precision=3"]:
        """Ratio between the brush radius and the radius that is going to be used to sample the normal"""
        ...
    @normal_radius_factor.setter
    def normal_radius_factor(self, value: Annotated[float, "subtype='FACTOR'", "step=0.0010000000474974513", "precision=3"]):
        ...
    @property
    def area_radius_factor(self) -> Annotated[float, "subtype='FACTOR'", "step=0.0010000000474974513", "precision=3"]:
        """Ratio between the brush radius and the radius that is going to be used to sample the area center"""
        ...
    @area_radius_factor.setter
    def area_radius_factor(self, value: Annotated[float, "subtype='FACTOR'", "step=0.0010000000474974513", "precision=3"]):
        ...
    @property
    def wet_paint_radius_factor(self) -> Annotated[float, "subtype='FACTOR'", "step=0.0010000000474974513", "precision=3"]:
        """Ratio between the brush radius and the radius that is going to be used to sample the color to blend in wet paint"""
        ...
    @wet_paint_radius_factor.setter
    def wet_paint_radius_factor(self, value: Annotated[float, "subtype='FACTOR'", "step=0.0010000000474974513", "precision=3"]):
        ...
    @property
    def stencil_pos(self) -> Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]:
        """Position of stencil in viewport"""
        ...
    @stencil_pos.setter
    def stencil_pos(self, value: Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]):
        ...
    @property
    def stencil_dimension(self) -> Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]:
        """Dimensions of stencil in viewport"""
        ...
    @stencil_dimension.setter
    def stencil_dimension(self, value: Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]):
        ...
    @property
    def mask_stencil_pos(self) -> Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]:
        """Position of mask stencil in viewport"""
        ...
    @mask_stencil_pos.setter
    def mask_stencil_pos(self, value: Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]):
        ...
    @property
    def mask_stencil_dimension(self) -> Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]:
        """Dimensions of mask stencil in viewport"""
        ...
    @mask_stencil_dimension.setter
    def mask_stencil_dimension(self, value: Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]):
        ...
    @property
    def sharp_threshold(self) -> Annotated[float, "step=1.0", "precision=3"]:
        """Threshold below which, no sharpening is done"""
        ...
    @sharp_threshold.setter
    def sharp_threshold(self, value: Annotated[float, "step=1.0", "precision=3"]):
        ...
    @property
    def fill_threshold(self) -> Annotated[float, "step=1.0", "precision=3"]:
        """Threshold above which filling is not propagated"""
        ...
    @fill_threshold.setter
    def fill_threshold(self, value: Annotated[float, "step=1.0", "precision=3"]):
        ...
    @property
    def blur_kernel_radius(self) -> Annotated[int, "step=1"]:
        """Radius of kernel used for soften and sharpen in pixels"""
        ...
    @blur_kernel_radius.setter
    def blur_kernel_radius(self, value: Annotated[int, "step=1"]):
        ...
    @property
    def blur_mode(self) -> Literal['BOX', 'GAUSSIAN']:

        ...
    @blur_mode.setter
    def blur_mode(self, value: Literal['BOX', 'GAUSSIAN']):
        ...
    @property
    def falloff_angle(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]:
        """Paint most on faces pointing towards the view according to this angle"""
        ...
    @falloff_angle.setter
    def falloff_angle(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]):
        ...
    @property
    def use_airbrush(self) -> bool:
        """Keep applying paint effect while holding mouse (spray)"""
        ...
    @use_airbrush.setter
    def use_airbrush(self, value: bool):
        ...
    @property
    def use_original_normal(self) -> bool:
        """When locked keep using normal of surface where stroke was initiated"""
        ...
    @use_original_normal.setter
    def use_original_normal(self, value: bool):
        ...
    @property
    def use_original_plane(self) -> bool:
        """When locked keep using the plane origin of surface where stroke was initiated"""
        ...
    @use_original_plane.setter
    def use_original_plane(self, value: bool):
        ...
    @property
    def use_automasking_topology(self) -> bool:
        """Affect only vertices connected to the active vertex under the brush"""
        ...
    @use_automasking_topology.setter
    def use_automasking_topology(self, value: bool):
        ...
    @property
    def use_automasking_face_sets(self) -> bool:
        """Affect only vertices that share Face Sets with the active vertex"""
        ...
    @use_automasking_face_sets.setter
    def use_automasking_face_sets(self, value: bool):
        ...
    @property
    def use_automasking_boundary_edges(self) -> bool:
        """Do not affect non manifold boundary edges"""
        ...
    @use_automasking_boundary_edges.setter
    def use_automasking_boundary_edges(self, value: bool):
        ...
    @property
    def use_automasking_boundary_face_sets(self) -> bool:
        """Do not affect vertices that belong to a Face Set boundary"""
        ...
    @use_automasking_boundary_face_sets.setter
    def use_automasking_boundary_face_sets(self, value: bool):
        ...
    @property
    def use_automasking_cavity(self) -> bool:
        """Do not affect vertices on peaks, based on the surface curvature"""
        ...
    @use_automasking_cavity.setter
    def use_automasking_cavity(self, value: bool):
        ...
    @property
    def use_automasking_cavity_inverted(self) -> bool:
        """Do not affect vertices within crevices, based on the surface curvature"""
        ...
    @use_automasking_cavity_inverted.setter
    def use_automasking_cavity_inverted(self, value: bool):
        ...
    @property
    def use_automasking_custom_cavity_curve(self) -> bool:
        """Use custom curve"""
        ...
    @use_automasking_custom_cavity_curve.setter
    def use_automasking_custom_cavity_curve(self, value: bool):
        ...
    @property
    def automasking_cavity_factor(self) -> Annotated[float, "subtype='FACTOR'", "step=0.10000000149011612", "precision=3"]:
        """The contrast of the cavity mask"""
        ...
    @automasking_cavity_factor.setter
    def automasking_cavity_factor(self, value: Annotated[float, "subtype='FACTOR'", "step=0.10000000149011612", "precision=3"]):
        ...
    @property
    def automasking_cavity_blur_steps(self) -> Annotated[int, "step=1"]:
        """The number of times the cavity mask is blurred"""
        ...
    @automasking_cavity_blur_steps.setter
    def automasking_cavity_blur_steps(self, value: Annotated[int, "step=1"]):
        ...
    @property
    def automasking_cavity_curve(self) -> Annotated[Optional['CurveMapping'], "is_animatable=False"]:
        """Curve used for the sensitivity"""
        ...
    @property
    def use_automasking_start_normal(self) -> bool:
        """Affect only vertices with a similar normal to where the stroke starts"""
        ...
    @use_automasking_start_normal.setter
    def use_automasking_start_normal(self, value: bool):
        ...
    @property
    def automasking_start_normal_limit(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]:
        """The range of angles that will be affected"""
        ...
    @automasking_start_normal_limit.setter
    def automasking_start_normal_limit(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]):
        ...
    @property
    def automasking_start_normal_falloff(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Extend the angular range with a falloff gradient"""
        ...
    @automasking_start_normal_falloff.setter
    def automasking_start_normal_falloff(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def use_automasking_view_normal(self) -> bool:
        """Affect only vertices with a normal that faces the viewer"""
        ...
    @use_automasking_view_normal.setter
    def use_automasking_view_normal(self, value: bool):
        ...
    @property
    def use_automasking_view_occlusion(self) -> bool:
        """Only affect vertices that are not occluded by other faces (slower performance)"""
        ...
    @use_automasking_view_occlusion.setter
    def use_automasking_view_occlusion(self, value: bool):
        ...
    @property
    def automasking_view_normal_limit(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]:
        """The range of angles that will be affected"""
        ...
    @automasking_view_normal_limit.setter
    def automasking_view_normal_limit(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]):
        ...
    @property
    def automasking_view_normal_falloff(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Extend the angular range with a falloff gradient"""
        ...
    @automasking_view_normal_falloff.setter
    def automasking_view_normal_falloff(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def use_scene_spacing(self) -> Literal['VIEW', 'SCENE']:
        """Calculate the brush spacing using view or scene distance"""
        ...
    @use_scene_spacing.setter
    def use_scene_spacing(self, value: Literal['VIEW', 'SCENE']):
        ...
    @property
    def use_grab_active_vertex(self) -> bool:
        """Apply the maximum grab strength to the active vertex instead of the cursor location"""
        ...
    @use_grab_active_vertex.setter
    def use_grab_active_vertex(self, value: bool):
        ...
    @property
    def use_grab_silhouette(self) -> bool:
        """Grabs trying to automask the silhouette of the object"""
        ...
    @use_grab_silhouette.setter
    def use_grab_silhouette(self, value: bool):
        ...
    @property
    def use_paint_antialiasing(self) -> bool:
        """Smooths the edges of the strokes"""
        ...
    @use_paint_antialiasing.setter
    def use_paint_antialiasing(self, value: bool):
        ...
    @property
    def use_multiplane_scrape_dynamic(self) -> bool:
        """The angle between the planes changes during the stroke to fit the surface under the cursor"""
        ...
    @use_multiplane_scrape_dynamic.setter
    def use_multiplane_scrape_dynamic(self, value: bool):
        ...
    @property
    def show_multiplane_scrape_planes_preview(self) -> bool:
        """Preview the scrape planes in the cursor during the stroke"""
        ...
    @show_multiplane_scrape_planes_preview.setter
    def show_multiplane_scrape_planes_preview(self, value: bool):
        ...
    @property
    def use_pose_ik_anchored(self) -> bool:
        """Keep the position of the last segment in the IK chain fixed"""
        ...
    @use_pose_ik_anchored.setter
    def use_pose_ik_anchored(self, value: bool):
        ...
    @property
    def use_pose_lock_rotation(self) -> bool:
        """Do not rotate the segment when using the scale deform mode"""
        ...
    @use_pose_lock_rotation.setter
    def use_pose_lock_rotation(self, value: bool):
        ...
    @property
    def use_connected_only(self) -> bool:
        """Affect only topologically connected elements"""
        ...
    @use_connected_only.setter
    def use_connected_only(self, value: bool):
        ...
    @property
    def use_cloth_pin_simulation_boundary(self) -> bool:
        """Lock the position of the vertices in the simulation falloff area to avoid artifacts and create a softer transition with unaffected areas"""
        ...
    @use_cloth_pin_simulation_boundary.setter
    def use_cloth_pin_simulation_boundary(self, value: bool):
        ...
    @property
    def use_cloth_collision(self) -> bool:
        """Collide with objects during the simulation"""
        ...
    @use_cloth_collision.setter
    def use_cloth_collision(self, value: bool):
        ...
    @property
    def invert_to_scrape_fill(self) -> bool:
        """Use Scrape or Fill brush when inverting this brush instead of inverting its displacement direction"""
        ...
    @invert_to_scrape_fill.setter
    def invert_to_scrape_fill(self, value: bool):
        ...
    @property
    def use_pressure_strength(self) -> bool:
        """Enable tablet pressure sensitivity for strength"""
        ...
    @use_pressure_strength.setter
    def use_pressure_strength(self, value: bool):
        ...
    @property
    def use_offset_pressure(self) -> bool:
        """Enable tablet pressure sensitivity for offset"""
        ...
    @use_offset_pressure.setter
    def use_offset_pressure(self, value: bool):
        ...
    @property
    def use_pressure_area_radius(self) -> bool:
        """Enable tablet pressure sensitivity for area radius"""
        ...
    @use_pressure_area_radius.setter
    def use_pressure_area_radius(self, value: bool):
        ...
    @property
    def use_pressure_size(self) -> bool:
        """Enable tablet pressure sensitivity for size"""
        ...
    @use_pressure_size.setter
    def use_pressure_size(self, value: bool):
        ...
    @property
    def use_pressure_jitter(self) -> bool:
        """Enable tablet pressure sensitivity for jitter"""
        ...
    @use_pressure_jitter.setter
    def use_pressure_jitter(self, value: bool):
        ...
    @property
    def use_pressure_spacing(self) -> bool:
        """Enable tablet pressure sensitivity for spacing"""
        ...
    @use_pressure_spacing.setter
    def use_pressure_spacing(self, value: bool):
        ...
    @property
    def use_pressure_masking(self) -> Literal['NONE', 'RAMP', 'CUTOFF']:
        """Pen pressure makes texture influence smaller"""
        ...
    @use_pressure_masking.setter
    def use_pressure_masking(self, value: Literal['NONE', 'RAMP', 'CUTOFF']):
        ...
    @property
    def use_inverse_smooth_pressure(self) -> bool:
        """Lighter pressure causes more smoothing to be applied"""
        ...
    @use_inverse_smooth_pressure.setter
    def use_inverse_smooth_pressure(self, value: bool):
        ...
    @property
    def use_plane_trim(self) -> bool:
        """Limit the distance from the offset plane that a vertex can be affected"""
        ...
    @use_plane_trim.setter
    def use_plane_trim(self, value: bool):
        ...
    @property
    def use_frontface(self) -> bool:
        """Brush only affects vertices that face the viewer"""
        ...
    @use_frontface.setter
    def use_frontface(self, value: bool):
        ...
    @property
    def use_frontface_falloff(self) -> bool:
        """Blend brush influence by how much they face the front"""
        ...
    @use_frontface_falloff.setter
    def use_frontface_falloff(self, value: bool):
        ...
    @property
    def use_anchor(self) -> bool:
        """Keep the brush anchored to the initial location"""
        ...
    @use_anchor.setter
    def use_anchor(self, value: bool):
        ...
    @property
    def use_space(self) -> bool:
        """Limit brush application to the distance specified by spacing"""
        ...
    @use_space.setter
    def use_space(self, value: bool):
        ...
    @property
    def use_line(self) -> bool:
        """Draw a line with dabs separated according to spacing"""
        ...
    @use_line.setter
    def use_line(self, value: bool):
        ...
    @property
    def use_curve(self) -> bool:
        """Define the stroke curve with a Bézier curve. Dabs are separated according to spacing."""
        ...
    @use_curve.setter
    def use_curve(self, value: bool):
        ...
    @property
    def use_smooth_stroke(self) -> bool:
        """Brush lags behind mouse and follows a smoother path"""
        ...
    @use_smooth_stroke.setter
    def use_smooth_stroke(self, value: bool):
        ...
    @property
    def use_persistent(self) -> bool:
        """Sculpt on a persistent layer of the mesh"""
        ...
    @use_persistent.setter
    def use_persistent(self, value: bool):
        ...
    @property
    def use_accumulate(self) -> bool:
        """Accumulate stroke daubs on top of each other"""
        ...
    @use_accumulate.setter
    def use_accumulate(self, value: bool):
        ...
    @property
    def use_space_attenuation(self) -> bool:
        """Automatically adjust strength to give consistent results for different spacings"""
        ...
    @use_space_attenuation.setter
    def use_space_attenuation(self, value: bool):
        ...
    @property
    def use_adaptive_space(self) -> bool:
        """Space daubs according to surface orientation instead of screen space"""
        ...
    @use_adaptive_space.setter
    def use_adaptive_space(self, value: bool):
        ...
    @property
    def use_locked_size(self) -> Literal['VIEW', 'SCENE']:
        """Measure brush size relative to the view or the scene"""
        ...
    @use_locked_size.setter
    def use_locked_size(self, value: Literal['VIEW', 'SCENE']):
        ...
    @property
    def color_type(self) -> Literal['COLOR', 'GRADIENT']:
        """Use single color or gradient when painting"""
        ...
    @color_type.setter
    def color_type(self, value: Literal['COLOR', 'GRADIENT']):
        ...
    @property
    def use_edge_to_edge(self) -> bool:
        """Drag anchor brush from edge-to-edge"""
        ...
    @use_edge_to_edge.setter
    def use_edge_to_edge(self, value: bool):
        ...
    @property
    def use_restore_mesh(self) -> bool:
        """Allow a single dot to be carefully positioned"""
        ...
    @use_restore_mesh.setter
    def use_restore_mesh(self, value: bool):
        ...
    @property
    def use_alpha(self) -> bool:
        """When this is disabled, lock alpha while painting"""
        ...
    @use_alpha.setter
    def use_alpha(self, value: bool):
        ...
    @property
    def curve_distance_falloff(self) -> Annotated['CurveMapping', "is_animatable=False"]:
        """Editable falloff curve"""
        ...
    @property
    def paint_curve(self) -> Annotated[Optional['PaintCurve'], "is_animatable=False"]:
        """Active paint curve"""
        ...
    @paint_curve.setter
    def paint_curve(self, value: Annotated[Optional['PaintCurve'], "is_animatable=False"]):
        ...
    @property
    def gradient(self) -> Annotated[Optional['ColorRamp'], "subtype=''", "unit='MASS'", "is_animatable=False"]:

        ...
    @property
    def gradient_stroke_mode(self) -> Literal['PRESSURE', 'SPACING_REPEAT', 'SPACING_CLAMP']:

        ...
    @gradient_stroke_mode.setter
    def gradient_stroke_mode(self, value: Literal['PRESSURE', 'SPACING_REPEAT', 'SPACING_CLAMP']):
        ...
    @property
    def gradient_fill_mode(self) -> Literal['LINEAR', 'RADIAL']:

        ...
    @gradient_fill_mode.setter
    def gradient_fill_mode(self, value: Literal['LINEAR', 'RADIAL']):
        ...
    @property
    def use_primary_overlay(self) -> bool:
        """Show texture in viewport"""
        ...
    @use_primary_overlay.setter
    def use_primary_overlay(self, value: bool):
        ...
    @property
    def use_secondary_overlay(self) -> bool:
        """Show texture in viewport"""
        ...
    @use_secondary_overlay.setter
    def use_secondary_overlay(self, value: bool):
        ...
    @property
    def use_cursor_overlay(self) -> bool:
        """Show cursor in viewport"""
        ...
    @use_cursor_overlay.setter
    def use_cursor_overlay(self, value: bool):
        ...
    @property
    def use_cursor_overlay_override(self) -> bool:
        """Don't show overlay during a stroke"""
        ...
    @use_cursor_overlay_override.setter
    def use_cursor_overlay_override(self, value: bool):
        ...
    @property
    def use_primary_overlay_override(self) -> bool:
        """Don't show overlay during a stroke"""
        ...
    @use_primary_overlay_override.setter
    def use_primary_overlay_override(self, value: bool):
        ...
    @property
    def use_secondary_overlay_override(self) -> bool:
        """Don't show overlay during a stroke"""
        ...
    @use_secondary_overlay_override.setter
    def use_secondary_overlay_override(self, value: bool):
        ...
    @property
    def use_paint_sculpt(self) -> bool:
        """Use this brush in sculpt mode"""
        ...
    @use_paint_sculpt.setter
    def use_paint_sculpt(self, value: bool):
        ...
    @property
    def use_paint_uv_sculpt(self) -> bool:
        """Use this brush in UV sculpt mode"""
        ...
    @use_paint_uv_sculpt.setter
    def use_paint_uv_sculpt(self, value: bool):
        ...
    @property
    def use_paint_vertex(self) -> bool:
        """Use this brush in vertex paint mode"""
        ...
    @use_paint_vertex.setter
    def use_paint_vertex(self, value: bool):
        ...
    @property
    def use_paint_weight(self) -> bool:
        """Use this brush in weight paint mode"""
        ...
    @use_paint_weight.setter
    def use_paint_weight(self, value: bool):
        ...
    @property
    def use_paint_image(self) -> bool:
        """Use this brush in texture paint mode"""
        ...
    @use_paint_image.setter
    def use_paint_image(self, value: bool):
        ...
    @property
    def use_paint_grease_pencil(self) -> bool:
        """Use this brush in Grease Pencil drawing mode"""
        ...
    @use_paint_grease_pencil.setter
    def use_paint_grease_pencil(self, value: bool):
        ...
    @property
    def use_vertex_grease_pencil(self) -> bool:
        """Use this brush in Grease Pencil vertex color mode"""
        ...
    @use_vertex_grease_pencil.setter
    def use_vertex_grease_pencil(self, value: bool):
        ...
    @property
    def use_paint_sculpt_curves(self) -> bool:
        """Use this brush in sculpt curves mode"""
        ...
    @use_paint_sculpt_curves.setter
    def use_paint_sculpt_curves(self, value: bool):
        ...
    @property
    def texture_slot(self) -> Annotated[Optional['BrushTextureSlot'], "is_animatable=False"]:

        ...
    @property
    def texture(self) -> Annotated[Optional['Texture'], "is_animatable=False"]:

        ...
    @texture.setter
    def texture(self, value: Annotated[Optional['Texture'], "is_animatable=False"]):
        ...
    @property
    def mask_texture_slot(self) -> Annotated[Optional['BrushTextureSlot'], "is_animatable=False"]:

        ...
    @property
    def mask_texture(self) -> Annotated[Optional['Texture'], "is_animatable=False"]:

        ...
    @mask_texture.setter
    def mask_texture(self, value: Annotated[Optional['Texture'], "is_animatable=False"]):
        ...
    @property
    def texture_overlay_alpha(self) -> Annotated[int, "subtype='PERCENTAGE'", "step=1"]:

        ...
    @texture_overlay_alpha.setter
    def texture_overlay_alpha(self, value: Annotated[int, "subtype='PERCENTAGE'", "step=1"]):
        ...
    @property
    def mask_overlay_alpha(self) -> Annotated[int, "subtype='PERCENTAGE'", "step=1"]:

        ...
    @mask_overlay_alpha.setter
    def mask_overlay_alpha(self, value: Annotated[int, "subtype='PERCENTAGE'", "step=1"]):
        ...
    @property
    def cursor_overlay_alpha(self) -> Annotated[int, "subtype='PERCENTAGE'", "step=1"]:

        ...
    @cursor_overlay_alpha.setter
    def cursor_overlay_alpha(self, value: Annotated[int, "subtype='PERCENTAGE'", "step=1"]):
        ...
    @property
    def cursor_color_add(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:
        """Color of cursor when adding"""
        ...
    @cursor_color_add.setter
    def cursor_color_add(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]):
        ...
    @property
    def cursor_color_subtract(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:
        """Color of cursor when subtracting"""
        ...
    @cursor_color_subtract.setter
    def cursor_color_subtract(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]):
        ...
    @property
    def brush_capabilities(self) -> Annotated['BrushCapabilities', "is_animatable=False"]:
        """Brush's capabilities"""
        ...
    @property
    def sculpt_capabilities(self) -> Annotated['BrushCapabilitiesSculpt', "is_animatable=False"]:

        ...
    @property
    def image_paint_capabilities(self) -> Annotated['BrushCapabilitiesImagePaint', "is_animatable=False"]:

        ...
    @property
    def vertex_paint_capabilities(self) -> Annotated['BrushCapabilitiesVertexPaint', "is_animatable=False"]:

        ...
    @property
    def weight_paint_capabilities(self) -> Annotated['BrushCapabilitiesWeightPaint', "is_animatable=False"]:

        ...
    @property
    def gpencil_settings(self) -> Annotated[Optional['BrushGpencilSettings'], "is_animatable=False"]:

        ...
    @property
    def curves_sculpt_settings(self) -> Annotated[Optional['BrushCurvesSculptSettings'], "is_animatable=False"]:

        ...
    def bl_system_properties_get(self, *args, **kwargs) -> Any: ...
    def rename(self, *args, **kwargs) -> Any: ...
    def evaluated_get(self, *args, **kwargs) -> Any: ...
    def copy(self, *args, **kwargs) -> Any: ...
    def asset_mark(self, *args, **kwargs) -> Any: ...
    def asset_clear(self, *args, **kwargs) -> Any: ...
    def asset_generate_preview(self, *args, **kwargs) -> Any: ...
    def override_create(self, *args, **kwargs) -> Any: ...
    def override_hierarchy_create(self, *args, **kwargs) -> Any: ...
    def user_clear(self, *args, **kwargs) -> Any: ...
    def user_remap(self, *args, **kwargs) -> Any: ...
    def make_local(self, *args, **kwargs) -> Any: ...
    def user_of_id(self, *args, **kwargs) -> Any: ...
    def animation_data_create(self, *args, **kwargs) -> Any: ...
    def animation_data_clear(self, *args, **kwargs) -> Any: ...
    def update_tag(self, *args, **kwargs) -> Any: ...
    def preview_ensure(self, *args, **kwargs) -> Any: ...