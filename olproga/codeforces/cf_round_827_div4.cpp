#include <bits/stdc++.h>

using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        int q;
        cin >> n >> q;
        vector<long long> pref = {0};
        vector<int> p;
        for(int i = 0; i < n; i++) {
            int a;
            cin >> a;
            pref.push_back(pref.back() + a);
            if(i == 0)
            {
                p.push_back(a);
            }
            else
            {
                p.push_back(max(p.back(), a));
            }
        }
        for (int i = 0; i < q; i++) {
            int k;
            cin >> k;
            int ans;
            ans = upper_bound(p.begin(), p.end(), k) - p.begin();
            cout << pref[ans] << " ";
        }
        cout << endl;
    }

    return 0;
}