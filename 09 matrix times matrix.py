import numpy as np

def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
	
	if len(a[0]) != len(b):
		return -1 

### NORMAL LOOP METHOD
	res = []
	for i in range(len(a)):
		hold = []
		for j in range(len(b[0])):
			val = 0
			for k in range(len(b)):
				val += a[i][k] * b[k][j]
			hold.append(val)
		res.append(hold)
	
	return res

                
### NUMPY
	return np.dot(a,b)
