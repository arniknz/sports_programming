# https://codeforces.com/problemset/problem/2047/B


"""for _ in range(int(input())):
    n = int(input())
    s = list(input())
    d = {}
    for e in s:
        if e not in d:
            d[e] = 1
        else:
            d[e] += 1
    mn, _ = min(d.items(), key=lambda x: x[1])
    s1 = s.copy()[::-1]
    d1 = {}
    for e in s1:
        if e not in d1:
            d1[e] = 1
        else:
            d1[e] += 1
    mx, _ = max(d1.items(), key=lambda x: x[1])
    print(mx, mn)
    print(s)
    for i in range(n):
        print(s[i] == mn)
        if s[i] == mn:
            s[i] = mx
            break
    print(''.join(s))"""


# https://codeforces.com/contest/2114/problem/B


"""for _ in range(int(input())):
    n, k = map(int, input().split())
    s = list(input())
    c0 = s.count('0')
    c1 = s.count('1')
    mn = max(c0, c1) - n // 2
    mx = c0 // 2 + c1 // 2
    if mx >= k >= mn and (k - mn) % 2 == 0:
        print('YES')
    else:
        print('NO')"""


# https://codeforces.com/problemset/problem/2110/B
def val_par(s):
    bal = 0
    for i in range(1, len(s) - 1):
        if s[i] == '(':
            bal += 1
        else:
            bal -= 1
        if bal < 0:
            return 'YES'
    if bal == 0:
        return 'NO'
    return 'YES'



for _ in range(int(input())):
    s = list(input())
    print(val_par(s))