n, s = map(int, input().split())
l = []
for _ in range(n):
    c, a = map(int, input().split())
    l.append((c, a))
l.sort(key=lambda x: x[0])
cnt = 0
for e in l:
    if e[1] < s:
        cnt += e[0] * e[1]
        s -= e[1]
    else:
        cnt += e[0] * s
        s = 0
print(cnt)