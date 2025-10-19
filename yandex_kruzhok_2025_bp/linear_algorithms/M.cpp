#include <bits/stdc++.h>

using namespace std;

using ll = long long;

int main() {
    ll n; cin >> n; vector<ll> a(n);
    for (auto &x : a) {cin >> x;}
    stack<ll> st;
    vector<ll> ans(n, -1);
    for (auto i = n - 1; i >= 0; i--) {
        while (!st.empty() && a[st.top()] >= a[i]) {st.pop();}
        if (!st.empty()) {ans[i] = st.top();}
        st.push(i);
    }
    for (auto x : ans) {cout << x << " ";}
    cout << endl;
    return 0;
}