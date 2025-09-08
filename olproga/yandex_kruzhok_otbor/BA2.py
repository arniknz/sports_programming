def pref(n, c):
    p = [0] * (n + 1)
    for i in range(n): p[i + 1] = p[i] + (c[i][0] * c[(i + 1) % n][1] - c[(i + 1) % n][0] * c[i][1])
    return p


n = int(input())
c = []
for _ in range(n):
    x, y = map(int, input().split())
    c.append((x, y))
p = pref(n, c)
cnt = [0] * 8
for i in range(n): cnt[(c[i][0] % 2) * 4 + (c[i][1] % 2) * 2 + (p[i] % 2)] += 1
gp = [[0] * 8 for _ in range(8)]
for i in range(8):
    for j in range(8):
        if (j % 2 + i % 2 + (i // 4) * ((j // 2) % 2) + (j // 4) * ((i // 2) % 2)) % 2 == 0:
            gp[i][j] = 1
ans = 0
for i in range(8):
    for j in range(i, 8):
        if gp[i][j] == 1:
            if i == j:
                ans += cnt[i] * (cnt[i] - 1) // 2
            else:
                ans += cnt[i] * cnt[j]
print(ans - n)