#include <bits/stdc++.h>

using namespace std;

using ll = long long;

int main() {
    ll n, ans;
    cin >> n;
    ll l = 1, r = n;
    while (r - l > 1) {
        ll m = (l + r) / 2;
        cout << "? " << m << endl;
        cout.flush();
        cin >> ans;
        if (ans == 1) {
            l = m;
        } else {
            r = m;
        }
    }
    cout << "! " << l << endl;
    cout.flush();
    return 0;
}