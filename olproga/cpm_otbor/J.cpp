#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define f(n) for (int i = 0; i < n; i++)

void solve() {
    int n;
    cin >> n;
    vector<int> a(n);
    for (auto &x: a) {
        cin >> x;
    }
    unordered_map<int, int> mp;
    int pref;
    int ans;
    int k = -1;
    f(n) {
        pref += a[i];
        if (pref == k) {
            ans = i + 1;
        } else if (mp.find(pref - k) != mp.end()) {
            ans = max(ans, i - mp[pref - k]);
        }

        if (mp.find(pref) == mp.end()) {
            mp[pref] = i;
        }
    }
    cout << ans << endl;
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
}