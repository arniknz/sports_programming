# A
"""def opr_one(n, a, b):
    for i in range(n):
        if a[i] > b[i]:
            a[i] -= 1
            return a
    return -1


def opr_two(n, a, b):
    for i in range(n):
        if a[i] < b[i]:
            a[i] += 1
            return a
    return a


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    cnt = 1
    while True:
        a = opr_one(n, a, b)
        if a != -1:
            cnt += 1
            a = opr_two(n, a, b)
        else:
            break
    print(cnt)"""


# B
"""for _ in range(int(input())):
    n = int(input())
    a = [-1] * n
    #s =  -1 * (n//2 + 1)
    if n == 2:
        a[1] = 2
    else:
        for i in range(1, n, 2):
            a[i] = 3
        if n % 2 == 0:
            a[-1] = 2
    t = 0
    for i in range(n):
        if a[i] != -1:
            t += a[i]
    print(s, t, sum(a))
    print(*a)"""

# C
"""for _ in range(int(input())):
    n, k = map(int, input().split())
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))
    s.sort()
    t.sort()
    if s == t:
        print('YES')
    else:
        f = True
        for i in range(n):
            if abs(s[i] - t[i]) % k != 0:
                f = False
            elif abs(s[i] - t[i]) // k not in [0, 1]:
                f = False
                break
        if f:
            print('YES')
        else:
            print('NO')"""


# C
for _ in range(int(input())):
    n, k = map(int, input().split())
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))
    s.sort()
    t.sort()
    ds = {}
    dt = {}
    for e in s:
        r = e % k
        if r not in ds:
            ds[r] = 1
        else:
            ds[r] += 1

    for e in t:
        rt = e % k
        if rt not in dt:
            dt[rt] = 1
        else:
            dt[rt] += 1
    f = True
    for i in range(k):
        if i == 0:
            if list(ds.values())[0] != list(dt.values())[0]:
                f = False
                break
        if list(ds.values())[i] + ds.get(k - i, 0) != list(dt.values())[i] + dt.get(k - 1, 0):
            f = False
            break

    if f:
        print('YES')
    else:
        print('NO')