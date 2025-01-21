#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n, m; cin >> n >> m;
    vector<int> a(n);
    for (auto &x : a) {
        cin >> x;
    }

    int cnt = 0; int r = n - 1;
    for (int l = 0; l < n; l++) {
        if (abs(a[l] - a[r]) > m) {
            cnt++;
        } else {
            r--;
        }
    }

    cout << cnt << '\n';

    return 0;
}