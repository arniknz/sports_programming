#include <bits/stdc++.h>

using namespace std;

using ll = long long;

int main() {
    ll n, l = 1, r, m1, m2, res;
    cin >> n;
    r = n;
    while (l < r) {
        ll m = (l + r) / 2;
        if (m % 2 == 0) {m--;}
        cout << "? " << m << endl;
        cout.flush();
        cin >> m1;
        cout << "? " << m + 1 << endl;
        cout.flush();
        cin >> m2;
        if (m1 == m2) {
            l = m + 2;
        } else {
            r = m;
        }
    }
    cout << "? " << l << endl;
    cout.flush();
    cin >> res;
    cout << "! " << res << endl;
    cout.flush();
    return 0;
}