s = list(input())
s.pop()
d = {}
for e in s:
    if e not in d:
        d[e] = 1
    else:
        d[e] += 1
#print(d)
d = dict(sorted(d.items(), key=lambda x: x[0], reverse=True))
#print(d)
od, ev = 0, 0
k = ''
for e in d:
    if d[e] % 2 != 0:
        od += 1
        k = e
        d[e] -= 1
    else:
        ev += 1
if od > 1:
    print('NO')
else:
    if od == 0:
        ans = ''
        for e in d:
            ans = e * (d[e] // 2) + ans + e * (d[e] // 2)
        print('YES')
        print(ans)
    else:
        ans = k
        for e in d:
            ans = e * (d[e] // 2) + ans + e * (d[e] // 2)
        print('YES')
        print(ans)