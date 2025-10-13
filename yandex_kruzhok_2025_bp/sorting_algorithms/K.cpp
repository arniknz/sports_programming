#include <bits/stdc++.h>

using namespace std;

struct cmp {
    bool operator()(const string &a, const string &b) const {
        return a + b > b + a;
    }
};

int main() {
    vector<string> a;
    string x;
    while (cin >> x) {a.push_back(x);}
    sort(a.begin(), a.end(), cmp());
    for (auto x : a) {cout << x;}
    cout << endl;
    return 0;
}