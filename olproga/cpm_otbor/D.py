n, m = map(int, input().split())
mt = []
s = {}
st = {}
for i in range(n):
    r = list(map(int, input().split()))
    s[i] = min(r)
    mt.append(r)

#st 
mt1 = list(zip(*mt[::-1]))
for i in range(m):
    st[i] = max(mt1[i])
cnt = 0
for i in s:
    for j in st:
        if s[i] == st[j]:
            cnt += 1
print(cnt)