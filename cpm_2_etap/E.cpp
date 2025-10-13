#include <bits/stdc++.h>

#define ll long long

using namespace std;

struct ms {
    ll idx;
    ll v;
    ll f;
    ll t;
};

struct cmp {
    bool operator()(const ms& a, ms& b) const {
        if (a.v != b.v) {return a.v > b.v;}
        if (a.f != b.f) {return a.f < b.f;}
        return a.t < b.t;
    }
};

int main() {
    ll n, k, m, cnt = 0;
    cin >> n >> k >> m;
    vector<ms> a(n);
    vector<ll> ans;
    for (auto i = 0; i < n; i++) {
        cin >> a[i].v >> a[i].f >> a[i].t;
        a[i].idx = i + 1;
    }
    sort(a.begin(), a.end(), cmp());
    for (auto i = 0; i < n; i++) {
        if (k - a[i].f >= 0 && m - a[i].t >= 0) {
            cnt += a[i].v;
            k -= a[i].f;
            m -= a[i].t;
            ans.push_back(a[i].idx);
        }
    }
    sort(ans.begin(), ans.end());
    cout << cnt << endl;
    for (auto x : ans) {
        cout << x << " ";
    }
    cout << endl;
    return 0;
}