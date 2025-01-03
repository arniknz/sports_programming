#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int mx_el(vector<int> &a) {
    auto m = 0;
    for (int i = 0; i < a.size(); i++) {
        if (a[i] > m) {
            m = a[i];
        }
    }

    return m;
}


int main() {
    int n;
    cin >> n;

    vector<int> a(n);
    for (auto& x : a) {
        cin >> x;
    }

    auto mx = mx_el(a);
    int cnt[mx + 1] = {0};

    for (auto e: a) {
        ++cnt[e];
    }

    auto b = 0;
    for (int i = 0; i < mx + 1; i++) {
        for (int j = 0; j < cnt[i]; j++) {
            a[b++] = i;
        }
    }

    for (auto c: a) {
        cout << c << " ";
    }
    cout << endl;
}