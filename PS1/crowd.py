import heapq
import math

### Store input data
n, m = map(int, input().strip().split(" "))
capacities = [{} for ii in range(0, n)] # Adjacency list to store street capacities
street_order = list()

for ii in range(0, m):
    a, b, c = map(int, input().strip().split(" "))
    capacities[a][b] = c
    capacities[b][a] = c
    street_order.append((a,b))

### Dijkstra Algorithm
maxcap_path = [0] * n # list to store max capacity path
predecessor = [None] * n # list to store previous intersection
pq = [(-math.inf, 0)] # priority queue considering maxcap_path

def get_neighbours(inter):
    neighbours = list()
    for ii, capacity in capacities[inter].items():
        neighbours.append(ii)
    return neighbours

while(pq):
    current_maxcap, current_inter = heapq.heappop(pq) # get intersection with max capacity path (PQ)
    current_maxcap = -current_maxcap
    for ii in get_neighbours(current_inter):
        possible_path = min(current_maxcap, capacities[current_inter][ii])
        if (possible_path > maxcap_path[ii]):
            predecessor[ii] = current_inter
            maxcap_path[ii] = possible_path
            heapq.heappush(pq, (-maxcap_path[ii], ii))

### Identify intersections of maxcap_path
intersections = list()
street = list()
node = n-1
while(node!=0 and node != None):
    street.append((predecessor[node], node))
    street.append((node, predecessor[node]))
    intersections.append(node)
    node = predecessor[node]
intersections.append(0)
intersections.reverse()

### Block streets
output = list()

for xx in street_order:
    if(xx not in street):
        if(xx[0] in intersections or xx[1] in intersections):
            output.append(street_order.index(xx))

if(output):
    output = [str(x) for x in sorted(output)]
    print(" ".join(output))
else:
    print("none")
