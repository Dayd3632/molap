import numpy as np
import matplotlib


cubing_data = np.zeros((2,4,4,4), dtype=np.int8)
cubing_data[0][0][0][0] = 1
cubing_data[0][0][3][2] = 1
cubing_data[0][1][1][1] = 1
cubing_data[1][2][2][3] = 1
cubing_data[1][3][2][3] = 1
print(cubing_data)