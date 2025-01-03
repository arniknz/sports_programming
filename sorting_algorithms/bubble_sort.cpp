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

    for (size_t i = 1; i < a.size(); i++) {
        for (size_t j = 0; j < a.size() - 1; j++) {
            if (a[j] > a[j + 1]) {
                swap(a[j], a[j + 1]);
            }
        }
    }

    for (auto i : a) {
        cout << i << ' ';
    }
}