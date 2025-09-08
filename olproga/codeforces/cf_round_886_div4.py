# ROUND: https://codeforces.com/contest/1850


# A
"""for _ in range(int(input())):
    a, b, c = map(int, input().split())
    if ((a + b) >= 10) or ((a + c) >= 10) or ((c + b) >= 10):
        print('YES')
    else:
        print('NO')"""


# B
"""for _ in range(int(input())):
    n = int(input())
    k = []
    mx = 0
    idx = 0
    for i in range(n):
        a, b = map(int, input().split())
        if a <= 10:
            if b > mx:
                mx = b
                idx = i + 1
    print(idx)"""


# C
"""for _ in range(int(input())):
    w = ''
    for i in range(8):
        r = list(input())
        for j in range(8):
            if r[j] != '.':
                w += r[j]
    print(w)"""


# D
"""for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    cnt = 1
    ans = 1
    for i in range(n - 1):
        if abs(a[i] - a[i + 1]) > k:
            cnt = 1
        else:
            cnt += 1
        ans = max(ans, cnt)
    print(n - ans)"""


# F
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    cnt = [0] * (n + 1)
    mx = [0] * (n + 1)
    for i in range(n):
        if a[i] <= n:
            cnt[a[i]] += 1
    
    for i in range(1, n + 1):
        for j in range(i, n + 1, i):
            mx[j] += cnt[i]
    print(max(mx))