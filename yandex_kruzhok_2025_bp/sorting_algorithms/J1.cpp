#include <bits/stdc++.h>

using namespace std;

int w[26];

struct cmp {
     bool operator()(const char &a, const char &b) const {
        if (w[a - 'a'] == w[b - 'a']) return a > b;
        return w[a - 'a'] > w[b - 'a'];
    }
};

int main() {
    string a, ans, pol;
    cin >> a;
    for (auto &x : w) {cin >> x;}
    sort(a.begin(), a.end(), cmp());
    for (int i = 0; i < a.size() - 1; i++) {
        if (a[i] == a[i + 1] && ((!pol.empty() && pol[pol.size() - 1] != a[i]) || pol.empty())) {
            pol.push_back(a[i]);
            i++;
        } else {
            ans.push_back(a[i]);
        }
    }
    if (a.size() > ans.size() + pol.size() * 2) {ans.push_back(a[a.size() - 1]);}
    cout << pol << ans;
    for (int i = pol.size() - 1; i >= 0; i--) {cout << pol[i];}
    cout << endl;
    return 0;
}