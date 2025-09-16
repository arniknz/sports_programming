n = int(input())
a = list(map(int, input().split()))
cur = []
ans = -1
for e in a:
    cur.append(e)
    while sum(cur) >= 0:
        cur = cur[1:]
    if sum(cur) <= -1:
            ans = max(ans, len(cur))
print(ans)