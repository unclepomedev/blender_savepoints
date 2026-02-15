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
from .ColorRamp import ColorRamp
from .ParticleSystem import ParticleSystem
class DynamicPaintBrushSettings(bpy_struct):
    paint_color: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    """Color of the paint"""
    paint_alpha: Annotated[float, "step=5.0", "precision=2"]
    """Paint alpha"""
    use_absolute_alpha: bool
    """Only increase alpha value if paint alpha is higher than existing"""
    paint_wetness: Annotated[float, "step=5.0", "precision=2"]
    """Paint wetness, visible in wetmap (some effects only affect wet paint)"""
    use_paint_erase: bool
    """Erase / remove paint instead of adding it"""
    wave_type: Annotated[Literal['CHANGE', 'DEPTH', 'FORCE', 'REFLECT'], "is_animatable=False"]
    wave_factor: Annotated[float, "step=5.0", "precision=2"]
    """Multiplier for wave influence of this brush"""
    wave_clamp: Annotated[float, "step=1.0", "precision=2"]
    """Maximum level of surface intersection used to influence waves (use 0.0 to disable)"""
    use_smudge: bool
    """Make this brush to smudge existing paint as it moves"""
    smudge_strength: Annotated[float, "step=5.0", "precision=2"]
    """Smudge effect strength"""
    velocity_max: Annotated[float, "step=5.0", "precision=2"]
    """Velocity considered as maximum influence (Blender units per frame)"""
    use_velocity_alpha: bool
    """Multiply brush influence by velocity color ramp alpha"""
    use_velocity_depth: bool
    """Multiply brush intersection depth (displace, waves) by velocity ramp alpha"""
    use_velocity_color: bool
    """Replace brush color by velocity color ramp"""
    paint_source: Annotated[Literal['PARTICLE_SYSTEM', 'POINT', 'DISTANCE', 'VOLUME_DISTANCE', 'VOLUME'], "is_animatable=False"]
    paint_distance: Annotated[float, "step=10.0", "precision=3"]
    """Maximum distance from brush to mesh surface to affect paint"""
    use_proximity_ramp_alpha: bool
    """Only read color ramp alpha"""
    proximity_falloff: Annotated[Literal['SMOOTH', 'CONSTANT', 'RAMP'], "is_animatable=False"]
    """Proximity falloff type"""
    use_proximity_project: bool
    """Brush is projected to canvas from defined direction within brush proximity"""
    ray_direction: Literal['CANVAS', 'BRUSH', 'Z_AXIS']
    """Ray direction to use for projection (if brush object is located in that direction it's painted)"""
    invert_proximity: bool
    """Proximity falloff is applied inside the volume"""
    use_negative_volume: bool
    """Negate influence inside the volume"""
    particle_system: Annotated[Optional['ParticleSystem'], "is_animatable=False"]
    """The particle system to paint with"""
    use_particle_radius: bool
    """Use radius from particle settings"""
    solid_radius: Annotated[float, "step=5.0", "precision=3"]
    """Radius that will be painted solid"""
    smooth_radius: Annotated[float, "step=5.0", "precision=-1"]
    """Smooth falloff added after solid radius"""
    @property
    def paint_ramp(self) -> Annotated[Optional['ColorRamp'], "is_animatable=False"]:
        """Color ramp used to define proximity falloff"""
        ...
    @property
    def velocity_ramp(self) -> Annotated[Optional['ColorRamp'], "is_animatable=False"]:
        """Color ramp used to define brush velocity effect"""
        ...