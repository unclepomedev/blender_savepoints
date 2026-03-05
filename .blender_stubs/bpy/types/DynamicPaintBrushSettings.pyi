# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.DynamicPaintBrushSettings.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .ColorRamp import ColorRamp
from .ParticleSystem import ParticleSystem

class DynamicPaintBrushSettings(bpy_struct):

    @property
    def paint_color(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:
        """Color of the paint"""
        ...
    @paint_color.setter
    def paint_color(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]):
        ...
    @property
    def paint_alpha(self) -> Annotated[float, "step=5.0", "precision=2"]:
        """Paint alpha"""
        ...
    @paint_alpha.setter
    def paint_alpha(self, value: Annotated[float, "step=5.0", "precision=2"]):
        ...
    @property
    def use_absolute_alpha(self) -> bool:
        """Only increase alpha value if paint alpha is higher than existing"""
        ...
    @use_absolute_alpha.setter
    def use_absolute_alpha(self, value: bool):
        ...
    @property
    def paint_wetness(self) -> Annotated[float, "step=5.0", "precision=2"]:
        """Paint wetness, visible in wetmap (some effects only affect wet paint)"""
        ...
    @paint_wetness.setter
    def paint_wetness(self, value: Annotated[float, "step=5.0", "precision=2"]):
        ...
    @property
    def use_paint_erase(self) -> bool:
        """Erase / remove paint instead of adding it"""
        ...
    @use_paint_erase.setter
    def use_paint_erase(self, value: bool):
        ...
    @property
    def wave_type(self) -> Annotated[Literal['CHANGE', 'DEPTH', 'FORCE', 'REFLECT'], "is_animatable=False"]:

        ...
    @wave_type.setter
    def wave_type(self, value: Annotated[Literal['CHANGE', 'DEPTH', 'FORCE', 'REFLECT'], "is_animatable=False"]):
        ...
    @property
    def wave_factor(self) -> Annotated[float, "step=5.0", "precision=2"]:
        """Multiplier for wave influence of this brush"""
        ...
    @wave_factor.setter
    def wave_factor(self, value: Annotated[float, "step=5.0", "precision=2"]):
        ...
    @property
    def wave_clamp(self) -> Annotated[float, "step=1.0", "precision=2"]:
        """Maximum level of surface intersection used to influence waves (use 0.0 to disable)"""
        ...
    @wave_clamp.setter
    def wave_clamp(self, value: Annotated[float, "step=1.0", "precision=2"]):
        ...
    @property
    def use_smudge(self) -> bool:
        """Make this brush to smudge existing paint as it moves"""
        ...
    @use_smudge.setter
    def use_smudge(self, value: bool):
        ...
    @property
    def smudge_strength(self) -> Annotated[float, "step=5.0", "precision=2"]:
        """Smudge effect strength"""
        ...
    @smudge_strength.setter
    def smudge_strength(self, value: Annotated[float, "step=5.0", "precision=2"]):
        ...
    @property
    def velocity_max(self) -> Annotated[float, "step=5.0", "precision=2"]:
        """Velocity considered as maximum influence (Blender units per frame)"""
        ...
    @velocity_max.setter
    def velocity_max(self, value: Annotated[float, "step=5.0", "precision=2"]):
        ...
    @property
    def use_velocity_alpha(self) -> bool:
        """Multiply brush influence by velocity color ramp alpha"""
        ...
    @use_velocity_alpha.setter
    def use_velocity_alpha(self, value: bool):
        ...
    @property
    def use_velocity_depth(self) -> bool:
        """Multiply brush intersection depth (displace, waves) by velocity ramp alpha"""
        ...
    @use_velocity_depth.setter
    def use_velocity_depth(self, value: bool):
        ...
    @property
    def use_velocity_color(self) -> bool:
        """Replace brush color by velocity color ramp"""
        ...
    @use_velocity_color.setter
    def use_velocity_color(self, value: bool):
        ...
    @property
    def paint_source(self) -> Annotated[Literal['PARTICLE_SYSTEM', 'POINT', 'DISTANCE', 'VOLUME_DISTANCE', 'VOLUME'], "is_animatable=False"]:

        ...
    @paint_source.setter
    def paint_source(self, value: Annotated[Literal['PARTICLE_SYSTEM', 'POINT', 'DISTANCE', 'VOLUME_DISTANCE', 'VOLUME'], "is_animatable=False"]):
        ...
    @property
    def paint_distance(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Maximum distance from brush to mesh surface to affect paint"""
        ...
    @paint_distance.setter
    def paint_distance(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def use_proximity_ramp_alpha(self) -> bool:
        """Only read color ramp alpha"""
        ...
    @use_proximity_ramp_alpha.setter
    def use_proximity_ramp_alpha(self, value: bool):
        ...
    @property
    def proximity_falloff(self) -> Annotated[Literal['SMOOTH', 'CONSTANT', 'RAMP'], "is_animatable=False"]:
        """Proximity falloff type"""
        ...
    @proximity_falloff.setter
    def proximity_falloff(self, value: Annotated[Literal['SMOOTH', 'CONSTANT', 'RAMP'], "is_animatable=False"]):
        ...
    @property
    def use_proximity_project(self) -> bool:
        """Brush is projected to canvas from defined direction within brush proximity"""
        ...
    @use_proximity_project.setter
    def use_proximity_project(self, value: bool):
        ...
    @property
    def ray_direction(self) -> Literal['CANVAS', 'BRUSH', 'Z_AXIS']:
        """Ray direction to use for projection (if brush object is located in that direction it's painted)"""
        ...
    @ray_direction.setter
    def ray_direction(self, value: Literal['CANVAS', 'BRUSH', 'Z_AXIS']):
        ...
    @property
    def invert_proximity(self) -> bool:
        """Proximity falloff is applied inside the volume"""
        ...
    @invert_proximity.setter
    def invert_proximity(self, value: bool):
        ...
    @property
    def use_negative_volume(self) -> bool:
        """Negate influence inside the volume"""
        ...
    @use_negative_volume.setter
    def use_negative_volume(self, value: bool):
        ...
    @property
    def particle_system(self) -> Annotated[Optional['ParticleSystem'], "is_animatable=False"]:
        """The particle system to paint with"""
        ...
    @particle_system.setter
    def particle_system(self, value: Annotated[Optional['ParticleSystem'], "is_animatable=False"]):
        ...
    @property
    def use_particle_radius(self) -> bool:
        """Use radius from particle settings"""
        ...
    @use_particle_radius.setter
    def use_particle_radius(self, value: bool):
        ...
    @property
    def solid_radius(self) -> Annotated[float, "step=5.0", "precision=3"]:
        """Radius that will be painted solid"""
        ...
    @solid_radius.setter
    def solid_radius(self, value: Annotated[float, "step=5.0", "precision=3"]):
        ...
    @property
    def smooth_radius(self) -> Annotated[float, "step=5.0", "precision=-1"]:
        """Smooth falloff added after solid radius"""
        ...
    @smooth_radius.setter
    def smooth_radius(self, value: Annotated[float, "step=5.0", "precision=-1"]):
        ...
    @property
    def paint_ramp(self) -> Annotated[Optional['ColorRamp'], "is_animatable=False"]:
        """Color ramp used to define proximity falloff"""
        ...
    @property
    def velocity_ramp(self) -> Annotated[Optional['ColorRamp'], "is_animatable=False"]:
        """Color ramp used to define brush velocity effect"""
        ...