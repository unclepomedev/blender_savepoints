# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.ParticleSettings.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

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
from .bpy_prop_collection import bpy_prop_collection

class ParticleSettings(ID):

    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:
        """Unique data-block ID name (within a same type and library)"""
        ...
    @name.setter
    def name(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
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
    @property
    def use_fake_user(self) -> bool:
        """Save this data-block even if it has no users"""
        ...
    @use_fake_user.setter
    def use_fake_user(self, value: bool) -> None:
        ...
    @property
    def use_extra_user(self) -> bool:
        """Indicates whether an extra user is set or not (mainly for internal/debug usages)"""
        ...
    @use_extra_user.setter
    def use_extra_user(self, value: bool) -> None:
        ...
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
    @property
    def is_runtime_data(self) -> bool:
        """This data-block is runtime data, i.e. it won't be saved in .blend file. Note that e.g. evaluated IDs are always runtime, so this value is only editable for data-blocks in Main data-base."""
        ...
    @is_runtime_data.setter
    def is_runtime_data(self, value: bool) -> None:
        ...
    @property
    def is_editable(self) -> bool:
        """This data-block is editable in the user interface. Linked data-blocks are not editable, except if they were loaded as editable assets."""
        ...
    @property
    def tag(self) -> bool:
        """Tools can use this to tag data for their own purposes (initial state is undefined)"""
        ...
    @tag.setter
    def tag(self, value: bool) -> None:
        ...
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
    @property
    def asset_data(self) -> Annotated[Optional['AssetMetaData'], "is_animatable=False"]:
        """Additional data for an asset data-block"""
        ...
    @asset_data.setter
    def asset_data(self, value: Annotated[Optional['AssetMetaData'], "is_animatable=False"]) -> None:
        ...
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
    @property
    def active_texture(self) -> Annotated[Optional['Texture'], "is_animatable=False"]:
        """Active texture slot being displayed"""
        ...
    @active_texture.setter
    def active_texture(self, value: Annotated[Optional['Texture'], "is_animatable=False"]) -> None:
        ...
    @property
    def active_texture_index(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Index of active texture slot"""
        ...
    @active_texture_index.setter
    def active_texture_index(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1"]) -> None:
        ...
    @property
    def is_fluid(self) -> bool:
        """Particles were created by a fluid simulation"""
        ...
    @property
    def use_react_start_end(self) -> Annotated[bool, "is_animatable=False"]:
        """Give birth to unreacted particles eventually"""
        ...
    @use_react_start_end.setter
    def use_react_start_end(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def use_react_multiple(self) -> Annotated[bool, "is_animatable=False"]:
        """React multiple times"""
        ...
    @use_react_multiple.setter
    def use_react_multiple(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def use_regrow_hair(self) -> bool:
        """Regrow hair for each frame"""
        ...
    @use_regrow_hair.setter
    def use_regrow_hair(self, value: bool) -> None:
        ...
    @property
    def show_unborn(self) -> bool:
        """Show particles before they are emitted"""
        ...
    @show_unborn.setter
    def show_unborn(self, value: bool) -> None:
        ...
    @property
    def use_dead(self) -> bool:
        """Show particles after they have died"""
        ...
    @use_dead.setter
    def use_dead(self, value: bool) -> None:
        ...
    @property
    def use_emit_random(self) -> Annotated[bool, "is_animatable=False"]:
        """Emit in random order of elements"""
        ...
    @use_emit_random.setter
    def use_emit_random(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def use_even_distribution(self) -> Annotated[bool, "is_animatable=False"]:
        """Use even distribution from faces based on face areas or edge lengths"""
        ...
    @use_even_distribution.setter
    def use_even_distribution(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def use_die_on_collision(self) -> Annotated[bool, "is_animatable=False"]:
        """Particles die when they collide with a deflector object"""
        ...
    @use_die_on_collision.setter
    def use_die_on_collision(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def use_size_deflect(self) -> Annotated[bool, "is_animatable=False"]:
        """Use particle's size in deflection"""
        ...
    @use_size_deflect.setter
    def use_size_deflect(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def use_rotations(self) -> Annotated[bool, "is_animatable=False"]:
        """Calculate particle rotations"""
        ...
    @use_rotations.setter
    def use_rotations(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def use_dynamic_rotation(self) -> Annotated[bool, "is_animatable=False"]:
        """Particle rotations are affected by collisions and effectors"""
        ...
    @use_dynamic_rotation.setter
    def use_dynamic_rotation(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def use_multiply_size_mass(self) -> Annotated[bool, "is_animatable=False"]:
        """Multiply mass by particle size"""
        ...
    @use_multiply_size_mass.setter
    def use_multiply_size_mass(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def use_advanced_hair(self) -> Annotated[bool, "is_animatable=False"]:
        """Use full physics calculations for growing hair"""
        ...
    @use_advanced_hair.setter
    def use_advanced_hair(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def lock_boids_to_surface(self) -> bool:
        """Constrain boids to a surface"""
        ...
    @lock_boids_to_surface.setter
    def lock_boids_to_surface(self, value: bool) -> None:
        ...
    @property
    def use_hair_bspline(self) -> bool:
        """Interpolate hair using B-Splines"""
        ...
    @use_hair_bspline.setter
    def use_hair_bspline(self, value: bool) -> None:
        ...
    @property
    def invert_grid(self) -> bool:
        """Invert what is considered object and what is not"""
        ...
    @invert_grid.setter
    def invert_grid(self, value: bool) -> None:
        ...
    @property
    def hexagonal_grid(self) -> bool:
        """Create the grid in a hexagonal pattern"""
        ...
    @hexagonal_grid.setter
    def hexagonal_grid(self, value: bool) -> None:
        ...
    @property
    def apply_effector_to_children(self) -> bool:
        """Apply effectors to children"""
        ...
    @apply_effector_to_children.setter
    def apply_effector_to_children(self, value: bool) -> None:
        ...
    @property
    def create_long_hair_children(self) -> bool:
        """Calculate children that suit long hair well"""
        ...
    @create_long_hair_children.setter
    def create_long_hair_children(self, value: bool) -> None:
        ...
    @property
    def apply_guide_to_children(self) -> bool:

        ...
    @apply_guide_to_children.setter
    def apply_guide_to_children(self, value: bool) -> None:
        ...
    @property
    def use_self_effect(self) -> bool:
        """Particle effectors affect themselves"""
        ...
    @use_self_effect.setter
    def use_self_effect(self, value: bool) -> None:
        ...
    @property
    def type(self) -> Annotated[Literal['EMITTER', 'HAIR'], "is_animatable=False"]:
        """Particle type"""
        ...
    @type.setter
    def type(self, value: Annotated[Literal['EMITTER', 'HAIR'], "is_animatable=False"]) -> None:
        ...
    @property
    def emit_from(self) -> Annotated[Literal['VERT', 'FACE', 'VOLUME'], "is_animatable=False"]:
        """Where to emit particles from"""
        ...
    @emit_from.setter
    def emit_from(self, value: Annotated[Literal['VERT', 'FACE', 'VOLUME'], "is_animatable=False"]) -> None:
        ...
    @property
    def distribution(self) -> Annotated[Literal['JIT', 'RAND', 'GRID'], "is_animatable=False"]:
        """How to distribute particles on selected element"""
        ...
    @distribution.setter
    def distribution(self, value: Annotated[Literal['JIT', 'RAND', 'GRID'], "is_animatable=False"]) -> None:
        ...
    @property
    def physics_type(self) -> Annotated[Literal['NO', 'NEWTON', 'KEYED', 'BOIDS', 'FLUID'], "is_animatable=False"]:
        """Particle physics type"""
        ...
    @physics_type.setter
    def physics_type(self, value: Annotated[Literal['NO', 'NEWTON', 'KEYED', 'BOIDS', 'FLUID'], "is_animatable=False"]) -> None:
        ...
    @property
    def rotation_mode(self) -> Annotated[Literal['NONE', 'NOR', 'NOR_TAN', 'VEL', 'GLOB_X', 'GLOB_Y', 'GLOB_Z', 'OB_X', 'OB_Y', 'OB_Z'], "is_animatable=False"]:
        """Particle orientation axis (does not affect Explode modifier's results)"""
        ...
    @rotation_mode.setter
    def rotation_mode(self, value: Annotated[Literal['NONE', 'NOR', 'NOR_TAN', 'VEL', 'GLOB_X', 'GLOB_Y', 'GLOB_Z', 'OB_X', 'OB_Y', 'OB_Z'], "is_animatable=False"]) -> None:
        ...
    @property
    def angular_velocity_mode(self) -> Annotated[Literal['NONE', 'VELOCITY', 'HORIZONTAL', 'VERTICAL', 'GLOBAL_X', 'GLOBAL_Y', 'GLOBAL_Z', 'RAND'], "is_animatable=False"]:
        """What axis is used to change particle rotation with time"""
        ...
    @angular_velocity_mode.setter
    def angular_velocity_mode(self, value: Annotated[Literal['NONE', 'VELOCITY', 'HORIZONTAL', 'VERTICAL', 'GLOBAL_X', 'GLOBAL_Y', 'GLOBAL_Z', 'RAND'], "is_animatable=False"]) -> None:
        ...
    @property
    def react_event(self) -> Annotated[Literal['DEATH', 'COLLIDE', 'NEAR'], "is_animatable=False"]:
        """The event of target particles to react on"""
        ...
    @react_event.setter
    def react_event(self, value: Annotated[Literal['DEATH', 'COLLIDE', 'NEAR'], "is_animatable=False"]) -> None:
        ...
    @property
    def show_guide_hairs(self) -> bool:
        """Show guide hairs"""
        ...
    @show_guide_hairs.setter
    def show_guide_hairs(self, value: bool) -> None:
        ...
    @property
    def show_hair_grid(self) -> bool:
        """Show hair simulation grid"""
        ...
    @show_hair_grid.setter
    def show_hair_grid(self, value: bool) -> None:
        ...
    @property
    def show_velocity(self) -> bool:
        """Show particle velocity"""
        ...
    @show_velocity.setter
    def show_velocity(self, value: bool) -> None:
        ...
    @property
    def show_size(self) -> bool:
        """Show particle size"""
        ...
    @show_size.setter
    def show_size(self, value: bool) -> None:
        ...
    @property
    def show_health(self) -> bool:
        """Display boid health"""
        ...
    @show_health.setter
    def show_health(self, value: bool) -> None:
        ...
    @property
    def use_absolute_path_time(self) -> bool:
        """Path timing is in absolute frames"""
        ...
    @use_absolute_path_time.setter
    def use_absolute_path_time(self, value: bool) -> None:
        ...
    @property
    def use_parent_particles(self) -> bool:
        """Render parent particles"""
        ...
    @use_parent_particles.setter
    def use_parent_particles(self, value: bool) -> None:
        ...
    @property
    def show_number(self) -> bool:
        """Show particle number"""
        ...
    @show_number.setter
    def show_number(self, value: bool) -> None:
        ...
    @property
    def use_collection_pick_random(self) -> bool:
        """Pick objects from collection randomly"""
        ...
    @use_collection_pick_random.setter
    def use_collection_pick_random(self, value: bool) -> None:
        ...
    @property
    def use_collection_count(self) -> bool:
        """Use object multiple times in the same collection"""
        ...
    @use_collection_count.setter
    def use_collection_count(self, value: bool) -> None:
        ...
    @property
    def use_global_instance(self) -> bool:
        """Use object's global coordinates for duplication"""
        ...
    @use_global_instance.setter
    def use_global_instance(self, value: bool) -> None:
        ...
    @property
    def use_rotation_instance(self) -> bool:
        """Use object's rotation for duplication (global x-axis is aligned particle rotation axis)"""
        ...
    @use_rotation_instance.setter
    def use_rotation_instance(self, value: bool) -> None:
        ...
    @property
    def use_scale_instance(self) -> bool:
        """Use object's scale for duplication"""
        ...
    @use_scale_instance.setter
    def use_scale_instance(self, value: bool) -> None:
        ...
    @property
    def use_render_adaptive(self) -> bool:
        """Display steps of the particle path"""
        ...
    @use_render_adaptive.setter
    def use_render_adaptive(self, value: bool) -> None:
        ...
    @property
    def use_velocity_length(self) -> bool:
        """Multiply line length by particle speed"""
        ...
    @use_velocity_length.setter
    def use_velocity_length(self, value: bool) -> None:
        ...
    @property
    def use_whole_collection(self) -> bool:
        """Use whole collection at once"""
        ...
    @use_whole_collection.setter
    def use_whole_collection(self, value: bool) -> None:
        ...
    @property
    def use_strand_primitive(self) -> bool:
        """Use the strand primitive for rendering"""
        ...
    @use_strand_primitive.setter
    def use_strand_primitive(self, value: bool) -> None:
        ...
    @property
    def display_method(self) -> Literal['NONE', 'RENDER', 'DOT', 'CIRC', 'CROSS', 'AXIS']:
        """How particles are displayed in viewport"""
        ...
    @display_method.setter
    def display_method(self, value: Literal['NONE', 'RENDER', 'DOT', 'CIRC', 'CROSS', 'AXIS']) -> None:
        ...
    @property
    def render_type(self) -> Literal['NONE', 'HALO', 'LINE', 'PATH', 'OBJECT', 'COLLECTION']:
        """How particles are rendered"""
        ...
    @render_type.setter
    def render_type(self, value: Literal['NONE', 'HALO', 'LINE', 'PATH', 'OBJECT', 'COLLECTION']) -> None:
        ...
    @property
    def display_color(self) -> Literal['NONE', 'MATERIAL', 'VELOCITY', 'ACCELERATION']:
        """Display additional particle data as a color"""
        ...
    @display_color.setter
    def display_color(self, value: Literal['NONE', 'MATERIAL', 'VELOCITY', 'ACCELERATION']) -> None:
        ...
    @property
    def display_size(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=1.0", "precision=-1"]:
        """Size of particles on viewport"""
        ...
    @display_size.setter
    def display_size(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=1.0", "precision=-1"]) -> None:
        ...
    @property
    def child_type(self) -> Literal['NONE', 'SIMPLE', 'INTERPOLATED']:
        """Create child particles"""
        ...
    @child_type.setter
    def child_type(self, value: Literal['NONE', 'SIMPLE', 'INTERPOLATED']) -> None:
        ...
    @property
    def display_step(self) -> Annotated[int, "step=1"]:
        """How many steps paths are displayed with (power of 2)"""
        ...
    @display_step.setter
    def display_step(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def render_step(self) -> Annotated[int, "step=1"]:
        """How many steps paths are rendered with (power of 2)"""
        ...
    @render_step.setter
    def render_step(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def hair_step(self) -> Annotated[int, "step=1", "is_animatable=False"]:
        """Number of hair segments"""
        ...
    @hair_step.setter
    def hair_step(self, value: Annotated[int, "step=1", "is_animatable=False"]) -> None:
        ...
    @property
    def bending_random(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Random stiffness of hairs"""
        ...
    @bending_random.setter
    def bending_random(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def keys_step(self) -> Annotated[int, "step=1"]:

        ...
    @keys_step.setter
    def keys_step(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def adaptive_angle(self) -> Annotated[int, "step=1"]:
        """How many degrees path has to curve to make another render segment"""
        ...
    @adaptive_angle.setter
    def adaptive_angle(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def adaptive_pixel(self) -> Annotated[int, "step=1"]:
        """How many pixels path has to cover to make another render segment"""
        ...
    @adaptive_pixel.setter
    def adaptive_pixel(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def display_percentage(self) -> Annotated[int, "subtype='PERCENTAGE'", "step=1"]:
        """Percentage of particles to display in 3D view"""
        ...
    @display_percentage.setter
    def display_percentage(self, value: Annotated[int, "subtype='PERCENTAGE'", "step=1"]) -> None:
        ...
    @property
    def material(self) -> Annotated[int, "step=1"]:
        """Index of material slot used for rendering particles"""
        ...
    @material.setter
    def material(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def material_slot(self) -> Literal['DEFAULT']:
        """Material slot used for rendering particles"""
        ...
    @material_slot.setter
    def material_slot(self, value: Literal['DEFAULT']) -> None:
        ...
    @property
    def integrator(self) -> Literal['EULER', 'VERLET', 'MIDPOINT', 'RK4']:
        """Algorithm used to calculate physics, from the fastest to the most stable and accurate: Midpoint, Euler, Verlet, RK4"""
        ...
    @integrator.setter
    def integrator(self, value: Literal['EULER', 'VERLET', 'MIDPOINT', 'RK4']) -> None:
        ...
    @property
    def kink(self) -> Literal['NO', 'CURL', 'RADIAL', 'WAVE', 'BRAID', 'SPIRAL']:
        """Type of periodic offset on the path"""
        ...
    @kink.setter
    def kink(self, value: Literal['NO', 'CURL', 'RADIAL', 'WAVE', 'BRAID', 'SPIRAL']) -> None:
        ...
    @property
    def kink_axis(self) -> Literal['X', 'Y', 'Z']:
        """Which axis to use for offset"""
        ...
    @kink_axis.setter
    def kink_axis(self, value: Literal['X', 'Y', 'Z']) -> None:
        ...
    @property
    def color_maximum(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Maximum length of the particle color vector"""
        ...
    @color_maximum.setter
    def color_maximum(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def frame_start(self) -> Annotated[float, "subtype='TIME'", "unit='TIME'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Frame number to start emitting particles"""
        ...
    @frame_start.setter
    def frame_start(self, value: Annotated[float, "subtype='TIME'", "unit='TIME'", "step=10.0", "precision=3", "is_animatable=False"]) -> None:
        ...
    @property
    def frame_end(self) -> Annotated[float, "subtype='TIME'", "unit='TIME'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Frame number to stop emitting particles"""
        ...
    @frame_end.setter
    def frame_end(self, value: Annotated[float, "subtype='TIME'", "unit='TIME'", "step=10.0", "precision=3", "is_animatable=False"]) -> None:
        ...
    @property
    def lifetime(self) -> Annotated[float, "subtype='TIME'", "unit='TIME'", "step=10.0", "precision=3"]:
        """Life span of the particles"""
        ...
    @lifetime.setter
    def lifetime(self, value: Annotated[float, "subtype='TIME'", "unit='TIME'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def lifetime_random(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Give the particle life a random variation"""
        ...
    @lifetime_random.setter
    def lifetime_random(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def time_tweak(self) -> Annotated[float, "step=1.0", "precision=3"]:
        """A multiplier for physics timestep (1.0 means one frame = 1/25 seconds)"""
        ...
    @time_tweak.setter
    def time_tweak(self, value: Annotated[float, "step=1.0", "precision=3"]) -> None:
        ...
    @property
    def timestep(self) -> Annotated[float, "step=1.0", "precision=3"]:
        """The simulation timestep per frame (seconds per frame)"""
        ...
    @timestep.setter
    def timestep(self, value: Annotated[float, "step=1.0", "precision=3"]) -> None:
        ...
    @property
    def use_adaptive_subframes(self) -> bool:
        """Automatically set the number of subframes"""
        ...
    @use_adaptive_subframes.setter
    def use_adaptive_subframes(self, value: bool) -> None:
        ...
    @property
    def subframes(self) -> Annotated[int, "step=1"]:
        """Subframes to simulate for improved stability and finer granularity simulations (dt = timestep / (subframes + 1))"""
        ...
    @subframes.setter
    def subframes(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def courant_target(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """The relative distance a particle can move before requiring more subframes (target Courant number); 0.01 to 0.3 is the recommended range"""
        ...
    @courant_target.setter
    def courant_target(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def jitter_factor(self) -> Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]:
        """Amount of jitter applied to the sampling"""
        ...
    @jitter_factor.setter
    def jitter_factor(self, value: Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]) -> None:
        ...
    @property
    def effect_hair(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Hair stiffness for effectors"""
        ...
    @effect_hair.setter
    def effect_hair(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def count(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]:
        """Total number of particles"""
        ...
    @count.setter
    def count(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]) -> None:
        ...
    @property
    def userjit(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]:
        """Emission locations per face (0 = automatic)"""
        ...
    @userjit.setter
    def userjit(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]) -> None:
        ...
    @property
    def grid_resolution(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]:
        """The resolution of the particle grid"""
        ...
    @grid_resolution.setter
    def grid_resolution(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]) -> None:
        ...
    @property
    def grid_random(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Add random offset to the grid locations"""
        ...
    @grid_random.setter
    def grid_random(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def effector_amount(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """How many particles are effectors (0 is all particles)"""
        ...
    @effector_amount.setter
    def effector_amount(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1"]) -> None:
        ...
    @property
    def normal_factor(self) -> Annotated[float, "subtype='VELOCITY'", "unit='VELOCITY'", "step=1.0", "precision=3"]:
        """Let the surface normal give the particle a starting velocity"""
        ...
    @normal_factor.setter
    def normal_factor(self, value: Annotated[float, "subtype='VELOCITY'", "unit='VELOCITY'", "step=1.0", "precision=3"]) -> None:
        ...
    @property
    def object_factor(self) -> Annotated[float, "step=0.10000000149011612", "precision=3"]:
        """Let the object give the particle a starting velocity"""
        ...
    @object_factor.setter
    def object_factor(self, value: Annotated[float, "step=0.10000000149011612", "precision=3"]) -> None:
        ...
    @property
    def factor_random(self) -> Annotated[float, "step=1.0", "precision=3"]:
        """Give the starting velocity a random variation"""
        ...
    @factor_random.setter
    def factor_random(self, value: Annotated[float, "step=1.0", "precision=3"]) -> None:
        ...
    @property
    def particle_factor(self) -> Annotated[float, "step=0.10000000149011612", "precision=3"]:
        """Let the target particle give the particle a starting velocity"""
        ...
    @particle_factor.setter
    def particle_factor(self, value: Annotated[float, "step=0.10000000149011612", "precision=3"]) -> None:
        ...
    @property
    def tangent_factor(self) -> Annotated[float, "subtype='VELOCITY'", "unit='VELOCITY'", "step=1.0", "precision=2"]:
        """Let the surface tangent give the particle a starting velocity"""
        ...
    @tangent_factor.setter
    def tangent_factor(self, value: Annotated[float, "subtype='VELOCITY'", "unit='VELOCITY'", "step=1.0", "precision=2"]) -> None:
        ...
    @property
    def tangent_phase(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Rotate the surface tangent"""
        ...
    @tangent_phase.setter
    def tangent_phase(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def reactor_factor(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Let the vector away from the target particle's location give the particle a starting velocity"""
        ...
    @reactor_factor.setter
    def reactor_factor(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def object_align_factor(self) -> Annotated[list[float], "subtype='VELOCITY'", "unit='VELOCITY'", "step=1.0", "precision=3"]:
        """Let the emitter object orientation give the particle a starting velocity"""
        ...
    @object_align_factor.setter
    def object_align_factor(self, value: Annotated[list[float], "subtype='VELOCITY'", "unit='VELOCITY'", "step=1.0", "precision=3"]) -> None:
        ...
    @property
    def angular_velocity_factor(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Angular velocity amount (in radians per second)"""
        ...
    @angular_velocity_factor.setter
    def angular_velocity_factor(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def phase_factor(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Rotation around the chosen orientation axis"""
        ...
    @phase_factor.setter
    def phase_factor(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def rotation_factor_random(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Randomize particle orientation"""
        ...
    @rotation_factor_random.setter
    def rotation_factor_random(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def phase_factor_random(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Randomize rotation around the chosen orientation axis"""
        ...
    @phase_factor_random.setter
    def phase_factor_random(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def hair_length(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=1.0", "precision=3"]:
        """Length of the hair"""
        ...
    @hair_length.setter
    def hair_length(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=1.0", "precision=3"]) -> None:
        ...
    @property
    def mass(self) -> Annotated[float, "subtype=''", "unit='MASS'", "step=1.0", "precision=4"]:
        """Mass of the particles"""
        ...
    @mass.setter
    def mass(self, value: Annotated[float, "subtype=''", "unit='MASS'", "step=1.0", "precision=4"]) -> None:
        ...
    @property
    def particle_size(self) -> Annotated[float, "step=1.0", "precision=3"]:
        """The size of the particles"""
        ...
    @particle_size.setter
    def particle_size(self, value: Annotated[float, "step=1.0", "precision=3"]) -> None:
        ...
    @property
    def size_random(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Give the particle size a random variation"""
        ...
    @size_random.setter
    def size_random(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def collision_collection(self) -> Annotated[Optional['Collection'], "is_animatable=False"]:
        """Limit colliders to this collection"""
        ...
    @collision_collection.setter
    def collision_collection(self, value: Annotated[Optional['Collection'], "is_animatable=False"]) -> None:
        ...
    @property
    def drag_factor(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Amount of air drag"""
        ...
    @drag_factor.setter
    def drag_factor(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def brownian_factor(self) -> Annotated[float, "step=1.0", "precision=3"]:
        """Amount of random, erratic particle movement"""
        ...
    @brownian_factor.setter
    def brownian_factor(self, value: Annotated[float, "step=1.0", "precision=3"]) -> None:
        ...
    @property
    def damping(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Amount of damping"""
        ...
    @damping.setter
    def damping(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def length_random(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Give path length a random variation"""
        ...
    @length_random.setter
    def length_random(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def child_percent(self) -> Annotated[int, "step=1"]:
        """Number of children per parent"""
        ...
    @child_percent.setter
    def child_percent(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def rendered_child_count(self) -> Annotated[int, "step=1"]:
        """Number of children per parent for rendering"""
        ...
    @rendered_child_count.setter
    def rendered_child_count(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def virtual_parents(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Relative amount of virtual parents"""
        ...
    @virtual_parents.setter
    def virtual_parents(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def child_size(self) -> Annotated[float, "step=0.10000000149011612", "precision=3"]:
        """A multiplier for the child particle size"""
        ...
    @child_size.setter
    def child_size(self, value: Annotated[float, "step=0.10000000149011612", "precision=3"]) -> None:
        ...
    @property
    def child_size_random(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Random variation to the size of the child particles"""
        ...
    @child_size_random.setter
    def child_size_random(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def child_radius(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.10000000149011612", "precision=3"]:
        """Radius of children around parent"""
        ...
    @child_radius.setter
    def child_radius(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.10000000149011612", "precision=3"]) -> None:
        ...
    @property
    def child_roundness(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Roundness of children around parent"""
        ...
    @child_roundness.setter
    def child_roundness(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def clump_factor(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Amount of clumping"""
        ...
    @clump_factor.setter
    def clump_factor(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def clump_shape(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Shape of clumping"""
        ...
    @clump_shape.setter
    def clump_shape(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def use_clump_curve(self) -> bool:
        """Use a curve to define clump tapering"""
        ...
    @use_clump_curve.setter
    def use_clump_curve(self, value: bool) -> None:
        ...
    @property
    def clump_curve(self) -> Annotated[Optional['CurveMapping'], "is_animatable=False"]:
        """Curve defining clump tapering"""
        ...
    @property
    def use_clump_noise(self) -> bool:
        """Create random clumps around the parent"""
        ...
    @use_clump_noise.setter
    def use_clump_noise(self, value: bool) -> None:
        ...
    @property
    def clump_noise_size(self) -> Annotated[float, "step=0.10000000149011612", "precision=3"]:
        """Size of clump noise"""
        ...
    @clump_noise_size.setter
    def clump_noise_size(self, value: Annotated[float, "step=0.10000000149011612", "precision=3"]) -> None:
        ...
    @property
    def kink_amplitude(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.10000000149011612", "precision=3"]:
        """The amplitude of the offset"""
        ...
    @kink_amplitude.setter
    def kink_amplitude(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.10000000149011612", "precision=3"]) -> None:
        ...
    @property
    def kink_amplitude_clump(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """How much clump affects kink amplitude"""
        ...
    @kink_amplitude_clump.setter
    def kink_amplitude_clump(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def kink_amplitude_random(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Random variation of the amplitude"""
        ...
    @kink_amplitude_random.setter
    def kink_amplitude_random(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def kink_frequency(self) -> Annotated[float, "step=0.10000000149011612", "precision=3"]:
        """The frequency of the offset (1/total length)"""
        ...
    @kink_frequency.setter
    def kink_frequency(self, value: Annotated[float, "step=0.10000000149011612", "precision=3"]) -> None:
        ...
    @property
    def kink_shape(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Adjust the offset to the beginning/end"""
        ...
    @kink_shape.setter
    def kink_shape(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def kink_flat(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """How flat the hairs are"""
        ...
    @kink_flat.setter
    def kink_flat(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def kink_extra_steps(self) -> Annotated[int, "step=1"]:
        """Extra steps for resolution of special kink features"""
        ...
    @kink_extra_steps.setter
    def kink_extra_steps(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def kink_axis_random(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Random variation of the orientation"""
        ...
    @kink_axis_random.setter
    def kink_axis_random(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def roughness_1(self) -> Annotated[float, "step=0.10000000149011612", "precision=3"]:
        """Amount of location dependent roughness"""
        ...
    @roughness_1.setter
    def roughness_1(self, value: Annotated[float, "step=0.10000000149011612", "precision=3"]) -> None:
        ...
    @property
    def roughness_1_size(self) -> Annotated[float, "step=0.10000000149011612", "precision=3"]:
        """Size of location dependent roughness"""
        ...
    @roughness_1_size.setter
    def roughness_1_size(self, value: Annotated[float, "step=0.10000000149011612", "precision=3"]) -> None:
        ...
    @property
    def roughness_2(self) -> Annotated[float, "step=0.10000000149011612", "precision=3"]:
        """Amount of random roughness"""
        ...
    @roughness_2.setter
    def roughness_2(self, value: Annotated[float, "step=0.10000000149011612", "precision=3"]) -> None:
        ...
    @property
    def roughness_2_size(self) -> Annotated[float, "step=0.10000000149011612", "precision=3"]:
        """Size of random roughness"""
        ...
    @roughness_2_size.setter
    def roughness_2_size(self, value: Annotated[float, "step=0.10000000149011612", "precision=3"]) -> None:
        ...
    @property
    def roughness_2_threshold(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Amount of particles left untouched by random roughness"""
        ...
    @roughness_2_threshold.setter
    def roughness_2_threshold(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def roughness_endpoint(self) -> Annotated[float, "step=0.10000000149011612", "precision=3"]:
        """Amount of endpoint roughness"""
        ...
    @roughness_endpoint.setter
    def roughness_endpoint(self, value: Annotated[float, "step=0.10000000149011612", "precision=3"]) -> None:
        ...
    @property
    def roughness_end_shape(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Shape of endpoint roughness"""
        ...
    @roughness_end_shape.setter
    def roughness_end_shape(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def use_roughness_curve(self) -> bool:
        """Use a curve to define roughness"""
        ...
    @use_roughness_curve.setter
    def use_roughness_curve(self, value: bool) -> None:
        ...
    @property
    def roughness_curve(self) -> Annotated[Optional['CurveMapping'], "is_animatable=False"]:
        """Curve defining roughness"""
        ...
    @property
    def child_length(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Length of child paths"""
        ...
    @child_length.setter
    def child_length(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def child_length_threshold(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Amount of particles left untouched by child path length"""
        ...
    @child_length_threshold.setter
    def child_length_threshold(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def child_parting_factor(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Create parting in the children based on parent strands"""
        ...
    @child_parting_factor.setter
    def child_parting_factor(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def child_parting_min(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Minimum root to tip angle (tip distance/root distance for long hair)"""
        ...
    @child_parting_min.setter
    def child_parting_min(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def child_parting_max(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Maximum root to tip angle (tip distance/root distance for long hair)"""
        ...
    @child_parting_max.setter
    def child_parting_max(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def branch_threshold(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Threshold of branching"""
        ...
    @branch_threshold.setter
    def branch_threshold(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def line_length_tail(self) -> Annotated[float, "step=0.10000000149011612", "precision=3"]:
        """Length of the line's tail"""
        ...
    @line_length_tail.setter
    def line_length_tail(self, value: Annotated[float, "step=0.10000000149011612", "precision=3"]) -> None:
        ...
    @property
    def line_length_head(self) -> Annotated[float, "step=0.10000000149011612", "precision=3"]:
        """Length of the line's head"""
        ...
    @line_length_head.setter
    def line_length_head(self, value: Annotated[float, "step=0.10000000149011612", "precision=3"]) -> None:
        ...
    @property
    def path_start(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Starting time of path"""
        ...
    @path_start.setter
    def path_start(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def path_end(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """End time of path"""
        ...
    @path_end.setter
    def path_end(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def trail_count(self) -> Annotated[int, "step=1"]:
        """Number of trail particles"""
        ...
    @trail_count.setter
    def trail_count(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def keyed_loops(self) -> Annotated[int, "step=1"]:
        """Number of times the keys are looped"""
        ...
    @keyed_loops.setter
    def keyed_loops(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def use_modifier_stack(self) -> bool:
        """Emit particles from mesh with modifiers applied (must use same subdivision surface level for viewport and render for correct results)"""
        ...
    @use_modifier_stack.setter
    def use_modifier_stack(self, value: bool) -> None:
        ...
    @property
    def instance_collection(self) -> Annotated[Optional['Collection'], "is_animatable=False"]:
        """Show objects in this collection in place of particles"""
        ...
    @instance_collection.setter
    def instance_collection(self, value: Annotated[Optional['Collection'], "is_animatable=False"]) -> None:
        ...
    @property
    def instance_weights(self) -> Annotated[bpy_prop_collection['ParticleDupliWeight'], "is_animatable=False"]:
        """Weights for all of the objects in the instance collection"""
        ...
    @property
    def active_instanceweight(self) -> Annotated[Optional['ParticleDupliWeight'], "is_animatable=False"]:

        ...
    @property
    def active_instanceweight_index(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:

        ...
    @active_instanceweight_index.setter
    def active_instanceweight_index(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1"]) -> None:
        ...
    @property
    def instance_object(self) -> Annotated[Optional['Object'], "is_animatable=False"]:
        """Show this object in place of particles"""
        ...
    @instance_object.setter
    def instance_object(self, value: Annotated[Optional['Object'], "is_animatable=False"]) -> None:
        ...
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
    @property
    def twist(self) -> Annotated[float, "step=0.10000000149011612", "precision=3"]:
        """Number of turns around parent along the strand"""
        ...
    @twist.setter
    def twist(self, value: Annotated[float, "step=0.10000000149011612", "precision=3"]) -> None:
        ...
    @property
    def use_twist_curve(self) -> bool:
        """Use a curve to define twist"""
        ...
    @use_twist_curve.setter
    def use_twist_curve(self, value: bool) -> None:
        ...
    @property
    def twist_curve(self) -> Annotated[Optional['CurveMapping'], "is_animatable=False"]:
        """Curve defining twist"""
        ...
    @property
    def use_close_tip(self) -> bool:
        """Set tip radius to zero"""
        ...
    @use_close_tip.setter
    def use_close_tip(self, value: bool) -> None:
        ...
    @property
    def shape(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Strand shape parameter"""
        ...
    @shape.setter
    def shape(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def root_radius(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.10000000149011612", "precision=2"]:
        """Strand diameter width at the root"""
        ...
    @root_radius.setter
    def root_radius(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.10000000149011612", "precision=2"]) -> None:
        ...
    @property
    def tip_radius(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.10000000149011612", "precision=2"]:
        """Strand diameter width at the tip"""
        ...
    @tip_radius.setter
    def tip_radius(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.10000000149011612", "precision=2"]) -> None:
        ...
    @property
    def radius_scale(self) -> Annotated[float, "step=0.10000000149011612", "precision=2"]:
        """Multiplier of diameter properties"""
        ...
    @radius_scale.setter
    def radius_scale(self, value: Annotated[float, "step=0.10000000149011612", "precision=2"]) -> None:
        ...
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