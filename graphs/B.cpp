#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    vector<int> g(n, 0);
    for (int c = 0; c < m; c++) {
        int u, v;
        cin >> u >> v;
        g[u - 1] += 1;
        g[v - 1] += 1;
    }

    for (auto c : g) {
        cout << c << " ";
    }
    cout << "\n";

    return 0;
}
