#include <bits/stdc++.h>

using namespace std;

using ll = long long;

struct chel {
    ll a, b, c, d;
};


int main() {
    ll n, m, p, a, b, c, d, cnt = 0;
    cin >> n >> m >> p;
    vector<chel> st;
    while (n--) {
        chel ch;
        cin >> a >> b >> c >> d;
        if (a < b) {
            cnt += b * (d - c);
        } else {
            
        }
    }
    return 0;
}