# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.SpaceImageEditor.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

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
    @property
    def show_locked_time(self) -> bool:
        """Synchronize the visible timeline range with other time-based editors"""
        ...
    @show_locked_time.setter
    def show_locked_time(self, value: bool) -> None:
        ...
    @property
    def show_region_header(self) -> bool:

        ...
    @show_region_header.setter
    def show_region_header(self, value: bool) -> None:
        ...
    @property
    def show_region_tool_header(self) -> bool:

        ...
    @show_region_tool_header.setter
    def show_region_tool_header(self, value: bool) -> None:
        ...
    @property
    def show_region_toolbar(self) -> bool:

        ...
    @show_region_toolbar.setter
    def show_region_toolbar(self, value: bool) -> None:
        ...
    @property
    def show_region_ui(self) -> bool:

        ...
    @show_region_ui.setter
    def show_region_ui(self, value: bool) -> None:
        ...
    @property
    def show_region_hud(self) -> bool:

        ...
    @show_region_hud.setter
    def show_region_hud(self, value: bool) -> None:
        ...
    @property
    def show_region_asset_shelf(self) -> bool:
        """Display a region with assets that may currently be relevant (such as brushes in paint modes, or poses in Pose Mode)"""
        ...
    @show_region_asset_shelf.setter
    def show_region_asset_shelf(self, value: bool) -> None:
        ...
    @property
    def image(self) -> Annotated[Optional['Image'], "is_animatable=False"]:
        """Image displayed and edited in this space"""
        ...
    @image.setter
    def image(self, value: Annotated[Optional['Image'], "is_animatable=False"]) -> None:
        ...
    @property
    def image_user(self) -> Annotated['ImageUser', "is_animatable=False"]:
        """Parameters defining which layer, pass and frame of the image is displayed"""
        ...
    @property
    def scopes(self) -> Annotated[Optional['Scopes'], "is_animatable=False"]:
        """Scopes to visualize image statistics"""
        ...
    @property
    def use_image_pin(self) -> bool:
        """Display current image regardless of object selection"""
        ...
    @use_image_pin.setter
    def use_image_pin(self, value: bool) -> None:
        ...
    @property
    def sample_histogram(self) -> Annotated[Optional['Histogram'], "is_animatable=False"]:
        """Sampled colors along line"""
        ...
    @property
    def zoom(self) -> Annotated[list[float], "step=10.0", "precision=3"]:
        """Zoom factor"""
        ...
    @property
    def zoom_percentage(self) -> Annotated[float, "subtype='PERCENTAGE'", "step=100.0", "precision=0"]:
        """Zoom percentage"""
        ...
    @zoom_percentage.setter
    def zoom_percentage(self, value: Annotated[float, "subtype='PERCENTAGE'", "step=100.0", "precision=0"]) -> None:
        ...
    @property
    def show_repeat(self) -> bool:
        """Display the image repeated outside of the main view"""
        ...
    @show_repeat.setter
    def show_repeat(self, value: bool) -> None:
        ...
    @property
    def show_annotation(self) -> bool:
        """Show annotations for this view"""
        ...
    @show_annotation.setter
    def show_annotation(self, value: bool) -> None:
        ...
    @property
    def display_channels(self) -> Literal['COLOR_ALPHA', 'COLOR', 'ALPHA', 'Z_BUFFER', 'RED', 'GREEN', 'BLUE']:
        """Channels of the image to display"""
        ...
    @display_channels.setter
    def display_channels(self, value: Literal['COLOR_ALPHA', 'COLOR', 'ALPHA', 'Z_BUFFER', 'RED', 'GREEN', 'BLUE']) -> None:
        ...
    @property
    def show_stereo_3d(self) -> bool:
        """Display the image in Stereo 3D"""
        ...
    @show_stereo_3d.setter
    def show_stereo_3d(self, value: bool) -> None:
        ...
    @property
    def show_sequencer_scene(self) -> bool:
        """Display the render result for the sequencer scene instead of the active scene"""
        ...
    @show_sequencer_scene.setter
    def show_sequencer_scene(self, value: bool) -> None:
        ...
    @property
    def uv_editor(self) -> Annotated['SpaceUVEditor', "is_animatable=False"]:
        """UV editor settings"""
        ...
    @property
    def mode(self) -> Literal['VIEW', 'UV', 'PAINT', 'MASK']:
        """Editing context being displayed"""
        ...
    @mode.setter
    def mode(self, value: Literal['VIEW', 'UV', 'PAINT', 'MASK']) -> None:
        ...
    @property
    def ui_mode(self) -> Literal['VIEW', 'PAINT', 'MASK']:
        """Editing context being displayed"""
        ...
    @ui_mode.setter
    def ui_mode(self, value: Literal['VIEW', 'PAINT', 'MASK']) -> None:
        ...
    @property
    def cursor_location(self) -> Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]:
        """2D cursor location for this view"""
        ...
    @cursor_location.setter
    def cursor_location(self, value: Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def pivot_point(self) -> Literal['BOUNDING_BOX_CENTER', 'CURSOR', 'INDIVIDUAL_ORIGINS', 'MEDIAN_POINT', 'ACTIVE_ELEMENT']:
        """Rotation/Scaling Pivot"""
        ...
    @pivot_point.setter
    def pivot_point(self, value: Literal['BOUNDING_BOX_CENTER', 'CURSOR', 'INDIVIDUAL_ORIGINS', 'MEDIAN_POINT', 'ACTIVE_ELEMENT']) -> None:
        ...
    @property
    def annotation(self) -> Annotated[Optional['Annotation'], "is_animatable=False"]:
        """Annotation data for this space"""
        ...
    @annotation.setter
    def annotation(self, value: Annotated[Optional['Annotation'], "is_animatable=False"]) -> None:
        ...
    @property
    def use_realtime_update(self) -> bool:
        """Update other affected window spaces automatically to reflect changes during interactive operations such as transform"""
        ...
    @use_realtime_update.setter
    def use_realtime_update(self, value: bool) -> None:
        ...
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
    @property
    def show_gizmo(self) -> bool:
        """Show gizmos of all types"""
        ...
    @show_gizmo.setter
    def show_gizmo(self, value: bool) -> None:
        ...
    @property
    def show_gizmo_navigate(self) -> bool:
        """Viewport navigation gizmo"""
        ...
    @show_gizmo_navigate.setter
    def show_gizmo_navigate(self, value: bool) -> None:
        ...
    @property
    def overlay(self) -> Annotated['SpaceImageOverlay', "is_animatable=False"]:
        """Settings for display of overlays in the UV/Image editor"""
        ...
    @property
    def mask(self) -> Annotated[Optional['Mask'], "is_animatable=False"]:
        """Mask displayed and edited in this space"""
        ...
    @mask.setter
    def mask(self, value: Annotated[Optional['Mask'], "is_animatable=False"]) -> None:
        ...
    @property
    def mask_display_type(self) -> Literal['OUTLINE', 'DASH', 'BLACK', 'WHITE']:
        """Display type for mask splines"""
        ...
    @mask_display_type.setter
    def mask_display_type(self, value: Literal['OUTLINE', 'DASH', 'BLACK', 'WHITE']) -> None:
        ...
    @property
    def show_mask_spline(self) -> bool:

        ...
    @show_mask_spline.setter
    def show_mask_spline(self, value: bool) -> None:
        ...
    @property
    def show_mask_overlay(self) -> bool:

        ...
    @show_mask_overlay.setter
    def show_mask_overlay(self, value: bool) -> None:
        ...
    @property
    def mask_overlay_mode(self) -> Literal['ALPHACHANNEL', 'COMBINED']:
        """Overlay mode of rasterized mask"""
        ...
    @mask_overlay_mode.setter
    def mask_overlay_mode(self, value: Literal['ALPHACHANNEL', 'COMBINED']) -> None:
        ...
    @property
    def blend_factor(self) -> Annotated[float, "subtype='FACTOR'", "step=0.10000000149011612", "precision=1"]:
        """Overlay blending factor of rasterized mask"""
        ...
    @blend_factor.setter
    def blend_factor(self, value: Annotated[float, "subtype='FACTOR'", "step=0.10000000149011612", "precision=1"]) -> None:
        ...