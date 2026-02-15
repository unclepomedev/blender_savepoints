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

    show_overlays: bool
    """Display overlays like colored or dashed wires"""
    show_wire_color: bool
    """Color node links based on their connected sockets"""
    show_reroute_auto_labels: bool
    """Label reroute nodes based on the label of connected reroute nodes"""
    show_timing: bool
    """Display each node's last execution time"""
    show_context_path: bool
    """Display breadcrumbs for the editor's context"""
    show_named_attributes: bool
    """Show when nodes are using named attributes"""
    show_previews: bool
    """Display each node's preview if node is toggled"""
    preview_shape: Literal['FLAT', '3D']
    """Preview shape used by the node previews"""