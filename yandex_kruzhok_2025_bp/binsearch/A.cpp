#include <bits/stdc++.h>

using namespace std;

using ll = long long;

bool check(ll x, vector<ll> &s, ll k) {
    ll st = 1;
    ll lst = s[0];
    for (auto c : s) {
        if (c - lst >= x) {
            st++;
            lst = c;
        }
    }
    return st >= k;
}

int main() {
    ll n, k;
    cin >> n >> k;
    vector<ll> s(n);
    for (auto &x : s) {cin >> x;}
    ll l = 0, r = s.back() - s[0] + 1;
    while (r - l > 1) {
        ll m = (l + r) / 2;
        if (check(m, s, k)) {
            l = m;
        } else {
            r = m;
        }
    }
    cout << l << endl;
    return 0;
}