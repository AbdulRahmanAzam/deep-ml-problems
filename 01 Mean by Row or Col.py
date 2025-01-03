import numpy as np
import pandas as pd 

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:

### NORMAL LOOP
	ans = []
	for i in range(len(matrix)):
		mean = 0
		for j in range(len(matrix[0])):
			if mode == "column":
				mean += matrix[j][i]
			else:
				mean += matrix[i][j]

		ans.append(mean/len(matrix))
	return ans


### LIST COMPREHENSION
	if mode == "row":
		return [sum(row)/ len(row) for row in matrix]
	else:
		return [(sum(matrix[col][row] for col in range(len(matrix[0]))) / len(matrix[0])) for row in range(len(matrix))]

  
### NUMPY
	if mode == "row":
		return np.mean(matrix, axis=1).tolist()
	else:
		return np.mean(matrix, axis=0).tolist()

  
### PANDAS
	df = pd.DataFrame(matrix)
	if mode == "row":
		return df.mean(axis=1).tolist()
	else:
		return df.mean(axis=0).tolist()








				
