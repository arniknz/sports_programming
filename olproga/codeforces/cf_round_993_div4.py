# ROUND: https://codeforces.com/contest/2044/my


# A
"""for _ in range(int(input())):
    n = int(input())
    cnt = 0
    for i in range(n):
        for j in range(n):
            if i == n - j:
                cnt += 1
    print(cnt)"""


# B
"""for _ in range(int(input())):
    a = list(input())
    b = a[::-1]
    for i in range(len(b)):
        if b[i] == 'p':
            b[i] = 'q'
        elif b[i] == 'q':
            b[i] = 'p'
    print(''.join(b))"""


# C
"""for _ in range(int(input())):
    m, a, b, c = map(int, input().split())
    res = 0
    if m <= a:
        res += m
    elif m > a:
        res += a
    if m <= b:
        res += m
    elif m > b:
        res += b
    res += min(2 * m - res, c)
    print(res)"""


# D
