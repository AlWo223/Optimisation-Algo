/*Courtesy of Steven Halim, Felix Halim, Suhendry Effendy
CP4 Free Source Code Project (cpp/gnu++17, java/java11, py/python3, and ml/ocaml).
https://github.com/stevenhalim/cpbook-code/blob/master/ch9/mcmf.py

-- Python implementation of library code translated to C++ --
*/

#include <bits/stdc++.h>

using namespace std;

const long long INF = 1e18;

struct Edge {
    int v;
    long long cap, flow, cost;
};

class MinCostMaxFlow {
    int V;
    vector<Edge> EL;
    vector<vector<int>> AL;
    vector<bool> vis;
    vector<long long> d;
    vector<int> last;
    long long total_cost = 0;

public:
    MinCostMaxFlow(int V) : V(V), AL(V), vis(V, false), d(V, INF) {}

    bool SPFA(int s, int t) {
        fill(d.begin(), d.end(), INF);
        d[s] = 0;
        vis[s] = true;
        queue<int> q;
        q.push(s);

        while (!q.empty()) {
            int u = q.front();
            q.pop();
            vis[u] = false;

            for (int idx : AL[u]) {
                int v = EL[idx].v;
                long long cap = EL[idx].cap, flow = EL[idx].flow, cost = EL[idx].cost;
                
                if (cap - flow > 0 && d[v] > d[u] + cost) {
                    d[v] = d[u] + cost;

                    if (!vis[v]) {
                        q.push(v);
                        vis[v] = true;
                    }
                }
            }
        }

        return d[t] != INF;
    }

    long long DFS(int u, int t, long long f = INF) {
        if (u == t || f == 0) return f;
        vis[u] = true;

        for (int &i = last[u]; i < AL[u].size(); ++i) {
            int idx = AL[u][i];
            Edge &e = EL[idx], &re = EL[idx^1];
            
            if (!vis[e.v] && d[e.v] == d[u] + e.cost && e.cap - e.flow > 0) {
                long long pushed = DFS(e.v, t, min(f, e.cap - e.flow));

                if (pushed != 0) {
                    total_cost += pushed * e.cost;
                    e.flow += pushed;
                    re.flow -= pushed;

                    vis[u] = false;
                    return pushed;
                }
            }
        }

        vis[u] = false;
        return 0;
    }

    void add_edge(int u, int v, long long w, long long c, bool directed = true) {
        if (u == v) return;

        EL.push_back({v, w, 0, c});
        AL[u].push_back(EL.size() - 1);
        
        EL.push_back({u, directed ? 0 : w, 0, -c});
        AL[v].push_back(EL.size() - 1);
    }

    pair<long long, long long> mcmf(int s, int t) {
        long long mf = 0;
        while (SPFA(s, t)) {
            last.assign(V, 0);
            long long f;

            while ((f = DFS(s, t)) != 0) {
                mf += f;
            }
        }

        return {mf, total_cost};
    }
};

int main() {
    int cases;
    cin >> cases;

    while (cases--) {
        int W, H;
        cin >> W >> H;
        int WH = W * H;
        
        MinCostMaxFlow mcmf(WH * 2 + 2);
        int s = WH * 2, t = WH * 2 + 1;
        
        mcmf.add_edge(s, 0, INF, 0, false);
        mcmf.add_edge(WH * 2 - 1, t, INF, 0, false);

        vector<string> graph(H);

        for (int i = 0; i < H; ++i) {
            cin >> graph[i];
        }

        for (int x = 0; x < H; ++x) {
            for (int y = 0; y < W; ++y) {
                int inNode = x * W + y;
                int outNode = inNode + WH;

                if (graph[x][y] == '*') {
                    mcmf.add_edge(inNode, outNode, 1, -1);
                    mcmf.add_edge(inNode, outNode, 1, 0);
                } else if (graph[x][y] != '#') {
                    mcmf.add_edge(inNode, outNode, 2, 0);
                }

                vector<pair<int, int>> neighboursSE = {{x + 1, y}, {x, y + 1}};

                for (auto [u, v] : neighboursSE) {
                    if (u < H && v < W && graph[u][v] != '#') {
                        int inIndex = u * W + v;
                        mcmf.add_edge(outNode, inIndex, 2, 0);
                    }
                }
            }
        }

        auto [mf1, cost1] = mcmf.mcmf(s, t);
        cout << -cost1 << endl;
    }

    return 0;
}