INF = 10**18

class min_cost_max_flow:
  def __init__(self, V):
    self.V = V
    self.EL = []
    self.AL = [list() for _ in range(V)]
    self.vis = [False] * V
    self.total_cost = 0
    self.d = None
    self.last = None

  def SPFA(self, s, t):
    self.d = [INF] * self.V
    self.d[s] = 0
    self.vis[s] = True
    q = [s]
    while len(q) != 0:
      u = q[0]
      q.pop(0)
      self.vis[u] = False
      for idx in self.AL[u]:
        v, cap, flow, cost = self.EL[idx]
        if cap-flow > 0 and self.d[v] > self.d[u]+cost:
          self.d[v] = self.d[u]+cost
          if not self.vis[v]:
            q.append(v)
            self.vis[v] = True
    return self.d[t] != INF

  def DFS(self, u, t, f=INF):
    if u == t or f == 0:
      return f
    self.vis[u] = True
    for i in range(self.last[u], len(self.AL[u])):
      v, cap, flow, cost = self.EL[self.AL[u][i]]
      if not self.vis[v] and self.d[v] == self.d[u]+cost:
        pushed = self.DFS(v, t, min(f, cap-flow))
        if pushed != 0:
          self.total_cost += pushed * cost
          flow += pushed
          self.EL[self.AL[u][i]][2] = flow
          rv, rcap, rflow, rcost = self.EL[self.AL[u][i]^1]
          rflow -= pushed
          self.EL[self.AL[u][i]^1][2] = rflow
          self.vis[u] = False
          self.last[u] = i
          return pushed
    self.vis[u] = False
    return 0

  def add_edge(self, u, v, w, c, directed=True):
    if u == v:
      return
    self.EL.append([v, w, 0, c])
    self.AL[u].append(len(self.EL)-1)
    self.EL.append([u, 0 if directed else w, 0, -c])
    self.AL[v].append(len(self.EL)-1)

  def mcmf(self, s, t):
    mf = 0
    while self.SPFA(s, t):
      self.last = [0] * self.V
      f = self.DFS(s, t)
      while f != 0:
        mf += f
        f = self.DFS(s, t)
    return mf, self.total_cost


def main():
  print("Reading cases...")
  cases = int(input().strip())
  print("Read cases.")
  for ii in range(0, cases):
    print("New test case")
    W, H = map(int, input().strip().split(" "))
    mcmf = min_cost_max_flow(W*H*2+2)
    s = W*H*2
    t = W*H*2+1
    mcmf.add_edge(s, 0, INF, 0, False)
    mcmf.add_edge(W*H*2-1, t, INF, 0, False)
        
    print("Reading input...")
    graph = [[] for ff in range(0, H)]
    for xx in range(0, H):
      for yy, cell in enumerate(input().strip()):
        graph[xx].append(cell)
        
    print("Building graph...")
    for xx in range(0, H):
      for yy in range(0, W):
        inNode = xx*W+yy
        outNode = inNode + W*H

        if(graph[xx][yy] == '*'):
          mcmf.add_edge(inNode, outNode, 1, -1)
        else:
          mcmf.add_edge(inNode, outNode, 1, 0)

        neighbours = [(xx+1, yy), (xx, yy+1)]
        for (uu, vv) in neighbours:
          if((uu>=0) and (uu<H) and (vv>=0) and (vv<W)) and (graph[uu][vv] != '#'):
            inIndex = uu*W+vv
            outIndex = inIndex + W*H
            mcmf.add_edge(outNode, inIndex, 1, 0)
            mcmf.add_edge(outIndex, inNode, 1, 0)
    print("Finished building graph.")
    print("Starting MCMF computation...")
    mf, cost = mcmf.mcmf(s, t)
    print("Finished MCMF computation.")
    print(-cost)
            
if __name__ == '__main__':
  main()