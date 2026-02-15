# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated
from .bpy_prop_collection import bpy_prop_collection

from .FModifier import FModifier
from .FModifierEnvelopeControlPoint import FModifierEnvelopeControlPoint
from .FModifierEnvelopeControlPoints import FModifierEnvelopeControlPoints
class FModifierEnvelope(FModifier):
    name: Annotated[str, "is_animatable=False"]
    """F-Curve Modifier name"""
    @property
    def type(self) -> Literal['NULL', 'GENERATOR', 'FNGENERATOR', 'ENVELOPE', 'CYCLES', 'NOISE', 'LIMITS', 'STEPPED']:
        """F-Curve Modifier Type"""
        ...
    show_expanded: bool
    """F-Curve Modifier's panel is expanded in UI"""
    mute: bool
    """Enable F-Curve modifier evaluation"""
    @property
    def is_valid(self) -> bool:
        """F-Curve Modifier has invalid settings and will not be evaluated"""
        ...
    active: bool
    """F-Curve modifier will show settings in the editor"""
    use_restricted_range: bool
    """F-Curve Modifier is only applied for the specified frame range to help mask off effects in order to chain them"""
    frame_start: Annotated[float, "step=10.0", "precision=3"]
    """Frame that modifier's influence starts (if Restrict Frame Range is in use)"""
    frame_end: Annotated[float, "step=10.0", "precision=3"]
    """Frame that modifier's influence ends (if Restrict Frame Range is in use)"""
    blend_in: Annotated[float, "step=10.0", "precision=3"]
    """Number of frames from start frame for influence to take effect"""
    blend_out: Annotated[float, "step=10.0", "precision=3"]
    """Number of frames from end frame for influence to fade out"""
    use_influence: bool
    """F-Curve Modifier's effects will be tempered by a default factor"""
    influence: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Amount of influence F-Curve Modifier will have when not fading in/out"""
    @property
    def control_points(self) -> Annotated['FModifierEnvelopeControlPoints', "is_animatable=False"]:
        """Control points defining the shape of the envelope"""
        ...
    reference_value: Annotated[float, "step=10.0", "precision=3"]
    """Value that envelope's influence is centered around / based on"""
    default_min: Annotated[float, "step=10.0", "precision=3"]
    """Lower distance from Reference Value for 1:1 default influence"""
    default_max: Annotated[float, "step=10.0", "precision=3"]
    """Upper distance from Reference Value for 1:1 default influence"""