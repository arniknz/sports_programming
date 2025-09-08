# ROUND: https://codeforces.com/contest/1791


# A
"""p = 'codeforces'
for _ in range(int(input())):
    s = input()
    if s in p:
        print('YES')
    else:
        print('NO')"""


# B
"""for _ in range(int(input())):
    n = int(input())
    s = list(input())
    x, y = 0, 0
    cx, cy = 1, 1
    f = False
    for i in range(n):
        if s[i] == 'L':
            x -= 1
        elif s[i] == 'R':
            x += 1
        elif s[i] == 'U':
            y += 1
        else:
            y -= 1
        if x == cx and y == cy:
            f = True
            break
    if f:
        print('YES')
    else:
        print('NO')"""


# C
"""for _ in range(int(input())):
    n = int(input())
    s = list(input())
    l, r = 0, n - 1
    cnt = 0
    while l < r:
        #print(s[l], s[r])
        if (s[l] == '0' and s[r] == '1') or (s[l] == '1' and s[r] == '0'):
            cnt += 1
        else:
            break
        l += 1
        r -= 1
    print(n - (cnt * 2))"""


# D
"""for _ in range(int(input())):
    n = int(input())
    s = list(input())
    cnt = [0] * 27 
    p = [0] * 27
    ans = 0
    for e in s:
        cnt[ord(e) - ord('a')] += 1
    for e in s:
        cnt[ord(e) - ord('a')] -= 1
        p[ord(e) - ord('a')] += 1
        curr = 0
        for i in range(26):
            curr += min(1, cnt[i]) + min(1, p[i])
            ans = max(ans, curr)
    print(ans)"""


# E
def cnt_otr(n, a):
    cnt = 0
    for i in range(n):
        if a[i] < 0:
            cnt += 1
    return cnt


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    cnt = cnt_otr(n, a)
    for i in range(n):
        a[i] = abs(a[i])
    if cnt % 2 == 0:
        print(sum(a))
    else:
        print(sum(a) - min(a) * 2)
