import numpy as np

def rotate_about_x(angle: float = 0.0) -> np.ndarray:
    """Performs an x-rotation
    """
    Rx = np.array(
        [
            [1.0, 0.0, 0.0],
            [0.0, np.cos(angle), -np.sin(angle)],
            [0.0, np.sin(angle), np.cos(angle)],
        ],
    )
    return Rx

def rotate_about_y(angle: float = 0.0) -> np.ndarray:
    """Performs a y-rotation
    """
    Ry = np.array(
        [
            [np.cos(angle), 0.0, np.sin(angle)],
            [0.0, 1.0, 0.0],
            [-np.sin(angle), 0.0, np.cos(angle)],
        ],
    )
    return Ry

def rotate_about_z(angle: float = 0.0) -> np.ndarray:
    """Performs a z-rotation
    """
    Rz = np.array(
        [
            [np.cos(angle), -np.sin(angle), 0.0],
            [np.sin(angle), np.cos(angle), 0.0],
            [0.0, 0.0, 1.0],
        ],
    )
    return Rz

def rotate_about_zyx(
    angle_x: float = 0.0,
    angle_y: float = 0.0,
    angle_z: float = 0.0,
) -> np.ndarray:
    """Performs a 321 rotation sequence
    """
    Rx = rotate_about_x(angle=angle_x)
    Ry = rotate_about_y(angle=angle_y)
    Rz = rotate_about_z(angle=angle_z)
    return Rz @ Ry @ Rx

