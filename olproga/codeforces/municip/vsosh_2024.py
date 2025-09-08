# ROUND: https://codeforces.com/gym/105641


#  A
# Решение на 60 баллов.
"""EPS = 2 * 10**9
n = int(input())
a = int(input())
b = int(input())
cnt = EPS + 7
res = [cnt]
for i in range(2, n):
    #print(abs(((i - 1) * a) - ((n - i) * b)))
    cnt = min(cnt, abs(((i - 1) * a) - ((n - i) * b)))
    res.append(cnt)
print(res.index(cnt) + 1)"""

# Решение на 100 баллов.
"""def f(a, b, x):
    return abs(a * (x - 1) - b * (n - x))


n = int(input())
a = int(input())
b = int(input())

x = max(2, (b * n + a)//(a + b))
if f(a, b, x) > f(a, b, x + 1) and x + 1 < n:
    x += 1
print(x)"""


# B
"""n = int(input())
m = int(input())
ans = 8 * n * m + 2 * n * (m - 1) + 2 * m * (n - 1) + 4 * (n - 1) * (m - 1)
print(ans)"""


# C
n = int(input())
a = input()
zeros = 0
c = ''
for i in range(n - 1):
    b = input()
    if len(a) + zeros >= len(b):
        while len(a) < len(b):
            a += '0'
            zeros -= 1
            ap = a[:len(b)]
            if ap == b:
                c = a
            elif ap > b:
                c = b
                zeros = zeros + len(a) + 1 - len(b)
            else:
                c = b
                zeros = zeros + len(a) - len(b)
    else:
        c = b
        zeros = 0
    a = c
print(a + '0' * zeros)
