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
class ColorManagedSequencerColorspaceSettings(bpy_struct):
    name: Literal['ACES 1.3 sRGB', 'ACES 2.0 sRGB', 'ACES2065-1', 'ACEScc', 'ACEScct', 'ACEScg', 'AgX Base sRGB', 'AgX Log', 'Display P3', 'Filmic Log', 'Filmic sRGB', 'Khronos PBR Neutral sRGB', 'Linear CIE-XYZ D65', 'Linear CIE-XYZ E', 'Linear DCI-P3 D65', 'Linear FilmLight E-Gamut', 'Linear Rec.2020', 'Linear Rec.709', 'Non-Color', 'Rec.1886', 'Rec.2020', 'Rec.2100-HLG', 'Rec.2100-PQ', 'sRGB', 'scene_linear']
    """Color space that the sequencer operates in"""