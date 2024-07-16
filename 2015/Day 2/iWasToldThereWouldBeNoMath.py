import numpy as np 

file = np.loadtxt('input.txt', dtype=str)

for x in range(0,len(file)):
    to_array = list(file[x])
    for y in range(0,len(to_array)):
        if to_array[y] != 'x':
            print(to_array[y])

            
