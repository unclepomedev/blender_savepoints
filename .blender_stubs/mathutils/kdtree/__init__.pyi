"""
Online Documentation:
https://docs.blender.org/api/current/mathutils.kdtree.html
"""

# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


import sys
import typing
from typing import Any, Union, Callable, Iterator

class KDTree:
    """KdTree(size) -> new kd-tree initialized to hold ``size`` items.

   :arg size: Number of items.
   :type size: int

.. note::

   :class:`KDTree.balance` must have been called before using any of the ``find`` methods.
"""
    """
    Online Documentation:
    https://docs.blender.org/api/current/mathutils.kdtree.html
    """
    def __init__(self, /, *args, **kwargs) -> Any: ...
    def balance(*args, **kwargs) -> Any: ...
    def find(*args, **kwargs) -> Any: ...
    def find_n(*args, **kwargs) -> Any: ...
    def find_range(*args, **kwargs) -> Any: ...
    def insert(*args, **kwargs) -> Any: ...
