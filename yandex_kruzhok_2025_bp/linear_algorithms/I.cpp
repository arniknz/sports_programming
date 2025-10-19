#include <bits/stdc++.h>

using namespace std;

using ll = long long;

ll histo(ll n, vector<ll> &a) {
    ll w, ans = 0;
    stack<ll> st;
    for (auto i = 0; i < n; i++) {
        while (!st.empty() && a[st.top()] >= a[i]) {
            ll h = a[st.top()];
            st.pop();
            if (!st.empty()) {
                w = i - st.top() - 1;
            } else {
                w = i;
            }
            ans = max(ans, h * w);
        }
        st.push(i);
    }
    while (!st.empty()) {
        ll h = a[st.top()];
        st.pop();
        if (!st.empty()) {
            w = n - st.top() - 1;
        } else {
            w = n;
        }
        ans = max(ans, h * w);
    }
    return ans;
}

ll ans(vector<vector<char>> &mt, ll n, ll m) {
    if (mt.empty() || mt[0].empty()) {return 0;}
    vector<vector<ll>> pref(n, vector<ll>(m, 0));
    for (ll i = 0; i < n; i++) {
        for (ll j = 0; j < m; j++) {
            if (mt[i][j] == '0') {
                pref[i][j] = (i == 0 ? 1 : pref[i - 1][j] + 1);
            } else {
                pref[i][j] = 0;
            }
        }
    }
    ll res = 0;
    for (ll i = 0; i < n; i++) {
        res = max(res, histo(m, pref[i]));
    }
    return res;
}

int main() {
    ll n, m; cin >> n >> m;
    vector<vector<char>> mt;
    for (ll i = 0; i < n; i++) {
        vector<char> mm(m); for (auto &x : mm) {cin >> x;}
        mt.push_back(mm);
    }
    ll res = ans(mt, n, m);
    cout << res << endl;
    return 0;
}