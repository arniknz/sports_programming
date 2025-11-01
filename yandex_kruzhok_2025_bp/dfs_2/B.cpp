#include <bits/stdc++.h>

using namespace std;

int MAXN = 1e5;
vector<vector<bool>> used(MAXN, vector<bool>(MAXN, false));

void dfs(int x, int y, vector<vector<int>> mt, int n) {
    used[x][y] = true;
    for (auto i = 0; i < n; i++) {
        for (auto j = 0; j < n; j++) {
            if (!used[i][j]) {

            }
        }
    }
}

int main() {
    int n, m; cin >> n >> m;
    vector<vector<int>> mt;
    for (int i = 0; i < n; i++) {
        vector<int> r(n);
        for (auto &x : r) {cin >> x;}
        mt.push_back(r);
    }
    return 0;
}