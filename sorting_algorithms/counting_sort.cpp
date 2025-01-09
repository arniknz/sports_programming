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

    int mx = *max_element(a.begin(), a.end());
    vector<int> cnt(mx + 1, 0);

    for (auto e: a) {
        cnt[e]++;
    }

    auto b = 0;
    for (size_t i = 0; i < mx + 1; i++) {
        for (int j = 0; j < cnt[i]; j++) {
            a[b++] = i;
        }
    }

    for (auto x: a) {
        cout << x << " ";
    }
    cout << endl;
}