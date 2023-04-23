"""Error metrics for characterizing a model's performance
"""

import numpy as np


def mean_squared_error( 
    expectation_vector: np.ndarray,
    estimation_vector: np.ndarray,
) -> float:
    """Mean squared error regression loss.

    Parameters
    ----------
    expectation_vector : array-like of shape (n_states,)
        Expected (reference) target values.

    estimation_vector : array-like of shape (n_states,)
        Estimated (observation) target values.

    Returns
    -------
    loss : float
        A non-negative floating point value.
    """
    if len(estimation_vector) != len(expectation_vector):
        raise ValueError("Input vector lengths do not match")
    else:
        return np.mean((estimation_vector - expectation_vector)**2)

def normalized_estimation_error_squared( 
    expectation_vector: np.ndarray,
    estimation_vector: np.ndarray,
    covariance_matrix: np.ndarray,
) -> float:
    """Normalized estimation error squared (NEES) regression loss.

    Parameters
    ----------
    expectation_vector : array-like of shape (n_states,)
        Expected (reference) target values.

    estimation_vector : array-like of shape (n_states,)
        Estimated (observation) target values.

    covariance_matrix : array-like of shape (n_states, n_states)
        A matrix of variances.

    Returns
    -------
    loss : float
        A non-negative floating point value.
    """
    if len(estimation_vector) != len(expectation_vector):
        raise ValueError("Input vector lengths do not match")
    else:
        error_vector = estimation_vector - expectation_vector
        inverse_covariance_matrix = np.linalg.inv(covariance_matrix)

        return error_vector.T @ inverse_covariance_matrix @ error_vector

def mean_nees(nees_vector: np.ndarray) -> float:
    """Mean normalized estimation error squared (NEES) regression loss.

    Parameters
    ----------
    nees_vector : array_like
        A vector of NEES values.

    Returns
    -------
    loss : float
        A non-negative floating point value.
    """
    return np.mean(nees_vector)

def mahalanobis_distance(
    expectation_vector: np.ndarray,
    estimation_vector: np.ndarray,
    covariance_matrix: np.ndarray,
) -> np.ndarray:
    if len(estimation_vector) != len(expectation_vector):
        raise ValueError("Input vector lengths do not match")
    else:
        error_vector = estimation_vector - expectation_vector
        inverse_covariance_matrix = np.linalg.inv(covariance_matrix)

        return np.sqrt(error_vector.T @ inverse_covariance_matrix @ error_vector)

