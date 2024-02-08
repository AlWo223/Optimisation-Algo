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
	n, m, r = map(int, input().strip().split(" "))
	mf = min_cost_max_flow(n+m+2)
	s = n+m
	t = n+m+1
	b_covered = [False]*m
	a_covered = [False]*n
	for xx in range(0, r):
		a, b, c = map(int, input().strip().split(" "))
		mf.add_edge(a-1, b+n-1, 1, -c, True)
		if not(b_covered[b-1]):
			mf.add_edge(b+n-1, t, 1, 0, True)
			b_covered[b-1] = True
		if not(a_covered[a-1]):
			mf.add_edge(s, a-1, 1, 0, True)
			a_covered[a-1] = True
			
	mf, total_cost = mf.mcmf(s, t)
	total_cost = total_cost*(-1)
	print("{} {}".format(n-mf, total_cost))

if __name__ == '__main__':
    main()