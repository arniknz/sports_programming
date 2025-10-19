#include <bits/stdc++.h>

using namespace std;

using ll = long long;

int main() {
    ll n, k; cin >> n >> k; vector<ll> a(n);
    for (auto &x : a) {cin >> x;}
    ll ans = 0, l = 0, cur = 0;
    for (auto r = 0; r < n; r++) {
        cur ^= a[r];
        while (l <= r && cur >= k) {
            ans += n - r;
            cur ^= a[l++];
        }
    }
    cout << ans << endl;
}