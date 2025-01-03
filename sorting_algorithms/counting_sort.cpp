#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> a(n);
    for (auto& x : a) {
        cin >> x;
    }

    for (auto x: a) {
        cout << x << " ";
    }
    cout << endl;

    //int mn = *min_element(a.begin(), a.end());
    //for (auto &m: a) {
    //    m -= mn;
    //}

    int mx = *max_element(a.begin(), a.end());
    vector<int> cnt(mx + 1, 0);

    for (auto e: a) {
        cnt[e]++;
    }

    auto b = 0;
    for (int i = 0; i < n; i++) {
        int c = cnt[i];
        for (int j = 0; j < c; j++) {
            a[b++] = i;
        }
    }

    for (auto x: a) {
        cout << x << " ";
    }
    cout << endl;
}