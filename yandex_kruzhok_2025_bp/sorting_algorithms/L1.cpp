#include <bits/stdc++.h>

using namespace std;

int main() {
    int n;
    string a;
    cin >> n >> a;
    map<char, int> m, p;
    for (auto x : a) {m[x]++;}
    string bok1, seredinka, bok2;
    for (const auto& p : m) {bok1 += string(p.second / 2, p.first);}
    for (const auto& p : m) {if (p.second % 2 != 0) {seredinka += p.first; break;}}
    bok2 = bok1;
    reverse(bok2.begin(), bok2.end());
    cout << bok1 << seredinka << bok2 << endl;
    return 0;
}