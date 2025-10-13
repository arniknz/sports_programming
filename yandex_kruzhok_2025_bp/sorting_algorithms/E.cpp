#include <bits/stdc++.h>

using namespace std;

pair<vector<int>, long long> mrg(vector<int> &l, vector<int> &r) {
    vector<int> ans;
    long long cnt = 0;
    int i = 0, j = 0;
    while (i < l.size() && j < r.size()) {
        if (l[i] <= r[j]) {
            ans.push_back(l[i]);
            i++;
        } else {
            ans.push_back(r[j]);
            j++;
            cnt += l.size() - i;
        }
    }
    while (i < l.size()) {ans.push_back(l[i]); i++;}
    while (j < r.size()) {ans.push_back(r[j]); j++;}
    return {ans, cnt};
}

pair<vector<int>, long long> ms(vector<int> &a) {
    if (a.size() == 1) {
        return {a, 0};
    }
    auto la = vector<int>(a.begin(), a.begin() + a.size() / 2);
    auto ra = vector<int>(a.begin() + a.size() / 2, a.end());
    auto l = ms(la);
    auto r = ms(ra);
    pair<vector<int>, long long> ans = mrg(l.first, r.first);
    return {ans.first, l.second + r.second + ans.second};
}

int main() {
    int n;
    cin >> n;
    vector<int> a(n);
    for (auto &x : a) {
        cin >> x;
    }
    pair<vector<int>, long long> ans = ms(a);
    cout << ans.second << endl;
    return 0;
}