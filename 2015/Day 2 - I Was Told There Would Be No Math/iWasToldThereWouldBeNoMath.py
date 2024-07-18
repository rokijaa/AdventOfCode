import numpy as np 

file = np.genfromtxt('input.txt', dtype=str)
sum = 0

for g in range(len(file)):
    l, w, h = file[g].split('x')
    l, w, h = int(l), int(w), int(h)
    slack = min(l*w, w*h, h*l)
    surfaceArea = 2*(l*w) + 2*(w*h) + 2*(h*l) + slack
    sum += surfaceArea
print(sum)
