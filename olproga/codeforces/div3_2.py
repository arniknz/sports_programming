"""for _ in range(int(input())):
    n = int(input())
    a = input()
    m = int(input())
    b = list(input())
    c = list(input())
    for i in range(m):
        if c[i] == 'D':
            a += b[i]
        else:
            a = b[i] + a
    print(a)"""


"""for _ in range(int(input())):
    n = int(input())
    ans = []
    for i in range(1, len(str(n)) + 1):
        x = str(n // (1 + 10**i))
        y = x + '0' * i
        if n == int(x) + int(y):
            ans.append(int(x))
    print(len(ans))
    if ans != []:
        ans.sort()
        print(*ans)"""

"""A = 3
B = 10
for _ in range(int(input())):
    n = int(input())
    print(n//3, n%3)
    cnt = (n // 3) * B + (n % 3) * A
    print(cnt)"""


"""for _ in range(int(input())):
    ans = 0
    n, k = map(int, input().split())
    i = 0
    opr = 0
    while n > 0:
        o = n % 3
        n //= 3
        c = 3 ** (i + 1)
        if i >= 1:
            c +=  i * 3 ** (i - 1)
        ans += o * c
        i += 1
        opr += 1
        
    print(ans)"""
