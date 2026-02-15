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

    name: Annotated[str, "is_animatable=False"]
    """Unique data-block ID name (within a same type and library)"""
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
    use_fake_user: bool
    """Save this data-block even if it has no users"""
    use_extra_user: bool
    """Indicates whether an extra user is set or not (mainly for internal/debug usages)"""
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
    is_runtime_data: bool
    """This data-block is runtime data, i.e. it won't be saved in .blend file. Note that e.g. evaluated IDs are always runtime, so this value is only editable for data-blocks in Main data-base."""
    @property
    def is_editable(self) -> bool:
        """This data-block is editable in the user interface. Linked data-blocks are not editable, except if they were loaded as editable assets."""
        ...
    tag: bool
    """Tools can use this to tag data for their own purposes (initial state is undefined)"""
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
    asset_data: Annotated[Optional['AssetMetaData'], "is_animatable=False"]
    """Additional data for an asset data-block"""
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
    blend: Literal['MIX', 'DARKEN', 'MUL', 'COLORBURN', 'LINEARBURN', 'LIGHTEN', 'SCREEN', 'COLORDODGE', 'ADD', 'OVERLAY', 'SOFTLIGHT', 'HARDLIGHT', 'VIVIDLIGHT', 'LINEARLIGHT', 'PINLIGHT', 'DIFFERENCE', 'EXCLUSION', 'SUB', 'HUE', 'SATURATION', 'COLOR', 'LUMINOSITY', 'ERASE_ALPHA', 'ADD_ALPHA']
    """Brush blending mode"""
    sculpt_brush_type: Literal['DRAW', 'DRAW_SHARP', 'CLAY', 'CLAY_STRIPS', 'CLAY_THUMB', 'LAYER', 'INFLATE', 'BLOB', 'CREASE', 'SMOOTH', 'PLANE', 'MULTIPLANE_SCRAPE', 'PINCH', 'GRAB', 'ELASTIC_DEFORM', 'SNAKE_HOOK', 'THUMB', 'POSE', 'NUDGE', 'ROTATE', 'TOPOLOGY', 'BOUNDARY', 'CLOTH', 'SIMPLIFY', 'MASK', 'DRAW_FACE_SETS', 'DISPLACEMENT_ERASER', 'DISPLACEMENT_SMEAR', 'PAINT', 'SMEAR']

    vertex_brush_type: Literal['DRAW', 'BLUR', 'AVERAGE', 'SMEAR']

    weight_brush_type: Literal['DRAW', 'BLUR', 'AVERAGE', 'SMEAR']

    image_brush_type: Literal['DRAW', 'SOFTEN', 'SMEAR', 'CLONE', 'FILL', 'MASK']

    gpencil_brush_type: Annotated[Literal['DRAW', 'FILL', 'ERASE', 'TINT'], "is_animatable=False"]

    gpencil_vertex_brush_type: Annotated[Literal['DRAW', 'BLUR', 'AVERAGE', 'SMEAR', 'REPLACE'], "is_animatable=False"]

    gpencil_sculpt_brush_type: Annotated[Literal['SMOOTH', 'THICKNESS', 'STRENGTH', 'RANDOMIZE', 'GRAB', 'PUSH', 'TWIST', 'PINCH', 'CLONE'], "is_animatable=False"]

    gpencil_weight_brush_type: Annotated[Literal['WEIGHT', 'BLUR', 'AVERAGE', 'SMEAR'], "is_animatable=False"]

    curves_sculpt_brush_type: Annotated[Literal['SELECTION_PAINT', 'ADD', 'DELETE', 'DENSITY', 'COMB', 'SNAKE_HOOK', 'GROW_SHRINK', 'PINCH', 'PUFF', 'SMOOTH', 'SLIDE'], "is_animatable=False"]

    direction: Literal['ADD', 'SUBTRACT']

    stroke_method: Literal['DOTS', 'DRAG_DOT', 'SPACE', 'AIRBRUSH', 'ANCHORED', 'LINE', 'CURVE']

    sculpt_plane: Literal['AREA', 'VIEW', 'X', 'Y', 'Z']

    mask_tool: Literal['DRAW', 'SMOOTH']

    curve_distance_falloff_preset: Literal['CUSTOM', 'SMOOTH', 'SMOOTHER', 'SPHERE', 'ROOT', 'SHARP', 'LIN', 'POW4', 'INVSQUARE', 'CONSTANT']

    deform_target: Literal['GEOMETRY', 'CLOTH_SIM']
    """How the deformation of the brush will affect the object"""
    elastic_deform_type: Literal['GRAB', 'GRAB_BISCALE', 'GRAB_TRISCALE', 'SCALE', 'TWIST']
    """Deformation type that is used in the brush"""
    snake_hook_deform_type: Literal['FALLOFF', 'ELASTIC']
    """Deformation type that is used in the brush"""
    plane_inversion_mode: Literal['INVERT_DISPLACEMENT', 'SWAP_DEPTH_AND_HEIGHT']
    """Inversion Mode"""
    cloth_deform_type: Literal['DRAG', 'PUSH', 'PINCH_POINT', 'PINCH_PERPENDICULAR', 'INFLATE', 'GRAB', 'EXPAND', 'SNAKE_HOOK']
    """Deformation type that is used in the brush"""
    cloth_force_falloff_type: Literal['RADIAL', 'PLANE']
    """Shape used in the brush to apply force to the cloth"""
    cloth_simulation_area_type: Literal['LOCAL', 'GLOBAL', 'DYNAMIC']
    """Part of the mesh that is going to be simulated when the stroke is active"""
    boundary_falloff_type: Literal['CONSTANT', 'RADIUS', 'LOOP', 'LOOP_INVERT']
    """How the brush falloff is applied across the boundary"""
    smooth_deform_type: Literal['LAPLACIAN', 'SURFACE']
    """Deformation type that is used in the brush"""
    smear_deform_type: Literal['DRAG', 'PINCH', 'EXPAND']
    """Deformation type that is used in the brush"""
    slide_deform_type: Literal['DRAG', 'PINCH', 'EXPAND']
    """Deformation type that is used in the brush"""
    boundary_deform_type: Literal['BEND', 'EXPAND', 'INFLATE', 'GRAB', 'TWIST', 'SMOOTH']
    """Deformation type that is used in the brush"""
    pose_deform_type: Literal['ROTATE_TWIST', 'SCALE_TRANSLATE', 'SQUASH_STRETCH']
    """Deformation type that is used in the brush"""
    pose_origin_type: Literal['TOPOLOGY', 'FACE_SETS', 'FACE_SETS_FK']
    """Method to set the rotation origins for the segments of the brush"""
    jitter_unit: Literal['VIEW', 'BRUSH']
    """Jitter in screen space or relative to brush size"""
    falloff_shape: Literal['SPHERE', 'PROJECTED']
    """Use projected or spherical falloff"""
    size: Annotated[int, "subtype='PIXEL_DIAMETER'", "step=1"]
    """Diameter of the brush in pixels"""
    unprojected_size: Annotated[float, "subtype='DISTANCE_DIAMETER'", "unit='LENGTH'", "step=1.0", "precision=-1"]
    """Diameter of brush in Blender units"""
    input_samples: Annotated[int, "subtype='UNSIGNED'", "step=1"]
    """Number of input samples to average together to smooth the brush stroke"""
    jitter: Annotated[float, "step=0.10000000149011612", "precision=4"]
    """Jitter the position of the brush while painting"""
    jitter_absolute: Annotated[int, "subtype='PIXEL'", "step=1"]
    """Jitter the position of the brush in pixels while painting"""
    spacing: Annotated[int, "subtype='PERCENTAGE'", "step=5"]
    """Spacing between brush daubs as a percentage of brush diameter"""
    grad_spacing: Annotated[int, "subtype='PIXEL'", "step=5"]
    """Spacing before brush gradient goes full circle"""
    use_color_jitter: Annotated[bool, "is_animatable=False"]
    """Jitter brush color"""
    hue_jitter: Annotated[float, "step=0.05000000074505806", "precision=2"]
    """Color jitter effect on hue"""
    saturation_jitter: Annotated[float, "step=0.05000000074505806", "precision=2"]
    """Color jitter effect on saturation"""
    value_jitter: Annotated[float, "step=0.05000000074505806", "precision=2"]
    """Color jitter effect on value"""
    use_stroke_random_hue: Annotated[bool, "is_animatable=False"]
    """Use randomness at stroke level"""
    use_stroke_random_sat: Annotated[bool, "is_animatable=False"]
    """Use randomness at stroke level"""
    use_stroke_random_val: Annotated[bool, "is_animatable=False"]
    """Use randomness at stroke level"""
    use_random_press_hue: Annotated[bool, "is_animatable=False"]
    """Use pressure to modulate randomness"""
    use_random_press_sat: Annotated[bool, "is_animatable=False"]
    """Use pressure to modulate randomness"""
    use_random_press_val: Annotated[bool, "is_animatable=False"]
    """Use pressure to modulate randomness"""
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
    smooth_stroke_radius: Annotated[int, "subtype='PIXEL'", "step=1"]
    """Minimum distance from last point before stroke continues"""
    smooth_stroke_factor: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Higher values give a smoother stroke"""
    rate: Annotated[float, "step=1.0", "precision=3"]
    """Interval between paints for Airbrush"""
    color: Annotated[list[float], "subtype='COLOR'", "step=0.0010000000474974513", "precision=3"]

    secondary_color: Annotated[list[float], "subtype='COLOR'", "step=0.0010000000474974513", "precision=3"]

    weight: Annotated[float, "subtype='FACTOR'", "step=0.0010000000474974513", "precision=3"]
    """Vertex weight when brush is applied"""
    strength: Annotated[float, "subtype='FACTOR'", "step=0.0010000000474974513", "precision=3"]
    """How powerful the effect of the brush is when applied"""
    flow: Annotated[float, "subtype='FACTOR'", "step=0.0010000000474974513", "precision=3"]
    """Amount of paint that is applied per stroke sample"""
    wet_mix: Annotated[float, "subtype='FACTOR'", "step=0.0010000000474974513", "precision=3"]
    """Amount of paint that is picked from the surface into the brush color"""
    wet_persistence: Annotated[float, "subtype='FACTOR'", "step=0.0010000000474974513", "precision=3"]
    """Amount of wet paint that stays in the brush after applying paint to the surface"""
    density: Annotated[float, "subtype='FACTOR'", "step=0.0010000000474974513", "precision=3"]
    """Amount of random elements that are going to be affected by the brush"""
    tip_scale_x: Annotated[float, "subtype='FACTOR'", "step=0.0010000000474974513", "precision=3"]
    """Scale of the brush tip in the X axis"""
    use_hardness_pressure: Annotated[bool, "is_animatable=False"]
    """Use pressure to modulate hardness"""
    invert_hardness_pressure: Annotated[bool, "is_animatable=False"]
    """Invert the modulation of pressure in hardness"""
    use_flow_pressure: Annotated[bool, "is_animatable=False"]
    """Use pressure to modulate flow"""
    invert_flow_pressure: Annotated[bool, "is_animatable=False"]
    """Invert the modulation of pressure in flow"""
    use_wet_mix_pressure: Annotated[bool, "is_animatable=False"]
    """Use pressure to modulate wet mix"""
    invert_wet_mix_pressure: Annotated[bool, "is_animatable=False"]
    """Invert the modulation of pressure in wet mix"""
    use_wet_persistence_pressure: Annotated[bool, "is_animatable=False"]
    """Use pressure to modulate wet persistence"""
    invert_wet_persistence_pressure: Annotated[bool, "is_animatable=False"]
    """Invert the modulation of pressure in wet persistence"""
    use_density_pressure: Annotated[bool, "is_animatable=False"]
    """Use pressure to modulate density"""
    invert_density_pressure: Annotated[bool, "is_animatable=False"]
    """Invert the modulation of pressure in density"""
    dash_ratio: Annotated[float, "subtype='FACTOR'", "step=0.0010000000474974513", "precision=3"]
    """Ratio of samples in a cycle that the brush is enabled"""
    dash_samples: Annotated[int, "subtype='UNSIGNED'", "step=5"]
    """Length of a dash cycle measured in stroke samples"""
    plane_offset: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.0010000000474974513", "precision=3"]
    """Adjust plane on which the brush acts towards or away from the object surface"""
    plane_trim: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]
    """If a vertex is further away from offset plane than this, then it is not affected"""
    height: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=1.0", "precision=3"]
    """Affectable height of brush (i.e. the layer height for the layer tool)"""
    plane_depth: Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=3"]
    """The maximum distance below the plane for affected vertices. Increasing the depth affects vertices farther below the plane."""
    plane_height: Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=3"]
    """The maximum distance above the plane for affected vertices. Increasing the height affects vertices farther above the plane."""
    stabilize_normal: Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=3"]
    """Stabilize the orientation of the brush plane."""
    stabilize_plane: Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=3"]
    """Stabilize the center of the brush plane."""
    texture_sample_bias: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]
    """Value added to texture samples"""
    use_color_as_displacement: bool
    """Handle each pixel color as individual vector for displacement (area plane mapping only)"""
    normal_weight: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """How much grab will pull vertices out of surface during a grab"""
    elastic_deform_volume_preservation: Annotated[float, "step=0.009999999776482582", "precision=3"]
    """Poisson ratio for elastic deformation. Higher values preserve volume more, but also lead to more bulging."""
    rake_factor: Annotated[float, "subtype='FACTOR'", "step=0.0010000000474974513", "precision=3"]
    """How much grab will follow cursor rotation"""
    crease_pinch_factor: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """How much the crease brush pinches"""
    pose_offset: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Offset of the pose origin in relation to the brush radius"""
    disconnected_distance_max: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]
    """Maximum distance to search for disconnected loose parts in the mesh"""
    boundary_offset: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Offset of the boundary origin in relation to the brush radius"""
    surface_smooth_shape_preservation: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """How much of the original shape is preserved when smoothing"""
    surface_smooth_current_vertex: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """How much the position of each individual vertex influences the final result"""
    surface_smooth_iterations: Annotated[int, "subtype='UNSIGNED'", "step=1"]
    """Number of smoothing iterations per brush step"""
    multiplane_scrape_angle: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Angle between the planes of the crease"""
    pose_smooth_iterations: Annotated[int, "subtype='UNSIGNED'", "step=1"]
    """Smooth iterations applied after calculating the pose factor of each vertex"""
    pose_ik_segments: Annotated[int, "subtype='UNSIGNED'", "step=1"]
    """Number of segments of the inverse kinematics chain that will deform the mesh"""
    tip_roundness: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Roundness of the brush tip"""
    cloth_mass: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Mass of each simulation particle"""
    cloth_damping: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """How much the applied forces are propagated through the cloth"""
    cloth_sim_limit: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Factor added relative to the size of the radius to limit the cloth simulation effects"""
    cloth_sim_falloff: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Area to apply deformation falloff to the effects of the simulation"""
    cloth_constraint_softbody_strength: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """How much the cloth preserves the original shape, acting as a soft body"""
    hardness: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """How close the brush falloff starts from the edge of the brush"""
    automasking_boundary_edges_propagation_steps: Annotated[int, "subtype='UNSIGNED'", "step=1"]
    """Distance where boundary edge automasking is going to protect vertices from the fully masked edge"""
    auto_smooth_factor: Annotated[float, "subtype='FACTOR'", "step=0.0010000000474974513", "precision=3"]
    """Amount of smoothing to automatically apply to each stroke"""
    topology_rake_factor: Annotated[float, "subtype='FACTOR'", "step=0.0010000000474974513", "precision=3"]
    """Automatically align edges to the brush direction to generate cleaner topology and define sharp features. Best used on low-poly meshes as it has a performance impact."""
    tilt_strength_factor: Annotated[float, "subtype='FACTOR'", "step=0.0010000000474974513", "precision=3"]
    """How much the tilt of the pen will affect the brush. Negative values indicate inverting the tilt directions."""
    normal_radius_factor: Annotated[float, "subtype='FACTOR'", "step=0.0010000000474974513", "precision=3"]
    """Ratio between the brush radius and the radius that is going to be used to sample the normal"""
    area_radius_factor: Annotated[float, "subtype='FACTOR'", "step=0.0010000000474974513", "precision=3"]
    """Ratio between the brush radius and the radius that is going to be used to sample the area center"""
    wet_paint_radius_factor: Annotated[float, "subtype='FACTOR'", "step=0.0010000000474974513", "precision=3"]
    """Ratio between the brush radius and the radius that is going to be used to sample the color to blend in wet paint"""
    stencil_pos: Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]
    """Position of stencil in viewport"""
    stencil_dimension: Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]
    """Dimensions of stencil in viewport"""
    mask_stencil_pos: Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]
    """Position of mask stencil in viewport"""
    mask_stencil_dimension: Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]
    """Dimensions of mask stencil in viewport"""
    sharp_threshold: Annotated[float, "step=1.0", "precision=3"]
    """Threshold below which, no sharpening is done"""
    fill_threshold: Annotated[float, "step=1.0", "precision=3"]
    """Threshold above which filling is not propagated"""
    blur_kernel_radius: Annotated[int, "step=1"]
    """Radius of kernel used for soften and sharpen in pixels"""
    blur_mode: Literal['BOX', 'GAUSSIAN']

    falloff_angle: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]
    """Paint most on faces pointing towards the view according to this angle"""
    use_airbrush: bool
    """Keep applying paint effect while holding mouse (spray)"""
    use_original_normal: bool
    """When locked keep using normal of surface where stroke was initiated"""
    use_original_plane: bool
    """When locked keep using the plane origin of surface where stroke was initiated"""
    use_automasking_topology: bool
    """Affect only vertices connected to the active vertex under the brush"""
    use_automasking_face_sets: bool
    """Affect only vertices that share Face Sets with the active vertex"""
    use_automasking_boundary_edges: bool
    """Do not affect non manifold boundary edges"""
    use_automasking_boundary_face_sets: bool
    """Do not affect vertices that belong to a Face Set boundary"""
    use_automasking_cavity: bool
    """Do not affect vertices on peaks, based on the surface curvature"""
    use_automasking_cavity_inverted: bool
    """Do not affect vertices within crevices, based on the surface curvature"""
    use_automasking_custom_cavity_curve: bool
    """Use custom curve"""
    automasking_cavity_factor: Annotated[float, "subtype='FACTOR'", "step=0.10000000149011612", "precision=3"]
    """The contrast of the cavity mask"""
    automasking_cavity_blur_steps: Annotated[int, "step=1"]
    """The number of times the cavity mask is blurred"""
    @property
    def automasking_cavity_curve(self) -> Annotated[Optional['CurveMapping'], "is_animatable=False"]:
        """Curve used for the sensitivity"""
        ...
    use_automasking_start_normal: bool
    """Affect only vertices with a similar normal to where the stroke starts"""
    automasking_start_normal_limit: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]
    """The range of angles that will be affected"""
    automasking_start_normal_falloff: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Extend the angular range with a falloff gradient"""
    use_automasking_view_normal: bool
    """Affect only vertices with a normal that faces the viewer"""
    use_automasking_view_occlusion: bool
    """Only affect vertices that are not occluded by other faces (slower performance)"""
    automasking_view_normal_limit: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]
    """The range of angles that will be affected"""
    automasking_view_normal_falloff: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Extend the angular range with a falloff gradient"""
    use_scene_spacing: Literal['VIEW', 'SCENE']
    """Calculate the brush spacing using view or scene distance"""
    use_grab_active_vertex: bool
    """Apply the maximum grab strength to the active vertex instead of the cursor location"""
    use_grab_silhouette: bool
    """Grabs trying to automask the silhouette of the object"""
    use_paint_antialiasing: bool
    """Smooths the edges of the strokes"""
    use_multiplane_scrape_dynamic: bool
    """The angle between the planes changes during the stroke to fit the surface under the cursor"""
    show_multiplane_scrape_planes_preview: bool
    """Preview the scrape planes in the cursor during the stroke"""
    use_pose_ik_anchored: bool
    """Keep the position of the last segment in the IK chain fixed"""
    use_pose_lock_rotation: bool
    """Do not rotate the segment when using the scale deform mode"""
    use_connected_only: bool
    """Affect only topologically connected elements"""
    use_cloth_pin_simulation_boundary: bool
    """Lock the position of the vertices in the simulation falloff area to avoid artifacts and create a softer transition with unaffected areas"""
    use_cloth_collision: bool
    """Collide with objects during the simulation"""
    invert_to_scrape_fill: bool
    """Use Scrape or Fill brush when inverting this brush instead of inverting its displacement direction"""
    use_pressure_strength: bool
    """Enable tablet pressure sensitivity for strength"""
    use_offset_pressure: bool
    """Enable tablet pressure sensitivity for offset"""
    use_pressure_area_radius: bool
    """Enable tablet pressure sensitivity for area radius"""
    use_pressure_size: bool
    """Enable tablet pressure sensitivity for size"""
    use_pressure_jitter: bool
    """Enable tablet pressure sensitivity for jitter"""
    use_pressure_spacing: bool
    """Enable tablet pressure sensitivity for spacing"""
    use_pressure_masking: Literal['NONE', 'RAMP', 'CUTOFF']
    """Pen pressure makes texture influence smaller"""
    use_inverse_smooth_pressure: bool
    """Lighter pressure causes more smoothing to be applied"""
    use_plane_trim: bool
    """Limit the distance from the offset plane that a vertex can be affected"""
    use_frontface: bool
    """Brush only affects vertices that face the viewer"""
    use_frontface_falloff: bool
    """Blend brush influence by how much they face the front"""
    use_anchor: bool
    """Keep the brush anchored to the initial location"""
    use_space: bool
    """Limit brush application to the distance specified by spacing"""
    use_line: bool
    """Draw a line with dabs separated according to spacing"""
    use_curve: bool
    """Define the stroke curve with a Bézier curve. Dabs are separated according to spacing."""
    use_smooth_stroke: bool
    """Brush lags behind mouse and follows a smoother path"""
    use_persistent: bool
    """Sculpt on a persistent layer of the mesh"""
    use_accumulate: bool
    """Accumulate stroke daubs on top of each other"""
    use_space_attenuation: bool
    """Automatically adjust strength to give consistent results for different spacings"""
    use_adaptive_space: bool
    """Space daubs according to surface orientation instead of screen space"""
    use_locked_size: Literal['VIEW', 'SCENE']
    """Measure brush size relative to the view or the scene"""
    color_type: Literal['COLOR', 'GRADIENT']
    """Use single color or gradient when painting"""
    use_edge_to_edge: bool
    """Drag anchor brush from edge-to-edge"""
    use_restore_mesh: bool
    """Allow a single dot to be carefully positioned"""
    use_alpha: bool
    """When this is disabled, lock alpha while painting"""
    @property
    def curve_distance_falloff(self) -> Annotated['CurveMapping', "is_animatable=False"]:
        """Editable falloff curve"""
        ...
    paint_curve: Annotated[Optional['PaintCurve'], "is_animatable=False"]
    """Active paint curve"""
    @property
    def gradient(self) -> Annotated[Optional['ColorRamp'], "subtype=''", "unit='MASS'", "is_animatable=False"]:

        ...
    gradient_stroke_mode: Literal['PRESSURE', 'SPACING_REPEAT', 'SPACING_CLAMP']

    gradient_fill_mode: Literal['LINEAR', 'RADIAL']

    use_primary_overlay: bool
    """Show texture in viewport"""
    use_secondary_overlay: bool
    """Show texture in viewport"""
    use_cursor_overlay: bool
    """Show cursor in viewport"""
    use_cursor_overlay_override: bool
    """Don't show overlay during a stroke"""
    use_primary_overlay_override: bool
    """Don't show overlay during a stroke"""
    use_secondary_overlay_override: bool
    """Don't show overlay during a stroke"""
    use_paint_sculpt: bool
    """Use this brush in sculpt mode"""
    use_paint_uv_sculpt: bool
    """Use this brush in UV sculpt mode"""
    use_paint_vertex: bool
    """Use this brush in vertex paint mode"""
    use_paint_weight: bool
    """Use this brush in weight paint mode"""
    use_paint_image: bool
    """Use this brush in texture paint mode"""
    use_paint_grease_pencil: bool
    """Use this brush in Grease Pencil drawing mode"""
    use_vertex_grease_pencil: bool
    """Use this brush in Grease Pencil vertex color mode"""
    use_paint_sculpt_curves: bool
    """Use this brush in sculpt curves mode"""
    @property
    def texture_slot(self) -> Annotated[Optional['BrushTextureSlot'], "is_animatable=False"]:

        ...
    texture: Annotated[Optional['Texture'], "is_animatable=False"]

    @property
    def mask_texture_slot(self) -> Annotated[Optional['BrushTextureSlot'], "is_animatable=False"]:

        ...
    mask_texture: Annotated[Optional['Texture'], "is_animatable=False"]

    texture_overlay_alpha: Annotated[int, "subtype='PERCENTAGE'", "step=1"]

    mask_overlay_alpha: Annotated[int, "subtype='PERCENTAGE'", "step=1"]

    cursor_overlay_alpha: Annotated[int, "subtype='PERCENTAGE'", "step=1"]

    cursor_color_add: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    """Color of cursor when adding"""
    cursor_color_subtract: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    """Color of cursor when subtracting"""
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