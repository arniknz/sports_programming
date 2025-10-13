#include <bits/stdc++.h>

using namespace std;

vector<int> ms(vector<int> &a) {
    if (a.size() == 1) {
        return a;
    }
    auto la = vector<int>(a.begin(), a.begin() + a.size() / 2);
    auto ra = vector<int>(a.begin() + a.size() / 2, a.end());
    auto l = ms(la);
    auto r = ms(ra);
    vector<int> ans;
    merge(l.begin(), l.end(), r.begin(), r.end(), back_inserter(ans));
    return ans;
}

int main() {
    int n;
    cin >> n;
    vector<int> a(n);
    for (auto &x : a) {
        cin >> x;
    }
    vector<int> ans = ms(a);
    for (auto x : ans) {
        cout << x << " ";
    }
    cout << endl;
    return 0;
}