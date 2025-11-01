#include <bits/stdc++.h>

using namespace std;

const int MAXN = 1e6;
bool used[MAXN] = {false};
int h[MAXN], d[MAXN];
map<int, vector<int>> g;
set<int> ans;

void dfs(int v, int p = -1) {
    used[v] = true;
    d[v] = h[v] = (p == -1 ? 0 : h[p] + 1);
    int c = 0;
    for (auto u : g[v]) {
        if (u != p) {
            if (used[u]) {
                d[v] = min(d[v], h[u]);
            } else {
                dfs(u, v);
                d[v] = min(d[v], d[u]);
                if (h[v] <= d[u] && p != -1) {
                    ans.insert(v);
                }
                c++;
            }
        }
    }
    if (p == -1 && c > 1) {
        ans.insert(v);
    }
}

int main() {
    int n, m; cin >> n >> m;
    for (int i = 1; i <= m; i++) {
        int u, v; cin >> u >> v;
        g[u].push_back(v); g[v].push_back(u);
    }
    for (int i = 1; i <= n; i++) {
        if (!used[i]) {
            dfs(i);
        }
    }
    cout << ans.size() << endl;
    for (auto x : ans) {
        cout << x << " ";
    }
    cout << endl;
    return 0;
}