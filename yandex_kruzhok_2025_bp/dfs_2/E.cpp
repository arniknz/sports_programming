#include <bits/stdc++.h>

using namespace std;

const int MAXN = 1e6;
bool used[MAXN] = {false};
int h[MAXN], d[MAXN];
map<int, vector<pair<int, int>>> g;
vector<bool> most(MAXN, false);
vector<int> comp(MAXN, -1);
int comp_cnt = 0;

void bridges(int v, int p = -1, int id = -1) {
    used[v] = true;
    d[v] = h[v] = (p == -1 ? 0 : h[p] + 1);
    for (auto &[u, i] : g[v]) {
        if (i == id) {continue;}
        if (used[u]) {
            d[v] = min(d[v], h[u]);
        } else {
            bridges(u, v, i);
            d[v] = min(d[v], d[u]);
            if (h[v] < d[u]) {
                most[i] = true;
            }
        }
    }
}

void comps(int v, int id) {
    comp[v] = id;
    for (auto &[u, i] : g[v]) {
        if (comp[u] == -1 && !most[i]) {
            comps(u, id);
        }
    }
}

pair<int, int> diameter(int v, int p, int d, vector<set<int>> &g) {
    pair<int, int> ans = {v, d};
    for (auto u : g[v]) {
        if (u != p) {
            auto curr = diameter(u, v, d + 1, g);
            if (curr.second > ans.second) {
                ans = curr;
            }
        }
    }
    return ans;
}

void dfs(int v, vector<set<int>> &g, vector<bool> &vs) {
    vs[v] = true;
    for (auto u : g[v]) {if (!vs[u]) {dfs(u, g, vs);}}
}

int fd(int st, vector<set<int>> &g, vector<bool> &vs) {
    auto [x, y] = diameter(st, -1, 0, g); auto [a, b] = diameter(x, -1, 0, g);
    dfs(st, g, vs);
    return b;
}

int main() {
    int n, m; cin >> n >> m;
    for (auto i = 1; i <= m; i++) {
        int u, v; cin >> u >> v;
        g[u].push_back({v, i}); g[v].push_back({u, i});
    }
    for (auto i = 1; i <= n; i++) {if (!used[i]) {bridges(i);}}
    for (auto i = 1; i <= n; i++) {if (comp[i] == -1) {comps(i, comp_cnt++);}}
    int b = 0, diam = 0;
    vector<set<int>> bt(comp_cnt);
    for (auto i = 1; i <= n; i++) {
        for (auto &[u, id] : g[i]) {
            if (comp[i] != comp[u]) {
                bt[comp[i]].insert(comp[u]);
                bt[comp[u]].insert(comp[i]);
            }
        }
    }
    for (auto i = 0; i < comp_cnt; i++) {b += bt[i].size();}
    b /= 2;
    vector<bool> vs(comp_cnt, false);
    for (auto i = 0; i < comp_cnt; i++) {
        if (!vs[i] && !bt[i].empty()) {diam = max(diam, fd(i, bt, vs));}
    }
    cout << max(0, b - diam) << endl;
    return 0;
}
