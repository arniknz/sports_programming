#include <bits/stdc++.h>

using namespace std;

using ll = long long;

int main() {
    ll n, k; cin >> n >> k; vector<ll> a(n);
    for (auto &x : a) {cin >> x;}
    deque<ll> dq;
    for (auto i = 0; i < n; i++) {
        if (!dq.empty() && dq.front() <= i - k) {dq.pop_front();}
        while (!dq.empty() && a[dq.back()] >= a[i]) {dq.pop_back();}
        dq.push_back(i);
        if (i >= k - 1) {
            cout << a[dq.front()] << endl;
        }
    }
    return 0;
}