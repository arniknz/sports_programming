# ROUND: https://codeforces.com/contest/1760

# A
for _ in range(int(input())):
    a = list(map(int, input().split()))
    a.sort()
    print(a[1])


# B 
a = 'abcdefghijklmnopqrstuvwxyz'

for _ in range(int(input())):
    n = int(input())
    s = list(set(input()))
    s.sort()
    last = a.find(s[-1])
    print(len(a[:last + 1]))


# C
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    res = []
    b = a.copy()
    b.sort(reverse=True)
    b = b[:2]
    for i in range(n):
        res.append(a[i] - (b[0] if a[i] != b[0] else b[1]))
    print(*res)


# D
cpp

#include <bits/stdc++.h>

using namespace std;

int32_t main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<int> a;
        for (int i = 0; i < n; i++) {
            int x;
            cin >> x;
            if (i == 0 || x != a.back()) {
                a.push_back(x);
            }
        }

        int cnt = 0;
        for (int i = 0; i < a.size(); i++) {
            if ((i == 0 || a[i] < a[i - 1]) && (i == a.size()-1 || a[i] < a[i + 1]))
            {
                cnt++;
            }
        }

        if (cnt == 1) {
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
        
    }

    return 0;
}


# E
import copy


def cnt(n, a):
    z = 0
    ans = 0
    for i in range(n - 1, -1, -1):
        if a[i] == 0:
            z += 1
        else:
            ans += z

    return ans


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = copy.deepcopy(a)
    c = copy.deepcopy(a)
    d = copy.deepcopy(a)
    if 0 in b:
        b[b.index(0)] = 1
    if 1 in c:
        c[len(d) - 1 - d[::-1].index(1)] = 0

    ans = cnt(n, a)
    ans = max(ans, cnt(len(b), b))
    ans = max(ans, cnt(len(c), c))

    print(ans)
