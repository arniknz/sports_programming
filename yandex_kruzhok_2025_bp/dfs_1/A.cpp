#include <bits/stdc++.h>

using namespace std;

using ll = long long;

int main() {
    ll n, m; cin >> n >> m;
    vector<vector<ll>> mt(n, vector<ll>(n, 0));
    vector<pair<ll, ll>> g;
    while (m--) {
        ll u, v; cin >> u >> v;
        g.push_back({u, v});
    }
    for (auto x : g) {
        auto i = x.first - 1, j = x.second - 1;
        mt[i][j] = 1;
    }
    for (auto r: mt) {
        for (auto c : r) {
            cout << c << " ";
        }
        cout << endl;
    }
    return 0;
}