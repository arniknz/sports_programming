#include <bits/stdc++.h>

using namespace std;

const int MAXN = 1e6;
map<int, vector<int>> t;
vector<int> ord;
bool used[MAXN] = {false};
int comps[MAXN] = {0};
int cnt = 0;

void dfs1(int v, map<int, vector<int>> &g) {
    used[v] = true;
    for (auto u : g[v]) {
        if (!used[u]) {
            dfs1(u, g);
        }
    }
    ord.push_back(v);
}

void dfs2(int v, map<int, vector<int>> &g) {
    comps[v] = cnt;
    for (auto u : g[v]) {
        if (comps[u] == 0) {
            dfs2(u, g);
        }
    }
}

map<int, vector<int>> mk(vector<pair<int, int>> &g) {
    map<int, vector<int>> gr;
    for (auto x : g) {gr[x.first].push_back(x.second);}
    return gr;
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
        for (auto u : gr[i]) {
            t[u].push_back(i);
        }
    }
    for (int i = 1; i <= n; i++) {
        if (!used[i]) {
            dfs1(i, gr);
        }
    }
    reverse(ord.begin(), ord.end());
    for (auto o : ord) {
        if (comps[o] == 0) {
            cnt++;
            dfs2(o, t);
        }
    }
    int ans = 0;
    map<int, set<int>> cond;
    for (int i = 1; i <= n; i++) {
        for (auto u : gr[i]) {
            int ci = comps[i], cu = comps[u];
            if (ci != cu && !cond[ci].count(cu)) {cond[ci].insert(cu); ans++;}
        }
    }
    cout << ans << endl;
    return 0;
}