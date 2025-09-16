n = int(input())
a = list(map(int, input().split()))
cnt = []
idxs = []
cl = []
for i in range(n):
    if a[i] < 0:
        cnt.append(i)
        if len(cnt) > len(idxs):
            idxs = cnt
    else:
        cnt = []
        cl.append(a[i])
s = sum(a[idxs[0]:idxs[-1] + 1])
ans = 0
k = 0
cnt = 0
if cl != []:
    for i in range(len(cl)):
        if s + cl[i] < k:
            s += cl[i]
            cnt += 1
        else:
            s += cl[i]
            cnt += 1
            while s > k:
                s -= cl[i - cnt + 1]
                cnt -= 1
        ans = max(ans, cnt)
    print(ans)
else:
    print(len(idxs))