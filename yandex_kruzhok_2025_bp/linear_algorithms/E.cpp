#include <bits/stdc++.h>

using namespace std;

using ll = long long;

int main() {
    ll n1, n2, n3, n4, i = 0, j = 0, x = 0, y = 0;
    cin >> n1; vector<ll> a(n1); for (auto &x : a) {cin >> x;}
    cin >> n2; vector<ll> b(n2); for (auto &x : b) {cin >> x;}
    cin >> n3; vector<ll> c(n3); for (auto &x : c) {cin >> x;}
    cin >> n4; vector<ll> d(n4); for (auto &x : d) {cin >> x;}
    sort(a.begin(), a.end()); sort(b.begin(), b.end()); sort(c.begin(), c.end()); sort(d.begin(), d.end());
    ll mn = abs(min({a[0], b[0], c[0], d[0]}) - max({a[0], b[0], c[0], d[0]})), ansa = 0, ansb = 0, ansc = 0, ansd = 0;
    while (i < n1 && j < n2 && x < n3 && y < n4) {
        if (abs(min({a[i], b[j], c[x], d[y]}) - max({a[i], b[j], c[x], d[y]})) == 0) {
            ansa = i; ansb = j; ansc = x; ansd = y;
            break;
        }
        if (abs(min({a[i], b[j], c[x], d[y]}) - max({a[i], b[j], c[x], d[y]})) < mn) {
            mn = abs(min({a[i], b[j], c[x], d[y]}) - max({a[i], b[j], c[x], d[y]}));
            ansa = i; ansb = j; ansc = x; ansd = y;
        }
        ll cm = min({a[i], b[j], c[x], d[y]});
        if (a[i] == cm) {
            i++;
        } else if (b[j] == cm) {
            j++;
        } else if (c[x] == cm) {
            x++;
        } else {
            y++;
        }
    }
    cout << a[ansa] << " " << b[ansb] << " " << c[ansc] << " " << d[ansd] << endl;
    return 0;
}