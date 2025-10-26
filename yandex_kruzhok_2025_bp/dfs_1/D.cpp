#include <bits/stdc++.h>

using namespace std;

const int MAXCL = 1e6;
int used[MAXCL] = {0};

map<int, vector<int>> mk(vector<pair<int, int>> &g) {
    map<int, vector<int>> gr;
    for (auto x : g) {gr[x.first].push_back(x.second); gr[x.second].push_back(x.first);}
    return gr;
}

void dfs(int v, map<int, vector<int>> &g, int id) {
    used[v] = id;
    for (auto u : g[v]) {
        if (!used[u]) {
            dfs(u, g, id);
        }
    }
}

int main() {
    int n, m, t, k; cin >> n >> m >> t;
    vector<pair<int, int>> g;
    while (m--) {
        int u, v; cin >> u >> v;
        if (u != t && v != t) {
            g.push_back({u, v});
        }
    }
    map<int, vector<int>> gr = mk(g);
    int id = 1;
    for (auto i = 1; i <= n; i++) {
        if (!used[i] && i != t) {
            dfs(i, gr, id++);
        }
    }
    cin >> k;
    while (k--) {
        int a, b; cin >> a >> b;
        if (used[a] == used[b] && a != t && b != t && used[a] != 0) {
            cout <<  "Yes" << endl;
        } else {
            cout << "No" << endl;
        }
    }
    return 0;
}