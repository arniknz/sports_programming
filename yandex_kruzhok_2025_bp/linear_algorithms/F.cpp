#include <bits/stdc++.h>

using namespace std;

using uint = unsigned int;

const uint N = 1 << 24;

vector<uint> df(N + 1, 0);
vector<uint> res(N), pref(N + 1, 0);

uint nextRand(uint a, uint b, uint &cur) {
    cur = cur * a + b;
    return cur >> 8;
}

int main() {
    uint m, q, a, b; cin >> m >> q >> a >> b;
    uint cur = 0;
    while (m--) {
        uint d = nextRand(a, b, cur);
        uint l = min(nextRand(a, b, cur), N - 1);
        uint r = min(nextRand(a, b, cur), N - 1);
        if (l > r) {swap(l, r);}
        df[l] += d;
        if (r + 1 < N) {df[r + 1] -= d;}
    }
    uint ans = 0, tmp = 0;
    for (uint i = 0; i < N; i++) {
        tmp += df[i]; res[i] = tmp;
    }
    for (uint i = 0; i < N; i++) {pref[i + 1] = pref[i] + res[i];}
    while (q--) {
        uint l = min(nextRand(a, b, cur), N - 1);
        uint r = min(nextRand(a, b, cur), N - 1);
        if (l > r) {swap(l, r);}
        ans += pref[r + 1] - pref[l];
    }
    cout << ans << endl;
    return 0;
}