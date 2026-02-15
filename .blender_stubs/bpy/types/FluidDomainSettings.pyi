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
    effector_group: Annotated[Optional['Collection'], "is_animatable=False"]
    """Limit effectors to this collection"""
    fluid_group: Annotated[Optional['Collection'], "is_animatable=False"]
    """Limit fluid objects to this collection"""
    force_collection: Annotated[Optional['Collection'], "is_animatable=False"]
    """Limit forces to this collection"""
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
    additional_res: Annotated[int, "step=1"]
    """Maximum number of additional cells"""
    adapt_margin: Annotated[int, "step=1"]
    """Margin added around fluid to minimize boundary interference"""
    adapt_threshold: Annotated[float, "step=0.0020000000949949026", "precision=6"]
    """Minimum amount of fluid grid values (smoke density, fuel and heat) a cell can contain, before it is considered empty"""
    use_adaptive_domain: Annotated[bool, "is_animatable=False"]
    """Adapt simulation resolution and size to fluid"""
    resolution_max: Annotated[int, "step=2", "is_animatable=False"]
    """Resolution used for the fluid domain. Value corresponds to the longest domain side (resolution for other domain sides is calculated automatically)."""
    use_collision_border_front: bool
    """Enable collisions with front domain border"""
    use_collision_border_back: bool
    """Enable collisions with back domain border"""
    use_collision_border_right: bool
    """Enable collisions with right domain border"""
    use_collision_border_left: bool
    """Enable collisions with left domain border"""
    use_collision_border_top: bool
    """Enable collisions with top domain border"""
    use_collision_border_bottom: bool
    """Enable collisions with bottom domain border"""
    gravity: Annotated[list[float], "subtype='ACCELERATION'", "unit='ACCELERATION'", "step=10.0", "precision=3"]
    """Gravity in X, Y and Z direction"""
    domain_type: Annotated[Literal['GAS', 'LIQUID'], "is_animatable=False"]
    """Change domain type of the simulation"""
    delete_in_obstacle: bool
    """Delete fluid inside obstacles"""
    alpha: Annotated[float, "step=0.019999999552965164", "precision=5"]
    """Buoyant force based on smoke density (higher value results in faster rising smoke)"""
    beta: Annotated[float, "step=0.019999999552965164", "precision=5"]
    """Buoyant force based on smoke heat (higher value results in faster rising smoke)"""
    dissolve_speed: Annotated[int, "step=1"]
    """Determine how quickly the smoke dissolves (lower value makes smoke disappear faster)"""
    vorticity: Annotated[float, "step=10.0", "precision=3"]
    """Amount of turbulence and rotation in smoke"""
    highres_sampling: Literal['FULLSAMPLE', 'LINEAR', 'NEAREST']
    """Method for sampling the high resolution flow"""
    use_dissolve_smoke: bool
    """Let smoke disappear over time"""
    use_dissolve_smoke_log: bool
    """Dissolve smoke in a logarithmic fashion. Dissolves quickly at first, but lingers longer."""
    burning_rate: Annotated[float, "step=1.0", "precision=5"]
    """Speed of the burning reaction (higher value results in smaller flames)"""
    flame_smoke: Annotated[float, "step=1.0", "precision=5"]
    """Amount of smoke created by burning fuel"""
    flame_vorticity: Annotated[float, "step=1.0", "precision=5"]
    """Additional vorticity for the flames"""
    flame_ignition: Annotated[float, "step=1.0", "precision=5"]
    """Minimum temperature of the flames (higher value results in faster rising flames)"""
    flame_max_temp: Annotated[float, "step=1.0", "precision=5"]
    """Maximum temperature of the flames (higher value results in faster rising flames)"""
    flame_smoke_color: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    """Color of smoke emitted from burning fuel"""
    noise_strength: Annotated[float, "step=1.0", "precision=2"]
    """Strength of noise"""
    noise_pos_scale: Annotated[float, "step=10.0", "precision=3"]
    """Scale of noise (higher value results in larger vortices)"""
    noise_time_anim: Annotated[float, "step=10.0", "precision=3"]
    """Animation time of noise"""
    noise_scale: Annotated[int, "step=1", "is_animatable=False"]
    """The noise simulation is scaled up by this factor (compared to the base resolution of the domain)"""
    use_noise: Annotated[bool, "is_animatable=False"]
    """Enable fluid noise (using amplification)"""
    simulation_method: Annotated[Literal['FLIP', 'APIC'], "is_animatable=False"]
    """Change the underlying simulation method"""
    flip_ratio: Annotated[float, "step=10.0", "precision=3"]
    """PIC/FLIP Ratio. A value of 1.0 will result in a completely FLIP based simulation. Use a lower value for simulations which should produce smaller splashes."""
    particle_randomness: Annotated[float, "step=10.0", "precision=3"]
    """Randomness factor for particle sampling"""
    particle_number: Annotated[int, "step=1"]
    """Particle number factor (higher value results in more particles)"""
    particle_min: Annotated[int, "step=1"]
    """Minimum number of particles per cell (ensures that each cell has at least this amount of particles)"""
    particle_max: Annotated[int, "step=1"]
    """Maximum number of particles per cell (ensures that each cell has at most this amount of particles)"""
    particle_radius: Annotated[float, "step=10.0", "precision=3"]
    """Particle radius factor. Increase this value if the simulation appears to leak volume, decrease it if the simulation seems to gain volume."""
    particle_band_width: Annotated[float, "step=10.0", "precision=3"]
    """Particle (narrow) band width (higher value results in thicker band and more particles)"""
    use_flip_particles: Annotated[bool, "is_animatable=False"]
    """Create liquid particle system"""
    use_fractions: Annotated[bool, "is_animatable=False"]
    """Fractional obstacles improve and smoothen the fluid-obstacle boundary"""
    fractions_threshold: Annotated[float, "step=0.05000000074505806", "precision=-1"]
    """Determines how much fluid is allowed in an obstacle cell (higher values will tag a boundary cell as an obstacle easier and reduce the boundary smoothening effect)"""
    fractions_distance: Annotated[float, "step=0.10000000149011612", "precision=-1"]
    """Determines how far apart fluid and obstacle are (higher values will result in fluid being further away from obstacles, smaller values will let fluid move towards the inside of obstacles)"""
    sys_particle_maximum: Annotated[int, "step=1"]
    """Maximum number of fluid particles that are allowed in this simulation"""
    use_viscosity: bool
    """Simulate fluids with high viscosity using a special solver"""
    viscosity_value: Annotated[float, "step=1.0", "precision=3"]
    """Viscosity of liquid (higher values result in more viscous fluids, a value of 0 will still apply some viscosity)"""
    use_diffusion: Annotated[bool, "is_animatable=False"]
    """Enable fluid diffusion settings (e.g. viscosity, surface tension)"""
    surface_tension: Annotated[float, "step=10.0", "precision=3"]
    """Surface tension of liquid (higher value results in greater hydrophobic behavior)"""
    viscosity_base: Annotated[float, "step=10.0", "precision=3"]
    """Viscosity setting: value that is multiplied by 10 to the power of (exponent*-1)"""
    viscosity_exponent: Annotated[int, "step=1"]
    """Negative exponent for the viscosity value (to simplify entering small values e.g. 5*10^-6)"""
    mesh_concave_upper: Annotated[float, "step=10.0", "precision=3"]
    """Upper mesh concavity bound (high values tend to smoothen and fill out concave regions)"""
    mesh_concave_lower: Annotated[float, "step=10.0", "precision=3"]
    """Lower mesh concavity bound (high values tend to smoothen and fill out concave regions)"""
    mesh_smoothen_pos: Annotated[int, "step=1"]
    """Positive mesh smoothening"""
    mesh_smoothen_neg: Annotated[int, "step=1"]
    """Negative mesh smoothening"""
    mesh_scale: Annotated[int, "step=1", "is_animatable=False"]
    """The mesh simulation is scaled up by this factor (compared to the base resolution of the domain). For best meshing, it is recommended to adjust the mesh particle radius alongside this value."""
    mesh_generator: Literal['IMPROVED', 'UNION']
    """Which particle level set generator to use"""
    use_mesh: Annotated[bool, "is_animatable=False"]
    """Enable fluid mesh (using amplification)"""
    use_speed_vectors: Annotated[bool, "is_animatable=False"]
    """Caches velocities of mesh vertices. These will be used (automatically) when rendering with motion blur enabled."""
    mesh_particle_radius: Annotated[float, "step=10.0", "precision=3"]
    """Particle radius factor (higher value results in larger (meshed) particles). Needs to be adjusted after changing the mesh scale."""
    sndparticle_potential_min_wavecrest: Annotated[float, "step=100.0", "precision=3"]
    """Lower clamping threshold for marking fluid cells as wave crests (lower value results in more marked cells)"""
    sndparticle_potential_max_wavecrest: Annotated[float, "step=100.0", "precision=3"]
    """Upper clamping threshold for marking fluid cells as wave crests (higher value results in less marked cells)"""
    sndparticle_potential_min_trappedair: Annotated[float, "step=100.0", "precision=3"]
    """Lower clamping threshold for marking fluid cells where air is trapped (lower value results in more marked cells)"""
    sndparticle_potential_max_trappedair: Annotated[float, "step=100.0", "precision=3"]
    """Upper clamping threshold for marking fluid cells where air is trapped (higher value results in less marked cells)"""
    sndparticle_potential_min_energy: Annotated[float, "step=100.0", "precision=3"]
    """Lower clamping threshold that indicates the fluid speed where cells start to emit particles (lower values result in generally more particles)"""
    sndparticle_potential_max_energy: Annotated[float, "step=100.0", "precision=3"]
    """Upper clamping threshold that indicates the fluid speed where cells no longer emit more particles (higher value results in generally less particles)"""
    sndparticle_sampling_wavecrest: Annotated[int, "step=1"]
    """Maximum number of particles generated per wave crest cell per frame"""
    sndparticle_sampling_trappedair: Annotated[int, "step=1"]
    """Maximum number of particles generated per trapped air cell per frame"""
    sndparticle_bubble_buoyancy: Annotated[float, "step=10.0", "precision=2"]
    """Amount of buoyancy force that rises bubbles (high value results in bubble movement mainly upwards)"""
    sndparticle_bubble_drag: Annotated[float, "step=10.0", "precision=2"]
    """Amount of drag force that moves bubbles along with the fluid (high value results in bubble movement mainly along with the fluid)"""
    sndparticle_life_min: Annotated[float, "step=100.0", "precision=1"]
    """Lowest possible particle lifetime"""
    sndparticle_life_max: Annotated[float, "step=100.0", "precision=1"]
    """Highest possible particle lifetime"""
    sndparticle_boundary: Literal['DELETE', 'PUSHOUT']
    """How particles that left the domain are treated"""
    sndparticle_combined_export: Literal['OFF', 'SPRAY_FOAM', 'SPRAY_BUBBLES', 'FOAM_BUBBLES', 'SPRAY_FOAM_BUBBLES']
    """Determines which particle systems are created from secondary particles"""
    sndparticle_potential_radius: Annotated[int, "step=1"]
    """Radius to compute potential for each cell (higher values are slower but create smoother potential grids)"""
    sndparticle_update_radius: Annotated[int, "step=1"]
    """Radius to compute position update for each particle (higher values are slower but particles move less chaotic)"""
    particle_scale: Annotated[int, "step=1", "is_animatable=False"]
    """The particle simulation is scaled up by this factor (compared to the base resolution of the domain)"""
    use_spray_particles: Annotated[bool, "is_animatable=False"]
    """Create spray particle system"""
    use_bubble_particles: Annotated[bool, "is_animatable=False"]
    """Create bubble particle system"""
    use_foam_particles: Annotated[bool, "is_animatable=False"]
    """Create foam particle system"""
    use_tracer_particles: Annotated[bool, "is_animatable=False"]
    """Create tracer particle system"""
    guide_alpha: Annotated[float, "step=10.0", "precision=3"]
    """Guiding weight (higher value results in greater lag)"""
    guide_beta: Annotated[int, "step=1"]
    """Guiding size (higher value results in larger vortices)"""
    guide_vel_factor: Annotated[float, "step=10.0", "precision=3"]
    """Guiding velocity factor (higher value results in greater guiding velocities)"""
    guide_source: Literal['DOMAIN', 'EFFECTOR']
    """Choose where to get guiding velocities from"""
    guide_parent: Annotated[Optional['Object'], "is_animatable=False"]
    """Use velocities from this object for the guiding effect (object needs to have fluid modifier and be of type domain))"""
    use_guide: Annotated[bool, "is_animatable=False"]
    """Enable fluid guiding"""
    cache_frame_start: Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1", "is_animatable=False"]
    """Frame on which the simulation starts (first frame baked)"""
    cache_frame_end: Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1", "is_animatable=False"]
    """Frame on which the simulation stops (last frame baked)"""
    cache_frame_offset: Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1", "is_animatable=False"]
    """Frame offset that is used when loading the simulation from the cache. It is not considered when baking the simulation, only when loading it."""
    cache_frame_pause_data: Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1"]

    cache_frame_pause_noise: Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1"]

    cache_frame_pause_mesh: Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1"]

    cache_frame_pause_particles: Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1"]

    cache_frame_pause_guide: Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1"]

    cache_mesh_format: Annotated[Literal['UNI', 'OPENVDB', 'RAW'], "is_animatable=False"]
    """Select the file format to be used for caching surface data"""
    cache_data_format: Annotated[Literal['UNI', 'OPENVDB', 'RAW'], "is_animatable=False"]
    """Select the file format to be used for caching volumetric data"""
    cache_particle_format: Annotated[Literal['UNI', 'OPENVDB', 'RAW'], "is_animatable=False"]
    """Select the file format to be used for caching particle data"""
    cache_noise_format: Annotated[Literal['UNI', 'OPENVDB', 'RAW'], "is_animatable=False"]
    """Select the file format to be used for caching noise data"""
    cache_type: Annotated[Literal['REPLAY', 'MODULAR', 'ALL'], "is_animatable=False"]
    """Change the cache type of the simulation"""
    cache_resumable: Annotated[bool, "is_animatable=False"]
    """Additional data will be saved so that the bake jobs can be resumed after pausing. Because more data will be written to disk it is recommended to avoid enabling this option when baking at high resolutions."""
    cache_directory: Annotated[str, "subtype='DIR_PATH'", "is_animatable=False"]
    """Directory that contains fluid cache files"""
    is_cache_baking_data: bool

    has_cache_baked_data: bool

    is_cache_baking_noise: bool

    has_cache_baked_noise: bool

    is_cache_baking_mesh: bool

    has_cache_baked_mesh: bool

    is_cache_baking_particles: bool

    has_cache_baked_particles: bool

    is_cache_baking_guide: bool

    has_cache_baked_guide: bool

    is_cache_baking_any: bool

    has_cache_baked_any: bool

    export_manta_script: Annotated[bool, "is_animatable=False"]
    """Generate and export Mantaflow script from current domain settings during bake. This is only needed if you plan to analyze the cache (e.g. view grids, velocity vectors, particles) in Mantaflow directly (outside of Blender) after baking the simulation."""
    openvdb_cache_compress_type: Literal['ZIP', 'NONE']
    """Compression method to be used"""
    openvdb_data_depth: Literal['NONE']
    """Bit depth for fluid particles and grids (lower bit values reduce file size)"""
    time_scale: Annotated[float, "step=10.0", "precision=3"]
    """Adjust simulation speed"""
    use_adaptive_timesteps: bool
    """Automatically decide when to perform multiple simulation steps per frame"""
    cfl_condition: Annotated[float, "step=10.0", "precision=3"]
    """Maximal velocity per cell (greater CFL numbers will minimize the number of simulation steps and the computation time.)"""
    timesteps_min: Annotated[int, "step=1"]
    """Minimum number of simulation steps to perform for one frame"""
    timesteps_max: Annotated[int, "step=1"]
    """Maximum number of simulation steps to perform for one frame"""
    use_slice: bool
    """Perform a single slice of the domain object"""
    slice_axis: Literal['AUTO', 'X', 'Y', 'Z']

    slice_per_voxel: Annotated[float, "step=0.10000000149011612", "precision=1"]
    """How many slices per voxel should be generated"""
    slice_depth: Annotated[float, "subtype='FACTOR'", "step=0.10000000149011612", "precision=3"]
    """Position of the slice"""
    display_thickness: Annotated[float, "step=0.10000000149011612", "precision=3"]
    """Thickness of smoke display in the viewport"""
    display_interpolation: Literal['LINEAR', 'CUBIC', 'CLOSEST']
    """Interpolation method to use for smoke/fire volumes in solid mode"""
    show_gridlines: bool
    """Show gridlines"""
    show_velocity: bool
    """Visualize vector fields"""
    vector_display_type: Literal['NEEDLE', 'STREAMLINE', 'MAC']

    vector_field: Literal['FLUID_VELOCITY', 'GUIDE_VELOCITY', 'FORCE']
    """Vector field to be represented by the display vectors"""
    vector_scale_with_magnitude: bool
    """Scale vectors with their magnitudes"""
    vector_show_mac_x: bool
    """Show X-component of MAC Grid"""
    vector_show_mac_y: bool
    """Show Y-component of MAC Grid"""
    vector_show_mac_z: bool
    """Show Z-component of MAC Grid"""
    vector_scale: Annotated[float, "step=0.10000000149011612", "precision=3"]
    """Multiplier for scaling the vectors"""
    use_color_ramp: bool
    """Render a simulation field while mapping its voxels values to the colors of a ramp or using a predefined color code"""
    color_ramp_field: Literal['NONE']
    """Simulation field to color map"""
    color_ramp_field_scale: Annotated[float, "step=0.10000000149011612", "precision=3"]
    """Multiplier for scaling the selected field to color map"""
    @property
    def color_ramp(self) -> Annotated[Optional['ColorRamp'], "subtype=''", "unit='MASS'", "is_animatable=False"]:

        ...
    clipping: Annotated[float, "step=0.10000000149011612", "precision=6"]
    """Value under which voxels are considered empty space to optimize rendering"""
    gridlines_color_field: Literal['NONE', 'FLAGS', 'RANGE']
    """Simulation field to color map onto gridlines"""
    gridlines_lower_bound: Annotated[float, "step=0.10000000149011612", "precision=6"]
    """Lower bound of the highlighting range"""
    gridlines_upper_bound: Annotated[float, "step=0.10000000149011612", "precision=6"]
    """Upper bound of the highlighting range"""
    gridlines_range_color: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    """Color used to highlight the range"""
    gridlines_cell_filter: Literal['NONE', 'FLUID', 'OBSTACLE', 'EMPTY', 'INFLOW', 'OUTFLOW']
    """Cell type to be highlighted"""
    velocity_scale: Annotated[float, "step=10.0", "precision=3"]
    """Factor to control the amount of motion blur"""