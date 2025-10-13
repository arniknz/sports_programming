#include <bits/stdc++.h>

using namespace std;

using ll = long long;

bool check(ll n, ll a, ll b, ll w, ll h, ll d) {
    ll ca = (w / (a + 2 * d)) * (h / (b + 2 * d));
    ll cb = (h / (a + 2 * d)) * (w / (b + 2 * d));
    return ca >= n || cb >= n;
}

int main() {
    ll n, a, b, w, h, l = 0, r = 1e18;
    cin >> n >> a >> b >> w >> h;
    while (r - l > 1) {
        ll m = (l + r) / 2;
        if (check(n, a, b, w, h, m)) {
            l = m;
        } else {
            r = m;
        }
    }
    cout << l << endl;
    return 0;
}