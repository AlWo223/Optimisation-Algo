import math
n, L = map(int, input().strip().split(" "))

graph = [[] for ii in range(0, n)]
for xx in range(0, n):
    for weight in input().strip().split(" "):
        graph[xx].append(int(weight))

from itertools import permutations
from itertools import combinations

### Handle trivial cases
if (n == 2):
    if (graph[0][1]*2 == L):
        print("possible")
    else:
        print("impossible")
    exit()

if (n == 3):
    if(graph[0][1]+graph[1][2]+graph[2][0]==L):
        print("possible")
    else:
        print("impossible")
    exit()

def calculateDistance(perm, middle):
    length = 0
    u = 0
    for ii in perm:
        length += graph[u][ii]
        u = ii
    length += graph[perm[-1]][middle]
    return length

def testMiddleApproach(middle):
    nodes = list(range(1, n))
    nodes.remove(middle)
    for set1 in combinations(nodes, n//2-1):
        set2 = set(range(1, n)) - set(set1) - {middle}
        distances = set()
        for perm in permutations(set1):
            length = calculateDistance(perm, middle)
            if(length >= L):
                continue
            distances.add(length)

        for perm2 in permutations(set2):
            length = calculateDistance(perm2, middle)
            if(length >= L):
                continue
            if(L-length) in distances:
                return True
    return False


for xx in range(1, n):
    if(testMiddleApproach(xx)):
        print("possible")
        exit()

print("impossible")