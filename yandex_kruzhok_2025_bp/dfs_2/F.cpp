#include <bits/stdc++.h>

using namespace std;

const int MAXN = 1e6;
bool used[MAXN] = {false};
int h[MAXN], d[MAXN];
map<int, vector<pair<int, int>>> g;
vector<int> ans;

void dfs(int v, int p = -1, int id = -1) {
    used[v] = true;
    d[v] = h[v] = (p == -1 ? 0 : h[p] + 1);
    for (auto &[u, i] : g[v]) {
        if (i == id) {continue;}
        if (used[u]) {
            d[v] = min(d[v], h[u]);
        } else {
            dfs(u, v, i);
            d[v] = min(d[v], d[u]);
            if (h[v] < d[u]) {
                ans.push_back(i);
            }
        }
    }
}

int main() {
    int n, m; cin >> n >> m;
    for (int i = 1; i <= m; i++) {
        int u, v; cin >> u >> v;
        g[u].push_back({v, i}); g[v].push_back({u, i});
    }
    for (int i = 1; i <= n; i++) {
        if (!used[i]) {
            dfs(i);
        }
    }
    sort(ans.begin(), ans.end());
    cout << ans.size() << endl;
    for (auto x : ans) {
        cout << x << endl;
    }
    return 0;
}