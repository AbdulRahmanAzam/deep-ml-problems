import numpy as np

def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:

  ### NORMAL METHOD
	a, b, c, d = matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]
  
	det = a * d - b * c
	trace = a + d
	discriminant = trace**2 - 4 * det

	ans1 = (trace + det**0.5) / 2
	ans2 = (trace - det**0.5) / 2

	return [ans1, ans2]

  
### NUMPY
	return np.linalg.eigvals(matrix)
