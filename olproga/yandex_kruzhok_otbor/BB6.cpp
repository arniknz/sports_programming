#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define f(n) for (int i = 0; i < n; i++)

ll cntmm(ll a, ll x) {
    if ((a & x) == x) {
        return max(0LL, x - a);
    }
    ll t = a;
    for (ll b = 30; b >= 0; b--) {
        if ((x >> b) & 1) {
            if (((t >> b) & 1) == 0) {
                t |= (1LL << b);
                t &= ~((1LL << b) - 1);
            }
        }
    }
    if (t < x) {t = x;}
    return t - a;
}

void solve() {
    int n;
    ll m;
    int k;
    cin >> n >> m >> k;
    vector<ll> a(n);
    for (auto &x: a) {cin >> x;}
    ll ans = 0;
    for (ll b = 30; b >= 0; b--) {
        ll x = ans | (1LL << b);
        vector<ll> mm;
        f(n) {
            mm.push_back(cntmm(a[i], x));
        }
        sort(mm.begin(), mm.end());
        ll cnt = 0;
        f(k) {cnt += mm[i];}
        if (cnt <= m) {ans = x;}
    }
    cout << ans << endl;
    
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
}
