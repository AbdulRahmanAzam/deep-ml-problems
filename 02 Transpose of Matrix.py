import numpy as np
def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:

### Direct Approach
	ans = []
	for i in range(len(a[0])):
		temp = []
		for j in range(len(a)):
			temp.append(a[i][j])
		ans.append(temp)
	return ans


### USING LIST COMPREHENSION
	return [[a[row][col] for row in range(len(a))] for col in range(len(a[0]))]


### USING ZIP AND *
	return [[row] for row in zip(*a)]


### USING NUMPY
	return [np.transpose(a)] # or .tolist()








