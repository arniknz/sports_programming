#include <bits/stdc++.h>

using namespace std;

//using ll = long long;

const int MAXCL = 1e5;
int colors[MAXCL] = {0};
bool used[MAXCL] = {false};
int par[MAXCL] = {0};
int c_end = -1, c_start = -1;
vector<int> ans;

map<int, vector<int>> mk(vector<pair<int, int>> &g) {
    map<int, vector<int>> gr;
    for (auto x : g) {gr[x.first].push_back(x.second); gr[x.second].push_back(x.first);}
    return gr;
}

bool dfs(int v, int col, map<int, vector<int>> &g) {
    colors[v] = col;
    for (auto u : g[v]) {
        if (!colors[u]) {
            par[u] = v;
            if (dfs(u, 3 - col, g)) {return true;}
        } else if (colors[u] == col) {
            c_end = v; c_start = u;
            return true;
        }
    }
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
    for (auto i = 1; i <= n; i++) {
        if (!colors[i]) {
            if (dfs(i, 1, gr)) {
                cout << "YES" << endl;
                int k = c_end;
                while (k != c_start) {
                    ans.push_back(k); k = par[k];
                }
                ans.push_back(c_start);
                cout << ans.size() << endl;
                for (auto x : ans) {cout << x << " ";}
                cout << endl;
                return 0;
            }
        }
    }
    cout << "NO" << endl;
    return 0;
}