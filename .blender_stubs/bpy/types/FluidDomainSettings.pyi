# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.FluidDomainSettings.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .Collection import Collection
from .ColorRamp import ColorRamp
from .EffectorWeights import EffectorWeights
from .Object import Object

class FluidDomainSettings(bpy_struct):

    @property
    def effector_weights(self) -> Annotated[Optional['EffectorWeights'], "is_animatable=False"]:

        ...
    @property
    def effector_group(self) -> Annotated[Optional['Collection'], "is_animatable=False"]:
        """Limit effectors to this collection"""
        ...
    @effector_group.setter
    def effector_group(self, value: Annotated[Optional['Collection'], "is_animatable=False"]) -> None:
        ...
    @property
    def fluid_group(self) -> Annotated[Optional['Collection'], "is_animatable=False"]:
        """Limit fluid objects to this collection"""
        ...
    @fluid_group.setter
    def fluid_group(self, value: Annotated[Optional['Collection'], "is_animatable=False"]) -> None:
        ...
    @property
    def force_collection(self) -> Annotated[Optional['Collection'], "is_animatable=False"]:
        """Limit forces to this collection"""
        ...
    @force_collection.setter
    def force_collection(self, value: Annotated[Optional['Collection'], "is_animatable=False"]) -> None:
        ...
    @property
    def density_grid(self) -> Annotated[list[float], "step=10.0", "precision=3"]:
        """Smoke density grid"""
        ...
    @property
    def velocity_grid(self) -> Annotated[list[float], "step=10.0", "precision=3"]:
        """Smoke velocity grid"""
        ...
    @property
    def flame_grid(self) -> Annotated[list[float], "step=10.0", "precision=3"]:
        """Smoke flame grid"""
        ...
    @property
    def color_grid(self) -> Annotated[list[float], "step=10.0", "precision=3"]:
        """Smoke color grid"""
        ...
    @property
    def heat_grid(self) -> Annotated[list[float], "step=10.0", "precision=3"]:
        """Smoke heat grid"""
        ...
    @property
    def temperature_grid(self) -> Annotated[list[float], "step=10.0", "precision=3"]:
        """Smoke temperature grid, range 0 to 1 represents 0 to 1000K"""
        ...
    @property
    def start_point(self) -> Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]:
        """Start point"""
        ...
    @property
    def cell_size(self) -> Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]:
        """Cell Size"""
        ...
    @property
    def domain_resolution(self) -> Annotated[list[int], "subtype='XYZ'", "step=1"]:
        """Smoke Grid Resolution"""
        ...
    @property
    def additional_res(self) -> Annotated[int, "step=1"]:
        """Maximum number of additional cells"""
        ...
    @additional_res.setter
    def additional_res(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def adapt_margin(self) -> Annotated[int, "step=1"]:
        """Margin added around fluid to minimize boundary interference"""
        ...
    @adapt_margin.setter
    def adapt_margin(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def adapt_threshold(self) -> Annotated[float, "step=0.0020000000949949026", "precision=6"]:
        """Minimum amount of fluid grid values (smoke density, fuel and heat) a cell can contain, before it is considered empty"""
        ...
    @adapt_threshold.setter
    def adapt_threshold(self, value: Annotated[float, "step=0.0020000000949949026", "precision=6"]) -> None:
        ...
    @property
    def use_adaptive_domain(self) -> Annotated[bool, "is_animatable=False"]:
        """Adapt simulation resolution and size to fluid"""
        ...
    @use_adaptive_domain.setter
    def use_adaptive_domain(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def resolution_max(self) -> Annotated[int, "step=2", "is_animatable=False"]:
        """Resolution used for the fluid domain. Value corresponds to the longest domain side (resolution for other domain sides is calculated automatically)."""
        ...
    @resolution_max.setter
    def resolution_max(self, value: Annotated[int, "step=2", "is_animatable=False"]) -> None:
        ...
    @property
    def use_collision_border_front(self) -> bool:
        """Enable collisions with front domain border"""
        ...
    @use_collision_border_front.setter
    def use_collision_border_front(self, value: bool) -> None:
        ...
    @property
    def use_collision_border_back(self) -> bool:
        """Enable collisions with back domain border"""
        ...
    @use_collision_border_back.setter
    def use_collision_border_back(self, value: bool) -> None:
        ...
    @property
    def use_collision_border_right(self) -> bool:
        """Enable collisions with right domain border"""
        ...
    @use_collision_border_right.setter
    def use_collision_border_right(self, value: bool) -> None:
        ...
    @property
    def use_collision_border_left(self) -> bool:
        """Enable collisions with left domain border"""
        ...
    @use_collision_border_left.setter
    def use_collision_border_left(self, value: bool) -> None:
        ...
    @property
    def use_collision_border_top(self) -> bool:
        """Enable collisions with top domain border"""
        ...
    @use_collision_border_top.setter
    def use_collision_border_top(self, value: bool) -> None:
        ...
    @property
    def use_collision_border_bottom(self) -> bool:
        """Enable collisions with bottom domain border"""
        ...
    @use_collision_border_bottom.setter
    def use_collision_border_bottom(self, value: bool) -> None:
        ...
    @property
    def gravity(self) -> Annotated[list[float], "subtype='ACCELERATION'", "unit='ACCELERATION'", "step=10.0", "precision=3"]:
        """Gravity in X, Y and Z direction"""
        ...
    @gravity.setter
    def gravity(self, value: Annotated[list[float], "subtype='ACCELERATION'", "unit='ACCELERATION'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def domain_type(self) -> Annotated[Literal['GAS', 'LIQUID'], "is_animatable=False"]:
        """Change domain type of the simulation"""
        ...
    @domain_type.setter
    def domain_type(self, value: Annotated[Literal['GAS', 'LIQUID'], "is_animatable=False"]) -> None:
        ...
    @property
    def delete_in_obstacle(self) -> bool:
        """Delete fluid inside obstacles"""
        ...
    @delete_in_obstacle.setter
    def delete_in_obstacle(self, value: bool) -> None:
        ...
    @property
    def alpha(self) -> Annotated[float, "step=0.019999999552965164", "precision=5"]:
        """Buoyant force based on smoke density (higher value results in faster rising smoke)"""
        ...
    @alpha.setter
    def alpha(self, value: Annotated[float, "step=0.019999999552965164", "precision=5"]) -> None:
        ...
    @property
    def beta(self) -> Annotated[float, "step=0.019999999552965164", "precision=5"]:
        """Buoyant force based on smoke heat (higher value results in faster rising smoke)"""
        ...
    @beta.setter
    def beta(self, value: Annotated[float, "step=0.019999999552965164", "precision=5"]) -> None:
        ...
    @property
    def dissolve_speed(self) -> Annotated[int, "step=1"]:
        """Determine how quickly the smoke dissolves (lower value makes smoke disappear faster)"""
        ...
    @dissolve_speed.setter
    def dissolve_speed(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def vorticity(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Amount of turbulence and rotation in smoke"""
        ...
    @vorticity.setter
    def vorticity(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def highres_sampling(self) -> Literal['FULLSAMPLE', 'LINEAR', 'NEAREST']:
        """Method for sampling the high resolution flow"""
        ...
    @highres_sampling.setter
    def highres_sampling(self, value: Literal['FULLSAMPLE', 'LINEAR', 'NEAREST']) -> None:
        ...
    @property
    def use_dissolve_smoke(self) -> bool:
        """Let smoke disappear over time"""
        ...
    @use_dissolve_smoke.setter
    def use_dissolve_smoke(self, value: bool) -> None:
        ...
    @property
    def use_dissolve_smoke_log(self) -> bool:
        """Dissolve smoke in a logarithmic fashion. Dissolves quickly at first, but lingers longer."""
        ...
    @use_dissolve_smoke_log.setter
    def use_dissolve_smoke_log(self, value: bool) -> None:
        ...
    @property
    def burning_rate(self) -> Annotated[float, "step=1.0", "precision=5"]:
        """Speed of the burning reaction (higher value results in smaller flames)"""
        ...
    @burning_rate.setter
    def burning_rate(self, value: Annotated[float, "step=1.0", "precision=5"]) -> None:
        ...
    @property
    def flame_smoke(self) -> Annotated[float, "step=1.0", "precision=5"]:
        """Amount of smoke created by burning fuel"""
        ...
    @flame_smoke.setter
    def flame_smoke(self, value: Annotated[float, "step=1.0", "precision=5"]) -> None:
        ...
    @property
    def flame_vorticity(self) -> Annotated[float, "step=1.0", "precision=5"]:
        """Additional vorticity for the flames"""
        ...
    @flame_vorticity.setter
    def flame_vorticity(self, value: Annotated[float, "step=1.0", "precision=5"]) -> None:
        ...
    @property
    def flame_ignition(self) -> Annotated[float, "step=1.0", "precision=5"]:
        """Minimum temperature of the flames (higher value results in faster rising flames)"""
        ...
    @flame_ignition.setter
    def flame_ignition(self, value: Annotated[float, "step=1.0", "precision=5"]) -> None:
        ...
    @property
    def flame_max_temp(self) -> Annotated[float, "step=1.0", "precision=5"]:
        """Maximum temperature of the flames (higher value results in faster rising flames)"""
        ...
    @flame_max_temp.setter
    def flame_max_temp(self, value: Annotated[float, "step=1.0", "precision=5"]) -> None:
        ...
    @property
    def flame_smoke_color(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:
        """Color of smoke emitted from burning fuel"""
        ...
    @flame_smoke_color.setter
    def flame_smoke_color(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def noise_strength(self) -> Annotated[float, "step=1.0", "precision=2"]:
        """Strength of noise"""
        ...
    @noise_strength.setter
    def noise_strength(self, value: Annotated[float, "step=1.0", "precision=2"]) -> None:
        ...
    @property
    def noise_pos_scale(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Scale of noise (higher value results in larger vortices)"""
        ...
    @noise_pos_scale.setter
    def noise_pos_scale(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def noise_time_anim(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Animation time of noise"""
        ...
    @noise_time_anim.setter
    def noise_time_anim(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def noise_scale(self) -> Annotated[int, "step=1", "is_animatable=False"]:
        """The noise simulation is scaled up by this factor (compared to the base resolution of the domain)"""
        ...
    @noise_scale.setter
    def noise_scale(self, value: Annotated[int, "step=1", "is_animatable=False"]) -> None:
        ...
    @property
    def use_noise(self) -> Annotated[bool, "is_animatable=False"]:
        """Enable fluid noise (using amplification)"""
        ...
    @use_noise.setter
    def use_noise(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def simulation_method(self) -> Annotated[Literal['FLIP', 'APIC'], "is_animatable=False"]:
        """Change the underlying simulation method"""
        ...
    @simulation_method.setter
    def simulation_method(self, value: Annotated[Literal['FLIP', 'APIC'], "is_animatable=False"]) -> None:
        ...
    @property
    def flip_ratio(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """PIC/FLIP Ratio. A value of 1.0 will result in a completely FLIP based simulation. Use a lower value for simulations which should produce smaller splashes."""
        ...
    @flip_ratio.setter
    def flip_ratio(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def particle_randomness(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Randomness factor for particle sampling"""
        ...
    @particle_randomness.setter
    def particle_randomness(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def particle_number(self) -> Annotated[int, "step=1"]:
        """Particle number factor (higher value results in more particles)"""
        ...
    @particle_number.setter
    def particle_number(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def particle_min(self) -> Annotated[int, "step=1"]:
        """Minimum number of particles per cell (ensures that each cell has at least this amount of particles)"""
        ...
    @particle_min.setter
    def particle_min(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def particle_max(self) -> Annotated[int, "step=1"]:
        """Maximum number of particles per cell (ensures that each cell has at most this amount of particles)"""
        ...
    @particle_max.setter
    def particle_max(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def particle_radius(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Particle radius factor. Increase this value if the simulation appears to leak volume, decrease it if the simulation seems to gain volume."""
        ...
    @particle_radius.setter
    def particle_radius(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def particle_band_width(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Particle (narrow) band width (higher value results in thicker band and more particles)"""
        ...
    @particle_band_width.setter
    def particle_band_width(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def use_flip_particles(self) -> Annotated[bool, "is_animatable=False"]:
        """Create liquid particle system"""
        ...
    @use_flip_particles.setter
    def use_flip_particles(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def use_fractions(self) -> Annotated[bool, "is_animatable=False"]:
        """Fractional obstacles improve and smoothen the fluid-obstacle boundary"""
        ...
    @use_fractions.setter
    def use_fractions(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def fractions_threshold(self) -> Annotated[float, "step=0.05000000074505806", "precision=-1"]:
        """Determines how much fluid is allowed in an obstacle cell (higher values will tag a boundary cell as an obstacle easier and reduce the boundary smoothening effect)"""
        ...
    @fractions_threshold.setter
    def fractions_threshold(self, value: Annotated[float, "step=0.05000000074505806", "precision=-1"]) -> None:
        ...
    @property
    def fractions_distance(self) -> Annotated[float, "step=0.10000000149011612", "precision=-1"]:
        """Determines how far apart fluid and obstacle are (higher values will result in fluid being further away from obstacles, smaller values will let fluid move towards the inside of obstacles)"""
        ...
    @fractions_distance.setter
    def fractions_distance(self, value: Annotated[float, "step=0.10000000149011612", "precision=-1"]) -> None:
        ...
    @property
    def sys_particle_maximum(self) -> Annotated[int, "step=1"]:
        """Maximum number of fluid particles that are allowed in this simulation"""
        ...
    @sys_particle_maximum.setter
    def sys_particle_maximum(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def use_viscosity(self) -> bool:
        """Simulate fluids with high viscosity using a special solver"""
        ...
    @use_viscosity.setter
    def use_viscosity(self, value: bool) -> None:
        ...
    @property
    def viscosity_value(self) -> Annotated[float, "step=1.0", "precision=3"]:
        """Viscosity of liquid (higher values result in more viscous fluids, a value of 0 will still apply some viscosity)"""
        ...
    @viscosity_value.setter
    def viscosity_value(self, value: Annotated[float, "step=1.0", "precision=3"]) -> None:
        ...
    @property
    def use_diffusion(self) -> Annotated[bool, "is_animatable=False"]:
        """Enable fluid diffusion settings (e.g. viscosity, surface tension)"""
        ...
    @use_diffusion.setter
    def use_diffusion(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def surface_tension(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Surface tension of liquid (higher value results in greater hydrophobic behavior)"""
        ...
    @surface_tension.setter
    def surface_tension(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def viscosity_base(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Viscosity setting: value that is multiplied by 10 to the power of (exponent*-1)"""
        ...
    @viscosity_base.setter
    def viscosity_base(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def viscosity_exponent(self) -> Annotated[int, "step=1"]:
        """Negative exponent for the viscosity value (to simplify entering small values e.g. 5*10^-6)"""
        ...
    @viscosity_exponent.setter
    def viscosity_exponent(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def mesh_concave_upper(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Upper mesh concavity bound (high values tend to smoothen and fill out concave regions)"""
        ...
    @mesh_concave_upper.setter
    def mesh_concave_upper(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def mesh_concave_lower(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Lower mesh concavity bound (high values tend to smoothen and fill out concave regions)"""
        ...
    @mesh_concave_lower.setter
    def mesh_concave_lower(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def mesh_smoothen_pos(self) -> Annotated[int, "step=1"]:
        """Positive mesh smoothening"""
        ...
    @mesh_smoothen_pos.setter
    def mesh_smoothen_pos(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def mesh_smoothen_neg(self) -> Annotated[int, "step=1"]:
        """Negative mesh smoothening"""
        ...
    @mesh_smoothen_neg.setter
    def mesh_smoothen_neg(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def mesh_scale(self) -> Annotated[int, "step=1", "is_animatable=False"]:
        """The mesh simulation is scaled up by this factor (compared to the base resolution of the domain). For best meshing, it is recommended to adjust the mesh particle radius alongside this value."""
        ...
    @mesh_scale.setter
    def mesh_scale(self, value: Annotated[int, "step=1", "is_animatable=False"]) -> None:
        ...
    @property
    def mesh_generator(self) -> Literal['IMPROVED', 'UNION']:
        """Which particle level set generator to use"""
        ...
    @mesh_generator.setter
    def mesh_generator(self, value: Literal['IMPROVED', 'UNION']) -> None:
        ...
    @property
    def use_mesh(self) -> Annotated[bool, "is_animatable=False"]:
        """Enable fluid mesh (using amplification)"""
        ...
    @use_mesh.setter
    def use_mesh(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def use_speed_vectors(self) -> Annotated[bool, "is_animatable=False"]:
        """Caches velocities of mesh vertices. These will be used (automatically) when rendering with motion blur enabled."""
        ...
    @use_speed_vectors.setter
    def use_speed_vectors(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def mesh_particle_radius(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Particle radius factor (higher value results in larger (meshed) particles). Needs to be adjusted after changing the mesh scale."""
        ...
    @mesh_particle_radius.setter
    def mesh_particle_radius(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def sndparticle_potential_min_wavecrest(self) -> Annotated[float, "step=100.0", "precision=3"]:
        """Lower clamping threshold for marking fluid cells as wave crests (lower value results in more marked cells)"""
        ...
    @sndparticle_potential_min_wavecrest.setter
    def sndparticle_potential_min_wavecrest(self, value: Annotated[float, "step=100.0", "precision=3"]) -> None:
        ...
    @property
    def sndparticle_potential_max_wavecrest(self) -> Annotated[float, "step=100.0", "precision=3"]:
        """Upper clamping threshold for marking fluid cells as wave crests (higher value results in less marked cells)"""
        ...
    @sndparticle_potential_max_wavecrest.setter
    def sndparticle_potential_max_wavecrest(self, value: Annotated[float, "step=100.0", "precision=3"]) -> None:
        ...
    @property
    def sndparticle_potential_min_trappedair(self) -> Annotated[float, "step=100.0", "precision=3"]:
        """Lower clamping threshold for marking fluid cells where air is trapped (lower value results in more marked cells)"""
        ...
    @sndparticle_potential_min_trappedair.setter
    def sndparticle_potential_min_trappedair(self, value: Annotated[float, "step=100.0", "precision=3"]) -> None:
        ...
    @property
    def sndparticle_potential_max_trappedair(self) -> Annotated[float, "step=100.0", "precision=3"]:
        """Upper clamping threshold for marking fluid cells where air is trapped (higher value results in less marked cells)"""
        ...
    @sndparticle_potential_max_trappedair.setter
    def sndparticle_potential_max_trappedair(self, value: Annotated[float, "step=100.0", "precision=3"]) -> None:
        ...
    @property
    def sndparticle_potential_min_energy(self) -> Annotated[float, "step=100.0", "precision=3"]:
        """Lower clamping threshold that indicates the fluid speed where cells start to emit particles (lower values result in generally more particles)"""
        ...
    @sndparticle_potential_min_energy.setter
    def sndparticle_potential_min_energy(self, value: Annotated[float, "step=100.0", "precision=3"]) -> None:
        ...
    @property
    def sndparticle_potential_max_energy(self) -> Annotated[float, "step=100.0", "precision=3"]:
        """Upper clamping threshold that indicates the fluid speed where cells no longer emit more particles (higher value results in generally less particles)"""
        ...
    @sndparticle_potential_max_energy.setter
    def sndparticle_potential_max_energy(self, value: Annotated[float, "step=100.0", "precision=3"]) -> None:
        ...
    @property
    def sndparticle_sampling_wavecrest(self) -> Annotated[int, "step=1"]:
        """Maximum number of particles generated per wave crest cell per frame"""
        ...
    @sndparticle_sampling_wavecrest.setter
    def sndparticle_sampling_wavecrest(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def sndparticle_sampling_trappedair(self) -> Annotated[int, "step=1"]:
        """Maximum number of particles generated per trapped air cell per frame"""
        ...
    @sndparticle_sampling_trappedair.setter
    def sndparticle_sampling_trappedair(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def sndparticle_bubble_buoyancy(self) -> Annotated[float, "step=10.0", "precision=2"]:
        """Amount of buoyancy force that rises bubbles (high value results in bubble movement mainly upwards)"""
        ...
    @sndparticle_bubble_buoyancy.setter
    def sndparticle_bubble_buoyancy(self, value: Annotated[float, "step=10.0", "precision=2"]) -> None:
        ...
    @property
    def sndparticle_bubble_drag(self) -> Annotated[float, "step=10.0", "precision=2"]:
        """Amount of drag force that moves bubbles along with the fluid (high value results in bubble movement mainly along with the fluid)"""
        ...
    @sndparticle_bubble_drag.setter
    def sndparticle_bubble_drag(self, value: Annotated[float, "step=10.0", "precision=2"]) -> None:
        ...
    @property
    def sndparticle_life_min(self) -> Annotated[float, "step=100.0", "precision=1"]:
        """Lowest possible particle lifetime"""
        ...
    @sndparticle_life_min.setter
    def sndparticle_life_min(self, value: Annotated[float, "step=100.0", "precision=1"]) -> None:
        ...
    @property
    def sndparticle_life_max(self) -> Annotated[float, "step=100.0", "precision=1"]:
        """Highest possible particle lifetime"""
        ...
    @sndparticle_life_max.setter
    def sndparticle_life_max(self, value: Annotated[float, "step=100.0", "precision=1"]) -> None:
        ...
    @property
    def sndparticle_boundary(self) -> Literal['DELETE', 'PUSHOUT']:
        """How particles that left the domain are treated"""
        ...
    @sndparticle_boundary.setter
    def sndparticle_boundary(self, value: Literal['DELETE', 'PUSHOUT']) -> None:
        ...
    @property
    def sndparticle_combined_export(self) -> Literal['OFF', 'SPRAY_FOAM', 'SPRAY_BUBBLES', 'FOAM_BUBBLES', 'SPRAY_FOAM_BUBBLES']:
        """Determines which particle systems are created from secondary particles"""
        ...
    @sndparticle_combined_export.setter
    def sndparticle_combined_export(self, value: Literal['OFF', 'SPRAY_FOAM', 'SPRAY_BUBBLES', 'FOAM_BUBBLES', 'SPRAY_FOAM_BUBBLES']) -> None:
        ...
    @property
    def sndparticle_potential_radius(self) -> Annotated[int, "step=1"]:
        """Radius to compute potential for each cell (higher values are slower but create smoother potential grids)"""
        ...
    @sndparticle_potential_radius.setter
    def sndparticle_potential_radius(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def sndparticle_update_radius(self) -> Annotated[int, "step=1"]:
        """Radius to compute position update for each particle (higher values are slower but particles move less chaotic)"""
        ...
    @sndparticle_update_radius.setter
    def sndparticle_update_radius(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def particle_scale(self) -> Annotated[int, "step=1", "is_animatable=False"]:
        """The particle simulation is scaled up by this factor (compared to the base resolution of the domain)"""
        ...
    @particle_scale.setter
    def particle_scale(self, value: Annotated[int, "step=1", "is_animatable=False"]) -> None:
        ...
    @property
    def use_spray_particles(self) -> Annotated[bool, "is_animatable=False"]:
        """Create spray particle system"""
        ...
    @use_spray_particles.setter
    def use_spray_particles(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def use_bubble_particles(self) -> Annotated[bool, "is_animatable=False"]:
        """Create bubble particle system"""
        ...
    @use_bubble_particles.setter
    def use_bubble_particles(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def use_foam_particles(self) -> Annotated[bool, "is_animatable=False"]:
        """Create foam particle system"""
        ...
    @use_foam_particles.setter
    def use_foam_particles(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def use_tracer_particles(self) -> Annotated[bool, "is_animatable=False"]:
        """Create tracer particle system"""
        ...
    @use_tracer_particles.setter
    def use_tracer_particles(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def guide_alpha(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Guiding weight (higher value results in greater lag)"""
        ...
    @guide_alpha.setter
    def guide_alpha(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def guide_beta(self) -> Annotated[int, "step=1"]:
        """Guiding size (higher value results in larger vortices)"""
        ...
    @guide_beta.setter
    def guide_beta(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def guide_vel_factor(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Guiding velocity factor (higher value results in greater guiding velocities)"""
        ...
    @guide_vel_factor.setter
    def guide_vel_factor(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def guide_source(self) -> Literal['DOMAIN', 'EFFECTOR']:
        """Choose where to get guiding velocities from"""
        ...
    @guide_source.setter
    def guide_source(self, value: Literal['DOMAIN', 'EFFECTOR']) -> None:
        ...
    @property
    def guide_parent(self) -> Annotated[Optional['Object'], "is_animatable=False"]:
        """Use velocities from this object for the guiding effect (object needs to have fluid modifier and be of type domain))"""
        ...
    @guide_parent.setter
    def guide_parent(self, value: Annotated[Optional['Object'], "is_animatable=False"]) -> None:
        ...
    @property
    def use_guide(self) -> Annotated[bool, "is_animatable=False"]:
        """Enable fluid guiding"""
        ...
    @use_guide.setter
    def use_guide(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def cache_frame_start(self) -> Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1", "is_animatable=False"]:
        """Frame on which the simulation starts (first frame baked)"""
        ...
    @cache_frame_start.setter
    def cache_frame_start(self, value: Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1", "is_animatable=False"]) -> None:
        ...
    @property
    def cache_frame_end(self) -> Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1", "is_animatable=False"]:
        """Frame on which the simulation stops (last frame baked)"""
        ...
    @cache_frame_end.setter
    def cache_frame_end(self, value: Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1", "is_animatable=False"]) -> None:
        ...
    @property
    def cache_frame_offset(self) -> Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1", "is_animatable=False"]:
        """Frame offset that is used when loading the simulation from the cache. It is not considered when baking the simulation, only when loading it."""
        ...
    @cache_frame_offset.setter
    def cache_frame_offset(self, value: Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1", "is_animatable=False"]) -> None:
        ...
    @property
    def cache_frame_pause_data(self) -> Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1"]:

        ...
    @cache_frame_pause_data.setter
    def cache_frame_pause_data(self, value: Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1"]) -> None:
        ...
    @property
    def cache_frame_pause_noise(self) -> Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1"]:

        ...
    @cache_frame_pause_noise.setter
    def cache_frame_pause_noise(self, value: Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1"]) -> None:
        ...
    @property
    def cache_frame_pause_mesh(self) -> Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1"]:

        ...
    @cache_frame_pause_mesh.setter
    def cache_frame_pause_mesh(self, value: Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1"]) -> None:
        ...
    @property
    def cache_frame_pause_particles(self) -> Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1"]:

        ...
    @cache_frame_pause_particles.setter
    def cache_frame_pause_particles(self, value: Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1"]) -> None:
        ...
    @property
    def cache_frame_pause_guide(self) -> Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1"]:

        ...
    @cache_frame_pause_guide.setter
    def cache_frame_pause_guide(self, value: Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1"]) -> None:
        ...
    @property
    def cache_mesh_format(self) -> Annotated[Literal['UNI', 'OPENVDB', 'RAW'], "is_animatable=False"]:
        """Select the file format to be used for caching surface data"""
        ...
    @cache_mesh_format.setter
    def cache_mesh_format(self, value: Annotated[Literal['UNI', 'OPENVDB', 'RAW'], "is_animatable=False"]) -> None:
        ...
    @property
    def cache_data_format(self) -> Annotated[Literal['UNI', 'OPENVDB', 'RAW'], "is_animatable=False"]:
        """Select the file format to be used for caching volumetric data"""
        ...
    @cache_data_format.setter
    def cache_data_format(self, value: Annotated[Literal['UNI', 'OPENVDB', 'RAW'], "is_animatable=False"]) -> None:
        ...
    @property
    def cache_particle_format(self) -> Annotated[Literal['UNI', 'OPENVDB', 'RAW'], "is_animatable=False"]:
        """Select the file format to be used for caching particle data"""
        ...
    @cache_particle_format.setter
    def cache_particle_format(self, value: Annotated[Literal['UNI', 'OPENVDB', 'RAW'], "is_animatable=False"]) -> None:
        ...
    @property
    def cache_noise_format(self) -> Annotated[Literal['UNI', 'OPENVDB', 'RAW'], "is_animatable=False"]:
        """Select the file format to be used for caching noise data"""
        ...
    @cache_noise_format.setter
    def cache_noise_format(self, value: Annotated[Literal['UNI', 'OPENVDB', 'RAW'], "is_animatable=False"]) -> None:
        ...
    @property
    def cache_type(self) -> Annotated[Literal['REPLAY', 'MODULAR', 'ALL'], "is_animatable=False"]:
        """Change the cache type of the simulation"""
        ...
    @cache_type.setter
    def cache_type(self, value: Annotated[Literal['REPLAY', 'MODULAR', 'ALL'], "is_animatable=False"]) -> None:
        ...
    @property
    def cache_resumable(self) -> Annotated[bool, "is_animatable=False"]:
        """Additional data will be saved so that the bake jobs can be resumed after pausing. Because more data will be written to disk it is recommended to avoid enabling this option when baking at high resolutions."""
        ...
    @cache_resumable.setter
    def cache_resumable(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def cache_directory(self) -> Annotated[str, "subtype='DIR_PATH'", "is_animatable=False"]:
        """Directory that contains fluid cache files"""
        ...
    @cache_directory.setter
    def cache_directory(self, value: Annotated[str, "subtype='DIR_PATH'", "is_animatable=False"]) -> None:
        ...
    @property
    def is_cache_baking_data(self) -> bool:

        ...
    @is_cache_baking_data.setter
    def is_cache_baking_data(self, value: bool) -> None:
        ...
    @property
    def has_cache_baked_data(self) -> bool:

        ...
    @has_cache_baked_data.setter
    def has_cache_baked_data(self, value: bool) -> None:
        ...
    @property
    def is_cache_baking_noise(self) -> bool:

        ...
    @is_cache_baking_noise.setter
    def is_cache_baking_noise(self, value: bool) -> None:
        ...
    @property
    def has_cache_baked_noise(self) -> bool:

        ...
    @has_cache_baked_noise.setter
    def has_cache_baked_noise(self, value: bool) -> None:
        ...
    @property
    def is_cache_baking_mesh(self) -> bool:

        ...
    @is_cache_baking_mesh.setter
    def is_cache_baking_mesh(self, value: bool) -> None:
        ...
    @property
    def has_cache_baked_mesh(self) -> bool:

        ...
    @has_cache_baked_mesh.setter
    def has_cache_baked_mesh(self, value: bool) -> None:
        ...
    @property
    def is_cache_baking_particles(self) -> bool:

        ...
    @is_cache_baking_particles.setter
    def is_cache_baking_particles(self, value: bool) -> None:
        ...
    @property
    def has_cache_baked_particles(self) -> bool:

        ...
    @has_cache_baked_particles.setter
    def has_cache_baked_particles(self, value: bool) -> None:
        ...
    @property
    def is_cache_baking_guide(self) -> bool:

        ...
    @is_cache_baking_guide.setter
    def is_cache_baking_guide(self, value: bool) -> None:
        ...
    @property
    def has_cache_baked_guide(self) -> bool:

        ...
    @has_cache_baked_guide.setter
    def has_cache_baked_guide(self, value: bool) -> None:
        ...
    @property
    def is_cache_baking_any(self) -> bool:

        ...
    @is_cache_baking_any.setter
    def is_cache_baking_any(self, value: bool) -> None:
        ...
    @property
    def has_cache_baked_any(self) -> bool:

        ...
    @has_cache_baked_any.setter
    def has_cache_baked_any(self, value: bool) -> None:
        ...
    @property
    def export_manta_script(self) -> Annotated[bool, "is_animatable=False"]:
        """Generate and export Mantaflow script from current domain settings during bake. This is only needed if you plan to analyze the cache (e.g. view grids, velocity vectors, particles) in Mantaflow directly (outside of Blender) after baking the simulation."""
        ...
    @export_manta_script.setter
    def export_manta_script(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def openvdb_cache_compress_type(self) -> Literal['ZIP', 'NONE']:
        """Compression method to be used"""
        ...
    @openvdb_cache_compress_type.setter
    def openvdb_cache_compress_type(self, value: Literal['ZIP', 'NONE']) -> None:
        ...
    @property
    def openvdb_data_depth(self) -> Literal['NONE']:
        """Bit depth for fluid particles and grids (lower bit values reduce file size)"""
        ...
    @openvdb_data_depth.setter
    def openvdb_data_depth(self, value: Literal['NONE']) -> None:
        ...
    @property
    def time_scale(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Adjust simulation speed"""
        ...
    @time_scale.setter
    def time_scale(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def use_adaptive_timesteps(self) -> bool:
        """Automatically decide when to perform multiple simulation steps per frame"""
        ...
    @use_adaptive_timesteps.setter
    def use_adaptive_timesteps(self, value: bool) -> None:
        ...
    @property
    def cfl_condition(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Maximal velocity per cell (greater CFL numbers will minimize the number of simulation steps and the computation time.)"""
        ...
    @cfl_condition.setter
    def cfl_condition(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def timesteps_min(self) -> Annotated[int, "step=1"]:
        """Minimum number of simulation steps to perform for one frame"""
        ...
    @timesteps_min.setter
    def timesteps_min(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def timesteps_max(self) -> Annotated[int, "step=1"]:
        """Maximum number of simulation steps to perform for one frame"""
        ...
    @timesteps_max.setter
    def timesteps_max(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def use_slice(self) -> bool:
        """Perform a single slice of the domain object"""
        ...
    @use_slice.setter
    def use_slice(self, value: bool) -> None:
        ...
    @property
    def slice_axis(self) -> Literal['AUTO', 'X', 'Y', 'Z']:

        ...
    @slice_axis.setter
    def slice_axis(self, value: Literal['AUTO', 'X', 'Y', 'Z']) -> None:
        ...
    @property
    def slice_per_voxel(self) -> Annotated[float, "step=0.10000000149011612", "precision=1"]:
        """How many slices per voxel should be generated"""
        ...
    @slice_per_voxel.setter
    def slice_per_voxel(self, value: Annotated[float, "step=0.10000000149011612", "precision=1"]) -> None:
        ...
    @property
    def slice_depth(self) -> Annotated[float, "subtype='FACTOR'", "step=0.10000000149011612", "precision=3"]:
        """Position of the slice"""
        ...
    @slice_depth.setter
    def slice_depth(self, value: Annotated[float, "subtype='FACTOR'", "step=0.10000000149011612", "precision=3"]) -> None:
        ...
    @property
    def display_thickness(self) -> Annotated[float, "step=0.10000000149011612", "precision=3"]:
        """Thickness of smoke display in the viewport"""
        ...
    @display_thickness.setter
    def display_thickness(self, value: Annotated[float, "step=0.10000000149011612", "precision=3"]) -> None:
        ...
    @property
    def display_interpolation(self) -> Literal['LINEAR', 'CUBIC', 'CLOSEST']:
        """Interpolation method to use for smoke/fire volumes in solid mode"""
        ...
    @display_interpolation.setter
    def display_interpolation(self, value: Literal['LINEAR', 'CUBIC', 'CLOSEST']) -> None:
        ...
    @property
    def show_gridlines(self) -> bool:
        """Show gridlines"""
        ...
    @show_gridlines.setter
    def show_gridlines(self, value: bool) -> None:
        ...
    @property
    def show_velocity(self) -> bool:
        """Visualize vector fields"""
        ...
    @show_velocity.setter
    def show_velocity(self, value: bool) -> None:
        ...
    @property
    def vector_display_type(self) -> Literal['NEEDLE', 'STREAMLINE', 'MAC']:

        ...
    @vector_display_type.setter
    def vector_display_type(self, value: Literal['NEEDLE', 'STREAMLINE', 'MAC']) -> None:
        ...
    @property
    def vector_field(self) -> Literal['FLUID_VELOCITY', 'GUIDE_VELOCITY', 'FORCE']:
        """Vector field to be represented by the display vectors"""
        ...
    @vector_field.setter
    def vector_field(self, value: Literal['FLUID_VELOCITY', 'GUIDE_VELOCITY', 'FORCE']) -> None:
        ...
    @property
    def vector_scale_with_magnitude(self) -> bool:
        """Scale vectors with their magnitudes"""
        ...
    @vector_scale_with_magnitude.setter
    def vector_scale_with_magnitude(self, value: bool) -> None:
        ...
    @property
    def vector_show_mac_x(self) -> bool:
        """Show X-component of MAC Grid"""
        ...
    @vector_show_mac_x.setter
    def vector_show_mac_x(self, value: bool) -> None:
        ...
    @property
    def vector_show_mac_y(self) -> bool:
        """Show Y-component of MAC Grid"""
        ...
    @vector_show_mac_y.setter
    def vector_show_mac_y(self, value: bool) -> None:
        ...
    @property
    def vector_show_mac_z(self) -> bool:
        """Show Z-component of MAC Grid"""
        ...
    @vector_show_mac_z.setter
    def vector_show_mac_z(self, value: bool) -> None:
        ...
    @property
    def vector_scale(self) -> Annotated[float, "step=0.10000000149011612", "precision=3"]:
        """Multiplier for scaling the vectors"""
        ...
    @vector_scale.setter
    def vector_scale(self, value: Annotated[float, "step=0.10000000149011612", "precision=3"]) -> None:
        ...
    @property
    def use_color_ramp(self) -> bool:
        """Render a simulation field while mapping its voxels values to the colors of a ramp or using a predefined color code"""
        ...
    @use_color_ramp.setter
    def use_color_ramp(self, value: bool) -> None:
        ...
    @property
    def color_ramp_field(self) -> Literal['NONE']:
        """Simulation field to color map"""
        ...
    @color_ramp_field.setter
    def color_ramp_field(self, value: Literal['NONE']) -> None:
        ...
    @property
    def color_ramp_field_scale(self) -> Annotated[float, "step=0.10000000149011612", "precision=3"]:
        """Multiplier for scaling the selected field to color map"""
        ...
    @color_ramp_field_scale.setter
    def color_ramp_field_scale(self, value: Annotated[float, "step=0.10000000149011612", "precision=3"]) -> None:
        ...
    @property
    def color_ramp(self) -> Annotated[Optional['ColorRamp'], "subtype=''", "unit='MASS'", "is_animatable=False"]:

        ...
    @property
    def clipping(self) -> Annotated[float, "step=0.10000000149011612", "precision=6"]:
        """Value under which voxels are considered empty space to optimize rendering"""
        ...
    @clipping.setter
    def clipping(self, value: Annotated[float, "step=0.10000000149011612", "precision=6"]) -> None:
        ...
    @property
    def gridlines_color_field(self) -> Literal['NONE', 'FLAGS', 'RANGE']:
        """Simulation field to color map onto gridlines"""
        ...
    @gridlines_color_field.setter
    def gridlines_color_field(self, value: Literal['NONE', 'FLAGS', 'RANGE']) -> None:
        ...
    @property
    def gridlines_lower_bound(self) -> Annotated[float, "step=0.10000000149011612", "precision=6"]:
        """Lower bound of the highlighting range"""
        ...
    @gridlines_lower_bound.setter
    def gridlines_lower_bound(self, value: Annotated[float, "step=0.10000000149011612", "precision=6"]) -> None:
        ...
    @property
    def gridlines_upper_bound(self) -> Annotated[float, "step=0.10000000149011612", "precision=6"]:
        """Upper bound of the highlighting range"""
        ...
    @gridlines_upper_bound.setter
    def gridlines_upper_bound(self, value: Annotated[float, "step=0.10000000149011612", "precision=6"]) -> None:
        ...
    @property
    def gridlines_range_color(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:
        """Color used to highlight the range"""
        ...
    @gridlines_range_color.setter
    def gridlines_range_color(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def gridlines_cell_filter(self) -> Literal['NONE', 'FLUID', 'OBSTACLE', 'EMPTY', 'INFLOW', 'OUTFLOW']:
        """Cell type to be highlighted"""
        ...
    @gridlines_cell_filter.setter
    def gridlines_cell_filter(self, value: Literal['NONE', 'FLUID', 'OBSTACLE', 'EMPTY', 'INFLOW', 'OUTFLOW']) -> None:
        ...
    @property
    def velocity_scale(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Factor to control the amount of motion blur"""
        ...
    @velocity_scale.setter
    def velocity_scale(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...