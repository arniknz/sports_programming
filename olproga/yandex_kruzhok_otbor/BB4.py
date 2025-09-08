MAX = 10**9


n = int(input())
a, b = map(int, input().split())
l = []
for _ in range(n):
    c, t = map(int, input().split())
    l.append((c, t))

dp = [[MAX] * (b + 1) for _ in range(a + 1)]
dp[0][0] = 0
for e in l:
    c, t = e
    for i in range(a, -1, -1):
        for j in range(b, -1, -1):
            if dp[i][j] != -1:
                x = min(i + c, a)
                y = min(j + t, b)
                dp[x][y] = min(dp[x][y], dp[i][j] + 1)
#for r in dp:
#    print(*r)
print(dp[a][b] if dp[a][b] != MAX else -1)
"""l.sort(key=lambda x: max(x[0], x[1]), reverse=True)
#print(l)
cnt_c, cnt_t = 0, 0
ans = 0
f = False
for e in l:
    cnt_c += e[0]
    cnt_t += e[1]
    ans += 1
    if cnt_c >= a and cnt_t >= b:
        f = True
        break

if f:
    print(ans)
else:
    print(-1)"""