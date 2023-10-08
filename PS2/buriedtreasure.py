import sys
sys.setrecursionlimit(1000000)
### Store input data
n, m = map(int, input().strip().split(" ")) # Number of treasure maps, number of possible locations

implications = [{} for ii in range(2*m+1)] # Adjacency list to store implications

for ii in range(n):
    m1, m2 = map(int, input().strip().split(" ")) # Location 1 and 2
    implications[-m1+m][m2+m] = 1
    implications[-m2+m][m1+m] = 1

### Check if there is a vertex which belongs to SCC just like its negation
### Use Tarjan SCC algorithm from Steven Halim's library (https://github.com/stevenhalim/cpbook-code/blob/26fb7376417799f8b84b504d46ea7c8c0cf71c29/ch4/traversal/UVa11838.py)

UNVISITED = -1

S = []

def tarjanSCC(u):
    global dfs_low, dfs_num, dfsNumberCounter, visited
    global numSCC, st

    dfs_low[u] = dfs_num[u] = dfsNumberCounter
    dfsNumberCounter += 1
    st.append(u)
    visited[u] = True
    for v, w in implications[u].items():
        if dfs_num[v] == UNVISITED:
            tarjanSCC(v)
        if visited[v]:
            dfs_low[u] = min(dfs_low[u], dfs_low[v])

    if dfs_low[u] == dfs_num[u]:
        numSCC += 1
        scc = set()
        while True:
            v = st[-1]
            st.pop()
            visited[v] = False
            scc.add(v)
            if u == v:
                break
        S.append(scc)

dfs_num = [UNVISITED] * (2*m+1)
dfs_low = [0] * (2*m+1)
visited = [False] * (2*m+1)
st = []
dfsNumberCounter = 0
numSCC = 0
for u in range(-m,m+1):
    if(u == 0): continue
    u += m
    if dfs_num[u] == UNVISITED:
        tarjanSCC(u)

for scc in S:
    for v in scc:
        if(m - (v-m) in scc):
            print("NO")
            exit()
            
print("YES")
