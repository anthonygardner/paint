from typing import Self

import numpy as np


class MotionModel2D:
    def __init__(
        self,
        position: np.ndarray,
        velocity: float,
        time_step: float,
        pointing_direction: float,
        steering_angle: float,
    ) -> Self:
        self.state = np.array([
            position[0] + velocity * time_step * np.cos(pointing_direction + steering_angle),
            position[1] + velocity * time_step * np.sin(pointing_direction + steering_angle),
            pointing_direction + velocity * time_step * np.sin(steering_angle),
        ])

