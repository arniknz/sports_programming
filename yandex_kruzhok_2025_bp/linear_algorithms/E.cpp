#include <bits/stdc++.h>

using namespace std;

using ll = long long;

int main() {
    ll t = 4, n;
    vector<vector<ll>> v;
    while (t--) {
        cin >> n;
        vector<ll> a(n);
        for (auto &x : a) {cin >> x;}
        v.push_back(a);
    }
    return 0;
}