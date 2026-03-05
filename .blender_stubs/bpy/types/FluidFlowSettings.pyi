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

    @property
    def density(self) -> Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=4"]:

        ...
    @density.setter
    def density(self, value: Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=4"]):
        ...
    @property
    def smoke_color(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:
        """Color of smoke"""
        ...
    @smoke_color.setter
    def smoke_color(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]):
        ...
    @property
    def fuel_amount(self) -> Annotated[float, "step=1.0", "precision=4"]:

        ...
    @fuel_amount.setter
    def fuel_amount(self, value: Annotated[float, "step=1.0", "precision=4"]):
        ...
    @property
    def temperature(self) -> Annotated[float, "step=1.0", "precision=1"]:
        """Temperature difference to ambient temperature"""
        ...
    @temperature.setter
    def temperature(self, value: Annotated[float, "step=1.0", "precision=1"]):
        ...
    @property
    def particle_system(self) -> Annotated[Optional['ParticleSystem'], "is_animatable=False"]:
        """Particle systems emitted from the object"""
        ...
    @particle_system.setter
    def particle_system(self, value: Annotated[Optional['ParticleSystem'], "is_animatable=False"]):
        ...
    @property
    def flow_type(self) -> Literal['SMOKE', 'BOTH', 'FIRE', 'LIQUID']:
        """Change type of fluid in the simulation"""
        ...
    @flow_type.setter
    def flow_type(self, value: Literal['SMOKE', 'BOTH', 'FIRE', 'LIQUID']):
        ...
    @property
    def flow_behavior(self) -> Literal['INFLOW', 'OUTFLOW', 'GEOMETRY']:
        """Change flow behavior in the simulation"""
        ...
    @flow_behavior.setter
    def flow_behavior(self, value: Literal['INFLOW', 'OUTFLOW', 'GEOMETRY']):
        ...
    @property
    def flow_source(self) -> Literal['NONE']:
        """Change how fluid is emitted"""
        ...
    @flow_source.setter
    def flow_source(self, value: Literal['NONE']):
        ...
    @property
    def use_absolute(self) -> bool:
        """Only allow given density value in emitter area and will not add up"""
        ...
    @use_absolute.setter
    def use_absolute(self, value: bool):
        ...
    @property
    def use_initial_velocity(self) -> bool:
        """Fluid has some initial velocity when it is emitted"""
        ...
    @use_initial_velocity.setter
    def use_initial_velocity(self, value: bool):
        ...
    @property
    def velocity_factor(self) -> Annotated[float, "step=0.05000000074505806", "precision=5"]:
        """Multiplier of source velocity passed to fluid (source velocity is non-zero only if object is moving)"""
        ...
    @velocity_factor.setter
    def velocity_factor(self, value: Annotated[float, "step=0.05000000074505806", "precision=5"]):
        ...
    @property
    def velocity_normal(self) -> Annotated[float, "step=0.05000000074505806", "precision=5"]:
        """Amount of normal directional velocity"""
        ...
    @velocity_normal.setter
    def velocity_normal(self, value: Annotated[float, "step=0.05000000074505806", "precision=5"]):
        ...
    @property
    def velocity_random(self) -> Annotated[float, "step=0.05000000074505806", "precision=5"]:
        """Amount of random velocity"""
        ...
    @velocity_random.setter
    def velocity_random(self, value: Annotated[float, "step=0.05000000074505806", "precision=5"]):
        ...
    @property
    def velocity_coord(self) -> Annotated[list[float], "subtype='VELOCITY'", "unit='VELOCITY'", "step=10.0", "precision=3"]:
        """Additional initial velocity in X, Y and Z direction (added to source velocity)"""
        ...
    @velocity_coord.setter
    def velocity_coord(self, value: Annotated[list[float], "subtype='VELOCITY'", "unit='VELOCITY'", "step=10.0", "precision=3"]):
        ...
    @property
    def volume_density(self) -> Annotated[float, "step=0.05000000074505806", "precision=5"]:
        """Controls fluid emission from within the mesh (higher value results in greater emissions from inside the mesh)"""
        ...
    @volume_density.setter
    def volume_density(self, value: Annotated[float, "step=0.05000000074505806", "precision=5"]):
        ...
    @property
    def surface_distance(self) -> Annotated[float, "step=0.05000000074505806", "precision=5"]:
        """Height (in domain grid units) of fluid emission above the mesh surface. Higher values result in emission further away from the mesh surface. If this value and the emitter size are smaller than the domain grid unit, fluid will not be created"""
        ...
    @surface_distance.setter
    def surface_distance(self, value: Annotated[float, "step=0.05000000074505806", "precision=5"]):
        ...
    @property
    def use_plane_init(self) -> bool:
        """Treat this object as a planar and unclosed mesh. Fluid will only be emitted from the mesh surface and based on the surface emission value."""
        ...
    @use_plane_init.setter
    def use_plane_init(self, value: bool):
        ...
    @property
    def particle_size(self) -> Annotated[float, "step=0.05000000074505806", "precision=5"]:
        """Particle size in simulation cells"""
        ...
    @particle_size.setter
    def particle_size(self, value: Annotated[float, "step=0.05000000074505806", "precision=5"]):
        ...
    @property
    def use_particle_size(self) -> bool:
        """Set particle size in simulation cells or use nearest cell"""
        ...
    @use_particle_size.setter
    def use_particle_size(self, value: bool):
        ...
    @property
    def use_inflow(self) -> bool:
        """Control when to apply fluid flow"""
        ...
    @use_inflow.setter
    def use_inflow(self, value: bool):
        ...
    @property
    def subframes(self) -> Annotated[int, "step=1"]:
        """Number of additional samples to take between frames to improve quality of fast moving flows"""
        ...
    @subframes.setter
    def subframes(self, value: Annotated[int, "step=1"]):
        ...
    @property
    def density_vertex_group(self) -> Annotated[str, "is_animatable=False"]:
        """Name of vertex group which determines surface emission rate"""
        ...
    @density_vertex_group.setter
    def density_vertex_group(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def use_texture(self) -> bool:
        """Use a texture to control emission strength"""
        ...
    @use_texture.setter
    def use_texture(self, value: bool):
        ...
    @property
    def texture_map_type(self) -> Literal['AUTO', 'UV']:
        """Texture mapping type"""
        ...
    @texture_map_type.setter
    def texture_map_type(self, value: Literal['AUTO', 'UV']):
        ...
    @property
    def uv_layer(self) -> Annotated[str, "is_animatable=False"]:
        """UV map name"""
        ...
    @uv_layer.setter
    def uv_layer(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def noise_texture(self) -> Annotated[Optional['Texture'], "is_animatable=False"]:
        """Texture that controls emission strength"""
        ...
    @noise_texture.setter
    def noise_texture(self, value: Annotated[Optional['Texture'], "is_animatable=False"]):
        ...
    @property
    def texture_size(self) -> Annotated[float, "step=0.05000000074505806", "precision=5"]:
        """Size of texture mapping"""
        ...
    @texture_size.setter
    def texture_size(self, value: Annotated[float, "step=0.05000000074505806", "precision=5"]):
        ...
    @property
    def texture_offset(self) -> Annotated[float, "step=0.05000000074505806", "precision=5"]:
        """Z-offset of texture mapping"""
        ...
    @texture_offset.setter
    def texture_offset(self, value: Annotated[float, "step=0.05000000074505806", "precision=5"]):
        ...