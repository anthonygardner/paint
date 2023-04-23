import numpy as np


# geometry
def get_normal_to_plane(
    x: np.ndarray,
    y: np.ndarray,
    z: np.ndarray,
) -> np.ndarray:
    return np.cross(y - x, z - x)

def is_point_in_plane(
    normal_vector: np.ndarray,
    point_in_plane: np.ndarray,
    point_of_interest: np.array,
) -> bool:
    if np.dot(normal_vector, point_of_interest - point_in_plane) == 0:
        return True
    else:
        return False


