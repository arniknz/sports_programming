# ROUND: https://codeforces.com/contest/1999


# A
"""def ch_sum(x):
    x1 = str(x)
    ans = 0
    for c in x1:
        ans += int(c)
    return ans

for _ in range(int(input())):
    n = int(input())
    print(ch_sum(n))"""


# B
"""def ans(a, b):
    if a > b:
        return 1
    elif a == b:
        return 0
    return -1
for _ in range(int(input())):
    a1, a2, b1, b2 = map(int, input().split())
    cnt = 0
    if ans(a1, b1) + ans(a2, b2) > 0:
        cnt += 1
    if ans(a1, b2) + ans(a2, b1) > 0:
        cnt += 1
    if ans(a2, b2) + ans(a1, b1) > 0:
        cnt += 1
    if ans(a2, b1) + ans(a1, b2) > 0:
        cnt += 1
    print(cnt)"""


# C
"""def solve():
    n, s, m = map(int, input().split())
    segm = [[0, 0], [m, m]] + [list(map(int, input().split())) for i in range(n)]
    segm.sort()
    for i in range(1, n + 2):
        if segm[i][0] - segm[i - 1][1] >= s:
            print("YES")
            return
    print("NO")

for _ in range(int(input())):
    solve()"""


# D
for _ in range(int(input())):
    s = list(input())
    t = list(input())
    j = 0
    for i in range(len(s)):
        if s[i] == '?':
            if j < len(t):
                s[i] = t[j]
                j += 1
            else:
                s[i] = 'a'
        elif j < len(t) and s[i] == t[j]:
            j += 1

    if j == len(t):
        print('YES')
        print(''.join(s))
    else:
        print('NO')
    #print(s, j)


# E
