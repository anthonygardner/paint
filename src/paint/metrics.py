"""Metrics for characterizing model performance
"""

import numpy as np


def mean_squared_error( 
    expectation_state_vector: np.ndarray,
    estimation_state_vector: np.ndarray,
) -> float:
    if len(estimation_state_vector) != len(expectation_state_vector):
        raise ValueError("Input vector lengths do not match")
    else:
        return np.mean((expectation_state_vector - estimation_state_vector)**2)

def normalized_estimation_error_squared( 
    expectation_state_vector: np.ndarray,
    estimation_state_vector: np.ndarray,
    covariance_matrix: np.ndarray,
) -> float: 
    if len(estimation_state_vector) != len(expectation_state_vector):
        raise ValueError("Input vector lengths do not match")
    else:
        error_vector = estimation_state_vector - expectation_state_vector
        inverse_covariance_matrix = np.linalg.inv(covariance_matrix)

        return error_vector.T @ inverse_covariance_matrix @ error_vector

