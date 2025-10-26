#include <bits/stdc++.h>

using namespace std;

map<int, vector<int>> mk(vector<pair<int, int>> &g) {
    map<int, vector<int>> gr;
    for (auto x : g) {gr[x.first].push_back(x.second); gr[x.second].push_back(x.first);}
    return gr;
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
        cout << gr[i].size() << " ";
    }
    cout << endl;
    return 0;
}