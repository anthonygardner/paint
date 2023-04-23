from typing import Self

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
    def __init__(self):
        pass

