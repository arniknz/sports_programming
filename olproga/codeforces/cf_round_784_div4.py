# ROUND: https://codeforces.com/contest/1669


# A
for _ in range(int(input())):
    r = int(input())
    if r <= 1399:
        print('Division 4')
    elif 1400 <= r <= 1599:
        print('Division 3')
    elif 1600 <= r <= 1899:
        print('Division 2')
    else:
        print('Division 1')


# B
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for e in a:
        if e not in d:
            d[e] = 1
        else:
            d[e] += 1
    
    f = -1
    for e in d:
        if d[e] >= 3:
            f = e
            break
    print(f)
# TLE ON 45 TEST (lol). На плюсах прошло. Прикол.


# C
def even_odd(n):
    return 'e' if n % 2 == 0 else 'o'


def check(n, a, c):
    for i in range(n):
        if even_odd(a[i]) != c:
            return False
    return True


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    c = 'e' if a[0] % 2 == 0 else 'o'
    f = c
    if check(n, a, c):
        print('YES')
    else:
        b = []
        d = []
        for i in range(1, n, 2):
            b.append(a[i])

        for i in range(0, n, 2):
            d.append(a[i])

        if c == 'e':
            c = 'o'
        else:
            c = 'e'

        if check(len(b), b, c) and check(len(d), d, f):
            print('YES')
        else:
            print('NO')


# D
for _ in range(int(input())):
    n = int(input())
    a = input().split('W')
    ok =  True
    for i in range(len(a)):
        if set(a[i]) == {'R'} or set(a[i]) == {'B'}:
            ok = False
            break
    if ok:
        print('YES')
    else:
        print('NO')

# Усложнила функцией сначала, но потом оказалось все гораздо проще.


# E
from collections import defaultdict


alph = 'abcdefghijk'


for _ in range(int(input())):
    n = int(input())
    cnt = defaultdict(int)
    ans = 0
    for _ in range(n):
        s = input()
        for j in range(2):
            for c in alph:
                if c != s[j]:
                    a = s[:j] + c + s[j + 1:]
                    ans += cnt[a]
            cnt[s] += 1
    print(ans // 2)
