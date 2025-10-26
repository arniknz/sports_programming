#include <bits/stdc++.h>

using namespace std;

//using ll = long long;

const int MAXCL = 1e5;
int used[MAXCL] = {0};
vector<int> ans;

map<int, vector<int>> mk(vector<pair<int, int>> &g) {
    map<int, vector<int>> gr;
    for (auto x : g) {gr[x.first].push_back(x.second);}
    return gr;
}

bool dfs(int v, map<int, vector<int>> &g) {
    used[v] = 1;
    for (auto u : g[v]) {
        if (used[u] == 0) {
            if (dfs(u, g)) {return true;}
        } else if (used[u] == 1) {
            return true;
        }
    }
    used[v] = 2;
    ans.push_back(v);
    return false;
}

int main() {
    int n, m; cin >> n >> m;
    vector<pair<int, int>> g;
    while (m--) {
        int u, v; cin >> u >> v;
        g.push_back({u, v});
    }
    map<int, vector<int>> gr = mk(g);
    vector<int> p(n); for (auto &x : p) {cin >> x;}
    for (auto i = 1; i <= n; i++) {
        if (used[i] == 0) {
            if (dfs(i, gr)) {
                cout << "NO" << endl;
                return 0;
            }
        }
    }
    reverse(ans.begin(), ans.end());
    vector<int> pos(n + 1);
    for (auto i = 0; i < n; i++) {pos[p[i]] = i;}
    for (auto &x : g) {
        if (pos[x.first] > pos[x.second]) {
            cout << "NO" << endl;
                return 0;
        }
    }
    cout << "YES" << endl;
    return 0;
}