def pref(a):
    if not a:
        return []
    p = [0] * (len(a) + 1)
    for i in range(1, len(a) + 1):
        p[i] = p[i-1] + a[i - 1]
    return p


n, m = map(int, input().split())
a = list(map(int, input().split()))
ans = -10**20
p = pref(a)
for i in range(n):
    ans = max(ans, (p[min(n, i + m + 1)] - p[i] + p[i] - p[max(0, i - m)]))
print(ans)