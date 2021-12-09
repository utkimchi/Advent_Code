import pandas as pd, numpy as np, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
file = open("input5.txt")

def isVertOrHor(l1,l2):
    if l1[0] == l2[0] or l1[1] == l2[1]:
        return True
    return False

def findOverlaps(p1,p2,htab):
    if p1[0] > p2[0]:
        for i in range(p2[0],p1[0]+1):
            val = (i,p2[1])
            if val in htab:
                htab[val] = htab[val] + 1
            else:
                htab[val] = 1
    elif p1[0] < p2 [0]:
        for i in range(p1[0],p2[0]+1):
            val = (i,p2[1])
            if val in htab:
                htab[val] = htab[val] + 1
            else:
                htab[val] = 1
    elif p1[1] < p2 [1]:
        for i in range(p1[1],p2[1]+1):
            val = (p1[0],i)
            if val in htab:
                htab[val] = htab[val] + 1
            else:
                htab[val] = 1
    elif p1[1] > p2[1]:
        for i in range(p2[1],p1[1]+1):
            val = (p1[0],i)
            if val in htab:
                htab[val] = htab[val] + 1
            else:
                htab[val] = 1
    return htab

epic_hash_table = {}
really_epic_hash_table = {}

def superOverlaps(p1,p2,htab):
    slope = int(((p2[1]-p1[1])/p2[0]-p1[0]))
    if p2[0] < p1[0]:
        additional = -1
        for val in range(p2[0],p1[0]+additional):
            val = (p2[0],p2[0]*slope)
            if val in htab:
                htab[val] = htab[val] + 1
            else:
                htab[val] = 1
    else:
        additional = 1
        for val in range(p1[0],p2[0]+additional):
            val=(p1[0],p1[0]*slope)
            if val in htab:
                htab[val] = htab[val] + 1
            else:
                htab[val] = 1
        
    return htab


for f in file:
    vals = f.split(" ")
    n1 = vals[0].split(",")
    n2 = vals[2].split(",")
    n2[1] = n2[1][:-1]
    n1 = [int(x) for x in n1]
    n2 = [int(x) for x in n2]
    hov = isVertOrHor(n1,n2)
    really_epic_hash_table = superOverlaps(n1,n2,really_epic_hash_table)
    if hov:
        epic_hash_table = findOverlaps(n1,n2,epic_hash_table) 

tot = 0
for val in epic_hash_table.values():
    if val >= 2:
        tot+=1

tot2 = 0
for val in really_epic_hash_table.values():
    if val >= 2:
        tot2+=1

print("tot")
print(tot)

print("second")
print(tot2)


