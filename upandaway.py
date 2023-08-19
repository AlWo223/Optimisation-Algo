import numpy as np
import math
### Store input data
nxk = list(map(int, input().strip().split(" ")))
n = nxk[0]
x = nxk[1]
k = nxk[2]
heights = list(map(int, input().strip().split(" ")))

distances = np.zeros((n, n))

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

shortest_path = {} # dictionary to store shortest path
predecessor = {} # dicitionary to store predecessor
unvisited = list(range(0, n)) # list of unvisited mountains

for ii in range(0, n):
    shortest_path[ii] = math.inf
    predecessor[ii] = None
shortest_path[0] = 0 # set distance of starting point to 0

while len(unvisited) > 0:
    current_mountain = min(unvisited) # get mountain with shortest path (PQ)
    for ii in get_neighbours(current_mountain):
        possible_path = shortest_path[current_mountain] + distances[current_mountain][ii]
        if possible_path < shortest_path[ii]:
            shortest_path[ii] = possible_path
            predecessor[ii] = current_mountain
    unvisited.remove(current_mountain) # set mountain to visited after having explored all neighbours

print(shortest_path[x-1])



