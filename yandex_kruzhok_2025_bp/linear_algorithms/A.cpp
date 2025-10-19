#include <bits/stdc++.h>

using namespace std;

using ll = long long;

vector<ll> prefsum(ll n, vector<ll> &a) {
    vector<ll> pref(n + 1, 0);
    for (ll i = 1; i <= n; i++) {pref[i] = pref[i - 1] + a[i - 1];}
    return pref;
}

vector<ll> diffsum(ll n, vector<ll> &a) {
    vector<ll> diffs(n, 0); diffs[0] = a[0];
    for (ll i = 1; i < n; i++) {diffs[i] = a[i] - a[i - 1];}
    return diffs;
}

void add(ll n, ll l, ll r, ll d, vector<ll> &a) {
    a[l] += d;
    if (r + 1 < n) {a[r + 1] -= d;}
}

void pre(vector<ll> &a, vector<ll> &b) {
    b = diffsum(a.size(), a);
}

void pst(vector<ll> &a, vector<ll> &ans) {
    ans = prefsum(a.size(), a);
    ans.erase(ans.begin());
}

int main() {
    int n, m, k; cin >> n >> m >> k; vector<ll> a(n); vector<pair<pair<ll, ll>, ll>> opr(m); vector<ll> opr_c(m + 1, 0);
    for (auto &x : a) {cin >> x;}
    for (ll i = 0; i < m; i++) {
        ll l, r, d; cin >> l >> r >> d;
        opr[i] = {{l - 1, r - 1}, d};
    }
    vector<ll> b;
    pre(a, b);
    for (ll i = 0; i < k; i++) {
        ll x, y; cin >> x >> y;
        opr_c[x - 1]++;
        if (y < m) {opr_c[y]--;}
    }
    for (ll i = 1; i < m; i++) {opr_c[i] += opr_c[i - 1];}
    for (ll i = 0; i < m; i++) {if (opr_c[i] > 0) {
        add(b.size(), opr[i].first.first, opr[i].first.second, opr[i].second * opr_c[i], b);
    }}
    vector<ll> ans;
    pst(b, ans);
    for (auto x : ans) {cout << x << " ";}
    cout << endl;
    return 0;
}