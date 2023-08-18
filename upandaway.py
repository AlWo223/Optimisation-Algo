import numpy as np

### Store input data
nxk = list(map(int, input().strip().split(" ")))
n = nxk[0]
x = nxk[1]
k = nxk[2]
heights = list(map(int, input().strip().split(" ")))

distances = np.zeros((n, n))

for ii in range(0, n):
    distances[ii] = list(map(int, input().strip().split(" ")))


