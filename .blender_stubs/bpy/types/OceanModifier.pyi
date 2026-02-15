# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated
from .bpy_prop_collection import bpy_prop_collection

from .Modifier import Modifier
class OceanModifier(Modifier):
    name: Annotated[str, "is_animatable=False"]
    """Modifier name"""
    @property
    def type(self) -> Literal['GREASE_PENCIL_VERTEX_WEIGHT_PROXIMITY', 'DATA_TRANSFER', 'MESH_CACHE', 'MESH_SEQUENCE_CACHE', 'NORMAL_EDIT', 'WEIGHTED_NORMAL', 'UV_PROJECT', 'UV_WARP', 'VERTEX_WEIGHT_EDIT', 'VERTEX_WEIGHT_MIX', 'VERTEX_WEIGHT_PROXIMITY', 'GREASE_PENCIL_COLOR', 'GREASE_PENCIL_TINT', 'GREASE_PENCIL_OPACITY', 'GREASE_PENCIL_VERTEX_WEIGHT_ANGLE', 'GREASE_PENCIL_TIME', 'GREASE_PENCIL_TEXTURE', 'ARRAY', 'BEVEL', 'BOOLEAN', 'BUILD', 'DECIMATE', 'EDGE_SPLIT', 'NODES', 'MASK', 'MIRROR', 'MESH_TO_VOLUME', 'MULTIRES', 'REMESH', 'SCREW', 'SKIN', 'SOLIDIFY', 'SUBSURF', 'TRIANGULATE', 'VOLUME_TO_MESH', 'WELD', 'WIREFRAME', 'GREASE_PENCIL_ARRAY', 'GREASE_PENCIL_BUILD', 'GREASE_PENCIL_LENGTH', 'LINEART', 'GREASE_PENCIL_MIRROR', 'GREASE_PENCIL_MULTIPLY', 'GREASE_PENCIL_SIMPLIFY', 'GREASE_PENCIL_SUBDIV', 'GREASE_PENCIL_ENVELOPE', 'GREASE_PENCIL_OUTLINE', 'ARMATURE', 'CAST', 'CURVE', 'DISPLACE', 'HOOK', 'LAPLACIANDEFORM', 'LATTICE', 'MESH_DEFORM', 'SHRINKWRAP', 'SIMPLE_DEFORM', 'SMOOTH', 'CORRECTIVE_SMOOTH', 'LAPLACIANSMOOTH', 'SURFACE_DEFORM', 'WARP', 'WAVE', 'VOLUME_DISPLACE', 'GREASE_PENCIL_HOOK', 'GREASE_PENCIL_NOISE', 'GREASE_PENCIL_OFFSET', 'GREASE_PENCIL_SMOOTH', 'GREASE_PENCIL_THICKNESS', 'GREASE_PENCIL_LATTICE', 'GREASE_PENCIL_DASH', 'GREASE_PENCIL_ARMATURE', 'GREASE_PENCIL_SHRINKWRAP', 'CLOTH', 'COLLISION', 'DYNAMIC_PAINT', 'EXPLODE', 'FLUID', 'OCEAN', 'PARTICLE_INSTANCE', 'PARTICLE_SYSTEM', 'SOFT_BODY', 'SURFACE']:
        ...
    show_viewport: bool
    """Display modifier in viewport"""
    show_render: bool
    """Use modifier during render"""
    show_in_editmode: bool
    """Display modifier in Edit mode"""
    show_on_cage: bool
    """Adjust edit cage to modifier result"""
    show_expanded: bool
    """Set modifier expanded in the user interface"""
    is_active: Annotated[bool, "is_animatable=False"]
    """The active modifier in the list"""
    use_pin_to_last: Annotated[bool, "is_animatable=False"]
    """Keep the modifier at the end of the list"""
    @property
    def is_override_data(self) -> bool:
        """In a local override object, whether this modifier comes from the linked reference object, or is local to the override"""
        ...
    use_apply_on_spline: bool
    """Apply this and all preceding deformation modifiers on splines' points rather than on filled curve/surface"""
    @property
    def execution_time(self) -> Annotated[float, "subtype='TIME_ABSOLUTE'", "unit='TIME_ABSOLUTE'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Time in seconds that the modifier took to evaluate. This is only set on evaluated objects. If multiple modifiers run in parallel, execution time is not a reliable metric."""
        ...
    @property
    def persistent_uid(self) -> Annotated[int, "step=1"]:
        """Uniquely identifies the modifier within the modifier stack that it is part of"""
        ...
    geometry_mode: Literal['GENERATE', 'DISPLACE']
    """Method of modifying geometry"""
    size: Annotated[float, "subtype='UNSIGNED'", "step=1.0", "precision=-1"]
    """Surface scale factor (does not affect the height of the waves)"""
    repeat_x: Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]
    """Repetitions of the generated surface in X"""
    repeat_y: Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]
    """Repetitions of the generated surface in Y"""
    use_normals: Annotated[bool, "is_animatable=False"]
    """Output normals for bump mapping - disabling can speed up performance if it's not needed"""
    use_foam: Annotated[bool, "is_animatable=False"]
    """Generate foam mask as a vertex color channel"""
    use_spray: Annotated[bool, "is_animatable=False"]
    """Generate map of spray direction as a vertex color channel"""
    invert_spray: Annotated[bool, "is_animatable=False"]
    """Invert the spray direction map"""
    spray_layer_name: Annotated[str, "is_animatable=False"]
    """Name of the vertex color layer used for the spray direction map"""
    resolution: Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]
    """Resolution of the generated surface for rendering and baking"""
    viewport_resolution: Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]
    """Viewport resolution of the generated surface"""
    spatial_size: Annotated[int, "step=2", "is_animatable=False"]
    """Size of the simulation domain (in meters), and of the generated geometry (in BU)"""
    wind_velocity: Annotated[float, "subtype='VELOCITY'", "unit='VELOCITY'", "step=10.0", "precision=3", "is_animatable=False"]
    """Wind speed"""
    damping: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]
    """Damp reflected waves going in opposite direction to the wind"""
    wave_scale_min: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3", "is_animatable=False"]
    """Shortest allowed wavelength"""
    wave_alignment: Annotated[float, "subtype='UNSIGNED'", "step=10.0", "precision=3", "is_animatable=False"]
    """How much the waves are aligned to each other"""
    wave_direction: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3", "is_animatable=False"]
    """Main direction of the waves when they are (partially) aligned"""
    wave_scale: Annotated[float, "subtype='UNSIGNED'", "step=10.0", "precision=3"]
    """Scale of the displacement effect"""
    depth: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=1.0", "precision=-1", "is_animatable=False"]
    """Depth of the solid ground below the water surface"""
    foam_coverage: Annotated[float, "step=10.0", "precision=3"]
    """Amount of generated foam"""
    bake_foam_fade: Annotated[float, "subtype='UNSIGNED'", "step=1.0", "precision=-1", "is_animatable=False"]
    """How much foam accumulates over time (baked ocean only)"""
    foam_layer_name: Annotated[str, "is_animatable=False"]
    """Name of the vertex color layer used for foam"""
    choppiness: Annotated[float, "subtype='UNSIGNED'", "step=3.0", "precision=-1"]
    """Choppiness of the wave's crest (adds some horizontal component to the displacement)"""
    time: Annotated[float, "subtype='UNSIGNED'", "step=1.0", "precision=-1"]
    """Current time of the simulation"""
    spectrum: Annotated[Literal['PHILLIPS', 'PIERSON_MOSKOWITZ', 'JONSWAP', 'TEXEL_MARSEN_ARSLOE'], "is_animatable=False"]
    """Spectrum to use"""
    fetch_jonswap: Annotated[float, "subtype='UNSIGNED'", "step=10.0", "precision=3", "is_animatable=False"]
    """This is the distance from a lee shore, called the fetch, or the distance over which the wind blows with constant velocity. Used by 'JONSWAP' and 'TMA' models."""
    sharpen_peak_jonswap: Annotated[float, "subtype='UNSIGNED'", "step=10.0", "precision=3", "is_animatable=False"]
    """Peak sharpening for 'JONSWAP' and 'TMA' models"""
    random_seed: Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]
    """Seed of the random generator"""
    frame_start: Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1", "is_animatable=False"]
    """Start frame of the ocean baking"""
    frame_end: Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1", "is_animatable=False"]
    """End frame of the ocean baking"""
    @property
    def is_cached(self) -> bool:
        """Whether the ocean is using cached data or simulating"""
        ...
    filepath: Annotated[str, "subtype='DIR_PATH'", "is_animatable=False"]
    """Path to a folder to store external baked images"""