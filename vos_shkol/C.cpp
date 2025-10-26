#include <bits/stdc++.h>

using namespace std;

#define ll long long

int main() {
    ll m, p; cin >> m >> p;
    ll g = gcd(m, p);
    ll m1 = m / g, p1 = p / g;
    if (m1 % 2 != 0 && p1 % 2 != 0) {
        cout << m / g * p << endl;
    } else {
        cout << -1 << endl;
    }
    return 0;
}