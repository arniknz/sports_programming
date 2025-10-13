#include <bits/stdc++.h>

using namespace std;

using ll = long long;

bool check(double x, double c) {
    return (x*x + sqrt(x)) <= c;
}

int main() {
    double c, l = 0.0, r = 1e10;
    cin >> c;
    for (auto i = 0; i < 100; i++) {
        double m = (l + r) / 2;
        if (check(m, c)) {
            l = m;
        } else {
            r = m;
        }
    }
    cout << fixed << setprecision(10) << l << endl;
    return 0;
}