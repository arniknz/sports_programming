#include <bits/stdc++.h>

using namespace std;

using ll = long long;

int main() {
    ll n, l = 0, r = 0, ans = -1e18, mx = 0, t = 0; cin >> n; vector<ll> a(n);
    for (auto &x : a) {cin >> x;}
    for (auto i = 0; i < n; i++) {
        mx += a[i];
        if (ans < mx) {
            ans = mx;
            l = t;
            r = i;
        }
        if (mx < 0) {
            mx = 0;
            t = i + 1;
        }
    }
    cout << l + 1 << " " << r + 1 << " " << ans << endl;
    return 0;
}