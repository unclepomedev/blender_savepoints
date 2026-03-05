# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.SPHFluidSettings.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class SPHFluidSettings(bpy_struct):

    @property
    def solver(self) -> Annotated[Literal['DDR', 'CLASSICAL'], "is_animatable=False"]:
        """The code used to calculate internal forces on particles"""
        ...
    @solver.setter
    def solver(self, value: Annotated[Literal['DDR', 'CLASSICAL'], "is_animatable=False"]):
        ...
    @property
    def spring_force(self) -> Annotated[float, "step=1.0", "precision=3"]:
        """Spring force"""
        ...
    @spring_force.setter
    def spring_force(self, value: Annotated[float, "step=1.0", "precision=3"]):
        ...
    @property
    def fluid_radius(self) -> Annotated[float, "step=1.0", "precision=3"]:
        """Fluid interaction radius"""
        ...
    @fluid_radius.setter
    def fluid_radius(self, value: Annotated[float, "step=1.0", "precision=3"]):
        ...
    @property
    def rest_length(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Spring rest length (factor of particle radius)"""
        ...
    @rest_length.setter
    def rest_length(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def use_viscoelastic_springs(self) -> bool:
        """Use viscoelastic springs instead of Hooke's springs"""
        ...
    @use_viscoelastic_springs.setter
    def use_viscoelastic_springs(self, value: bool):
        ...
    @property
    def use_initial_rest_length(self) -> bool:
        """Use the initial length as spring rest length instead of 2 * particle size"""
        ...
    @use_initial_rest_length.setter
    def use_initial_rest_length(self, value: bool):
        ...
    @property
    def plasticity(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """How much the spring rest length can change after the elastic limit is crossed"""
        ...
    @plasticity.setter
    def plasticity(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def yield_ratio(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """How much the spring has to be stretched/compressed in order to change its rest length"""
        ...
    @yield_ratio.setter
    def yield_ratio(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def spring_frames(self) -> Annotated[int, "step=1"]:
        """Create springs for this number of frames since particles birth (0 is always)"""
        ...
    @spring_frames.setter
    def spring_frames(self, value: Annotated[int, "step=1"]):
        ...
    @property
    def linear_viscosity(self) -> Annotated[float, "step=1.0", "precision=3"]:
        """Linear viscosity"""
        ...
    @linear_viscosity.setter
    def linear_viscosity(self, value: Annotated[float, "step=1.0", "precision=3"]):
        ...
    @property
    def stiff_viscosity(self) -> Annotated[float, "step=1.0", "precision=3"]:
        """Creates viscosity for expanding fluid"""
        ...
    @stiff_viscosity.setter
    def stiff_viscosity(self, value: Annotated[float, "step=1.0", "precision=3"]):
        ...
    @property
    def stiffness(self) -> Annotated[float, "step=1.0", "precision=3"]:
        """How incompressible the fluid is (speed of sound)"""
        ...
    @stiffness.setter
    def stiffness(self, value: Annotated[float, "step=1.0", "precision=3"]):
        ...
    @property
    def repulsion(self) -> Annotated[float, "step=1.0", "precision=3"]:
        """How strongly the fluid tries to keep from clustering (factor of stiffness)"""
        ...
    @repulsion.setter
    def repulsion(self, value: Annotated[float, "step=1.0", "precision=3"]):
        ...
    @property
    def rest_density(self) -> Annotated[float, "step=1.0", "precision=3"]:
        """Fluid rest density"""
        ...
    @rest_density.setter
    def rest_density(self, value: Annotated[float, "step=1.0", "precision=3"]):
        ...
    @property
    def buoyancy(self) -> Annotated[float, "step=1.0", "precision=3"]:
        """Artificial buoyancy force in negative gravity direction based on pressure differences inside the fluid"""
        ...
    @buoyancy.setter
    def buoyancy(self, value: Annotated[float, "step=1.0", "precision=3"]):
        ...
    @property
    def use_factor_repulsion(self) -> bool:
        """Repulsion is a factor of stiffness"""
        ...
    @use_factor_repulsion.setter
    def use_factor_repulsion(self, value: bool):
        ...
    @property
    def use_factor_density(self) -> bool:
        """Density is calculated as a factor of default density (depends on particle size)"""
        ...
    @use_factor_density.setter
    def use_factor_density(self, value: bool):
        ...
    @property
    def use_factor_radius(self) -> bool:
        """Interaction radius is a factor of 4 * particle size"""
        ...
    @use_factor_radius.setter
    def use_factor_radius(self, value: bool):
        ...
    @property
    def use_factor_stiff_viscosity(self) -> bool:
        """Stiff viscosity is a factor of normal viscosity"""
        ...
    @use_factor_stiff_viscosity.setter
    def use_factor_stiff_viscosity(self, value: bool):
        ...
    @property
    def use_factor_rest_length(self) -> bool:
        """Spring rest length is a factor of 2 * particle size"""
        ...
    @use_factor_rest_length.setter
    def use_factor_rest_length(self, value: bool):
        ...