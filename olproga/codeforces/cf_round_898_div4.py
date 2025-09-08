# ROUND: https://codeforces.com/contest/1873


# A
# Решено, нужно найти посылку


# B
# Решено, нужно найти посылку


# C
"""pat = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 2, 3, 3, 3, 3, 3, 3, 2, 1],
    [1, 2, 3, 4, 4, 4, 4, 3, 2, 1],
    [1, 2, 3, 4, 5, 5, 4, 3, 2, 1],
    [1, 2, 3, 4, 5, 5, 4, 3, 2, 1],
    [1, 2, 3, 4, 4, 4, 4, 3, 2, 1],
    [1, 2, 3, 3, 3, 3, 3, 3, 2, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]
for _ in range(int(input())):
    mt = []
    for _ in range(10):
        mt.append(list(input()))

    cnt = 0
    for i in range(10):
        for j in range(10):
            if mt[i][j] == 'X':
                cnt += pat[i][j]
    print(cnt)"""


# D
"""for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(input())
    b = a.count('B')
    if k == 1 or b == 0:
        print(b)
    else:
        cnt = 0
        l = 0
        while l < n:
            if a[l] == 'B':
                cnt += 1
                l += k
            else:
                l += 1
        print(cnt)"""



# E
EPS = int(2e10) + 7
for _ in range(int(input())):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    l, r = 0, EPS
    while l < r:
        mid = l + (r - l + 1) // 2
        cnt = 0
        for i in range(n):
            cnt += max(mid - a[i], 0)
        if cnt <= x:
            l = mid
        else:
            r = mid - 1
    print(l)