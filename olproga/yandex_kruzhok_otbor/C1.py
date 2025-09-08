import math as m


n = int(input())
a = []
dists = []
for _ in range(n):
    x, y = map(int, input().split())
    a.append((x, y))
for i in range(n):
    for j in range(n):
        if a[i] != a[j]:
            dists.append(m.dist(a[i], a[j]))
ans = max(dists)
print(round(ans, 10) if ans != int(ans) else format(ans, '.10f'))