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
placedLamps = set(map(int, input().strip().split(" "))) # Positions of placed Lamps

### BFS to calculate reachable positions (based on Steven Halim Library)
dist = [math.inf] * N
dist[0] = 0
q = deque()
q.append(0)
reachablePositions = set()
reachablePositions.add(0)

while (len(q) > 0):
        u = q.popleft()
        for v, w in trails[u].items(): 
            if dist[u] + w < dist[v]:                                            
                dist[v] = dist[u]+w
                if not (dist[v] >= S and u==0):
                    reachablePositions.add(v)           # problematic if first edge too far
                if(dist[v]*2 < S):
                    q.append(v)

stack = [(0, -1)]
dp = {}

while len(stack) > 0:
    node, parent = stack[-1]
    if (node in dp):
        stack.pop()
        continue

    nodeFinished = True

    for child, w in trails[node].items():
            if(child == parent): 
                continue
            if not(child in dp):
                stack.append((child, node))
                nodeFinished = False
    
    if(nodeFinished):
        stack.pop()
        if(node+1 in placedLamps):
            inv = 0
        else: 
            inv = 1
        outv = 0
        for child, w in trails[node].items():
            if(child == parent): 
                continue
            cinout = dp[child]
            inv += min(cinout)
            outv += cinout[0]
        dp[node] = (inv, outv)

additionalLamps = min(dp[0])
print(additionalLamps)
