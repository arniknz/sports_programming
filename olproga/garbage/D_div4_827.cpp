#include <bits/stdc++.h>

using namespace std;

#define f(n) for (int i = 0; i < n; i++)

int my_gcd(int a, int b) {
    if (b == 0) {
        return a;
    }
    return my_gcd(b, a % b);
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<int> a(n), v(1001, -1);
        f(n) cin >> a[i];
        f(n) v[a[i]] = i;

        auto mx = -1;
        for (int i = 0; i < 1001; i++) {
            if (v[i] != -1) {
                for (int j = i; j < 1001; j++) {
                    if (v[j] != -1) {
                        if ((my_gcd(i, j) == 1)) {
                            mx = max(mx, v[i] + v[j] + 2);
                        }
                    }
                }
            }
        }
        cout << mx << endl;
    }

    return 0;
}
