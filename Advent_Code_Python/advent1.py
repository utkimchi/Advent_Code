import numpy as np,os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
inp = np.loadtxt('dumpy.txt')
a = np.sum(np.array(np.diff(inp)) > 0, axis=0)
b = np.sum(np.array(np.diff([sum(inp[i:i+3]) for i in range(len(inp)-2)])) > 0, axis=0)
print(a,b)


