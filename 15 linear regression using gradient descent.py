import numpy as np
def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:
	# Your code here, make sure to round
	m, n = X.shape
	theta = np.zeros((n, 1))

### NORMAL METHOD
	for _ in range(iterations):
		predictions = X @ theta
		errors = predictions - y.reshape(-1, 1)
		updates = (1/ m) * (X.T @ errors)
		theta -= alpha * updates 

	return np.round(theta, 4)


  
### TRIED FOR 1 LINER
	for _ in range(iterations):
		theta -= alpha * (1 / m) * (X.T @ (X @ theta - y.reshape(-1, 1)))

	return np.round(theta, 4)
