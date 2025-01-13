#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    vector<pair<int, int>> e;
    for (int c = 0; c < m; c++) {
        int u, v;
        cin >> u >> v;
        e.push_back({u, v});
    }

    vector<vector<int>> mat(n, vector<int>(n, 0));
    for (auto el : e) {
        int i = el.first - 1;
        int j = el.second - 1;
        mat[i][j] = 1;
    }

    for (auto el : mat) {
        for (auto c : el) {
            cout << c << " ";
        }
        cout << '\n';
    }

    return 0;
}