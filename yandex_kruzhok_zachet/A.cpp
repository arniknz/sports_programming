#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n, t;
    cin >> n >> t;
    vector<int> a(n);
    for (auto &x: a) {
        cin >> x;
    }

    vector<int> res;
    for (int i = 0; i < a.size() - 1; i++) {
        if (a[i] + a[i + 1] != t) {
            res.push_back(a[i] + a[i + 1]);
        }
    }

    cout << a.size() - (res.size() + 1) << "\n";
}