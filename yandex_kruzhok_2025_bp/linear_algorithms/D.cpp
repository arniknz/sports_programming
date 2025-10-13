#include <bits/stdc++.h>

using namespace std;

using ll = long long;

int main() {
    ll x, l = 1, r = 1, ans = 0; cin >> x;
    for (auto i = 0; i < x; i++) {
        if ((l * l) == (r * r * r)) {
            ans = (l * l);
            l++; r++;
        } else if ((l * l) < (r * r * r)) {
            ans = (l * l);
            l++;
        } else {
            ans = (r * r * r);
            r++;
        }
    }
    cout << ans << endl;
    return 0;
}