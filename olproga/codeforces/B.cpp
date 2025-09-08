#include <bits/stdc++.h>

using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<int> a(n);
        map<int, int> mp;
        for (auto &x: a) {
            cin >> x;
        }
        for (auto e: a) {
            mp[e]++;
        }

        int f = -1;
        for (const auto& pair: mp) {
            if (pair.second >= 3) {
                f = pair.first;
                break;
            }
        }

        cout << f << endl;

    }

    return 0;
}