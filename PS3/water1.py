"""
Courtesy of Steven Halim, Felix Halim, Suhendry Effendy
CP4 Free Source Code Project (cpp/gnu++17, java/java11, py/python3, and ml/ocaml).
https://github.com/stevenhalim/cpbook-code/blob/master/ch8/maxflow.py
"""
from numbers import Number
from copy import deepcopy

INF = float('inf')


class MaxFlow:
    def __init__(self, V: int):
        """
        Creates a new instance of the MaxFlow class. The general way you'll
        want to use this library is to create a new instance of the class,
        add edges, then call the `edmonds_karp` or `dinic` methods.
        While the library does support floats, be aware that it is not advised
        to use due to the potential for floating point errors, meaning small
        amounts of flow may be sent many times.

        Arguments:
            V: The number of vertices in the graph.

        Example:
            >>> mf = MaxFlow(3)
            >>> mf.add_edge(0, 1, 3)
            >>> mf.add_edge(0, 2, 3)
            >>> mf.add_edge(1, 2, 3)
            >>> mf.dinic(0, 2)  # or mf.edmonds_karp(0, 2)
            6
        """
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
        self.p = [[-1, -1] for _ in range(self.V)]
        q = [s]
        while len(q) != 0:
            u = q[0]
            q.pop(0)
            if u == t:
                break
            for idx in self.AL[u]:
                v, cap, flow = self.EL[idx]
                if cap - flow > 0 and self.d[v] == -1:
                    self.d[v] = self.d[u]+1
                    q.append(v)
                    self.p[v] = [u, idx]
        return self.d[t] != -1

    def send_one_flow(self, s: int, t: int, f: Number = INF) -> Number:
        if s == t:
            return f
        u, idx = self.p[t]
        _, cap, flow = self.EL[idx]
        pushed = self.send_one_flow(s, u, min(f, cap-flow))
        flow += pushed
        self.EL[idx][2] = flow
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
                flow += pushed
                self.EL[self.AL[u][i]][2] = flow
                self.EL[self.AL[u][i] ^ 1][2] -= pushed
                return pushed
        return 0

    def add_edge(self, u: int, v: int, capacity: Number,
                 directed: bool = True) -> None:
        """
        Adds an edge from `u` to `v` with capacity `w`. By default, the edge is
        directed, i.e. `u`->`v`. You can set `directed = False` to add it
        as an undirected edge `u`<->`v`.

        Arguments:
            `u`: The first vertex.
            `v`: The second vertex.
            `capacity`: The capacity of the edge.
            `directed`: Whether the edge is directed. True by default.

        Example:
            >>> mf = MaxFlow(3)
            >>> mf.add_edge(0, 1, 3)
            >>> mf.add_edge(2, 1, 3)
        """
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
        """
        Returns the max flow obtained by running Dinic's algorithm.
        Modifies the graph in place.

        Arguments:
            `s`: The source vertex.
            `t`: The sink vertex.

        Returns:
            The max flow.
        """
        self.assert_has_not_already_been_run()

        mf = 0
        while self.BFS(s, t):
            self.last = [0] * self.V
            f = self.DFS(s, t)
            while f != 0:
                mf += f
                f = self.DFS(s, t)
        return mf

    def copy(self) -> 'MaxFlow':
        """
        Returns a deep copy of the current instance. This is convenient for
        problems where you need to run MaxFlow multiple times on slightly
        different graphs, since the instance is destroyed after each max flow
        run.

        Example:
            >>> mf = MaxFlow(4)
            >>> mf.add_edge(0, 1, 3)
            >>> mf.add_edge(1, 2, 3)
            >>> for c in range(1, 4):
            >>>     mf_copy = mf.copy()
            >>>     mf_copy.add_edge(2, 3, c)
            >>>     res = mf_copy.dinic(0, 3)  # Will not modify mf
        """
        return deepcopy(self)

    def edmonds_karp(self, s: int, t: int) -> Number:
        """
        Returns the max flow obtained by running Edmons-Karp algorithm.
        Modifies the graph in place.

        Arguments:
            `s`: The source vertex.
            `t`: The sink vertex.

        Returns:
            The max flow.
        """
        self.assert_has_not_already_been_run()

        mf = 0
        while self.BFS(s, t):
            f = self.send_one_flow(s, t)
            if f == 0:
                break
            mf += f
        return mf

def main():
    ### Store input data
    n, p, k = map(int, input().strip().split(" ")) # number of stations, number of initial pipes, number of improvements

    edges = [{} for ii in range(n)]

    max_flow = MaxFlow(n)
    for xx in range(0, p):
        a, b, c = map(int, input().strip().split(" "))
        edges[a][b] = c
        max_flow.add_edge(a-1, b-1, c, False)
    
    result = list()
    result.append(max_flow.dinic(0, 1))

    for xx in range(0, k):
        a, b, c = map(int, input().strip().split(" "))
        #max_flow = MaxFlow(n)
        edges[a][b] = edges[a].get(b, 0) + c
        for xx in range(0, n):
            for yy, cap in edges[xx].items():
                max_flow.add_edge(xx-1, yy-1, cap, False)
        result.append(max_flow.dinic(0, 1))

    for xx in result:
        print(xx)

if __name__ == '__main__':
    main()