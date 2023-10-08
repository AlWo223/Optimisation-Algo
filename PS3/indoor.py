import math
import sys
sys.setrecursionlimit(1000000000)

### Store input data
n, L = map(int, input().strip().split(" "))

graph = [[] for ii in range(0, n)]
for xx in range(0, n):
    for weight in input().strip().split(" "):
        graph[xx].append(int(weight))

min_distances = list()
max_distances = list()
for ii in range(0, n):
    distances = sorted(graph[ii])
    min_distances.append(distances[1])
    max_distances.append(distances[-1])

### Calculate rough estimate for solutions boundaries
def checkSolutionBoundaries(current, remainingNodes, remainingL):
    #print("Check boundaries")
    min_edge_sum = 0
    max_edge_sum = 0
    for id in remainingNodes:
        min_edge_sum += min_distances[id]
        max_edge_sum += max_distances[id]
    min_edge_sum += min_distances[current]
    max_edge_sum += max_distances[current]
    #print("Remaining L: {}".format(remainingL))
    #print("Min edge sum: {}".format(min_edge_sum))
    #print("Max edge sum: {}".format(max_edge_sum))

    ### Check if L within boundaries
    if (remainingL < min_edge_sum) or (remainingL > max_edge_sum):
        #print("impossible")
        #exit()
        return False
    return True

def backtrack(current, remaining, dist):
    #print("Visit node: {}".format(current))
    if len(remaining) == 0:
        if(dist + graph[current][0]) == L:
            print("possible")
            exit()
        return
    if dist > L:
        return
    if not checkSolutionBoundaries(current, remaining, L-dist):
        #print("Exceeding boundaries, go back to parent")
        return
    """if (len(remaining)+1 > L-dist):
        #print("-- drop path, go back to parent --")
        return"""
    #print("-- Explore children --")
    for xx in remaining:
        #print("Explore child: {}".format(xx))
        dist_new = dist + graph[current][xx]
        if(dist_new < L):
            backtrack(xx, remaining - {xx}, dist_new)
        #print("Exploration ended or not feasible")

nodes = set(range(1, n))
backtrack(0, nodes, 0)
print("impossible")
