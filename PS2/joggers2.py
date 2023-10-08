N, S = map(int, input().strip().split(" ")) # Number of intersections, total distance

trails = [{} for ii in range(0, N)] # Adjacency list to store graph

for ii in range(0, N-1):
    a, b, c = map(int, input().strip().split(" "))
    trails[a-1][b-1] = c
    trails[b-1][a-1] = c

amountPlaced = int(input().strip()) # Number of placed lamps
placedLamps = set(map(int, input().strip().split(" "))) # Positions of placed Lamps

### DFS traversal to obtain postorder
dp = [0] * N
def dfsVisitNode(node, parent, dist):
    dp[node] = 0
    for child, w in trails[node].items():
        if(child == parent):
            continue
        dfsVisitNode(child, node, dist + w)

        dp[node] += dp[child]

        if(2*dist + w <= S):
            dp[node] = max(0, dp[node]-1)
    if(node+1 in placedLamps):
        dp[node] = max(0, dp[node]-1)

dfsVisitNode(0, -1, 0)
print(dp[0])

