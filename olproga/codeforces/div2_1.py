# A
"""for _ in range(int(input())):
    n, a, b = map(int, input().split())
    if a > b:
        if n % 2 == 0:
            if a % 2 == 0 and b % 2 == 0:
                print('YES')
            else:
                print('NO')
        else:
            if a % 2 != 0 and b % 2 != 0:
                print('YES')
            else:
                print('NO')
    else:
        if n % 2 == 0 and b % 2 == 0:
            print('YES')
        elif n % 2 != 0 and b % 2 != 0:
            print('YES')
        else:
            print('NO')"""


# B
import math as m
def my_gcd(a):
    if not a:
        return 0
    if len(a) == 1:
        return a[0]
    res = a[0]
    for i in range(1, len(a)):
        res = m.gcd(res, a[i])
    return res
for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    cnt = 0
    if k % 2 != 0:
        for i in range(n):
            if a[i] % 2 != 0:
                a[i] += k
        print(*a)
    else:
        if k == 2:
            for i in range(n):
                if a[i] % 3 != 0:
                    a[i] += k
                    if a[i] % 3 != 0:
                        a[i] += k
            print(*a)
        else:
            for i in range(n):
                if a[i] % (k - 1) != 0:
                    a[i] += k * (k - 1 - a[i])
            print(*a)