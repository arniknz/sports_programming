#include <bits/stdc++.h>

using namespace std;

const int MAXCL = 1e5;
bool used[MAXCL] = {0};
int cnt = 0;

void dfs(int v, map<int, vector<int>> &g) {
    used[v] = true;
    for (auto u : g[v]) {
        if (!used[u]) {
            cnt++;
            dfs(u, g);
        }
    }
}

int main() {
    int n, s; cin >> n >> s;
    vector<vector<int>> mt;
    for (int i = 0; i < n; i++) {
        vector<int> r(n);
        for (auto &x : r) {cin >> x;}
        mt.push_back(r);
    }
    map<int, vector<int>> g;
    for (auto i = 0; i < n; i++) {
        for (auto j = 0; j < n; j++) {
            if (mt[i][j] != 0) {
                g[i + 1].push_back(j + 1);
            }
        }
    }
    dfs(s, g);
    cout << cnt + 1 << endl;
    return 0;
}