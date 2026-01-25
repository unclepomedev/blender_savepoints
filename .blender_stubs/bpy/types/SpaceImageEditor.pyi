# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .Space import Space
from .Annotation import Annotation
from .Histogram import Histogram
from .Image import Image
from .ImageUser import ImageUser
from .Mask import Mask
from .Scopes import Scopes
from .SpaceImageOverlay import SpaceImageOverlay
from .SpaceUVEditor import SpaceUVEditor
class SpaceImageEditor(Space):
    type: str
    show_locked_time: bool
    show_region_header: bool
    show_region_tool_header: bool
    show_region_toolbar: bool
    show_region_ui: bool
    show_region_hud: bool
    show_region_asset_shelf: bool
    image: 'Image'
    image_user: 'ImageUser'
    scopes: 'Scopes'
    use_image_pin: bool
    sample_histogram: 'Histogram'
    zoom: float
    zoom_percentage: float
    show_repeat: bool
    show_annotation: bool
    display_channels: str
    show_stereo_3d: bool
    show_sequencer_scene: bool
    uv_editor: 'SpaceUVEditor'
    mode: str
    ui_mode: str
    cursor_location: float
    pivot_point: str
    annotation: 'Annotation'
    use_realtime_update: bool
    show_render: bool
    show_paint: bool
    show_uvedit: bool
    show_maskedit: bool
    show_gizmo: bool
    show_gizmo_navigate: bool
    overlay: 'SpaceImageOverlay'
    mask: 'Mask'
    mask_display_type: str
    show_mask_spline: bool
    show_mask_overlay: bool
    mask_overlay_mode: str
    blend_factor: float