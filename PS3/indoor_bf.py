### Generate all possible permutations with fix start --> (n-1)!
### Calculate length
import math
import sys
sys.setrecursionlimit(1000000000)

### Store input data
n, L = map(int, input().strip().split(" "))

graph = [[] for ii in range(0, n)]
for xx in range(0, n):
    for weight in input().strip().split(" "):
        graph[xx].append(int(weight))
        
from itertools import permutations
visited = set()
for perm in permutations(range(1, n), n-1):
    if(perm in visited):
        continue
    visited.add(perm)
    visited.add(reversed(perm))
    length = 0
    u = 0
    for ii in perm:
        length += graph[u][ii]
        u = ii
    length += graph[u][0]
    if(length == L):
        print("possible")
        exit()
print("impossible")

"""### Handle trivial cases
if (n == 2):
    if (graph[0][1] == L):
        print("possible")
    else:
        print("impossible")
    exit()

if (n == 3):
    if(graph[0][1]+graph[1][2]==L):
        print("possible")
    else:
        print("impossible")
    exit()"""