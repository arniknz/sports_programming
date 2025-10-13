#include <bits/stdc++.h>

using namespace std;

using ll = long long;

int main() {
    ll q, t, n, k;
    string nm, s;
    cin >> q;
    map<string, ll> mp;
    while (q--) {
        cin >> t;
        if (t == 1) {
            cin >> nm >> n;
            bool f = true;
            vector<pair<string, ll>> tmp;
            while (n--) {
                cin >> k >> s;
                tmp.push_back({s, k});
                if (mp.find(s) == mp.end() || mp[s] < k) {
                    f = false;
                }
            }
            if (f) {
                for (auto x : tmp) {mp[x.first] -= x.second;}
                cout << "Milkshake " << nm << " is ready" << endl;
            } else {
                cout << ":(" << endl;
            }
        } else {
            cin >> k >> s;
            mp[s] += k;
            cout << s << ": " << mp[s] << endl;
        }
    }
    return 0;
}