# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated
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
    @property
    def type(self) -> Literal['EMPTY', 'VIEW_3D', 'IMAGE_EDITOR', 'NODE_EDITOR', 'SEQUENCE_EDITOR', 'CLIP_EDITOR', 'DOPESHEET_EDITOR', 'GRAPH_EDITOR', 'NLA_EDITOR', 'TEXT_EDITOR', 'CONSOLE', 'INFO', 'TOPBAR', 'STATUSBAR', 'OUTLINER', 'PROPERTIES', 'FILE_BROWSER', 'SPREADSHEET', 'PREFERENCES']:
        """Space data type"""
        ...
    show_locked_time: bool
    """Synchronize the visible timeline range with other time-based editors"""
    show_region_header: bool
    show_region_tool_header: bool
    show_region_toolbar: bool
    show_region_ui: bool
    show_region_hud: bool
    show_region_asset_shelf: bool
    """Display a region with assets that may currently be relevant (such as brushes in paint modes, or poses in Pose Mode)"""
    image: Annotated[Optional['Image'], "is_animatable=False"]
    """Image displayed and edited in this space"""
    @property
    def image_user(self) -> Annotated['ImageUser', "is_animatable=False"]:
        """Parameters defining which layer, pass and frame of the image is displayed"""
        ...
    @property
    def scopes(self) -> Annotated[Optional['Scopes'], "is_animatable=False"]:
        """Scopes to visualize image statistics"""
        ...
    use_image_pin: bool
    """Display current image regardless of object selection"""
    @property
    def sample_histogram(self) -> Annotated[Optional['Histogram'], "is_animatable=False"]:
        """Sampled colors along line"""
        ...
    @property
    def zoom(self) -> Annotated[list[float], "step=10.0", "precision=3"]:
        """Zoom factor"""
        ...
    zoom_percentage: Annotated[float, "subtype='PERCENTAGE'", "step=100.0", "precision=0"]
    """Zoom percentage"""
    show_repeat: bool
    """Display the image repeated outside of the main view"""
    show_annotation: bool
    """Show annotations for this view"""
    display_channels: Literal['COLOR_ALPHA', 'COLOR', 'ALPHA', 'Z_BUFFER', 'RED', 'GREEN', 'BLUE']
    """Channels of the image to display"""
    show_stereo_3d: bool
    """Display the image in Stereo 3D"""
    show_sequencer_scene: bool
    """Display the render result for the sequencer scene instead of the active scene"""
    @property
    def uv_editor(self) -> Annotated['SpaceUVEditor', "is_animatable=False"]:
        """UV editor settings"""
        ...
    mode: Literal['VIEW', 'UV', 'PAINT', 'MASK']
    """Editing context being displayed"""
    ui_mode: Literal['VIEW', 'PAINT', 'MASK']
    """Editing context being displayed"""
    cursor_location: Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]
    """2D cursor location for this view"""
    pivot_point: Literal['BOUNDING_BOX_CENTER', 'CURSOR', 'INDIVIDUAL_ORIGINS', 'MEDIAN_POINT', 'ACTIVE_ELEMENT']
    """Rotation/Scaling Pivot"""
    annotation: Annotated[Optional['Annotation'], "is_animatable=False"]
    """Annotation data for this space"""
    use_realtime_update: bool
    """Update other affected window spaces automatically to reflect changes during interactive operations such as transform"""
    @property
    def show_render(self) -> bool:
        """Show render related properties"""
        ...
    @property
    def show_paint(self) -> bool:
        """Show paint related properties"""
        ...
    @property
    def show_uvedit(self) -> bool:
        """Show UV editing related properties"""
        ...
    @property
    def show_maskedit(self) -> bool:
        """Show Mask editing related properties"""
        ...
    show_gizmo: bool
    """Show gizmos of all types"""
    show_gizmo_navigate: bool
    """Viewport navigation gizmo"""
    @property
    def overlay(self) -> Annotated['SpaceImageOverlay', "is_animatable=False"]:
        """Settings for display of overlays in the UV/Image editor"""
        ...
    mask: Annotated[Optional['Mask'], "is_animatable=False"]
    """Mask displayed and edited in this space"""
    mask_display_type: Literal['OUTLINE', 'DASH', 'BLACK', 'WHITE']
    """Display type for mask splines"""
    show_mask_spline: bool
    show_mask_overlay: bool
    mask_overlay_mode: Literal['ALPHACHANNEL', 'COMBINED']
    """Overlay mode of rasterized mask"""
    blend_factor: Annotated[float, "subtype='FACTOR'", "step=0.10000000149011612", "precision=1"]
    """Overlay blending factor of rasterized mask"""