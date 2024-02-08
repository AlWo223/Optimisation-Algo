INF = 10**18

"""
Courtesy of Steven Halim, Felix Halim, Suhendry Effendy
CP4 Free Source Code Project (cpp/gnu++17, java/java11, py/python3, and ml/ocaml).
https://github.com/stevenhalim/cpbook-code/blob/master/ch4/sssp/bellman_ford.py
"""
def bellman_ford(V, s, AL):
    dist = [INF for u in range(V)]               # INF = 1e9 here
    dist[s] = 0
    for i in range(0, V-1):                      # total O(V*E)
        modified = False                         # optimization
        for u in range(0, V):                    # these two loops = O(E)
            if (not dist[u] == INF):             # important check
                for v, w in AL[u]:
                    if (dist[u]+w >= dist[v]): continue # not improving, skip
                    dist[v] = dist[u]+w       # relax operation
                    modified = True              # optimization
        if (not modified): break                 # optimization
    return dist

"""
Modified dp bitmask mcm from cpbook:
Courtesy of Steven Halim, Felix Halim, Suhendry Effendy
CP4 Free Source Code Project (cpp/gnu++17, java/java11, py/python3, and ml/ocaml).
https://github.com/stevenhalim/cpbook-code/blob/master/ch8/UVa10911.py
"""
import sys, math
from functools import lru_cache
sys.setrecursionlimit(5000)

def LSOne(S):
    return ((S) & -(S))                          # important speedup

def mcpm_dp(N, dist):

        @lru_cache(maxsize=None)
        def dp(mask):                            # DP state = mask
            if mask == 0: return (0, [])         # all have been matched
            ans = (1e9, [])                      # init with a large value
            two_pow_p1 = LSOne(mask)             # speedup
            p1 = int(math.log2(two_pow_p1))      # p1 is first on bit
            m = mask-two_pow_p1                  # turn off bit p1
            while m:
                two_pow_p2 = LSOne(m);           # then, try to match p1
                p2 = int(math.log2(two_pow_p2))  # with another on bit p2
                sub = dp(mask^two_pow_p1^two_pow_p2)
                cost = dist[p1][p2]
                cost += sub[0]
                matching = [(p1, p2)] + sub[1]
                ans = min(ans, (cost, matching))
                m -= two_pow_p2                  # turn off bit p2
            return ans
        cost, matching = dp((1<<(N)) - 1)
        return cost, matching
    
def main():
    done = False
    output = list()
    while not(done):
        ### Store input data
        first_line = input().strip()
        if(first_line == "0"):
            done = True
            break
        n, m = map(int, first_line.split(" ")) # number of water stations, number of trails
        graph = [{} for xx in range(n)] # adjacency list with multiple edges between two nodes
        total = 0 # total cost of the jogging trail

        for xx in range(0, m):
            a, b, c = map(int, input().split(" ")) # station a, station b, cost c
            if(b-1 not in graph[a-1]):
                graph[a-1][b-1] = list()
            graph[a-1][b-1].append(c)
            if(len(graph[a-1][b-1]) > 1):
                graph[a-1][b-1].sort()
            graph[b-1][a-1] = graph[a-1][b-1]
            total += c
            
        ### Calculate degree of each node
        degree = [0]*n
        for xx in range(0, n):
            counter = 0
            for yy in range(0, n):
                if (yy in graph[xx]) and (xx != yy):
                    counter += len(graph[xx][yy])
            degree[xx] = counter

        ### Find odd nodes
        odd_nodes = list()
        for xx in range(0, n):
            if(degree[xx]%2 == 1):
                odd_nodes.append(xx)

        ### Graph with only one edge between two nodes (shortest one)
        AL = [[] for u in range(n)]
        for xx in range(0, n):
            for yy in range(0, n):
                if(yy in graph[xx]):
                    AL[xx].append((yy, graph[xx][yy][0]))
        
        ### Build graph with only odd nodes (shortest paths)
        num_odd_nodes = len(odd_nodes)
        if(num_odd_nodes == 0):
            output.append(total)
            continue

        odd_graph = [[0]*num_odd_nodes for xx in range(num_odd_nodes)]
        for xx in range(0, num_odd_nodes):
            min_paths = bellman_ford(n, odd_nodes[xx], AL)
            for yy in range(xx+1, num_odd_nodes):
                odd_graph[xx][yy] = min_paths[odd_nodes[yy]]
                odd_graph[yy][xx] = min_paths[odd_nodes[yy]]

        ### Min-Cost-Perfect-Matching (DP as n is small)
        cost, matching = mcpm_dp(num_odd_nodes, odd_graph)
        total += cost
        output.append(total)
    
    for xx in output:
        print(xx)

if __name__ == '__main__':
    main()