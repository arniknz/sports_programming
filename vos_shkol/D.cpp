#include <bits/stdc++.h>

using namespace std;

#define ll long long

int main() {
    ll n, m; cin >> n >> m;
    for (ll r = 1; r <= n; r++) {
        ll start = (r % 2 == 1) ? 1 : 2;
        for (ll c = start; c <= m; c += 2) {
            ll ans = ((r + c) / 2) % 3 + 1;
            cout << ans;
        }
    }
    cout << endl;
    return 0;
}