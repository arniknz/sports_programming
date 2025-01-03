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

    for (size_t i = 1; i < n; i++) {
        for (size_t j = i; j >= 1; j--) {
            if (a[j - 1] > a[j]) {
                auto tmp = a[j - 1];
                a[j - 1] = a[j];
                a[j] = tmp;
            }
        }
    }

    for (auto c : a) {
        cout << c << " ";
    }
}