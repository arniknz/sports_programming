#include <bits/stdc++.h>

using namespace std;

int main() {
    int q, t, n, k;
    string nm, s;
    cin >> q;
    map<string, int> mp;
    while (q--) {
        cin >> t;
        if (t == 1) {
            cin >> nm >> n;
            bool f = true;
            vector<pair<string, int>> t;
            while (n--) {
                cin >> k >> s;
                t.push_back({s, k});
                /*if (mp[s] == 0 || mp[s] - k < 0) {
                    cout << ":(" << endl;
                    f = false;
                    continue;
                }
                mp[s] -= k;*/
            }
            //if (f) {cout << "Milkshake " << nm << " is ready" << endl;}
        } else {
            cin >> k >> s;
            mp[s] += k;
            cout << s << ": " << mp[s] << endl;
        }
    }
    return 0;
}