"""
Courtesy of Steven Halim, Felix Halim, Suhendry Effendy
CP4 Free Source Code Project (cpp/gnu++17, java/java11, py/python3, and ml/ocaml).
https://github.com/stevenhalim/cpbook-code/blob/master/ch8/maxflow.py
"""
from numbers import Number
from copy import deepcopy
from collections import deque


INF = float('inf')


class MaxFlow:
    def __init__(self, V: int):
        self.V = V
        self.EL = []
        self.AL = [list() for _ in range(self.V)]
        self.d = []
        self.last = []
        self.p = []
        self.has_been_run = False

    def BFS(self, s: int, t: int) -> bool:
        self.d = [-1] * self.V
        self.d[s] = 0
        self.p = [[-1] for _ in range(self.V)]
        q = deque([s])
        while len(q) != 0:
            u = q.popleft()
            if u == t:
                break
            for idx in self.AL[u]:
                v, cap, flow = self.EL[idx]
                if cap - flow > 0 and self.d[v] == -1:
                    self.d[v] = self.d[u]+1
                    q.append(v)
                    self.p[v] = idx
        return self.d[t] != -1

    def send_one_flow(self, s: int, t: int, f: Number = INF) -> Number:
        if s == t:
            return f
        idx = self.p[t]
        u, cap, flow = self.EL[idx]
        pushed = self.send_one_flow(s, u, min(f, cap-flow))
        self.EL[idx][2] += pushed
        self.EL[idx ^ 1][2] -= pushed
        return pushed

    def DFS(self, u: int, t: int, f: Number = INF) -> Number:
        if u == t or f == 0:
            return f
        for i in range(self.last[u], len(self.AL[u])):
            self.last[u] = i
            v, cap, flow = self.EL[self.AL[u][i]]
            if self.d[v] != self.d[u]+1:
                continue
            pushed = self.DFS(v, t, min(f, cap - flow))
            if pushed != 0:
                self.EL[self.AL[u][i]][2] += pushed
                self.EL[self.AL[u][i] ^ 1][2] -= pushed
                return pushed
        return 0

    def add_edge(self, u: int, v: int, capacity: Number,
                 directed: bool = True) -> None:
        if u == v:
            return
        self.EL.append([v, capacity, 0])
        self.AL[u].append(len(self.EL)-1)
        self.EL.append([u, 0 if directed else capacity, 0])
        self.AL[v].append(len(self.EL)-1)

    def assert_has_not_already_been_run(self):
        if self.has_been_run:
            msg = ('Rerunning a max flow algorithm on the same graph will '
                   + 'result in incorrect behaviour. Please use .copy() '
                   + 'before you run any max flow algorithm if you need to '
                   + 'run multiple iterations')
            raise Exception(msg)

        self.has_been_run = True

    def dinic(self, s: int, t: int) -> Number:
        #self.assert_has_not_already_been_run()
        for edge in self.EL:
            edge[2] = 0

        mf = 0
        while self.BFS(s, t):
            self.last = [0] * self.V
            f = self.DFS(s, t)
            while f != 0:
                mf += f
                f = self.DFS(s, t)
        return mf

def main():
    ### Store input data
    n, p, k = map(int, input().strip().split(" ")) # number of stations, number of initial pipes, number of improvements

    edgesID = {}
    #edges = set()

    max_flow = MaxFlow(n)
    for xx in range(0, p):
        a, b, c = map(int, input().strip().split(" "))
        max_flow.add_edge(a-1, b-1, c, False)
        edgesID[(a, b)] = len(max_flow.EL)-2
        edgesID[(b, a)] = len(max_flow.EL)-1
        #edges.add((a, b))
        #edges.add((b, a))
    
    result = list()
    result.append(max_flow.dinic(0, 1))

    for xx in range(0, k):
        a, b, c = map(int, input().strip().split(" "))
        if((a,b) in edgesID):
            max_flow.EL[edgesID[(a, b)]][1] += c
            max_flow.EL[edgesID[(b, a)]][1] += c
        else:
            max_flow.add_edge(a-1, b-1, c, False)
            edgesID[(a, b)] = len(max_flow.EL)-2
            edgesID[(b, a)] = len(max_flow.EL)-1
            #edges.add((a, b))
            #edges.add((b, a))
        additional_flow = max_flow.dinic(0, 1)
        result.append(additional_flow)

    for xx in result:
        print(xx)

if __name__ == '__main__':
    main()