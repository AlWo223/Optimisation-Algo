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
    cases = int(input().strip())
    for ii in range(0, cases):
        W, H = map(int, input().strip().split(" "))
        WH = W*H
        mcmf = min_cost_max_flow(WH*2+2)
        s = WH*2
        t = WH*2+1
        mcmf.add_edge(s, 0, INF, 0, False)
        mcmf.add_edge(WH*2-1, t, INF, 0, False)
    
        graph = [[None]*W for xx in range(0, H)]
        for xx in range(0, H):
            row = input().strip()
            for yy, cell in enumerate(row):
                graph[xx][yy] = cell
        
        for xx in range(0, H):
            for yy in range(0, W):
                inNode = xx*W+yy
                outNode = inNode + WH

                if(graph[xx][yy] == '*'):
                    mcmf.add_edge(inNode, outNode, 1, -1)
                    mcmf.add_edge(inNode, outNode, 1, 0)
                elif (graph[xx][yy] != '#'):
                    mcmf.add_edge(inNode, outNode, 2, 0)

                neighboursSE = [(xx+1, yy), (xx, yy+1)]
                for (uu, vv) in neighboursSE:
                    if((uu<H) and (vv<W)) and (graph[uu][vv] != '#'):
                        inIndex = uu*W+vv
                        mcmf.add_edge(outNode, inIndex, 2, 0)
        mf1, cost1 = mcmf.mcmf(s, t)
        print(-cost1)
            
if __name__ == '__main__':
    main()