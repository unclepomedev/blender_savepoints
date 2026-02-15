# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.FModifierNoise.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .FModifier import FModifier

class FModifierNoise(FModifier):

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
    blend_type: Literal['REPLACE', 'ADD', 'SUBTRACT', 'MULTIPLY']
    """Method of modifying the existing F-Curve"""
    scale: Annotated[float, "step=10.0", "precision=3"]
    """Scaling (in time) of the noise"""
    strength: Annotated[float, "step=10.0", "precision=3"]
    """Amplitude of the noise - the amount that it modifies the underlying curve"""
    phase: Annotated[float, "step=10.0", "precision=3"]
    """A random seed for the noise effect"""
    offset: Annotated[float, "step=10.0", "precision=3"]
    """Time offset for the noise effect"""
    lacunarity: Annotated[float, "step=10.0", "precision=3"]
    """Gap between successive frequencies. Depth needs to be greater than 0 for this to have an effect"""
    roughness: Annotated[float, "step=10.0", "precision=3"]
    """Amount of high frequency detail. Depth needs to be greater than 0 for this to have an effect"""
    depth: Annotated[int, "subtype='UNSIGNED'", "step=1"]
    """Amount of fine level detail present in the noise"""
    use_legacy_noise: bool
    """Use the legacy way of generating noise. Has the issue that it can produce values outside of -1/1"""