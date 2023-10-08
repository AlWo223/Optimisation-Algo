import math
import heapq
### Store input data
nxk = list(map(int, input().strip().split(" ")))
n = nxk[0]
x = nxk[1]
k = nxk[2]
heights = list(map(int, input().strip().split(" ")))

distances = [[]] * n
for ii in range(0, n):
   distances[ii] = list(map(int, input().strip().split(" ")))

### Dijkstra Algorithm to find shortest path

### get neighbours of specific mountain
def get_neighbours(mountain):
    neighbours = list()
    for ii in range(0, n):
        if distances[mountain][ii] > 0:
            neighbours.append(ii)
    return neighbours

shortest_path = [math.inf] * n # list to store shortest path
predecessor = [None] * n # dicitionary to store predecessor
required_k = [math.inf] * n # list to store required k for travel
required_k[0] = 0
pq = [(0, 0, 0)] # Priority Queue considering shortest_path and required_k
shortest_path[0] = 0 # set distance of starting point to 0
visited = set()

while pq:
    current_shortest, current_k, current_mountain = heapq.heappop(pq) # get mountain with shortest path (PQ)
    if((current_shortest, current_k, current_mountain) in visited):
        continue
    if(current_mountain==x-1): break
    for ii in get_neighbours(current_mountain):
        possible_path = shortest_path[current_mountain] + distances[current_mountain][ii]
        possible_required_k = required_k[current_mountain] + max(heights[ii]-heights[current_mountain], 0)
        if (((possible_path < shortest_path[ii]) or (possible_path == shortest_path[ii] and possible_required_k < required_k[ii])) and (possible_required_k<=k)):
            shortest_path[ii] = possible_path
            predecessor[ii] = current_mountain
            required_k[ii] = possible_required_k
            heapq.heappush(pq, (shortest_path[ii], required_k[ii], ii))
    visited.add((shortest_path[current_mountain], required_k[current_mountain], current_mountain))

if(shortest_path[x-1]<=1000):
    output = shortest_path[x-1]
else:
    output = -1
print(output)