#include <bits/stdc++.h>

#define ll long long

using namespace std;

ll f(ll i, ll n) {
    return i * i + (n - i) * (n - i + 1) / 2;
}

int main() {
    ll n;
    cin >> n;
    ll cnt = n * (n + 1) / 2;
    double a = (2.0 * n + 1) / 6.0;
    vector<ll> ans = {0LL, n};
    ll i1 = (ll)floor(a);
    ll i2 = (ll)ceil(a);
    if (i1 >= 0 && i1 <= n) {ans.push_back(i1);}
    if (i2 >= 0 && i2 <= n) {ans.push_back(i2);}
    for (auto x : ans) {
        cnt = min(cnt, f(x, n));
    }
    cout << cnt << endl;
    return 0;
}