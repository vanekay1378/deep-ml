import numpy as np

def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:

    m, n = X.shape
    y = y.reshape(-1, 1)  # Ensure y is a column vector
    theta = np.zeros((n, 1))  # Initialize weights to zeros

    for i in range(iterations):
        h = X @ theta   # предсказания, вектор (m,)
        error = h - y   # ошибки, вектор (m,)
        gradient = (1/m) * X.T @ error # вектор (n,)
        theta = theta - alpha * gradient # обновление, вектор (n,)
    return theta.flatten()