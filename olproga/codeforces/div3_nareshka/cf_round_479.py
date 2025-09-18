#ROUND: https://codeforces.com/contest/977


# A
"""n, k = map(int, input().split())
for _ in range(k):
    if n % 10 != 0:
        n -= 1
    else:
        n //= 10
print(n)"""

# B
"""import re
n = int(input())
s = input()
ans = {}
for i in range(n):
    if len(s[i:i+2]) == 2:
        ans[s[i:i+2]] = len(re.findall(fr'(?={s[i:i+2]})', s))
print(max(ans, key=ans.get))"""

# C
"""n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
if k != 0:
    x = a[k - 1]
    cnt = 0
    for i in range(n):
        if a[i] <= x:
            cnt += 1
    print(x if k == cnt else -1)
else:
    if a[0] == 1:
        print(-1)
    else:
        print(a[0] - 1)"""

# D
def tr(x):
    cnt = 0
    while x % 3 == 0:
        cnt += 1
        x //= 3
    return cnt
n = int(input())
a = list(map(int, input().split()))
ans = []
for i in range(n):
    ans.append((-tr(a[i]), a[i]))
ans.sort()
res = []
for i in range(n):
    res.append(ans[i][1])
print(*res)