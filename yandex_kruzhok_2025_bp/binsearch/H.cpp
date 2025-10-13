#include <bits/stdc++.h>

using namespace std;

using ll = long long;

ll check(ll x, vector<ll> &a) {
    ll cnt = 0;
    for (auto c : a) {cnt += (c / x);}
    return cnt;
}

int main() {
    ll n, k;
    cin >> n >> k;
    vector<ll> a(n);
    for (auto &x : a) {cin >> x;}
    ll l = 1, r = *max_element(a.begin(), a.end());
    while (l <= r) {
        ll m = (l + r) / 2;
        if (check(m, a) >= k) {
            l = m + 1;
        } else {
            r = m - 1;
        }
    }
    cout << r << endl;
    return 0;
}