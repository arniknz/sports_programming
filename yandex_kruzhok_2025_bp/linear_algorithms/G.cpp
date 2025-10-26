#include <bits/stdc++.h>

using namespace std;

using ll = long long;

int main() {
    ll n, m; cin >> n;
    vector<ll> a(n); for (auto &x : a) {cin >> x;}
    cin >> m;
    vector<ll> ks(m); for (auto &x : ks) {cin >> x;}
    for (auto k : ks) {
        deque<ll> dmx, dmn;
        pair<ll, pair<ll, ll>> ans = {-10000000, {-1, -1}};
        ll l = 0;
        for (auto r = 0; r < n; r++) {
            while (!dmx.empty() && a[dmx.back()] <= a[r]) {dmx.pop_back();}
            dmx.push_back(r);
            while (!dmn.empty() && a[dmn.back()] >= a[r]) {dmn.pop_back();}
            dmn.push_back(r);
            while (a[dmx.front()] - a[dmn.front()] > k) {
                if (dmx.front() == l) {dmx.pop_front();}
                if (dmn.front() == l) {dmn.pop_front();}
                l++;
            }
            if (r - l + 1 > ans.first) {
                ans.first = r - l + 1;
                ans.second.first = l;
                ans.second.second = r;
            }
        }
        cout << ans.second.first + 1 << " " << ans.second.second + 1 << endl;
    }
    return 0;
}