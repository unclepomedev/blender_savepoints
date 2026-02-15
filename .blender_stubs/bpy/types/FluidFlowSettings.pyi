# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.FluidFlowSettings.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .ParticleSystem import ParticleSystem
from .Texture import Texture

class FluidFlowSettings(bpy_struct):

    density: Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=4"]

    smoke_color: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    """Color of smoke"""
    fuel_amount: Annotated[float, "step=1.0", "precision=4"]

    temperature: Annotated[float, "step=1.0", "precision=1"]
    """Temperature difference to ambient temperature"""
    particle_system: Annotated[Optional['ParticleSystem'], "is_animatable=False"]
    """Particle systems emitted from the object"""
    flow_type: Literal['SMOKE', 'BOTH', 'FIRE', 'LIQUID']
    """Change type of fluid in the simulation"""
    flow_behavior: Literal['INFLOW', 'OUTFLOW', 'GEOMETRY']
    """Change flow behavior in the simulation"""
    flow_source: Literal['NONE']
    """Change how fluid is emitted"""
    use_absolute: bool
    """Only allow given density value in emitter area and will not add up"""
    use_initial_velocity: bool
    """Fluid has some initial velocity when it is emitted"""
    velocity_factor: Annotated[float, "step=0.05000000074505806", "precision=5"]
    """Multiplier of source velocity passed to fluid (source velocity is non-zero only if object is moving)"""
    velocity_normal: Annotated[float, "step=0.05000000074505806", "precision=5"]
    """Amount of normal directional velocity"""
    velocity_random: Annotated[float, "step=0.05000000074505806", "precision=5"]
    """Amount of random velocity"""
    velocity_coord: Annotated[list[float], "subtype='VELOCITY'", "unit='VELOCITY'", "step=10.0", "precision=3"]
    """Additional initial velocity in X, Y and Z direction (added to source velocity)"""
    volume_density: Annotated[float, "step=0.05000000074505806", "precision=5"]
    """Controls fluid emission from within the mesh (higher value results in greater emissions from inside the mesh)"""
    surface_distance: Annotated[float, "step=0.05000000074505806", "precision=5"]
    """Height (in domain grid units) of fluid emission above the mesh surface. Higher values result in emission further away from the mesh surface. If this value and the emitter size are smaller than the domain grid unit, fluid will not be created"""
    use_plane_init: bool
    """Treat this object as a planar and unclosed mesh. Fluid will only be emitted from the mesh surface and based on the surface emission value."""
    particle_size: Annotated[float, "step=0.05000000074505806", "precision=5"]
    """Particle size in simulation cells"""
    use_particle_size: bool
    """Set particle size in simulation cells or use nearest cell"""
    use_inflow: bool
    """Control when to apply fluid flow"""
    subframes: Annotated[int, "step=1"]
    """Number of additional samples to take between frames to improve quality of fast moving flows"""
    density_vertex_group: Annotated[str, "is_animatable=False"]
    """Name of vertex group which determines surface emission rate"""
    use_texture: bool
    """Use a texture to control emission strength"""
    texture_map_type: Literal['AUTO', 'UV']
    """Texture mapping type"""
    uv_layer: Annotated[str, "is_animatable=False"]
    """UV map name"""
    noise_texture: Annotated[Optional['Texture'], "is_animatable=False"]
    """Texture that controls emission strength"""
    texture_size: Annotated[float, "step=0.05000000074505806", "precision=5"]
    """Size of texture mapping"""
    texture_offset: Annotated[float, "step=0.05000000074505806", "precision=5"]
    """Z-offset of texture mapping"""