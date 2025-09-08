# ROUND: https://codeforces.com/contest/1352


# МНОГО НА МАТЕМАТИКУ


# A
"""for _ in range(int(input())):
    n = input()
    s = len(n)
    n = int(n)
    res = []
    for i in range(1, s + 1):
        p = n % (10 ** i)
        if p != 0:
            res.append(p)
            n = n - p
    print(len(res))
    print(*res)"""


# B
def even_or_odd(a):
    c = 'e' if a[0] % 2 == 0 else 'o'
    for i in range(len(a)):
        pass


for _ in range(int(input())):
    n, k = map(int, input().split())
    if n % k == 0:
        print(str(n // k) * k)
    else:
        pass


# C
"""for _ in range(int(input())):
    n, k = map(int, input().split())
    if n == k:
        print(k + 1)
    elif n > k:
        print(k)
    else:
        ans = k + ((k - 1) // (n - 1))
        print(ans)"""

# Важно! K-ое число всегда правее. Мы сдвигаем ответ на 1