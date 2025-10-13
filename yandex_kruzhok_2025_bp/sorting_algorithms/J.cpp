#include <bits/stdc++.h>

using namespace std;

struct cmp {
     bool operator()(const pair<pair<char, int>, long long>& a, const pair<pair<char, int>, long long>& b) const {
        if (a.second == b.second) {
            return a.first.first > b.first.first;
        }
        return a.second < b.second;
     }
};

int main() {
    string a;
    cin >> a;
    vector<long long> w;
    for (int i = 0; i < 26; i++) {
        int x;
        cin >> x;
        w.push_back(x);
    }
    vector<pair<pair<char, int>, long long>> cnt(26, {{'.', 0}, 0});
    for (auto x : a) {
        cnt[x - 'a'].first.first = x;
        cnt[x - 'a'].first.second++;
        cnt[x - 'a'].second = w[x - 'a'];
    }
    sort(cnt.begin(), cnt.end(), cmp());
    string s;
    for (auto x : cnt) {
        if (x.first.second == 1) {
            s += x.first.first;
        }
    }
    for (auto x : cnt) {
        if (x.first.second >= 2) {
            s = string(x.first.second / 2, x.first.first) + s + string((x.first.second + 1) / 2, x.first.first);
        }
    }
    cout << s << endl;
    return 0;
}