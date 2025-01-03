import numpy as np

def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	result = []
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			result.append(scalar * matrix[i][j])
	
	return result


### NUMPY
	return [np.array(matrix) * scalar]


### LIST COMPREHENSION
	return [[scalar * elem for elem in row] for row in matrix]

