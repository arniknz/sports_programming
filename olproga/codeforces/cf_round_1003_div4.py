# ROUND: https://codeforces.com/contest/2065


# A
"""res = []
for _ in range(int(input())):
    s = input()

    res.append([s[:-2] + "i"])

for r in res:
    print(*r)"""


# B
"""def solve(s):
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return 1
    
    return len(s)


for _ in range(int(input())):
    print(solve(input()))"""


# C1
def is_sorted(a):
    b = sorted(a)
    return a == b


for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if n == 1 or is_sorted(a):
        print('YES')
    else:
        a[0] = min(a[0], b[0] - a[0])
        for i in range(1, n):
            if min(a[i], b[0] - a[i]) >= a[i - 1]:
                a[i] = min(a[i], b[0] - a[i])
            elif max(a[i], b[0] - a[i]) >= a[i - 1]:
                a[i] = max(a[i], b[0] - a[i])
        if is_sorted(a):
            print('YES')
        else:
            print('NO')