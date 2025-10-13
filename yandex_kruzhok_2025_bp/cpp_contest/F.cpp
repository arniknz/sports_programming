#include <bits/stdc++.h>

using namespace std;

int main() {
    long long n;
    cin >> n;
    deque<long long> q;
    while (n--) {
        char a;
        cin >> a;
        if (a == '+') {
            long long x;
            cin >> x;
            q.push_back(x);
        } else if (a == '-') {
            cout << q.back() << endl;
            q.pop_back();
        } else {
            long long k, cnt = 0;
            cin >> k;
            for (auto i = q.size() - k; i < q.size(); i++) {
                cnt += q[i];
            }
            cout << cnt << endl;
        }
    }
    return 0;
}