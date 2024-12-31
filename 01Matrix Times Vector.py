import numpy as np

def matrix_dot_vector(a:list[list[int|float]],b:list[int|float])-> list[int|float]:

	if len(a[0]) != len(b):
		return -1

## BASIC SOLUTION
	ans = []
	for i in a:
		hold = 0
		for j in range(len(i)):
			hold += (i[j] * b[j])
		ans.append(hold)
	return ans

### LIST COMPREHENSION
	return [sum(row[i] * b[i] for i in range(len(b))) for row in a]

### USING ZIP
	return [sum(x * y for x,y in zip(row, b)) for row in a]

### USING NUMPY
	return np.dot(np.array(a), np.array(b)).tolist()

### USING LAMBDA
	dot_product = lambda row, vec: sum(x * y for x,y in zip(row, vec))
	return [dot_product(row, b) for row in a]











