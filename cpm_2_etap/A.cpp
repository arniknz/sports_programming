#include <bits/stdc++.h>

#define ll long long

using namespace std;

int main() {
    string n, s;
    cin >> n;
    for (auto x : n) {if (x == '4') {s += '0';} else {s += '1';}}
    ll ans = 0;
    for (auto i = 1; i < n.size(); i++) {ans += pow(2, i);}
    cout << ans + stoi(s, nullptr, 2) + 1 << endl;
    return 0;
}