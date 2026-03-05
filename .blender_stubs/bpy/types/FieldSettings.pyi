# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.FieldSettings.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .Object import Object
from .Texture import Texture

class FieldSettings(bpy_struct):

    @property
    def type(self) -> Literal['NONE', 'BOID', 'CHARGE', 'GUIDE', 'DRAG', 'FLUID_FLOW', 'FORCE', 'HARMONIC', 'LENNARDJ', 'MAGNET', 'TEXTURE', 'TURBULENCE', 'VORTEX', 'WIND']:
        """Type of field"""
        ...
    @type.setter
    def type(self, value: Literal['NONE', 'BOID', 'CHARGE', 'GUIDE', 'DRAG', 'FLUID_FLOW', 'FORCE', 'HARMONIC', 'LENNARDJ', 'MAGNET', 'TEXTURE', 'TURBULENCE', 'VORTEX', 'WIND']) -> None:
        ...
    @property
    def shape(self) -> Literal['POINT', 'LINE', 'PLANE', 'SURFACE', 'POINTS']:
        """Which direction is used to calculate the effector force"""
        ...
    @shape.setter
    def shape(self, value: Literal['POINT', 'LINE', 'PLANE', 'SURFACE', 'POINTS']) -> None:
        ...
    @property
    def falloff_type(self) -> Literal['CONE', 'SPHERE', 'TUBE']:

        ...
    @falloff_type.setter
    def falloff_type(self, value: Literal['CONE', 'SPHERE', 'TUBE']) -> None:
        ...
    @property
    def texture_mode(self) -> Literal['CURL', 'GRADIENT', 'RGB']:
        """How the texture effect is calculated (RGB and Curl need a RGB texture, else Gradient will be used instead)"""
        ...
    @texture_mode.setter
    def texture_mode(self, value: Literal['CURL', 'GRADIENT', 'RGB']) -> None:
        ...
    @property
    def z_direction(self) -> Literal['POSITIVE', 'NEGATIVE', 'BOTH']:
        """Effect in full or only positive/negative Z direction"""
        ...
    @z_direction.setter
    def z_direction(self, value: Literal['POSITIVE', 'NEGATIVE', 'BOTH']) -> None:
        ...
    @property
    def strength(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Strength of force field"""
        ...
    @strength.setter
    def strength(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def linear_drag(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Drag component proportional to velocity"""
        ...
    @linear_drag.setter
    def linear_drag(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def harmonic_damping(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Damping of the harmonic force"""
        ...
    @harmonic_damping.setter
    def harmonic_damping(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def quadratic_drag(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Drag component proportional to the square of velocity"""
        ...
    @quadratic_drag.setter
    def quadratic_drag(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def flow(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Convert effector force into air flow velocity"""
        ...
    @flow.setter
    def flow(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def wind_factor(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """How much the force is reduced when acting parallel to a surface, e.g. cloth"""
        ...
    @wind_factor.setter
    def wind_factor(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def inflow(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Inwards component of the vortex force"""
        ...
    @inflow.setter
    def inflow(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def size(self) -> Annotated[float, "step=1.0", "precision=3"]:
        """Size of the turbulence"""
        ...
    @size.setter
    def size(self, value: Annotated[float, "step=1.0", "precision=3"]) -> None:
        ...
    @property
    def rest_length(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Rest length of the harmonic force"""
        ...
    @rest_length.setter
    def rest_length(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def falloff_power(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """How quickly strength falls off with distance from the force field"""
        ...
    @falloff_power.setter
    def falloff_power(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def distance_min(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]:
        """Minimum distance for the field's falloff"""
        ...
    @distance_min.setter
    def distance_min(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def distance_max(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=1.0", "precision=3"]:
        """Maximum distance for the field to work"""
        ...
    @distance_max.setter
    def distance_max(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=1.0", "precision=3"]) -> None:
        ...
    @property
    def radial_min(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Minimum radial distance for the field's falloff"""
        ...
    @radial_min.setter
    def radial_min(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def radial_max(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Maximum radial distance for the field to work"""
        ...
    @radial_max.setter
    def radial_max(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def radial_falloff(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Radial falloff power (real gravitational falloff = 2)"""
        ...
    @radial_falloff.setter
    def radial_falloff(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def texture_nabla(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Defines size of derivative offset used for calculating gradient and curl"""
        ...
    @texture_nabla.setter
    def texture_nabla(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def noise(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Amount of noise for the force strength"""
        ...
    @noise.setter
    def noise(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def seed(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Seed of the noise"""
        ...
    @seed.setter
    def seed(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1"]) -> None:
        ...
    @property
    def use_min_distance(self) -> bool:
        """Use a minimum distance for the field's falloff"""
        ...
    @use_min_distance.setter
    def use_min_distance(self, value: bool) -> None:
        ...
    @property
    def use_max_distance(self) -> bool:
        """Use a maximum distance for the field to work"""
        ...
    @use_max_distance.setter
    def use_max_distance(self, value: bool) -> None:
        ...
    @property
    def use_radial_min(self) -> bool:
        """Use a minimum radial distance for the field's falloff"""
        ...
    @use_radial_min.setter
    def use_radial_min(self, value: bool) -> None:
        ...
    @property
    def use_radial_max(self) -> bool:
        """Use a maximum radial distance for the field to work"""
        ...
    @use_radial_max.setter
    def use_radial_max(self, value: bool) -> None:
        ...
    @property
    def use_object_coords(self) -> bool:
        """Use object/global coordinates for texture"""
        ...
    @use_object_coords.setter
    def use_object_coords(self, value: bool) -> None:
        ...
    @property
    def use_global_coords(self) -> bool:
        """Use effector/global coordinates for turbulence"""
        ...
    @use_global_coords.setter
    def use_global_coords(self, value: bool) -> None:
        ...
    @property
    def use_2d_force(self) -> bool:
        """Apply force only in 2D"""
        ...
    @use_2d_force.setter
    def use_2d_force(self, value: bool) -> None:
        ...
    @property
    def use_root_coords(self) -> bool:
        """Texture coordinates from root particle locations"""
        ...
    @use_root_coords.setter
    def use_root_coords(self, value: bool) -> None:
        ...
    @property
    def apply_to_location(self) -> bool:
        """Affect particle's location"""
        ...
    @apply_to_location.setter
    def apply_to_location(self, value: bool) -> None:
        ...
    @property
    def apply_to_rotation(self) -> bool:
        """Affect particle's dynamic rotation"""
        ...
    @apply_to_rotation.setter
    def apply_to_rotation(self, value: bool) -> None:
        ...
    @property
    def use_absorption(self) -> bool:
        """Force gets absorbed by collision objects"""
        ...
    @use_absorption.setter
    def use_absorption(self, value: bool) -> None:
        ...
    @property
    def use_multiple_springs(self) -> bool:
        """Every point is affected by multiple springs"""
        ...
    @use_multiple_springs.setter
    def use_multiple_springs(self, value: bool) -> None:
        ...
    @property
    def use_smoke_density(self) -> bool:
        """Adjust force strength based on smoke density"""
        ...
    @use_smoke_density.setter
    def use_smoke_density(self, value: bool) -> None:
        ...
    @property
    def use_gravity_falloff(self) -> bool:
        """Multiply force by 1/distance²"""
        ...
    @use_gravity_falloff.setter
    def use_gravity_falloff(self, value: bool) -> None:
        ...
    @property
    def texture(self) -> Annotated[Optional['Texture'], "is_animatable=False"]:
        """Texture to use as force"""
        ...
    @texture.setter
    def texture(self, value: Annotated[Optional['Texture'], "is_animatable=False"]) -> None:
        ...
    @property
    def source_object(self) -> Annotated[Optional['Object'], "is_animatable=False"]:
        """Select domain object of the smoke simulation"""
        ...
    @source_object.setter
    def source_object(self, value: Annotated[Optional['Object'], "is_animatable=False"]) -> None:
        ...
    @property
    def guide_minimum(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """The distance from which particles are affected fully"""
        ...
    @guide_minimum.setter
    def guide_minimum(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def guide_free(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Guide-free time from particle life's end"""
        ...
    @guide_free.setter
    def guide_free(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def use_guide_path_add(self) -> bool:
        """Based on distance/falloff it adds a portion of the entire path"""
        ...
    @use_guide_path_add.setter
    def use_guide_path_add(self, value: bool) -> None:
        ...
    @property
    def use_guide_path_weight(self) -> bool:
        """Use curve weights to influence the particle influence along the curve"""
        ...
    @use_guide_path_weight.setter
    def use_guide_path_weight(self, value: bool) -> None:
        ...
    @property
    def guide_clump_amount(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Amount of clumping"""
        ...
    @guide_clump_amount.setter
    def guide_clump_amount(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def guide_clump_shape(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Shape of clumping"""
        ...
    @guide_clump_shape.setter
    def guide_clump_shape(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def guide_kink_type(self) -> Literal['NONE', 'BRAID', 'CURL', 'RADIAL', 'ROLL', 'ROTATION', 'WAVE']:
        """Type of periodic offset on the curve"""
        ...
    @guide_kink_type.setter
    def guide_kink_type(self, value: Literal['NONE', 'BRAID', 'CURL', 'RADIAL', 'ROLL', 'ROTATION', 'WAVE']) -> None:
        ...
    @property
    def guide_kink_axis(self) -> Literal['X', 'Y', 'Z']:
        """Which axis to use for offset"""
        ...
    @guide_kink_axis.setter
    def guide_kink_axis(self, value: Literal['X', 'Y', 'Z']) -> None:
        ...
    @property
    def guide_kink_frequency(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """The frequency of the offset (1/total length)"""
        ...
    @guide_kink_frequency.setter
    def guide_kink_frequency(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def guide_kink_shape(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Adjust the offset to the beginning/end"""
        ...
    @guide_kink_shape.setter
    def guide_kink_shape(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def guide_kink_amplitude(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """The amplitude of the offset"""
        ...
    @guide_kink_amplitude.setter
    def guide_kink_amplitude(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...