from collections import deque
import math
import sys
sys.setrecursionlimit(1000000)
### Store input data

N, S = map(int, input().strip().split(" ")) # Number of intersections, total distance

trails = [{} for ii in range(0, N)] # Adjacency list to store graph

for ii in range(0, N-1):
    a, b, c = map(int, input().strip().split(" "))
    trails[a-1][b-1] = c
    trails[b-1][a-1] = c

amountPlaced = int(input().strip()) # Number of placed lamps
placedLamps = set()
if(amountPlaced>0):
    placedLamps = set(map(int, input().strip().split(" "))) # Positions of placed Lamps

enlighted = [0] * N
for xx in placedLamps:
    enlighted[xx -1] = 1

### BFS to calculate reachable positions (based on Steven Halim Library)
dist = [math.inf for u in range(N)]
dist[0] = 0
q = deque()
q.append(0)
reachablePositions = [False] * N
reachablePositions[0] = True

while (len(q) > 0):
        u = q.popleft()
        for v, w in trails[u].items():
            if(dist[u]+w <= S):                                    
                dist[v] = dist[u]+w
                reachablePositions[v] = True           # in case first edge too far
                if(dist[v]*2 < S):
                    q.append(v)
            elif(dist[u]<S):
                reachablePositions[v] = True         

memoization = {}

def dpVisitNode(node, parent):
    stack = [(node, parent, 0)]

    while(len(stack)>0):
        node, parent, _ = stack.pop()
    if(reachablePositions[node]):
        if((node, parent) in memoization):
            return memoization[(node, parent)]

        if(enlighted[node]==1):
            inv = 0
        else: 
            inv = 1
        outv = 0
        for child, w in trails[node].items():
            if(child == parent): 
                continue
            cinout = dpVisitNode(child, node)
            inv += min(cinout)
            outv += cinout[0]
        output = (inv, outv)
        memoization[(node, parent)] = output
        return output
    else:
        return (0, 0)

additionalLamps = min(dpVisitNode(0, -1))
print(additionalLamps)