# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.ClothSettings.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .EffectorWeights import EffectorWeights
from .ShapeKey import ShapeKey

class ClothSettings(bpy_struct):

    @property
    def goal_min(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Goal minimum, vertex group weights are scaled to match this range"""
        ...
    @goal_min.setter
    def goal_min(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def goal_max(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Goal maximum, vertex group weights are scaled to match this range"""
        ...
    @goal_max.setter
    def goal_max(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def goal_default(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Default Goal (vertex target position) value, when no Vertex Group used"""
        ...
    @goal_default.setter
    def goal_default(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def goal_spring(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Goal (vertex target position) spring stiffness"""
        ...
    @goal_spring.setter
    def goal_spring(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def goal_friction(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Goal (vertex target position) friction"""
        ...
    @goal_friction.setter
    def goal_friction(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def internal_friction(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:

        ...
    @internal_friction.setter
    def internal_friction(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def collider_friction(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:

        ...
    @collider_friction.setter
    def collider_friction(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def density_target(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Maximum density of hair"""
        ...
    @density_target.setter
    def density_target(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def density_strength(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Influence of target density on the simulation"""
        ...
    @density_strength.setter
    def density_strength(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def mass(self) -> Annotated[float, "subtype=''", "unit='MASS'", "step=10.0", "precision=3"]:
        """The mass of each vertex on the cloth material"""
        ...
    @mass.setter
    def mass(self, value: Annotated[float, "subtype=''", "unit='MASS'", "step=10.0", "precision=3"]):
        ...
    @property
    def vertex_group_mass(self) -> Annotated[str, "is_animatable=False"]:
        """Vertex Group for pinning of vertices"""
        ...
    @vertex_group_mass.setter
    def vertex_group_mass(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def gravity(self) -> Annotated[list[float], "subtype='ACCELERATION'", "unit='ACCELERATION'", "step=10.0", "precision=3"]:
        """Gravity or external force vector"""
        ...
    @gravity.setter
    def gravity(self, value: Annotated[list[float], "subtype='ACCELERATION'", "unit='ACCELERATION'", "step=10.0", "precision=3"]):
        ...
    @property
    def air_damping(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Air has normally some thickness which slows falling things down"""
        ...
    @air_damping.setter
    def air_damping(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def pin_stiffness(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Pin (vertex target position) spring stiffness"""
        ...
    @pin_stiffness.setter
    def pin_stiffness(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def quality(self) -> Annotated[int, "step=1"]:
        """Quality of the simulation in steps per frame (higher is better quality but slower)"""
        ...
    @quality.setter
    def quality(self, value: Annotated[int, "step=1"]):
        ...
    @property
    def time_scale(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Cloth speed is multiplied by this value"""
        ...
    @time_scale.setter
    def time_scale(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def vertex_group_shrink(self) -> Annotated[str, "is_animatable=False"]:
        """Vertex Group for shrinking cloth"""
        ...
    @vertex_group_shrink.setter
    def vertex_group_shrink(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def shrink_min(self) -> Annotated[float, "subtype='FACTOR'", "step=0.05000000074505806", "precision=3"]:
        """Factor by which to shrink cloth"""
        ...
    @shrink_min.setter
    def shrink_min(self, value: Annotated[float, "subtype='FACTOR'", "step=0.05000000074505806", "precision=3"]):
        ...
    @property
    def shrink_max(self) -> Annotated[float, "subtype='FACTOR'", "step=0.05000000074505806", "precision=3"]:
        """Max amount to shrink cloth by"""
        ...
    @shrink_max.setter
    def shrink_max(self, value: Annotated[float, "subtype='FACTOR'", "step=0.05000000074505806", "precision=3"]):
        ...
    @property
    def voxel_cell_size(self) -> Annotated[float, "subtype='UNSIGNED'", "step=10.0", "precision=3"]:
        """Size of the voxel grid cells for interaction effects"""
        ...
    @voxel_cell_size.setter
    def voxel_cell_size(self, value: Annotated[float, "subtype='UNSIGNED'", "step=10.0", "precision=3"]):
        ...
    @property
    def tension_damping(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Amount of damping in stretching behavior"""
        ...
    @tension_damping.setter
    def tension_damping(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def compression_damping(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Amount of damping in compression behavior"""
        ...
    @compression_damping.setter
    def compression_damping(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def shear_damping(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Amount of damping in shearing behavior"""
        ...
    @shear_damping.setter
    def shear_damping(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def tension_stiffness(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """How much the material resists stretching"""
        ...
    @tension_stiffness.setter
    def tension_stiffness(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def tension_stiffness_max(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Maximum tension stiffness value"""
        ...
    @tension_stiffness_max.setter
    def tension_stiffness_max(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def compression_stiffness(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """How much the material resists compression"""
        ...
    @compression_stiffness.setter
    def compression_stiffness(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def compression_stiffness_max(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Maximum compression stiffness value"""
        ...
    @compression_stiffness_max.setter
    def compression_stiffness_max(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def shear_stiffness(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """How much the material resists shearing"""
        ...
    @shear_stiffness.setter
    def shear_stiffness(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def shear_stiffness_max(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Maximum shear scaling value"""
        ...
    @shear_stiffness_max.setter
    def shear_stiffness_max(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def sewing_force_max(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Maximum sewing force"""
        ...
    @sewing_force_max.setter
    def sewing_force_max(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def vertex_group_structural_stiffness(self) -> Annotated[str, "is_animatable=False"]:
        """Vertex group for fine control over structural stiffness"""
        ...
    @vertex_group_structural_stiffness.setter
    def vertex_group_structural_stiffness(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def vertex_group_shear_stiffness(self) -> Annotated[str, "is_animatable=False"]:
        """Vertex group for fine control over shear stiffness"""
        ...
    @vertex_group_shear_stiffness.setter
    def vertex_group_shear_stiffness(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def bending_stiffness(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """How much the material resists bending"""
        ...
    @bending_stiffness.setter
    def bending_stiffness(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def bending_stiffness_max(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Maximum bending stiffness value"""
        ...
    @bending_stiffness_max.setter
    def bending_stiffness_max(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def bending_damping(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Amount of damping in bending behavior"""
        ...
    @bending_damping.setter
    def bending_damping(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def use_sewing_springs(self) -> Annotated[bool, "is_animatable=False"]:
        """Pulls loose edges together"""
        ...
    @use_sewing_springs.setter
    def use_sewing_springs(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def vertex_group_bending(self) -> Annotated[str, "is_animatable=False"]:
        """Vertex group for fine control over bending stiffness"""
        ...
    @vertex_group_bending.setter
    def vertex_group_bending(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def effector_weights(self) -> Annotated[Optional['EffectorWeights'], "is_animatable=False"]:

        ...
    @property
    def rest_shape_key(self) -> Annotated[Optional['ShapeKey'], "is_animatable=False"]:
        """Shape key to use the rest spring lengths from"""
        ...
    @rest_shape_key.setter
    def rest_shape_key(self, value: Annotated[Optional['ShapeKey'], "is_animatable=False"]):
        ...
    @property
    def use_dynamic_mesh(self) -> Annotated[bool, "is_animatable=False"]:
        """Make simulation respect deformations in the base mesh"""
        ...
    @use_dynamic_mesh.setter
    def use_dynamic_mesh(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def bending_model(self) -> Annotated[Literal['ANGULAR', 'LINEAR'], "is_animatable=False"]:
        """Physical model for simulating bending forces"""
        ...
    @bending_model.setter
    def bending_model(self, value: Annotated[Literal['ANGULAR', 'LINEAR'], "is_animatable=False"]):
        ...
    @property
    def use_internal_springs(self) -> Annotated[bool, "is_animatable=False"]:
        """Simulate an internal volume structure by creating springs connecting the opposite sides of the mesh"""
        ...
    @use_internal_springs.setter
    def use_internal_springs(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def internal_spring_normal_check(self) -> Annotated[bool, "is_animatable=False"]:
        """Require the points the internal springs connect to have opposite normal directions"""
        ...
    @internal_spring_normal_check.setter
    def internal_spring_normal_check(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def internal_spring_max_length(self) -> Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]:
        """The maximum length an internal spring can have during creation. If the distance between internal points is greater than this, no internal spring will be created between these points. A length of zero means that there is no length limit."""
        ...
    @internal_spring_max_length.setter
    def internal_spring_max_length(self, value: Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def internal_spring_max_diversion(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3", "is_animatable=False"]:
        """How much the rays used to connect the internal points can diverge from the vertex normal"""
        ...
    @internal_spring_max_diversion.setter
    def internal_spring_max_diversion(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def internal_tension_stiffness(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """How much the material resists stretching"""
        ...
    @internal_tension_stiffness.setter
    def internal_tension_stiffness(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def internal_tension_stiffness_max(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Maximum tension stiffness value"""
        ...
    @internal_tension_stiffness_max.setter
    def internal_tension_stiffness_max(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def internal_compression_stiffness(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """How much the material resists compression"""
        ...
    @internal_compression_stiffness.setter
    def internal_compression_stiffness(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def internal_compression_stiffness_max(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Maximum compression stiffness value"""
        ...
    @internal_compression_stiffness_max.setter
    def internal_compression_stiffness_max(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def vertex_group_intern(self) -> Annotated[str, "is_animatable=False"]:
        """Vertex group for fine control over the internal spring stiffness"""
        ...
    @vertex_group_intern.setter
    def vertex_group_intern(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def use_pressure(self) -> Annotated[bool, "is_animatable=False"]:
        """Simulate pressure inside a closed cloth mesh"""
        ...
    @use_pressure.setter
    def use_pressure(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_pressure_volume(self) -> Annotated[bool, "is_animatable=False"]:
        """Use the Target Volume parameter as the initial volume, instead of calculating it from the mesh itself"""
        ...
    @use_pressure_volume.setter
    def use_pressure_volume(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def uniform_pressure_force(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """The uniform pressure that is constantly applied to the mesh, in units of Pressure Scale. Can be negative."""
        ...
    @uniform_pressure_force.setter
    def uniform_pressure_force(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def target_volume(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """The mesh volume where the inner/outer pressure will be the same. If set to zero the change in volume will not affect pressure."""
        ...
    @target_volume.setter
    def target_volume(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def pressure_factor(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Ambient pressure (kPa) that balances out between the inside and outside of the object when it has the target volume"""
        ...
    @pressure_factor.setter
    def pressure_factor(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def fluid_density(self) -> Annotated[float, "step=0.05000000074505806", "precision=4"]:
        """Density (kg/l) of the fluid contained inside the object, used to create a hydrostatic pressure gradient simulating the weight of the internal fluid, or buoyancy from the surrounding fluid if negative"""
        ...
    @fluid_density.setter
    def fluid_density(self, value: Annotated[float, "step=0.05000000074505806", "precision=4"]):
        ...
    @property
    def vertex_group_pressure(self) -> Annotated[str, "is_animatable=False"]:
        """Vertex Group for where to apply pressure. Zero weight means no pressure while a weight of one means full pressure. Faces with a vertex that has zero weight will be excluded from the volume calculation."""
        ...
    @vertex_group_pressure.setter
    def vertex_group_pressure(self, value: Annotated[str, "is_animatable=False"]):
        ...