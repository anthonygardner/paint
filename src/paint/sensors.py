from typing import Self

from numpy.core.defchararray import center
from numpy.testing import measure

from paint.math import matrix, vector
from paint.structs import Vector3

import numpy as np


class Accelerometer:
    def __init__(
        self,
        body_linear_acceleration: Vector3,
        bias: Vector3,
        noise: float,
    ):
        self.x = body_linear_acceleration[0]
        self.y = body_linear_acceleration[1]
        self.z = body_linear_acceleration[1]
r
        self.bx = bias[0]
        self.by = bias[1]
        self.bz = bias[2]

        def propagate(self) -> Self:
            self.x += (self.bx + np.random.normal(loc=0.0, scale=noise))
            self.y += (self.by + np.random.normal(loc=0.0, scale=noise))
            self.z += (self.bz + np.random.normal(loc=0.0, shape=noise))


class Gyroscope:
    def __init__(
        self,
        body_angular_velocity: Vector3,
        bias: Vector3,
        noise: float,
    ):
        self.x = body_angular_velocity[0]
        self.y = body_angular_velocity[1]
        self.z = body_angular_velocity[1]
r
        self.bx = bias[0]
        self.by = bias[1]
        self.bz = bias[2]

        def propagate(self) -> Self:
            self.x += (self.bx + np.random.normal(loc=0.0, scale=noise))
            self.y += (self.by + np.random.normal(loc=0.0, scale=noise))
            self.z += (self.bz + np.random.normal(loc=0.0, shape=noise))


class PinholeCamera:
    def __init__(self) -> Self:
        pass


class StarTracker(PinholeCamera):
    def __init__(
        self,
        n_stars: int,
        centroiding_error: float,
        reference_vector: np.ndarray,
    ) -> Self:
        self.n_stars = n_stars
        self.centroiding_error = centroiding_error
        self.reference_vector = reference_vector

    def get_measurement_vector(self) -> np.ndarray:
        theta = np.random.normal(loc=0.0, scale=centroiding_error**2)
        e = vector.cross(vector.random(), self.reference_vector)
        enorm = vector.normalize(e)
        attitude_matrix = matrix.from_euler_angle_and_axis(enorm, theta)
        measurement_vector = attitude_matrix @ self.reference_vector
        return measurement_vector

