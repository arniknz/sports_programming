#include <bits/stdc++.h>

using namespace std;

using ull = unsigned long long;

ull f(ull a, ull k, ull b, ull m, ull n) {
    return a * (n - n / k) + b * (n - n / m);
}

int main() {
    ull a, k, b, m, x, l = 0, r = 1;
    cin >> a >> k >> b >> m >> x;
    while (f(a, k, b, m, r) < x) {l = r; r *= 2;}
    while (l + 1 < r) {
        ull md = (l + r) / 2;
        if (f(a, k, b, m, md) < x) {
            l = md;
        } else {
            r = md;
        }
    }
    cout << r << endl;
    return 0;
}