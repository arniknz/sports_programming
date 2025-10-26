#include <bits/stdc++.h>

using namespace std;

//using ll = long long;

const int MAXCL = 1e5;
int comp[MAXCL] = {0};
map<int, vector<int>> comps;

map<int, vector<int>> mk(vector<pair<int, int>> &g) {
    map<int, vector<int>> gr;
    for (auto x : g) {gr[x.first].push_back(x.second); gr[x.second].push_back(x.first);}
    return gr;
}

void dfs(int v, int num, map<int, vector<int>> &g) {
    comp[v] = num;
    comps[num].push_back(v);
    for (auto u : g[v]) {
        if (!comp[u]) {
            dfs(u, num, g);
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
    int ans = 0;
    for (auto i = 1; i <= n; i++) {
        if (!comp[i]) {dfs(i, ++ans, gr);}
    }
    cout << ans << endl;
    for (auto &[cmp, vrt] : comps) {
        cout << vrt.size() << endl;
        sort(vrt.begin(), vrt.end());
        for (auto x : vrt) {cout << x << " ";}
        cout << endl;
    }
    return 0;
}