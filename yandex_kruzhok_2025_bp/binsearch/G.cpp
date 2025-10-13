#include <bits/stdc++.h>

using namespace std;

using ll = long long;

ll f(ll t, ll x, ll y) {
    return t / x + t / y;
}

int main() {
    ll n, x, y;
    cin >> n >> x >> y;
    ll l = 0, r = max(x, y) * (n - 1);
    while (l < r) {
        ll m = (l + r) / 2;
        if (f(m, x, y) < n - 1) {
            l = m + 1;
        } else {
            r = m;
        }
    }
    cout << l + min(x, y) << endl;
    return 0;
}