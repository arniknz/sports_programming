#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    vector<vector<int>> g(n + 1);
    for (int c = 0; c < m; c++) {
        int u, v;
        cin >> u >> v;
        g[u - 1].push_back(v - 1);
    }

    for (int i = 0; i < n; i++) {
        sort(g[i].begin(), g[i].end());
        cout << g[i].size();
        for (int v : g[i]) {
            cout << " " << v + 1;
        }
        cout << '\n';
    }

    return 0;
}