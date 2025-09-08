def mk_dig(n):
    return [int(e) for e in str(n)]

def f(n, sm):
    d = mk_dig(n)
    dp = [[dict() for _ in range(2)] for _ in range(len(d) + 1)]
    dp[0][1][(0, 1)] = 1
    for i in range(len(d)):
        tmpdp = [dict() for _ in range(2)]
        for o in range(2):
            for (s, p), cnt in dp[i][o].items():
                u = d[i] if o else 9
                for j in range(u + 1):
                    no = 1 if o == 1 and j == u else 0
                    ns = s + j
                    np = p * j
                    if ns <= sm:
                        if (ns, np) not in tmpdp[no]:
                            tmpdp[no][(ns, np)] = 0
                        tmpdp[no][(ns, np)] += cnt
        for o in range(2):
            dp[i + 1][o] = tmpdp[o]
    res = 0
    for o in range(2):
        for (s, p), cnt in dp[len(d)][o].items():
            if s == sm and p % sm == 0:
                res += cnt
    return res


"""l, r = map(int, input().split())
mxr = 9 * len(mk_dig(r))
mxl = 9 * len(mk_dig(l - 1))
#print(mk_dig(l - 1))
fr = 0
fl = 0
for i in range(1, mxr + 1):
    fr += f(r, i)
for i in range(1, mxl + 1):
    fl += f(l - 1, i)
print(fr - fl)"""
print(f(100, 1))