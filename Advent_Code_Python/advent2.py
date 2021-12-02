import numpy as np,os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
f = open("input2.txt")
#Part 1
print(np.prod((sum([int(line[-2]) for line in open('input2.txt').readlines() if line[0] == "f"]) , sum([-int(line[-2]) if line[0] == "u" else (int(line[-2]) if line[0] == "d" else 0) for line in open('input2.txt').readlines()]))))

#part 2
aim =0
forward = 0
depth = 0

for line in f.readlines():
    val = int(line[-2])
    if line[0] == 'f':
        forward += val
        depth += aim * val
    elif line[0] == 'd':
        aim += val
    else:
         aim -= val
print(forward*depth)