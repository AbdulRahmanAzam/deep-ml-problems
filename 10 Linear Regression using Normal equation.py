import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:

	X = np.array(X)
	y = np.array(y)

	theta = np.linalg.inv(X.T @ X) @ X.T @ y

	# OR
	# theta = np.linalg.inv((X.T).dot(X)).dot(X.T).dot(y)

	return np.round(theta).tolist()
