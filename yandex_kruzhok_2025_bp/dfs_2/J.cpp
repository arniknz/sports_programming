#include <bits/stdc++.h>

using namespace std;

const int MAXN = 1e6;
bool used[MAXN] = {false};
int hup[MAXN], h[MAXN];
vector<pair<int, int>> ans;

map<int, vector<int>> mk(vector<pair<int, int>> &g) {
    map<int, vector<int>> gr;
    for (auto x : g) {gr[x.first].push_back(x.second); gr[x.second].push_back(x.first);}
    return gr;
}

void dfs(int v, map<int, vector<int>> &g, int p = -1) {
    used[v] = true;
    h[v] = hup[v] = (p == -1 ? 0 : hup[p] + 1);
    for (auto u : g[v]) {
        if (u != p) {
            if (used[u]) {
                h[u] = min(h[u], hup[u]);
            } else {
                dfs(u, g, v);
                h[v] = min(h[v], h[u]);
                if (hup[v] < h[u]) {
                    ans.push_back({v, u});
                }
            }
        }
    }
}

int main() {
    int n, m; cin >> n >> m;
    vector<pair<int, int>> g;
    while (m--) {
        int u, v; cin >> u >> v;
        g.push_back({u, v});
    }
    map<int, vector<int>> gr = mk(g);
    for (int i = 1; i <= n; i++) {
        if (!used[i]) {
            dfs(i, gr);
        }
    }
    cout << ans.size() << endl;
    for (auto &[v, u] : ans) {
        auto it = find(g.begin(), g.end(), pair{v, u});
        if (it != g.end()) {
            cout << it - g.begin() + 1 << endl;
        }
    }
    return 0;
}