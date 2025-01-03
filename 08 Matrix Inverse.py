import numpy as np

def inverse_2x2(matrix: list[list[float]]) -> list[list[float]]:

### NORMAL METHOD
	a, b, c, d = matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]
	det = a * d - b * c
  
	if det == 0:
			return "None"

	res = [[d / det, - b / det], [-c / det, a / det]]
	return res

### NUMPY
	if np.linalg.det(matrix) == 0:
		return "None"

	return (np.linalg.inv(matrix)).tolist()
