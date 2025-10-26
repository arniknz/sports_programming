#include <bits/stdc++.h>

using namespace std;

//using ll = long long;

const int MAXCL = 1e5;
int colors[MAXCL] = {0};

bool f = true;

map<int, vector<int>> mk(vector<pair<int, int>> &g) {
    map<int, vector<int>> gr;
    for (auto x : g) {gr[x.first].push_back(x.second); gr[x.second].push_back(x.first);}
    return gr;
}

void dfs(int v, int col, map<int, vector<int>> &g) {
    colors[v] = col;
    for (auto u : g[v]) {
        if (!colors[u]) {
            dfs(u, -col, g);
        } else if (colors[u] != -col) {
            f = false;
            return;
        }
        if (!f) {return;}
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
    for (auto i = 1; i <= n; i++) {
        if (!colors[i]) {
            dfs(i, 1, gr);
        }
    }
    if (f) {
        cout << "YES" << endl;
    } else {
        cout << "NO" << endl;
    }
    return 0;
}