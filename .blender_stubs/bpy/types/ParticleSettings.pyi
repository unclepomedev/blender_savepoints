# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated
from .bpy_prop_collection import bpy_prop_collection

from .ID import ID
from .AnimData import AnimData
from .AssetMetaData import AssetMetaData
from .BoidSettings import BoidSettings
from .Collection import Collection
from .CurveMapping import CurveMapping
from .EffectorWeights import EffectorWeights
from .FieldSettings import FieldSettings
from .IDOverrideLibrary import IDOverrideLibrary
from .ImagePreview import ImagePreview
from .Library import Library
from .LibraryWeakReference import LibraryWeakReference
from .Object import Object
from .ParticleDupliWeight import ParticleDupliWeight
from .ParticleSettingsTextureSlot import ParticleSettingsTextureSlot
from .ParticleSettingsTextureSlots import ParticleSettingsTextureSlots
from .SPHFluidSettings import SPHFluidSettings
from .Texture import Texture
class ParticleSettings(ID):
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
    def texture_slots(self) -> Annotated['ParticleSettingsTextureSlots', "is_animatable=False"]:
        """Texture slots defining the mapping and influence of textures"""
        ...
    active_texture: Annotated[Optional['Texture'], "is_animatable=False"]
    """Active texture slot being displayed"""
    active_texture_index: Annotated[int, "subtype='UNSIGNED'", "step=1"]
    """Index of active texture slot"""
    @property
    def is_fluid(self) -> bool:
        """Particles were created by a fluid simulation"""
        ...
    use_react_start_end: Annotated[bool, "is_animatable=False"]
    """Give birth to unreacted particles eventually"""
    use_react_multiple: Annotated[bool, "is_animatable=False"]
    """React multiple times"""
    use_regrow_hair: bool
    """Regrow hair for each frame"""
    show_unborn: bool
    """Show particles before they are emitted"""
    use_dead: bool
    """Show particles after they have died"""
    use_emit_random: Annotated[bool, "is_animatable=False"]
    """Emit in random order of elements"""
    use_even_distribution: Annotated[bool, "is_animatable=False"]
    """Use even distribution from faces based on face areas or edge lengths"""
    use_die_on_collision: Annotated[bool, "is_animatable=False"]
    """Particles die when they collide with a deflector object"""
    use_size_deflect: Annotated[bool, "is_animatable=False"]
    """Use particle's size in deflection"""
    use_rotations: Annotated[bool, "is_animatable=False"]
    """Calculate particle rotations"""
    use_dynamic_rotation: Annotated[bool, "is_animatable=False"]
    """Particle rotations are affected by collisions and effectors"""
    use_multiply_size_mass: Annotated[bool, "is_animatable=False"]
    """Multiply mass by particle size"""
    use_advanced_hair: Annotated[bool, "is_animatable=False"]
    """Use full physics calculations for growing hair"""
    lock_boids_to_surface: bool
    """Constrain boids to a surface"""
    use_hair_bspline: bool
    """Interpolate hair using B-Splines"""
    invert_grid: bool
    """Invert what is considered object and what is not"""
    hexagonal_grid: bool
    """Create the grid in a hexagonal pattern"""
    apply_effector_to_children: bool
    """Apply effectors to children"""
    create_long_hair_children: bool
    """Calculate children that suit long hair well"""
    apply_guide_to_children: bool
    use_self_effect: bool
    """Particle effectors affect themselves"""
    type: Annotated[Literal['EMITTER', 'HAIR'], "is_animatable=False"]
    """Particle type"""
    emit_from: Annotated[Literal['VERT', 'FACE', 'VOLUME'], "is_animatable=False"]
    """Where to emit particles from"""
    distribution: Annotated[Literal['JIT', 'RAND', 'GRID'], "is_animatable=False"]
    """How to distribute particles on selected element"""
    physics_type: Annotated[Literal['NO', 'NEWTON', 'KEYED', 'BOIDS', 'FLUID'], "is_animatable=False"]
    """Particle physics type"""
    rotation_mode: Annotated[Literal['NONE', 'NOR', 'NOR_TAN', 'VEL', 'GLOB_X', 'GLOB_Y', 'GLOB_Z', 'OB_X', 'OB_Y', 'OB_Z'], "is_animatable=False"]
    """Particle orientation axis (does not affect Explode modifier's results)"""
    angular_velocity_mode: Annotated[Literal['NONE', 'VELOCITY', 'HORIZONTAL', 'VERTICAL', 'GLOBAL_X', 'GLOBAL_Y', 'GLOBAL_Z', 'RAND'], "is_animatable=False"]
    """What axis is used to change particle rotation with time"""
    react_event: Annotated[Literal['DEATH', 'COLLIDE', 'NEAR'], "is_animatable=False"]
    """The event of target particles to react on"""
    show_guide_hairs: bool
    """Show guide hairs"""
    show_hair_grid: bool
    """Show hair simulation grid"""
    show_velocity: bool
    """Show particle velocity"""
    show_size: bool
    """Show particle size"""
    show_health: bool
    """Display boid health"""
    use_absolute_path_time: bool
    """Path timing is in absolute frames"""
    use_parent_particles: bool
    """Render parent particles"""
    show_number: bool
    """Show particle number"""
    use_collection_pick_random: bool
    """Pick objects from collection randomly"""
    use_collection_count: bool
    """Use object multiple times in the same collection"""
    use_global_instance: bool
    """Use object's global coordinates for duplication"""
    use_rotation_instance: bool
    """Use object's rotation for duplication (global x-axis is aligned particle rotation axis)"""
    use_scale_instance: bool
    """Use object's scale for duplication"""
    use_render_adaptive: bool
    """Display steps of the particle path"""
    use_velocity_length: bool
    """Multiply line length by particle speed"""
    use_whole_collection: bool
    """Use whole collection at once"""
    use_strand_primitive: bool
    """Use the strand primitive for rendering"""
    display_method: Literal['NONE', 'RENDER', 'DOT', 'CIRC', 'CROSS', 'AXIS']
    """How particles are displayed in viewport"""
    render_type: Literal['NONE', 'HALO', 'LINE', 'PATH', 'OBJECT', 'COLLECTION']
    """How particles are rendered"""
    display_color: Literal['NONE', 'MATERIAL', 'VELOCITY', 'ACCELERATION']
    """Display additional particle data as a color"""
    display_size: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=1.0", "precision=-1"]
    """Size of particles on viewport"""
    child_type: Literal['NONE', 'SIMPLE', 'INTERPOLATED']
    """Create child particles"""
    display_step: Annotated[int, "step=1"]
    """How many steps paths are displayed with (power of 2)"""
    render_step: Annotated[int, "step=1"]
    """How many steps paths are rendered with (power of 2)"""
    hair_step: Annotated[int, "step=1", "is_animatable=False"]
    """Number of hair segments"""
    bending_random: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Random stiffness of hairs"""
    keys_step: Annotated[int, "step=1"]
    adaptive_angle: Annotated[int, "step=1"]
    """How many degrees path has to curve to make another render segment"""
    adaptive_pixel: Annotated[int, "step=1"]
    """How many pixels path has to cover to make another render segment"""
    display_percentage: Annotated[int, "subtype='PERCENTAGE'", "step=1"]
    """Percentage of particles to display in 3D view"""
    material: Annotated[int, "step=1"]
    """Index of material slot used for rendering particles"""
    material_slot: Literal['DEFAULT']
    """Material slot used for rendering particles"""
    integrator: Literal['EULER', 'VERLET', 'MIDPOINT', 'RK4']
    """Algorithm used to calculate physics, from the fastest to the most stable and accurate: Midpoint, Euler, Verlet, RK4"""
    kink: Literal['NO', 'CURL', 'RADIAL', 'WAVE', 'BRAID', 'SPIRAL']
    """Type of periodic offset on the path"""
    kink_axis: Literal['X', 'Y', 'Z']
    """Which axis to use for offset"""
    color_maximum: Annotated[float, "step=10.0", "precision=3"]
    """Maximum length of the particle color vector"""
    frame_start: Annotated[float, "subtype='TIME'", "unit='TIME'", "step=10.0", "precision=3", "is_animatable=False"]
    """Frame number to start emitting particles"""
    frame_end: Annotated[float, "subtype='TIME'", "unit='TIME'", "step=10.0", "precision=3", "is_animatable=False"]
    """Frame number to stop emitting particles"""
    lifetime: Annotated[float, "subtype='TIME'", "unit='TIME'", "step=10.0", "precision=3"]
    """Life span of the particles"""
    lifetime_random: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Give the particle life a random variation"""
    time_tweak: Annotated[float, "step=1.0", "precision=3"]
    """A multiplier for physics timestep (1.0 means one frame = 1/25 seconds)"""
    timestep: Annotated[float, "step=1.0", "precision=3"]
    """The simulation timestep per frame (seconds per frame)"""
    use_adaptive_subframes: bool
    """Automatically set the number of subframes"""
    subframes: Annotated[int, "step=1"]
    """Subframes to simulate for improved stability and finer granularity simulations (dt = timestep / (subframes + 1))"""
    courant_target: Annotated[float, "step=10.0", "precision=3"]
    """The relative distance a particle can move before requiring more subframes (target Courant number); 0.01 to 0.3 is the recommended range"""
    jitter_factor: Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]
    """Amount of jitter applied to the sampling"""
    effect_hair: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Hair stiffness for effectors"""
    count: Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]
    """Total number of particles"""
    userjit: Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]
    """Emission locations per face (0 = automatic)"""
    grid_resolution: Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]
    """The resolution of the particle grid"""
    grid_random: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Add random offset to the grid locations"""
    effector_amount: Annotated[int, "subtype='UNSIGNED'", "step=1"]
    """How many particles are effectors (0 is all particles)"""
    normal_factor: Annotated[float, "subtype='VELOCITY'", "unit='VELOCITY'", "step=1.0", "precision=3"]
    """Let the surface normal give the particle a starting velocity"""
    object_factor: Annotated[float, "step=0.10000000149011612", "precision=3"]
    """Let the object give the particle a starting velocity"""
    factor_random: Annotated[float, "step=1.0", "precision=3"]
    """Give the starting velocity a random variation"""
    particle_factor: Annotated[float, "step=0.10000000149011612", "precision=3"]
    """Let the target particle give the particle a starting velocity"""
    tangent_factor: Annotated[float, "subtype='VELOCITY'", "unit='VELOCITY'", "step=1.0", "precision=2"]
    """Let the surface tangent give the particle a starting velocity"""
    tangent_phase: Annotated[float, "step=10.0", "precision=3"]
    """Rotate the surface tangent"""
    reactor_factor: Annotated[float, "step=10.0", "precision=3"]
    """Let the vector away from the target particle's location give the particle a starting velocity"""
    object_align_factor: Annotated[list[float], "subtype='VELOCITY'", "unit='VELOCITY'", "step=1.0", "precision=3"]
    """Let the emitter object orientation give the particle a starting velocity"""
    angular_velocity_factor: Annotated[float, "step=10.0", "precision=3"]
    """Angular velocity amount (in radians per second)"""
    phase_factor: Annotated[float, "step=10.0", "precision=3"]
    """Rotation around the chosen orientation axis"""
    rotation_factor_random: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Randomize particle orientation"""
    phase_factor_random: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Randomize rotation around the chosen orientation axis"""
    hair_length: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=1.0", "precision=3"]
    """Length of the hair"""
    mass: Annotated[float, "subtype=''", "unit='MASS'", "step=1.0", "precision=4"]
    """Mass of the particles"""
    particle_size: Annotated[float, "step=1.0", "precision=3"]
    """The size of the particles"""
    size_random: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Give the particle size a random variation"""
    collision_collection: Annotated[Optional['Collection'], "is_animatable=False"]
    """Limit colliders to this collection"""
    drag_factor: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Amount of air drag"""
    brownian_factor: Annotated[float, "step=1.0", "precision=3"]
    """Amount of random, erratic particle movement"""
    damping: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Amount of damping"""
    length_random: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Give path length a random variation"""
    child_percent: Annotated[int, "step=1"]
    """Number of children per parent"""
    rendered_child_count: Annotated[int, "step=1"]
    """Number of children per parent for rendering"""
    virtual_parents: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Relative amount of virtual parents"""
    child_size: Annotated[float, "step=0.10000000149011612", "precision=3"]
    """A multiplier for the child particle size"""
    child_size_random: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Random variation to the size of the child particles"""
    child_radius: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.10000000149011612", "precision=3"]
    """Radius of children around parent"""
    child_roundness: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Roundness of children around parent"""
    clump_factor: Annotated[float, "step=10.0", "precision=3"]
    """Amount of clumping"""
    clump_shape: Annotated[float, "step=10.0", "precision=3"]
    """Shape of clumping"""
    use_clump_curve: bool
    """Use a curve to define clump tapering"""
    @property
    def clump_curve(self) -> Annotated[Optional['CurveMapping'], "is_animatable=False"]:
        """Curve defining clump tapering"""
        ...
    use_clump_noise: bool
    """Create random clumps around the parent"""
    clump_noise_size: Annotated[float, "step=0.10000000149011612", "precision=3"]
    """Size of clump noise"""
    kink_amplitude: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.10000000149011612", "precision=3"]
    """The amplitude of the offset"""
    kink_amplitude_clump: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """How much clump affects kink amplitude"""
    kink_amplitude_random: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Random variation of the amplitude"""
    kink_frequency: Annotated[float, "step=0.10000000149011612", "precision=3"]
    """The frequency of the offset (1/total length)"""
    kink_shape: Annotated[float, "step=10.0", "precision=3"]
    """Adjust the offset to the beginning/end"""
    kink_flat: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """How flat the hairs are"""
    kink_extra_steps: Annotated[int, "step=1"]
    """Extra steps for resolution of special kink features"""
    kink_axis_random: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Random variation of the orientation"""
    roughness_1: Annotated[float, "step=0.10000000149011612", "precision=3"]
    """Amount of location dependent roughness"""
    roughness_1_size: Annotated[float, "step=0.10000000149011612", "precision=3"]
    """Size of location dependent roughness"""
    roughness_2: Annotated[float, "step=0.10000000149011612", "precision=3"]
    """Amount of random roughness"""
    roughness_2_size: Annotated[float, "step=0.10000000149011612", "precision=3"]
    """Size of random roughness"""
    roughness_2_threshold: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Amount of particles left untouched by random roughness"""
    roughness_endpoint: Annotated[float, "step=0.10000000149011612", "precision=3"]
    """Amount of endpoint roughness"""
    roughness_end_shape: Annotated[float, "step=10.0", "precision=3"]
    """Shape of endpoint roughness"""
    use_roughness_curve: bool
    """Use a curve to define roughness"""
    @property
    def roughness_curve(self) -> Annotated[Optional['CurveMapping'], "is_animatable=False"]:
        """Curve defining roughness"""
        ...
    child_length: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Length of child paths"""
    child_length_threshold: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Amount of particles left untouched by child path length"""
    child_parting_factor: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Create parting in the children based on parent strands"""
    child_parting_min: Annotated[float, "step=10.0", "precision=3"]
    """Minimum root to tip angle (tip distance/root distance for long hair)"""
    child_parting_max: Annotated[float, "step=10.0", "precision=3"]
    """Maximum root to tip angle (tip distance/root distance for long hair)"""
    branch_threshold: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Threshold of branching"""
    line_length_tail: Annotated[float, "step=0.10000000149011612", "precision=3"]
    """Length of the line's tail"""
    line_length_head: Annotated[float, "step=0.10000000149011612", "precision=3"]
    """Length of the line's head"""
    path_start: Annotated[float, "step=10.0", "precision=3"]
    """Starting time of path"""
    path_end: Annotated[float, "step=10.0", "precision=3"]
    """End time of path"""
    trail_count: Annotated[int, "step=1"]
    """Number of trail particles"""
    keyed_loops: Annotated[int, "step=1"]
    """Number of times the keys are looped"""
    use_modifier_stack: bool
    """Emit particles from mesh with modifiers applied (must use same subdivision surface level for viewport and render for correct results)"""
    instance_collection: Annotated[Optional['Collection'], "is_animatable=False"]
    """Show objects in this collection in place of particles"""
    @property
    def instance_weights(self) -> Annotated[bpy_prop_collection['ParticleDupliWeight'], "is_animatable=False"]:
        """Weights for all of the objects in the instance collection"""
        ...
    @property
    def active_instanceweight(self) -> Annotated[Optional['ParticleDupliWeight'], "is_animatable=False"]:
        ...
    active_instanceweight_index: Annotated[int, "subtype='UNSIGNED'", "step=1"]
    instance_object: Annotated[Optional['Object'], "is_animatable=False"]
    """Show this object in place of particles"""
    @property
    def boids(self) -> Annotated[Optional['BoidSettings'], "is_animatable=False"]:
        ...
    @property
    def fluid(self) -> Annotated[Optional['SPHFluidSettings'], "is_animatable=False"]:
        ...
    @property
    def effector_weights(self) -> Annotated[Optional['EffectorWeights'], "is_animatable=False"]:
        ...
    @property
    def animation_data(self) -> Annotated[Optional['AnimData'], "is_animatable=False"]:
        """Animation data for this data-block"""
        ...
    @property
    def force_field_1(self) -> Annotated[Optional['FieldSettings'], "is_animatable=False"]:
        ...
    @property
    def force_field_2(self) -> Annotated[Optional['FieldSettings'], "is_animatable=False"]:
        ...
    twist: Annotated[float, "step=0.10000000149011612", "precision=3"]
    """Number of turns around parent along the strand"""
    use_twist_curve: bool
    """Use a curve to define twist"""
    @property
    def twist_curve(self) -> Annotated[Optional['CurveMapping'], "is_animatable=False"]:
        """Curve defining twist"""
        ...
    use_close_tip: bool
    """Set tip radius to zero"""
    shape: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Strand shape parameter"""
    root_radius: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.10000000149011612", "precision=2"]
    """Strand diameter width at the root"""
    tip_radius: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.10000000149011612", "precision=2"]
    """Strand diameter width at the tip"""
    radius_scale: Annotated[float, "step=0.10000000149011612", "precision=2"]
    """Multiplier of diameter properties"""
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