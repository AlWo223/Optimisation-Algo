import math
import heapq

### Store input data
nxk = list(map(int, input().strip().split(" ")))
n = nxk[0]
x = nxk[1]
k = nxk[2]
heights = list(map(int, input().strip().split(" ")))

### Build n*(k+1) matrix
#graph = [[math.inf for ii in range(0, n*(k+1))] for jj in range(0, n*(k+1))]
graph = [{} for ii in range(0, n*(k+1))]

for ii in range(0, n):
    graph[ii][ii] = 0
    distances = list(map(int, input().strip().split(" ")))
    for jj in range(0, n):
        if distances[jj] != 0:
            height_diff = heights[ii]-heights[jj]
            if(height_diff>=0):
                for dd in range(0, k+1):
                    graph[ii*(k+1) + dd][jj*(k+1) + dd] = distances[jj]
            elif((-height_diff) <= k):
                for dd in range(0, k+1+height_diff):
                    graph[ii*(k+1) + dd][jj*(k+1) + dd - height_diff] = distances[jj]

#print(graph)

### Apply Dijkstra Algorithm
shortest_path = [math.inf] * n*(k+1) # list to store shortest path
shortest_path[0] = 0 # set distance of starting point to 0
visited = set()
pq = [(0, 0)] #Priority Queue considering shortest_path: (shortest_path, mountain)

def get_neighbours(mountain):
    neighbours = list()
    for ii, distance in graph[mountain].items():
        if (distance > 0) and (distance <= 10000):
            neighbours.append(ii)
    return neighbours

while pq:
    current_shortest, current_mountain = heapq.heappop(pq) # get mountain with shortest path (PQ)
    if((current_shortest, current_mountain) in visited):
        continue
    if(current_shortest>shortest_path[current_mountain]):
        continue
    for ii in get_neighbours(current_mountain):
        possible_path = shortest_path[current_mountain] + graph[current_mountain][ii]
        if ((possible_path < shortest_path[ii])):
            shortest_path[ii] = possible_path
            heapq.heappush(pq, (shortest_path[ii], ii))
    visited.add((shortest_path[current_mountain], current_mountain))

minimum = min(shortest_path[(x-1)*(k+1):((x-1)*(k+1)+k+1)])

if minimum <= n*1000:
    output = minimum
else:
    output = -1
print(output)
