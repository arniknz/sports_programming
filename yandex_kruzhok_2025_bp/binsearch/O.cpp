#include <bits/stdc++.h>

using namespace std;

using ll = long long;

ll check(ll l, ll w, ll h) {return (l / w) * (l / h);}

int main() {
    ll n, w, h;
    cin >> w >> h >> n;
    ll l = 0, r = max(w * n, h * n);
    while (r - l > 1) {
        ll m = (l + r) / 2;
        if (check(m, w, h) < n) {
            l = m;
        } else {
            r = m;
        }
    }
    cout << r << endl;
    return 0;
}