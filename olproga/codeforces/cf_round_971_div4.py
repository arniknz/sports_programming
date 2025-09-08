# ROUND: https://codeforces.com/contest/2009


# A
"""def solve(a, b):
    ans = []
    for c in range(a, b + 1):
        ans.append((c - a) + (b - c))

    return min(ans)

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(solve(a, b))"""


# B
"""def solve(n):
    res = []
    for _ in range(n):
        s = input()
        for i in range(4):
            if s[i] == "#":
                res.append(i + 1)

    return res[::-1]

for _ in range(int(input())):
    n = int(input())
    print(*solve(n))"""


# C
"""import math as m


for _ in range(int(input())):
    x, y, k = map(int, input().split())
    xd = m.ceil(x / k)
    yd = m.ceil(y / k)
    if xd > yd:
        print(2 * xd - 1)
    else:
        print(2 * yd)"""


# D
from collections import Counter
for _ in range(int(input())):
    n = int(input())
    cr = []
    for _ in range(n):
        x, y = map(int, input().split())
        cr.append((x, y))
    cnt = Counter(x[0] for x in cr)
    st = set(cr)
    ans = 0
    for e in cnt:
        if cnt[e] == 2:
            ans += n - 2
    for c in st:
        if (c[0] - 1, c[1] ^ 1) in st and (c[0] + 1, c[1] ^ 1) in st:
            ans += 1
    print(ans)