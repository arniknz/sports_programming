#include <bits/stdc++.h>

using namespace std;

const int MAXCL = 1e5;
int used[MAXCL] = {0};

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
    return false;
}

int main() {
    int n; cin >> n; vector<pair<int, int>> r, b;
    for (auto i = 0; i < n - 1; i++) {
        for (auto j = 0; j < n - i; j++) {
            char s; cin >> s;
            if (s == 'R') {
                r.push_back({i, i + j});
            } else {
                b.push_back({i + j, i});
            }
        }
    }
    map<int, vector<int>> gr = mk(r), gb = mk(b);
    return 0;
}