# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/mathutils.noise.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated


def cell(*args, **kwargs) -> Any:
    """.. function:: cell(position, /)

   Returns cell noise value at the specified position.

   :arg position: The position to evaluate the selected noise function.
   :type position: :class:`mathutils.Vector`
   :return: The cell noise value.
   :rtype: float


    Online Documentation:
    https://docs.blender.org/api/current/mathutils.noise.html"""
    ...

def cell_vector(*args, **kwargs) -> Any:
    """.. function:: cell_vector(position, /)

   Returns cell noise vector at the specified position.

   :arg position: The position to evaluate the selected noise function.
   :type position: :class:`mathutils.Vector`
   :return: The cell noise vector.
   :rtype: :class:`mathutils.Vector`


    Online Documentation:
    https://docs.blender.org/api/current/mathutils.noise.html"""
    ...

def fractal(*args, **kwargs) -> Any:
    """.. function:: fractal(position, H, lacunarity, octaves, /, *, noise_basis='PERLIN_ORIGINAL')

   Returns the fractal Brownian motion (fBm) noise value from the noise basis at the specified position.

   :arg position: The position to evaluate the selected noise function.
   :type position: :class:`mathutils.Vector`
   :arg H: The fractal increment factor.
   :type H: float
   :arg lacunarity: The gap between successive frequencies.
   :type lacunarity: float
   :arg octaves: The number of different noise frequencies used.
   :type octaves: int
   :arg noise_basis: A noise basis string.
   :type noise_basis: Literal['BLENDER', 'PERLIN_ORIGINAL', 'PERLIN_NEW', 'VORONOI_F1', 'VORONOI_F2', 'VORONOI_F3', 'VORONOI_F4', 'VORONOI_F2F1', 'VORONOI_CRACKLE', 'CELLNOISE'].
   :return: The fractal Brownian motion noise value.
   :rtype: float


    Online Documentation:
    https://docs.blender.org/api/current/mathutils.noise.html"""
    ...

def hetero_terrain(*args, **kwargs) -> Any:
    """.. function:: hetero_terrain(position, H, lacunarity, octaves, offset, /, *, noise_basis='PERLIN_ORIGINAL')

   Returns the heterogeneous terrain value from the noise basis at the specified position.

   :arg position: The position to evaluate the selected noise function.
   :type position: :class:`mathutils.Vector`
   :arg H: The fractal dimension of the roughest areas.
   :type H: float
   :arg lacunarity: The gap between successive frequencies.
   :type lacunarity: float
   :arg octaves: The number of different noise frequencies used.
   :type octaves: int
   :arg offset: The height of the terrain above 'sea level'.
   :type offset: float
   :arg noise_basis: A noise basis string.
   :type noise_basis: Literal['BLENDER', 'PERLIN_ORIGINAL', 'PERLIN_NEW', 'VORONOI_F1', 'VORONOI_F2', 'VORONOI_F3', 'VORONOI_F4', 'VORONOI_F2F1', 'VORONOI_CRACKLE', 'CELLNOISE'].
   :return: The heterogeneous terrain value.
   :rtype: float


    Online Documentation:
    https://docs.blender.org/api/current/mathutils.noise.html"""
    ...

def hybrid_multi_fractal(*args, **kwargs) -> Any:
    """.. function:: hybrid_multi_fractal(position, H, lacunarity, octaves, offset, gain, /, *, noise_basis='PERLIN_ORIGINAL')

   Returns hybrid multifractal value from the noise basis at the specified position.

   :arg position: The position to evaluate the selected noise function.
   :type position: :class:`mathutils.Vector`
   :arg H: The fractal dimension of the roughest areas.
   :type H: float
   :arg lacunarity: The gap between successive frequencies.
   :type lacunarity: float
   :arg octaves: The number of different noise frequencies used.
   :type octaves: int
   :arg offset: The height of the terrain above 'sea level'.
   :type offset: float
   :arg gain: Scaling applied to the values.
   :type gain: float
   :arg noise_basis: A noise basis string.
   :type noise_basis: Literal['BLENDER', 'PERLIN_ORIGINAL', 'PERLIN_NEW', 'VORONOI_F1', 'VORONOI_F2', 'VORONOI_F3', 'VORONOI_F4', 'VORONOI_F2F1', 'VORONOI_CRACKLE', 'CELLNOISE'].
   :return: The hybrid multifractal value.
   :rtype: float


    Online Documentation:
    https://docs.blender.org/api/current/mathutils.noise.html"""
    ...

def multi_fractal(*args, **kwargs) -> Any:
    """.. function:: multi_fractal(position, H, lacunarity, octaves, /, *, noise_basis='PERLIN_ORIGINAL')

   Returns multifractal noise value from the noise basis at the specified position.

   :arg position: The position to evaluate the selected noise function.
   :type position: :class:`mathutils.Vector`
   :arg H: The fractal increment factor.
   :type H: float
   :arg lacunarity: The gap between successive frequencies.
   :type lacunarity: float
   :arg octaves: The number of different noise frequencies used.
   :type octaves: int
   :arg noise_basis: A noise basis string.
   :type noise_basis: Literal['BLENDER', 'PERLIN_ORIGINAL', 'PERLIN_NEW', 'VORONOI_F1', 'VORONOI_F2', 'VORONOI_F3', 'VORONOI_F4', 'VORONOI_F2F1', 'VORONOI_CRACKLE', 'CELLNOISE'].
   :return: The multifractal noise value.
   :rtype: float


    Online Documentation:
    https://docs.blender.org/api/current/mathutils.noise.html"""
    ...

def noise(*args, **kwargs) -> Any:
    """.. function:: noise(position, /, *, noise_basis='PERLIN_ORIGINAL')

   Returns noise value from the noise basis at the position specified.

   :arg position: The position to evaluate the selected noise function.
   :type position: :class:`mathutils.Vector`
   :arg noise_basis: A noise basis string.
   :type noise_basis: Literal['BLENDER', 'PERLIN_ORIGINAL', 'PERLIN_NEW', 'VORONOI_F1', 'VORONOI_F2', 'VORONOI_F3', 'VORONOI_F4', 'VORONOI_F2F1', 'VORONOI_CRACKLE', 'CELLNOISE'].
   :return: The noise value.
   :rtype: float


    Online Documentation:
    https://docs.blender.org/api/current/mathutils.noise.html"""
    ...

def noise_vector(*args, **kwargs) -> Any:
    """.. function:: noise_vector(position, /, *, noise_basis='PERLIN_ORIGINAL')

   Returns the noise vector from the noise basis at the specified position.

   :arg position: The position to evaluate the selected noise function.
   :type position: :class:`mathutils.Vector`
   :arg noise_basis: A noise basis string.
   :type noise_basis: Literal['BLENDER', 'PERLIN_ORIGINAL', 'PERLIN_NEW', 'VORONOI_F1', 'VORONOI_F2', 'VORONOI_F3', 'VORONOI_F4', 'VORONOI_F2F1', 'VORONOI_CRACKLE', 'CELLNOISE'].
   :return: The noise vector.
   :rtype: :class:`mathutils.Vector`


    Online Documentation:
    https://docs.blender.org/api/current/mathutils.noise.html"""
    ...

def random(*args, **kwargs) -> Any:
    """.. function:: random()

   Returns a random number in the range [0, 1).

   :return: The random number.
   :rtype: float


    Online Documentation:
    https://docs.blender.org/api/current/mathutils.noise.html"""
    ...

def random_unit_vector(*args, **kwargs) -> Any:
    """.. function:: random_unit_vector(*, size=3)

   Returns a unit vector with random entries.

   :arg size: The size of the vector to be produced, in the range [2, 4].
   :type size: int
   :return: The random unit vector.
   :rtype: :class:`mathutils.Vector`


    Online Documentation:
    https://docs.blender.org/api/current/mathutils.noise.html"""
    ...

def random_vector(*args, **kwargs) -> Any:
    """.. function:: random_vector(*, size=3)

   Returns a vector with random entries in the range (-1, 1).

   :arg size: The size of the vector to be produced.
   :type size: int
   :return: The random vector.
   :rtype: :class:`mathutils.Vector`


    Online Documentation:
    https://docs.blender.org/api/current/mathutils.noise.html"""
    ...

def ridged_multi_fractal(*args, **kwargs) -> Any:
    """.. function:: ridged_multi_fractal(position, H, lacunarity, octaves, offset, gain, /, *, noise_basis='PERLIN_ORIGINAL')

   Returns ridged multifractal value from the noise basis at the specified position.

   :arg position: The position to evaluate the selected noise function.
   :type position: :class:`mathutils.Vector`
   :arg H: The fractal dimension of the roughest areas.
   :type H: float
   :arg lacunarity: The gap between successive frequencies.
   :type lacunarity: float
   :arg octaves: The number of different noise frequencies used.
   :type octaves: int
   :arg offset: The height of the terrain above 'sea level'.
   :type offset: float
   :arg gain: Scaling applied to the values.
   :type gain: float
   :arg noise_basis: A noise basis string.
   :type noise_basis: Literal['BLENDER', 'PERLIN_ORIGINAL', 'PERLIN_NEW', 'VORONOI_F1', 'VORONOI_F2', 'VORONOI_F3', 'VORONOI_F4', 'VORONOI_F2F1', 'VORONOI_CRACKLE', 'CELLNOISE'].
   :return: The ridged multifractal value.
   :rtype: float


    Online Documentation:
    https://docs.blender.org/api/current/mathutils.noise.html"""
    ...

def seed_set(*args, **kwargs) -> Any:
    """.. function:: seed_set(seed, /)

   Sets the random seed used for random_unit_vector, and random.

   :arg seed: Seed used for the random generator.
      When seed is zero, the current time will be used instead.
   :type seed: int


    Online Documentation:
    https://docs.blender.org/api/current/mathutils.noise.html"""
    ...

def turbulence(*args, **kwargs) -> Any:
    """.. function:: turbulence(position, octaves, hard, /, *, noise_basis='PERLIN_ORIGINAL', amplitude_scale=0.5, frequency_scale=2.0)

   Returns the turbulence value from the noise basis at the specified position.

   :arg position: The position to evaluate the selected noise function.
   :type position: :class:`mathutils.Vector`
   :arg octaves: The number of different noise frequencies used.
   :type octaves: int
   :arg hard: Specifies whether returned turbulence is hard (sharp transitions) or soft (smooth transitions).
   :type hard: bool
   :arg noise_basis: A noise basis string.
   :type noise_basis: Literal['BLENDER', 'PERLIN_ORIGINAL', 'PERLIN_NEW', 'VORONOI_F1', 'VORONOI_F2', 'VORONOI_F3', 'VORONOI_F4', 'VORONOI_F2F1', 'VORONOI_CRACKLE', 'CELLNOISE'].
   :arg amplitude_scale: The amplitude scaling factor.
   :type amplitude_scale: float
   :arg frequency_scale: The frequency scaling factor
   :type frequency_scale: float
   :return: The turbulence value.
   :rtype: float


    Online Documentation:
    https://docs.blender.org/api/current/mathutils.noise.html"""
    ...

def turbulence_vector(*args, **kwargs) -> Any:
    """.. function:: turbulence_vector(position, octaves, hard, /, *, noise_basis='PERLIN_ORIGINAL', amplitude_scale=0.5, frequency_scale=2.0)

   Returns the turbulence vector from the noise basis at the specified position.

   :arg position: The position to evaluate the selected noise function.
   :type position: :class:`mathutils.Vector`
   :arg octaves: The number of different noise frequencies used.
   :type octaves: int
   :arg hard: Specifies whether returned turbulence is hard (sharp transitions) or soft (smooth transitions).
   :type hard: bool
   :arg noise_basis: A noise basis string.
   :type noise_basis: Literal['BLENDER', 'PERLIN_ORIGINAL', 'PERLIN_NEW', 'VORONOI_F1', 'VORONOI_F2', 'VORONOI_F3', 'VORONOI_F4', 'VORONOI_F2F1', 'VORONOI_CRACKLE', 'CELLNOISE'].
   :arg amplitude_scale: The amplitude scaling factor.
   :type amplitude_scale: float
   :arg frequency_scale: The frequency scaling factor
   :type frequency_scale: float
   :return: The turbulence vector.
   :rtype: :class:`mathutils.Vector`


    Online Documentation:
    https://docs.blender.org/api/current/mathutils.noise.html"""
    ...

def variable_lacunarity(*args, **kwargs) -> Any:
    """.. function:: variable_lacunarity(position, distortion, /, *, noise_type1='PERLIN_ORIGINAL', noise_type2='PERLIN_ORIGINAL')

   Returns variable lacunarity noise value, a distorted variety of noise, from noise type 1 distorted by noise type 2 at the specified position.

   :arg position: The position to evaluate the selected noise function.
   :type position: :class:`mathutils.Vector`
   :arg distortion: The amount of distortion.
   :type distortion: float
   :arg noise_type1: A noise type string.
   :type noise_type1: Literal['BLENDER', 'PERLIN_ORIGINAL', 'PERLIN_NEW', 'VORONOI_F1', 'VORONOI_F2', 'VORONOI_F3', 'VORONOI_F4', 'VORONOI_F2F1', 'VORONOI_CRACKLE', 'CELLNOISE'].
   :arg noise_type2: A noise type string.
   :type noise_type2: Literal['BLENDER', 'PERLIN_ORIGINAL', 'PERLIN_NEW', 'VORONOI_F1', 'VORONOI_F2', 'VORONOI_F3', 'VORONOI_F4', 'VORONOI_F2F1', 'VORONOI_CRACKLE', 'CELLNOISE'].
   :return: The variable lacunarity noise value.
   :rtype: float


    Online Documentation:
    https://docs.blender.org/api/current/mathutils.noise.html"""
    ...

def voronoi(*args, **kwargs) -> Any:
    """.. function:: voronoi(position, /, *, distance_metric='DISTANCE', exponent=2.5)

   Returns a list of distances to the four closest features and their locations.

   :arg position: The position to evaluate the selected noise function.
   :type position: :class:`mathutils.Vector`
   :arg distance_metric: A distance metric string.
   :type distance_metric: Literal['DISTANCE', 'DISTANCE_SQUARED', 'MANHATTAN', 'CHEBYCHEV', 'MINKOVSKY', 'MINKOVSKY_HALF', 'MINKOVSKY_FOUR'].
   :arg exponent: The exponent for Minkowski distance metric.
   :type exponent: float
   :return: A list of distances to the four closest features and their locations.
   :rtype: list[list[float] | list[:class:`mathutils.Vector`]]


    Online Documentation:
    https://docs.blender.org/api/current/mathutils.noise.html"""
    ...
