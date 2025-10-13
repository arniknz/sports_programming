#include <bits/stdc++.h>

using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> a(n);
    for (auto &x : a) {
        cin >> x;
    }
    int mx = 0;
    for (int i = 0; i < n; i++) {
        if (abs(a[i]) > mx) {
            mx = abs(a[i]);
        }
    }
    vector<int> cnt(2 * mx + 1, 0);
    for (auto e : a) {
        cnt[e+mx]++;
    }
    int b = 0;
    for (int i = 0; i < 2 * mx + 1; i++) {
        for (int j = 0; j < cnt[i]; j++) {
            a[b++] = i-mx;
        }
    }
    for (auto x : a) {
        cout << x << " ";
    }
    cout << endl;
    return 0;
}