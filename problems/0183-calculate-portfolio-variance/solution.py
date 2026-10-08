import numpy as np

def calculate_portfolio_variance(cov_matrix: list[list[float]], weights: list[float]) -> float:
    """
    Calculate the variance of a portfolio.

    Args:
        cov_matrix (list[list[float]]): Covariance matrix of asset returns.
        weights (list[float]): Portfolio weights.

    Returns:
        float: Portfolio variance.
    """
    cov_matrix_array = np.asarray(cov_matrix)
    w = np.asarray(weights)

    if len(cov_matrix_array[0]) == len(w) and len(cov_matrix_array) == len(cov_matrix_array.T):
        v = cov_matrix_array @ w.T
        return v @ w

    pass