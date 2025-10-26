#include <bits/stdc++.h>

using namespace std;

#define ll long long

int main() {
    ll a, b, n; cin >> a >> b >> n;
    ll m = (n + a - 1) / a;
    cout << n + (m - 1) * b << endl;
    return 0;
}