#include <bits/stdc++.h>

using namespace std;

int main() {
    int n;
    cin >> n;
    vector<pair<int, vector<pair<int, int>>>> m;
    vector<int> poryadok;
    for (int i = 0; i < n; i++) {
        int c;
        cin >> c;
        vector<pair<int, int>> a;
        for (int j = 0; j < c; j++) {
            int x, y;
            cin >> x >> y;
            a.push_back({x, y});
        }
        m.push_back({i + 1, a});
        poryadok.push_back(i + 1);
    }
    sort(m.begin(), m.end(), [](const auto& a, const auto& b) {
        auto am = *min_element(a.second.begin(), a.second.end());
        auto bm = *min_element(b.second.begin(), b.second.end());
        return am < bm;
    });
    map<int, int> ans;
    for (int i = 0; i < m.size(); i++) {
        ans[m[i].first] = i;
    }
    for (auto x : poryadok) {
        cout << ans[x] << " ";
    }
    cout << endl;
    return 0;
}