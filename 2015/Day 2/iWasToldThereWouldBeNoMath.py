import numpy as np 

file = np.loadtxt('input.txt', dtype=str)

for x in range(0,len(file)):
    to_array = list(file[x])
    print(to_array[0])

