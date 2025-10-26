#include <bits/stdc++.h>

using namespace std;

const int MAXCL = 1e6;
int mxd = 0;
int otd = 0;

map<int, vector<int>> mk(vector<pair<int, int>> &g) {
    map<int, vector<int>> gr;
    for (auto x : g) {gr[x.first].push_back(x.second); gr[x.second].push_back(x.first);}
    return gr;
}

void dfs(int v, int p, int d, map<int, vector<int>> &g) {
    if (d > mxd) {
        mxd = d;
        otd = v;
    }
    for (auto u : g[v]) {
        if (u != p) {
            dfs(u, v, d + 1, g);
        }
    }
}

int main() {
    int n; cin >> n;
    vector<pair<int, int>> g;
    for (auto i = 1; i <= n - 1; i++) {
        int u, v; cin >> u >> v;
        g.push_back({u, v});
    }
    map<int, vector<int>> gr = mk(g);
    mxd = 0, otd = 1;
    dfs(1, -1, 0, gr);
    int fotd = otd; mxd = 0;
    dfs(fotd, -1, 0, gr);
    cout << mxd + 1 << endl;
    return 0;
}