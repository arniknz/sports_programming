n = int(input())
a = list(map(int, input().split()))
pd = [0] * n
i = 0
p = 0
while i < n:
    if a[i] != 1:
        pd[p] += 1
    else:
        p += 1
        pd[p] += 1
    i += 1

ans = []
for e in pd:
    if e != 0:
        ans.append(e)
print(len(ans))
print(*ans)