import numpy as np, pandas as pd
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

file = open("input3.txt")

arr = [0,0,0,0,0,0,0,0,0,0,0,0]
count = 0

for f in file.readlines():
    for i in range(len(f)-1):
        arr[i] += int(f[i])
    count += 1

arr = [x / count for x in arr]

gamma = ""
epsilon = ""

for value in arr:
    if value > 0.5:
        gamma += '1'
        epsilon += '0'
    else:
        gamma+='0'
        epsilon += '1'

gamma = int(gamma,2)
epsilon = int(epsilon,2)

print(gamma * epsilon)