#include <bits/stdc++.h>

using ll = long long;

using namespace std;

int main() {
    int n, k;
    cin >> n;
    vector<ll> a(n), t1, t2, ans1, ans2;
    for (auto &x : a) {cin >> x;}
    cin >> k;
    for (auto i = 0; i < n; i++) {if (i != k - 1) {t1.push_back(a[i]); t2.push_back(a[i]);}}
    sort(t1.begin(), t1.end());
    sort(t2.rbegin(), t2.rend());
    for (auto i = 0; i < k - 1; i++) {ans1.push_back(t1[i]);}
    ans1.push_back(a[k - 1]);
    for (auto i = k - 1; i < t1.size(); i++) {ans1.push_back(t1[i]);}
    for (auto i = 0; i < k - 1; i++) {ans2.push_back(t2[i]);}
    ans2.push_back(a[k - 1]);
    for (auto i = k - 1; i < t2.size(); i++) {ans2.push_back(t2[i]);}
    ll cnt1 = 0, cnt2 = 0;
    for (auto i = 0; i < n - 1; i++) {
        cnt1 += abs(ans1[i] - ans1[i + 1]);
        cnt2 += abs(ans2[i] - ans2[i + 1]);
    }
    if (cnt1 < cnt2) {
        for (auto x : ans1) {
            cout << x << " ";
        }
        cout << endl;
    } else {
        for (auto x : ans2) {
            cout << x << " ";
        }
        cout << endl;
    }
    return 0;
}

// WA