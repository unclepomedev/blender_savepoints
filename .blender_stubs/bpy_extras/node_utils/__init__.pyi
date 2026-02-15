# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy_extras.node_utils.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated


def connect_sockets(input, output) -> Any:
    """
    Connect sockets in a node tree.

    This is useful because the links created through the normal Python API are
    invalid when one of the sockets is a virtual socket (grayed out sockets in
    Group Input and Group Output nodes).

    It replaces node_tree.links.new(input, output)
    

    Online Documentation:
    https://docs.blender.org/api/current/bpy_extras.node_utils.html"""
    ...

def find_base_socket_type(socket) -> Any:
    """
    Find the base class of the socket.

    Sockets can have a subtype such as NodeSocketFloatFactor,
    but only the base type is allowed, e. g. NodeSocketFloat
    

    Online Documentation:
    https://docs.blender.org/api/current/bpy_extras.node_utils.html"""
    ...

def find_node_input(node, name) -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy_extras.node_utils.html"""
    ...
