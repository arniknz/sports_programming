#include <bits/stdc++.h>

using namespace std;

#define ll long long

int main() {
    ll a, b, c; cin >> a >> b >> c;
    ll m = max(max({a, b, c}), (a + b + c) / 2 + (a + b + c) % 2);
    cout << m << endl;
    return 0;
}