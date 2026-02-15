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
from .Object import Object
from .Texture import Texture
class FieldSettings(bpy_struct):
    type: Literal['NONE', 'BOID', 'CHARGE', 'GUIDE', 'DRAG', 'FLUID_FLOW', 'FORCE', 'HARMONIC', 'LENNARDJ', 'MAGNET', 'TEXTURE', 'TURBULENCE', 'VORTEX', 'WIND']
    """Type of field"""
    shape: Literal['POINT', 'LINE', 'PLANE', 'SURFACE', 'POINTS']
    """Which direction is used to calculate the effector force"""
    falloff_type: Literal['CONE', 'SPHERE', 'TUBE']
    texture_mode: Literal['CURL', 'GRADIENT', 'RGB']
    """How the texture effect is calculated (RGB and Curl need a RGB texture, else Gradient will be used instead)"""
    z_direction: Literal['POSITIVE', 'NEGATIVE', 'BOTH']
    """Effect in full or only positive/negative Z direction"""
    strength: Annotated[float, "step=10.0", "precision=3"]
    """Strength of force field"""
    linear_drag: Annotated[float, "step=10.0", "precision=3"]
    """Drag component proportional to velocity"""
    harmonic_damping: Annotated[float, "step=10.0", "precision=3"]
    """Damping of the harmonic force"""
    quadratic_drag: Annotated[float, "step=10.0", "precision=3"]
    """Drag component proportional to the square of velocity"""
    flow: Annotated[float, "step=10.0", "precision=3"]
    """Convert effector force into air flow velocity"""
    wind_factor: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """How much the force is reduced when acting parallel to a surface, e.g. cloth"""
    inflow: Annotated[float, "step=10.0", "precision=3"]
    """Inwards component of the vortex force"""
    size: Annotated[float, "step=1.0", "precision=3"]
    """Size of the turbulence"""
    rest_length: Annotated[float, "step=10.0", "precision=3"]
    """Rest length of the harmonic force"""
    falloff_power: Annotated[float, "step=10.0", "precision=3"]
    """How quickly strength falls off with distance from the force field"""
    distance_min: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]
    """Minimum distance for the field's falloff"""
    distance_max: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=1.0", "precision=3"]
    """Maximum distance for the field to work"""
    radial_min: Annotated[float, "step=10.0", "precision=3"]
    """Minimum radial distance for the field's falloff"""
    radial_max: Annotated[float, "step=10.0", "precision=3"]
    """Maximum radial distance for the field to work"""
    radial_falloff: Annotated[float, "step=10.0", "precision=3"]
    """Radial falloff power (real gravitational falloff = 2)"""
    texture_nabla: Annotated[float, "step=10.0", "precision=3"]
    """Defines size of derivative offset used for calculating gradient and curl"""
    noise: Annotated[float, "step=10.0", "precision=3"]
    """Amount of noise for the force strength"""
    seed: Annotated[int, "subtype='UNSIGNED'", "step=1"]
    """Seed of the noise"""
    use_min_distance: bool
    """Use a minimum distance for the field's falloff"""
    use_max_distance: bool
    """Use a maximum distance for the field to work"""
    use_radial_min: bool
    """Use a minimum radial distance for the field's falloff"""
    use_radial_max: bool
    """Use a maximum radial distance for the field to work"""
    use_object_coords: bool
    """Use object/global coordinates for texture"""
    use_global_coords: bool
    """Use effector/global coordinates for turbulence"""
    use_2d_force: bool
    """Apply force only in 2D"""
    use_root_coords: bool
    """Texture coordinates from root particle locations"""
    apply_to_location: bool
    """Affect particle's location"""
    apply_to_rotation: bool
    """Affect particle's dynamic rotation"""
    use_absorption: bool
    """Force gets absorbed by collision objects"""
    use_multiple_springs: bool
    """Every point is affected by multiple springs"""
    use_smoke_density: bool
    """Adjust force strength based on smoke density"""
    use_gravity_falloff: bool
    """Multiply force by 1/distance²"""
    texture: Annotated[Optional['Texture'], "is_animatable=False"]
    """Texture to use as force"""
    source_object: Annotated[Optional['Object'], "is_animatable=False"]
    """Select domain object of the smoke simulation"""
    guide_minimum: Annotated[float, "step=10.0", "precision=3"]
    """The distance from which particles are affected fully"""
    guide_free: Annotated[float, "step=10.0", "precision=3"]
    """Guide-free time from particle life's end"""
    use_guide_path_add: bool
    """Based on distance/falloff it adds a portion of the entire path"""
    use_guide_path_weight: bool
    """Use curve weights to influence the particle influence along the curve"""
    guide_clump_amount: Annotated[float, "step=10.0", "precision=3"]
    """Amount of clumping"""
    guide_clump_shape: Annotated[float, "step=10.0", "precision=3"]
    """Shape of clumping"""
    guide_kink_type: Literal['NONE', 'BRAID', 'CURL', 'RADIAL', 'ROLL', 'ROTATION', 'WAVE']
    """Type of periodic offset on the curve"""
    guide_kink_axis: Literal['X', 'Y', 'Z']
    """Which axis to use for offset"""
    guide_kink_frequency: Annotated[float, "step=10.0", "precision=3"]
    """The frequency of the offset (1/total length)"""
    guide_kink_shape: Annotated[float, "step=10.0", "precision=3"]
    """Adjust the offset to the beginning/end"""
    guide_kink_amplitude: Annotated[float, "step=10.0", "precision=3"]
    """The amplitude of the offset"""