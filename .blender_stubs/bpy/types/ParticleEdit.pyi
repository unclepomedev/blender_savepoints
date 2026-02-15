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
from .Object import Object
from .ParticleBrush import ParticleBrush
class ParticleEdit(bpy_struct):
    tool: Annotated[Literal['COMB', 'SMOOTH', 'ADD', 'LENGTH', 'PUFF', 'CUT', 'WEIGHT'], "is_animatable=False"]
    select_mode: Annotated[Literal['PATH', 'POINT', 'TIP'], "is_animatable=False"]
    """Particle select and display mode"""
    use_preserve_length: Annotated[bool, "is_animatable=False"]
    """Keep path lengths constant"""
    use_preserve_root: Annotated[bool, "is_animatable=False"]
    """Keep root keys unmodified"""
    use_emitter_deflect: Annotated[bool, "is_animatable=False"]
    """Keep paths from intersecting the emitter"""
    emitter_distance: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3", "is_animatable=False"]
    """Distance to keep particles away from the emitter"""
    use_fade_time: Annotated[bool, "is_animatable=False"]
    """Fade paths and keys further away from current frame"""
    use_auto_velocity: Annotated[bool, "is_animatable=False"]
    """Calculate point velocities automatically"""
    show_particles: Annotated[bool, "is_animatable=False"]
    """Display actual particles"""
    use_default_interpolate: Annotated[bool, "is_animatable=False"]
    """Interpolate new particles from the existing ones"""
    default_key_count: Annotated[int, "step=10", "is_animatable=False"]
    """How many keys to make new particles with"""
    @property
    def brush(self) -> Annotated[Optional['ParticleBrush'], "is_animatable=False"]:
        ...
    display_step: Annotated[int, "step=1", "is_animatable=False"]
    """How many steps to display the path with"""
    fade_frames: Annotated[int, "step=1", "is_animatable=False"]
    """How many frames to fade"""
    type: Annotated[Literal['PARTICLES', 'SOFT_BODY', 'CLOTH'], "is_animatable=False"]
    @property
    def is_editable(self) -> Annotated[bool, "is_animatable=False"]:
        """A valid edit mode exists"""
        ...
    @property
    def is_hair(self) -> Annotated[bool, "is_animatable=False"]:
        """Editing hair"""
        ...
    @property
    def object(self) -> Annotated[Optional['Object'], "is_animatable=False"]:
        """The edited object"""
        ...
    shape_object: Annotated[Optional['Object'], "is_animatable=False"]
    """Outer shape to use for tools"""