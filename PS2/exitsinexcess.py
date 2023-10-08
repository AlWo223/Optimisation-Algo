### Store input data
n, m = map(int, input().strip().split(" ")) # number of rooms, number of corridors

graph = [{} for ii in range(0, n)] # Adjacency list

forwardGraph = set()
backwardGraph = set()

for ii in range(m):
    u, v = map(int, input().strip().split(" ")) # corridor from u to v
    graph[u-1][v-1] = ii
    if(u<v):
        forwardGraph.add((u-1, v-1))
    else:
        backwardGraph.add((u-1, v-1))

if(len(forwardGraph) > len(backwardGraph)):
    acyclicGraph = forwardGraph
else:
    acyclicGraph = backwardGraph

result = list()

for xx in range(n):
    for v, id in graph[xx].items():
        if((xx, v) not in acyclicGraph):
            result.append(id)

print(len(result))
for ee in result:
    print(ee+1)
    