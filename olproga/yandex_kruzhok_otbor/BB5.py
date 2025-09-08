import bisect


def pref_sum_a(s):
    ans = [0] * (len(s) + 1)
    for i in range(1, len(s) + 1):
        if s[i - 1] == 'a':
            ans[i] = ans[i - 1] + 1
        else:
            ans[i] = ans[i - 1]
    return ans


def pref_sum_c(s):
    ans = [0] * (len(s) + 1)
    for i in range(1, len(s) + 1):
        if s[i - 1] == 'c':
            ans[i] = ans[i - 1] + 1
        else:
            ans[i] = ans[i - 1]
    return ans


n, q = map(int, input().split())
s = list(input())
#print(len(s))
b = []
pa = pref_sum_a(s)
pc = pref_sum_c(s)
#print(pa)
#print(pc)
# mx = max(mx, 2 * min(pa[b[i]] - pa[l - 1], pc[r] - pc[b[i] + 1]) + 1)
for i in range(n):
    if s[i] == 'b':
        b.append(i)
for _ in range(q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    mx = 0
    nl, nr = bisect.bisect_left(b, l), bisect.bisect_right(b, r) - 1
    if nl > nr or nr < 0 or nl >= len(b):
        print(0)
        continue
    while nr - nl >= 0:
        m = (nl + nr) // 2
        bi = b[m]
        a = pa[bi] - pa[l]
        c = pc[r + 1] - pc[bi + 1]
        if l <= bi <= r:
            mx = max(mx, 2 * min(a, c) + 1)
        if a < c:
            nl = m + 1
        else:
            nr = m - 1
    print(mx)