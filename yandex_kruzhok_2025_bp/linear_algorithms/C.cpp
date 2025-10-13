#include <bits/stdc++.h>

using namespace std;

using ll = long long;

int main() {
    ll n, w, ans = 0; cin >> n; vector<ll> a(n);
    for (auto &x : a) {cin >> x;}
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
    cout << ans << endl;
    return 0;
}