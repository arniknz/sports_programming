# ROUND: https://codeforces.com/contest/1703

# A
for _ in range(int(input())):
    s = input().lower()
    pat = 'yes'
    if s == pat:
        print('YES')
    else:
        print('NO')


# B
for _ in range(int(input())):
    n = int(input())
    s = list(input())
    d = {}
    for e in s:
        if e not in d:
            d[e] = 1
        else:
            d[e] += 1

    cnt = len(list(d.values())) * 2
    for e in list(set(s)):
        d[e] -= 1
        cnt += d[e]
    print(cnt)


# C
c = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def rotate(a, k):
    return a[k % len(a):] + a[:k % len(a)]


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    res = []
    for i in range(n):
        bi, s = map(str, input().split())
        s = list(s)
        bi = int(bi)
        f = c.index(a[i])
        for j in range(bi):
            if s[j] == 'U':
                c = rotate(c, -1)
            else:
                c = rotate(c, 1)
        res.append(c[f])
    print(*res)


# D
cpp

#include <bits/stdc++.h>

using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        string s[n];
        map<string, bool> mp;
        for (int i = 0; i < n; i++) {
            cin >> s[i];
            mp[s[i]] = true;
        }
        for (int i = 0; i < n; i++) {
            bool ok = false;
            for (int j = 1; j < s[i].length(); j++) {
                string pref = s[i].substr(0, j), suff = s[i].substr(j, s[i].length() - j);
                if (mp[pref] && mp[suff]) {ok = true;}
            }
            cout << ok;
        }
        cout << endl;
    }

    return 0;
}
