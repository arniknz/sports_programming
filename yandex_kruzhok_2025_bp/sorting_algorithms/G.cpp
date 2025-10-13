#include <bits/stdc++.h>

using namespace std;

int main() {
    int n;
    int k;
    cin >> n >> k;
    vector<long long> a(n);
    for (auto &x : a) {
        cin >> x;
    }
    nth_element(a.begin(), a.begin() + (k - 1), a.end());
    cout << a[k - 1] << endl;
    return 0;
}