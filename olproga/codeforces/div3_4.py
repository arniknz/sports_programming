"""for _ in range(int(input())):
    k, x = map(int, input().split())
    for _ in range(k):
        x *= 2
    print(x)"""


for _ in range(int(input())):
    n = int(input())
    p = list(map(int, input().split()))
    ans = [0] * n
    a = []
    b = []
    c = []
    for i in range(n):
        if p[i] % 3 == 0:
            a.append(i)
        elif p[i] % 3 == 1:
            b.append(i)
        elif p[i] % 3 == 2:
            c.append(i)
    a1 = []
    b1 = []
    c1 = []
    for i in range(1, n + 1):
        if i % 3 == 0:
            a1.append(i)
        elif i % 3 == 1:
            c1.append(i)
        elif i % 3 == 2:
            b1.append(i)
    print(a, b, c, a1, b1, c1)
    for x in a:
        ans[x] = a1.pop()
    for y in b:
        ans[y] = b1.pop()
    for z in c:
        ans[z] = c1.pop()
    print(*ans)


"""for _ in range(int(input())):
    a, b = map(int, input().split())
    if b == 0:
        print(a if a % 2 == 0 else -1)
        continue
    c = [1, b]
    if b % 2 == 0:
        c.append(2)
    tmp = b
    while tmp % 2 == 0:
        tmp //= 2
    if tmp > 1:
        c.append(tmp)
    if b % 2 == 0:
        c.append(b // tmp)
    if b > 1:
        c.append(b // 2) if b % 2 == 0 else None
        c.append(2 * b) if 2 * b <= 10**9 else None
    ans = -10**20
    f = False
    for k in set(c):
        if b % k == 0:
            if (a * k + b // k) % 2 == 0:
                f = True
                ans = max(ans, a * k + b // k)
    
    print(ans if f else -1)"""