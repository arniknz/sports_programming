#include <bits/stdc++.h>

using namespace std;

int f(int x) {
    return max(1000 - x, 1);
}

int main() {
    int n, st = 0, s = 0;
    cin >> n;
    vector<int> a(n);
    for (auto &x : a) {cin >> x;}
    priority_queue<pair<int, int>> pq;
    for (int i = 0; i < n; i++) {pq.push({-f(a[i]), i});}
    while (!pq.empty()) {
        pair<int, int> p = pq.top();
        pq.pop();
        if (s + abs(st - p.second) > abs(p.first)) {cout << abs(p.first) << endl; break;}
        a[p.second]++;
        st = p.second;
        s = abs(p.first);
        int nv = abs(p.first) + f(a[p.second]);
        pq.push({-nv, p.second});
    }
    return 0;
}