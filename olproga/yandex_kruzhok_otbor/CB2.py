def raspakovka(v):
    tmp = v.split()
    c = int(tmp[0])
    l = int(tmp[1])
    r = [int(tmp[i]) for i in range(2, len(tmp))]
    r.sort()
    r = set(r)
    return c, l, r



n, m = map(int, input().split())
d = []
for _ in range(n):
    c, _, r = raspakovka(input())
    d.append((c, r))

#print(d)
f = False
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        ci, ri = d[i]
        cj, rj = d[j]
        if ci >= cj and ri.issubset(rj) and (ci > cj or len(list(rj)) > len(list(ri))):
            f = True
            break
        
if f:
    print('Yes')
else:
    print('No')