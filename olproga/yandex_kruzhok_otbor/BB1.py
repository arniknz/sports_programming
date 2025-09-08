"""def clc_pref_sum(a):
    if not a:
        return []
    ans = [0] * len(a)
    ans[0] = a[0][0]
    for i in range(1, len(a)):
        ans[i] = ans[i - 1] + a[i][0]
    return ans


b, k, x, y = map(int, input().split())
d = list(map(int, input().split()))
p = list(map(int, input().split()))
dd = []
for i in range(x):
    dd.append((d[i], i))
pp = []
for i in range(y):
    pp.append((p[i], i))
dd.sort(key=lambda x: x[0], reverse=True)
pp.sort(key=lambda x: x[0], reverse=True)

pdd = clc_pref_sum(dd)
ppp = clc_pref_sum(pp)
mx, ansn, ansm = 0, 0, 0
for n in range(min(k, y) + 1):
    m = min(k - n, x)
    mx = max(mx, (b + pdd[(n - 1) if n > 0 else 0]) * (100 + ppp[(m - 1) if m > 0 else 0]))
    ansm = m
    ansn = n
print(ansn, ansm)
ansn_a = []
ansm_a = []
for i in range(ansn):
    ansn_a.append(dd[i][1] + 1)
for i in range(ansm):
    ansm_a.append(pp[i][1] + 1)
if ansn_a != []:
    print(*ansn_a)
if ansm_a != []:
    print(*ansm_a)"""

def clc_pref_sum(a):
    if not a:
        return []
    ans = [0] * (len(a) + 1)
    for i in range(1, len(a) + 1):
        ans[i] = ans[i - 1] + a[i - 1][0]
    return ans


b, k, x, y = map(int, input().split())
d = list(map(int, input().split()))
p = list(map(int, input().split()))
dd = []
for i in range(x):
    dd.append((d[i], i))
pp = []
for i in range(y):
    pp.append((p[i], i))
dd.sort(key=lambda x: x[0], reverse=True)
pp.sort(key=lambda x: x[0], reverse=True)
#print(dd)
#print(pp)
pdd = clc_pref_sum(dd)
ppp = clc_pref_sum(pp)
#print(pdd)
#print(ppp)
mx, ansn, ansm = 0, 0, 0
for n in range(min(k, x) + 1):
    m = min(k - n, y)
    #print(n, m, ': n & m')
    #print(mx, ': mx')
    #print((b + pdd[n]) * ((100 + ppp[m]) / 100), ': formula')
    #print(pdd[n], ': pdd[n]')
    #print(ppp[m], ': ppp[m]')
    if (b + pdd[n]) * ((100 + ppp[m]) / 100) > mx:
        mx = (b + pdd[n]) * ((100 + ppp[m]) / 100)
        ansn, ansm = n, m
    #mx = max(mx, (b + pdd[n]) * ((100 + ppp[m]) / 100))
ansd, ansp = [], []
for i in range(ansn):
    ansd.append(dd[i][1] + 1)
for i in range(ansm):
    ansp.append(pp[i][1] + 1)
print(ansn, ansm)
print(*ansd)
print(*ansp)