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
class SPHFluidSettings(bpy_struct):
    solver: Annotated[Literal['DDR', 'CLASSICAL'], "is_animatable=False"]
    """The code used to calculate internal forces on particles"""
    spring_force: Annotated[float, "step=1.0", "precision=3"]
    """Spring force"""
    fluid_radius: Annotated[float, "step=1.0", "precision=3"]
    """Fluid interaction radius"""
    rest_length: Annotated[float, "step=10.0", "precision=3"]
    """Spring rest length (factor of particle radius)"""
    use_viscoelastic_springs: bool
    """Use viscoelastic springs instead of Hooke's springs"""
    use_initial_rest_length: bool
    """Use the initial length as spring rest length instead of 2 * particle size"""
    plasticity: Annotated[float, "step=10.0", "precision=3"]
    """How much the spring rest length can change after the elastic limit is crossed"""
    yield_ratio: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """How much the spring has to be stretched/compressed in order to change its rest length"""
    spring_frames: Annotated[int, "step=1"]
    """Create springs for this number of frames since particles birth (0 is always)"""
    linear_viscosity: Annotated[float, "step=1.0", "precision=3"]
    """Linear viscosity"""
    stiff_viscosity: Annotated[float, "step=1.0", "precision=3"]
    """Creates viscosity for expanding fluid"""
    stiffness: Annotated[float, "step=1.0", "precision=3"]
    """How incompressible the fluid is (speed of sound)"""
    repulsion: Annotated[float, "step=1.0", "precision=3"]
    """How strongly the fluid tries to keep from clustering (factor of stiffness)"""
    rest_density: Annotated[float, "step=1.0", "precision=3"]
    """Fluid rest density"""
    buoyancy: Annotated[float, "step=1.0", "precision=3"]
    """Artificial buoyancy force in negative gravity direction based on pressure differences inside the fluid"""
    use_factor_repulsion: bool
    """Repulsion is a factor of stiffness"""
    use_factor_density: bool
    """Density is calculated as a factor of default density (depends on particle size)"""
    use_factor_radius: bool
    """Interaction radius is a factor of 4 * particle size"""
    use_factor_stiff_viscosity: bool
    """Stiff viscosity is a factor of normal viscosity"""
    use_factor_rest_length: bool
    """Spring rest length is a factor of 2 * particle size"""