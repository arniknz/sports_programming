#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define f(n) for (int i = 0; i < n; i++)

int INF = 2147483647;

struct cmp {
     bool operator()(const pair<int, int>& a, const pair<int, int>& b) const {
        if (a.first == b.first) {
            return a.second < b.second;
        }
        return a.first > b.first;
     }
};


void solve() {
    int n;
    cin >> n;
    vector<int> a(n);
    for (auto &x: a) {
        cin >> x;
    }
    vector<int> pref(n + 1, 0);
    for (int i = 1; i <= n; i++) {
        pref[i] = pref[i - 1] + a[i - 1];
    }
    vector<pair<int, int>> p;
    for (int i = 0; i <= n; i++) {
        p.push_back({pref[i], i});
    }
    sort(p.begin(), p.end(), cmp());
    int allm = INF;
    int gm = INF;
    optional<int> l = nullopt;
    int ans = 0;
    for (int i = 0; i < p.size(); i++) {
        if (!l.has_value() || p[i].first != l) {
            if (l.has_value()) {
                allm = min(allm, gm);
            }
            gm = INF;
            l = p[i].first;
        }
        if (allm < p[i].second) {
            ans = max(ans, p[i].second - allm);
        }
        gm = min(gm, p[i].second);
    }
    cout << ans << endl;
    
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
}