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
from .Collection import Collection
from .EffectorWeights import EffectorWeights
class SoftBodySettings(bpy_struct):
    friction: Annotated[float, "step=10.0", "precision=3"]
    """General media friction for point movements"""
    mass: Annotated[float, "subtype=''", "unit='MASS'", "step=10.0", "precision=3"]
    """General Mass value"""
    vertex_group_mass: Annotated[str, "is_animatable=False"]
    """Control point mass values"""
    gravity: Annotated[float, "subtype='ACCELERATION'", "unit='ACCELERATION'", "step=10.0", "precision=3"]
    """Apply gravitation to point movement"""
    speed: Annotated[float, "step=10.0", "precision=3"]
    """Tweak timing for physics to control frequency and speed"""
    vertex_group_goal: Annotated[str, "is_animatable=False"]
    """Control point weight values"""
    goal_min: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Goal minimum, vertex weights are scaled to match this range"""
    goal_max: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Goal maximum, vertex weights are scaled to match this range"""
    goal_default: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]
    """Default Goal (vertex target position) value"""
    goal_spring: Annotated[float, "step=10.0", "precision=3"]
    """Goal (vertex target position) spring stiffness"""
    goal_friction: Annotated[float, "step=10.0", "precision=3"]
    """Goal (vertex target position) friction"""
    pull: Annotated[float, "step=10.0", "precision=3"]
    """Edge spring stiffness when longer than rest length"""
    push: Annotated[float, "step=10.0", "precision=3"]
    """Edge spring stiffness when shorter than rest length"""
    damping: Annotated[float, "step=10.0", "precision=3"]
    """Edge spring friction"""
    spring_length: Annotated[int, "step=1"]
    """Alter spring length to shrink/blow up (unit %) 0 to disable"""
    aero: Annotated[int, "step=1"]
    """Make edges 'sail'"""
    plastic: Annotated[int, "step=1"]
    """Permanent deform"""
    bend: Annotated[float, "step=10.0", "precision=3"]
    """Bending Stiffness"""
    shear: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Shear Stiffness"""
    vertex_group_spring: Annotated[str, "is_animatable=False"]
    """Control point spring strength values"""
    collision_type: Annotated[Literal['MANUAL', 'AVERAGE', 'MINIMAL', 'MAXIMAL', 'MINMAX'], "is_animatable=False"]
    """Choose Collision Type"""
    ball_size: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3", "is_animatable=False"]
    """Absolute ball size or factor if not manually adjusted"""
    ball_stiff: Annotated[float, "step=10.0", "precision=3"]
    """Ball inflating pressure"""
    ball_damp: Annotated[float, "step=10.0", "precision=3"]
    """Blending to inelastic collision"""
    error_threshold: Annotated[float, "step=10.0", "precision=3"]
    """The Runge-Kutta ODE solver error limit, low value gives more precision, high values speed"""
    step_min: Annotated[int, "step=1"]
    """Minimal # solver steps/frame"""
    step_max: Annotated[int, "step=1"]
    """Maximal # solver steps/frame"""
    choke: Annotated[int, "step=1"]
    """'Viscosity' inside collision target"""
    fuzzy: Annotated[int, "step=1"]
    """Fuzziness while on collision, high values make collision handling faster but less stable"""
    use_auto_step: bool
    """Use velocities for automagic step sizes"""
    use_diagnose: bool
    """Turn on SB diagnose console prints"""
    use_estimate_matrix: bool
    """Store the estimated transforms in the soft body settings"""
    location_mass_center: Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=1.0", "precision=5"]
    """Location of center of mass"""
    rotation_estimate: Annotated[list[float], "subtype='MATRIX'", "step=10.0", "precision=3"]
    """Estimated rotation matrix"""
    scale_estimate: Annotated[list[float], "subtype='MATRIX'", "step=10.0", "precision=3"]
    """Estimated scale matrix"""
    use_goal: Annotated[bool, "is_animatable=False"]
    """Define forces for vertices to stick to animated position"""
    use_edges: Annotated[bool, "is_animatable=False"]
    """Use Edges as springs"""
    use_stiff_quads: Annotated[bool, "is_animatable=False"]
    """Add diagonal springs on 4-gons"""
    use_edge_collision: bool
    """Edges collide too"""
    use_face_collision: bool
    """Faces collide too, can be very slow"""
    aerodynamics_type: Literal['SIMPLE', 'LIFT_FORCE']
    """Method of calculating aerodynamic interaction"""
    use_self_collision: Annotated[bool, "is_animatable=False"]
    """Enable naive vertex ball self collision"""
    collision_collection: Annotated[Optional['Collection'], "is_animatable=False"]
    """Limit colliders to this collection"""
    @property
    def effector_weights(self) -> Annotated[Optional['EffectorWeights'], "is_animatable=False"]:
        ...