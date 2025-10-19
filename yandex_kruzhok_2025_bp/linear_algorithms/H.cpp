#include <bits/stdc++.h>

using namespace std;

using ll = long long;

int main() {
    ll n, k; cin >> n >> k; vector<ll> a(n);
    for (auto &x : a) {cin >> x;}
    ll mx = *max_element(a.begin(), a.end());
    vector<ll> div(mx + 1, 0);
    for (ll i = 0; i < n; i++) {
        for (ll j = 1; j <= sqrt(a[i]); j++) {
            if (a[i] % j == 0) {
                div[j]++;
                if (j != a[i] / j && a[i] / j <= mx) {
                    div[a[i] / j]++;
                }
            }
        }
    }
    for (ll i = mx; i >= 1; i--) {
        if (div[i] >= k) {
            cout << i << endl;
            break;
        }
    }
    return 0;
}