#include <bits/stdc++.h>

using namespace std;

using ll = long long;

int main() {
    ll n, m, s, q, x, y;
    cin >> n >> m >> s;
    map<int, vector<ll>> a;
    map<int, vector<ll>> b;
    for (int i = 0; i < n; i++) {
        vector<ll> tmp(s);
        for (auto &x : tmp) {cin >> x;}
        a[i] = tmp;
    }
    for (int i = 0; i < m; i++) {
        vector<ll> tmp(s);
        for (auto &x : tmp) {cin >> x;}
        b[i] = tmp;
    }
    cin >> q;
    while (q--) {
        cin >> x >> y;
        x--; y--;
        ll l = 0, r = s - 1;
        while (l < r) {
            ll m = (l + r) / 2;
            if (a[x][m] < b[y][m]) {
                l = m + 1;
            } else {
                r = m;
            }
        }
        vector<ll> ans = {l};
        if (l != 0) {ans.push_back(l - 1);}
        if (l != s - 1) {ans.push_back(l + 1);}
        pair<ll, ll> res = {-1, 1e10};
        for (auto k : ans) {
            if (max(a[x][k], b[y][k]) < res.second) {
                res.first = k;
                res.second = max(a[x][k], b[y][k]);
            }
        }
        cout << res.first + 1 << endl;
    }
    return 0;
}