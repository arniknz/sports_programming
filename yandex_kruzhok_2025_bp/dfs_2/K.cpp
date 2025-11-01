#include <bits/stdc++.h>

using namespace std;

const int MAXN = 1e6;
bool used[MAXN] = {false};
map<int, vector<pair<int, int>>> g;


int main() {
    int n, m; cin >> n >> m;
    for (auto i = 1; i <= m; i++) {
        int u, v; cin >> u >> v;
        g[u].push_back({v, i}); g[v].push_back({u, i});
    }
    return 0;
}
