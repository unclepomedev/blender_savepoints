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

    goal_min: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Goal minimum, vertex group weights are scaled to match this range"""
    goal_max: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Goal maximum, vertex group weights are scaled to match this range"""
    goal_default: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Default Goal (vertex target position) value, when no Vertex Group used"""
    goal_spring: Annotated[float, "step=10.0", "precision=3"]
    """Goal (vertex target position) spring stiffness"""
    goal_friction: Annotated[float, "step=10.0", "precision=3"]
    """Goal (vertex target position) friction"""
    internal_friction: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]

    collider_friction: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]

    density_target: Annotated[float, "step=10.0", "precision=3"]
    """Maximum density of hair"""
    density_strength: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Influence of target density on the simulation"""
    mass: Annotated[float, "subtype=''", "unit='MASS'", "step=10.0", "precision=3"]
    """The mass of each vertex on the cloth material"""
    vertex_group_mass: Annotated[str, "is_animatable=False"]
    """Vertex Group for pinning of vertices"""
    gravity: Annotated[list[float], "subtype='ACCELERATION'", "unit='ACCELERATION'", "step=10.0", "precision=3"]
    """Gravity or external force vector"""
    air_damping: Annotated[float, "step=10.0", "precision=3"]
    """Air has normally some thickness which slows falling things down"""
    pin_stiffness: Annotated[float, "step=10.0", "precision=3"]
    """Pin (vertex target position) spring stiffness"""
    quality: Annotated[int, "step=1"]
    """Quality of the simulation in steps per frame (higher is better quality but slower)"""
    time_scale: Annotated[float, "step=10.0", "precision=3"]
    """Cloth speed is multiplied by this value"""
    vertex_group_shrink: Annotated[str, "is_animatable=False"]
    """Vertex Group for shrinking cloth"""
    shrink_min: Annotated[float, "subtype='FACTOR'", "step=0.05000000074505806", "precision=3"]
    """Factor by which to shrink cloth"""
    shrink_max: Annotated[float, "subtype='FACTOR'", "step=0.05000000074505806", "precision=3"]
    """Max amount to shrink cloth by"""
    voxel_cell_size: Annotated[float, "subtype='UNSIGNED'", "step=10.0", "precision=3"]
    """Size of the voxel grid cells for interaction effects"""
    tension_damping: Annotated[float, "step=10.0", "precision=3"]
    """Amount of damping in stretching behavior"""
    compression_damping: Annotated[float, "step=10.0", "precision=3"]
    """Amount of damping in compression behavior"""
    shear_damping: Annotated[float, "step=10.0", "precision=3"]
    """Amount of damping in shearing behavior"""
    tension_stiffness: Annotated[float, "step=10.0", "precision=3"]
    """How much the material resists stretching"""
    tension_stiffness_max: Annotated[float, "step=10.0", "precision=3"]
    """Maximum tension stiffness value"""
    compression_stiffness: Annotated[float, "step=10.0", "precision=3"]
    """How much the material resists compression"""
    compression_stiffness_max: Annotated[float, "step=10.0", "precision=3"]
    """Maximum compression stiffness value"""
    shear_stiffness: Annotated[float, "step=10.0", "precision=3"]
    """How much the material resists shearing"""
    shear_stiffness_max: Annotated[float, "step=10.0", "precision=3"]
    """Maximum shear scaling value"""
    sewing_force_max: Annotated[float, "step=10.0", "precision=3"]
    """Maximum sewing force"""
    vertex_group_structural_stiffness: Annotated[str, "is_animatable=False"]
    """Vertex group for fine control over structural stiffness"""
    vertex_group_shear_stiffness: Annotated[str, "is_animatable=False"]
    """Vertex group for fine control over shear stiffness"""
    bending_stiffness: Annotated[float, "step=10.0", "precision=3"]
    """How much the material resists bending"""
    bending_stiffness_max: Annotated[float, "step=10.0", "precision=3"]
    """Maximum bending stiffness value"""
    bending_damping: Annotated[float, "step=10.0", "precision=3"]
    """Amount of damping in bending behavior"""
    use_sewing_springs: Annotated[bool, "is_animatable=False"]
    """Pulls loose edges together"""
    vertex_group_bending: Annotated[str, "is_animatable=False"]
    """Vertex group for fine control over bending stiffness"""
    @property
    def effector_weights(self) -> Annotated[Optional['EffectorWeights'], "is_animatable=False"]:

        ...
    rest_shape_key: Annotated[Optional['ShapeKey'], "is_animatable=False"]
    """Shape key to use the rest spring lengths from"""
    use_dynamic_mesh: Annotated[bool, "is_animatable=False"]
    """Make simulation respect deformations in the base mesh"""
    bending_model: Annotated[Literal['ANGULAR', 'LINEAR'], "is_animatable=False"]
    """Physical model for simulating bending forces"""
    use_internal_springs: Annotated[bool, "is_animatable=False"]
    """Simulate an internal volume structure by creating springs connecting the opposite sides of the mesh"""
    internal_spring_normal_check: Annotated[bool, "is_animatable=False"]
    """Require the points the internal springs connect to have opposite normal directions"""
    internal_spring_max_length: Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]
    """The maximum length an internal spring can have during creation. If the distance between internal points is greater than this, no internal spring will be created between these points. A length of zero means that there is no length limit."""
    internal_spring_max_diversion: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3", "is_animatable=False"]
    """How much the rays used to connect the internal points can diverge from the vertex normal"""
    internal_tension_stiffness: Annotated[float, "step=10.0", "precision=3"]
    """How much the material resists stretching"""
    internal_tension_stiffness_max: Annotated[float, "step=10.0", "precision=3"]
    """Maximum tension stiffness value"""
    internal_compression_stiffness: Annotated[float, "step=10.0", "precision=3"]
    """How much the material resists compression"""
    internal_compression_stiffness_max: Annotated[float, "step=10.0", "precision=3"]
    """Maximum compression stiffness value"""
    vertex_group_intern: Annotated[str, "is_animatable=False"]
    """Vertex group for fine control over the internal spring stiffness"""
    use_pressure: Annotated[bool, "is_animatable=False"]
    """Simulate pressure inside a closed cloth mesh"""
    use_pressure_volume: Annotated[bool, "is_animatable=False"]
    """Use the Target Volume parameter as the initial volume, instead of calculating it from the mesh itself"""
    uniform_pressure_force: Annotated[float, "step=10.0", "precision=3"]
    """The uniform pressure that is constantly applied to the mesh, in units of Pressure Scale. Can be negative."""
    target_volume: Annotated[float, "step=10.0", "precision=3"]
    """The mesh volume where the inner/outer pressure will be the same. If set to zero the change in volume will not affect pressure."""
    pressure_factor: Annotated[float, "step=10.0", "precision=3"]
    """Ambient pressure (kPa) that balances out between the inside and outside of the object when it has the target volume"""
    fluid_density: Annotated[float, "step=0.05000000074505806", "precision=4"]
    """Density (kg/l) of the fluid contained inside the object, used to create a hydrostatic pressure gradient simulating the weight of the internal fluid, or buoyancy from the surrounding fluid if negative"""
    vertex_group_pressure: Annotated[str, "is_animatable=False"]
    """Vertex Group for where to apply pressure. Zero weight means no pressure while a weight of one means full pressure. Faces with a vertex that has zero weight will be excluded from the volume calculation."""