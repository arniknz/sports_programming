#include <bits/stdc++.h>

using namespace std;

struct cmp {
     bool operator()(const pair<int, int>& a, const pair<int, int>& b) const {
        if (a.second == b.second) {
            return a.first < b.first;
        }
        return a.second > b.second;
     }
};

int main() {
    int n;
    cin >> n;
    vector<pair<int, int>> a;
    for (int i = 0; i < n; i++) {
        int x, y;
        cin >> x >> y;
        a.push_back({x, y});
    }
    sort(a.begin(), a.end(), cmp());
    for (auto x : a) {
        cout << x.first << " " << x.second << endl;
    }
    return 0;
}