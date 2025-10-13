#include <bits/stdc++.h>

using namespace std;

using ll = long long;

int main() {
    ll n, q, t, x, y, xx, yy, xxx, yyy;
    cin >> n >> q;
    set<ll> r, c;
    vector<ll> rv(n + 1, 0), cv(n + 1, 0);
    for (auto i = 1; i <= n; i++) {
        r.insert(i);
        c.insert(i);
    }
    while (q--) {
        cin >> t;
        if (t == 1) {
            cin >> x >> y;
            rv[x]++;
            cv[y]++;
            if (rv[x] == 1) {r.erase(x);}
            if (cv[y] == 1) {c.erase(y);}
        } else if (t == 2) {
            cin >> x >> y;
            rv[x]--;
            cv[y]--;
            if (rv[x] == 0) {r.insert(x);}
            if (cv[y] == 0) {c.insert(y);}
        } else {
            cin >> xx >> yy >> xxx >> yyy;
            bool rf = true, cf = true;
            auto ir = r.lower_bound(xx), ic = c.lower_bound(yy);
            if (ir != r.end() && *ir <= xxx) {
                rf = false;
            }
            if (ic != c.end() && *ic <= yyy) {
                cf = false;
            }
            if (rf || cf) {
                cout << "Yes" << endl;
            } else {
                cout << "No" << endl;
            }
        }
    }
    return 0;
}