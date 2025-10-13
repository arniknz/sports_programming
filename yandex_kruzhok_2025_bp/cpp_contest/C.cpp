#include <bits/stdc++.h>

using namespace std;

int main() {
    long long n, m, k;
    cin >> n >> m >> k;
    map<long long, set<long long>> mp;
    map<long long, set<long long>> np;
    while (k--) {
        string a;
        cin >> a;
        if (a == "ADD") {
            long long e, s;
            cin >> e >> s;
            mp[s].insert(e);
            np[e].insert(s);
        } else if (a == "DELETE") {
            long long e, s;
            cin >> e >> s;
            mp[s].erase(e);
            np[e].erase(s);
        } else if (a == "CLEAR") {
            long long s;
            cin >> s;
            for (auto x : mp[s]) {np[x].erase(s);}
            mp[s].clear();
        } else if (a == "LISTSET") {
            long long s;
            cin >> s;
            if (mp[s].empty()) {
                cout << -1 << endl;
            } else {
                for (auto x : mp[s]) {cout << x << " ";}
                cout << endl;
            }
        } else {
            long long e;
            cin >> e;
            if (np[e].empty()) {
                cout << -1;
            } else {
                for (auto x : np[e]) {cout << x << " ";}
            }
            cout << endl;
        }
    }
    return 0;
}