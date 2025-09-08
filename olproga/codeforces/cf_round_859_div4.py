# ROUND: https://codeforces.com/contest/1807


# A
"""for _ in range(int(input())):
    a, b, c = map(int, input().split())
    if (a + b) == c:
        print('+')
    else:
        print('-')"""


# B
"""for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    e, o = 0, 0
    for i in range(n):
        if a[i] % 2 == 0:
            e += a[i]
        else:
            o += a[i]
    if e > o:
        print('YES')
    else:
        print('NO')"""


# C
"""for _ in range(int(input())):
    n = int(input())
    s = list(input())
    if set(s) == n:
        print('YES')
    else:
        t = '01' * (n // 2)
        if n % 2 != 0:
            t += '0'
        t = list(t)
        d = {}
        f = True
        for i in range(n):
            if s[i] not in d:
                d[s[i]] = t[i]
            else:
                if t[i] != d[s[i]]:
                    f = False
                    break
        if f:
            print('YES')
        else:
            print('NO')"""


# D
def calculate_prefix_sum(a):
    if not a:
        return []

    p = [0] * len(a)
    p[0] = a[0]

    for i in range(1, len(a)):
        p[i] = p[i-1] + a[i]

    return p


for _ in range(int(input())):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    p = calculate_prefix_sum(a)
    for _ in range(q):
        l, r, k = map(int, input().split())
        left = p[l - 2] if (l - 2) >= 0 else 0
        res = ((r - l + 1) * k) + left + (p[-1] - p[r - 1])
        if res % 2 != 0:
            print('YES')
        else:
            print('NO')
        