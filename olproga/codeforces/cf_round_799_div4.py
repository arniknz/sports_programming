# ROUND: https://codeforces.com/contest/1692


# A
"""for _ in range(int(input())):
    a = list(map(int, input().split()))
    t = a[0]
    cnt = 0
    for i in range(1, 4):
        if a[i] > t:
            cnt += 1
    print(cnt)"""


# B
"""for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for e in a:
        if e not in d:
            d[e] = 1
        else:
            d[e] += 1
    print(len(list(d.keys())) if (len(list(d.keys())) % 2 == 0 and n % 2 == 0) or (len(list(d.keys())) % 2 != 0 and n % 2 != 0) else len(list(d.keys())) - 1)
"""

# C

# cpp

"""#include <bits/stdc++.h>

using namespace std;

void solve() {
    char mt[9][9];
    for (int i = 1; i <= 8; i++) {
        for (int j = 1; j <= 8; j++) {
            cin >> mt[i][j];
        }
    }

    int r = 0, c = 0;
    for (int i = 2; i <= 7; i++) {
        for (int j = 2; j <= 7; j++) {
            if (mt[i][j] == '#' && 
                mt[i - 1][j - 1] == '#' &&
                mt[i - 1][j + 1] == '#' &&
                mt[i + 1][j + 1] == '#' &&
                mt[i + 1][j - 1] == '#') {
                cout << i << " " << j << endl;
                return;
            }
        }
    }
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int tt; cin >> tt; for (int i = 1; i <= tt; i++) {solve();}
}"""


# D
"""import datetime

def is_palindrome(s):
    return s == s[::-1]

for _ in range(int(input())):
    t, m = map(str, input().split())
    m = int(m)
    a = 0
    cnt = 0
    d = datetime.datetime.strptime(t, '%H:%M')
    while t != a:
        a = (d + datetime.timedelta(minutes=m)).strftime("%H:%M")
        d = datetime.datetime.strptime(a, '%H:%M')
        if is_palindrome(a):
            cnt += 1
    print(cnt)"""

# TL on 5 TEST (Python3.12)



# OK (Pypy)
"""import datetime

def is_palindrome(s):
    return s == s[::-1]

def cnt(t, m):
    d = datetime.datetime.strptime(t, '%H:%M')
    cnt = 0
    while True:
        d += datetime.timedelta(minutes=m)
        a = d.strftime("%H:%M")
        if is_palindrome(a):
            cnt += 1
        if a == t:
            return cnt

for _ in range(int(input())):
    t, m = input().split()
    m = int(m)
    print(cnt(t, m))"""


# E
def solve(n, s, a):
    sm = sum(a)
    if sm < s:
        return -1
    
    l, r = 0, 0
    op = 0
    sp = 0
    while l < n:
        while r < n and sp + a[r] <= s:
            sp += a[r]
            r += 1
        op = max(op, r - l)
        sp -= a[l]
        l += 1
    return n - op

        


for _ in range(int(input())):
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(n, s, a))