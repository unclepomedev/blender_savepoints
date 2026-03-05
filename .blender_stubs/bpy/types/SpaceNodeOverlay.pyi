# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.SpaceNodeOverlay.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class SpaceNodeOverlay(bpy_struct):

    @property
    def show_overlays(self) -> bool:
        """Display overlays like colored or dashed wires"""
        ...
    @show_overlays.setter
    def show_overlays(self, value: bool):
        ...
    @property
    def show_wire_color(self) -> bool:
        """Color node links based on their connected sockets"""
        ...
    @show_wire_color.setter
    def show_wire_color(self, value: bool):
        ...
    @property
    def show_reroute_auto_labels(self) -> bool:
        """Label reroute nodes based on the label of connected reroute nodes"""
        ...
    @show_reroute_auto_labels.setter
    def show_reroute_auto_labels(self, value: bool):
        ...
    @property
    def show_timing(self) -> bool:
        """Display each node's last execution time"""
        ...
    @show_timing.setter
    def show_timing(self, value: bool):
        ...
    @property
    def show_context_path(self) -> bool:
        """Display breadcrumbs for the editor's context"""
        ...
    @show_context_path.setter
    def show_context_path(self, value: bool):
        ...
    @property
    def show_named_attributes(self) -> bool:
        """Show when nodes are using named attributes"""
        ...
    @show_named_attributes.setter
    def show_named_attributes(self, value: bool):
        ...
    @property
    def show_previews(self) -> bool:
        """Display each node's preview if node is toggled"""
        ...
    @show_previews.setter
    def show_previews(self, value: bool):
        ...
    @property
    def preview_shape(self) -> Literal['FLAT', '3D']:
        """Preview shape used by the node previews"""
        ...
    @preview_shape.setter
    def preview_shape(self, value: Literal['FLAT', '3D']):
        ...