# A

"""for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    f = True
    for k in range(n, 0, -1):
        if not f:
            break
        if max(a) == 0:
            continue
        m = a.index(max(a))
        fnd = False
        for l in range(n - k + 1):
            if l <= m <= l + k - 1:
                v = True
                for i in range(l, l + k):
                    if a[i] < 1:
                        v = False
                        break
                if v:
                    for i in range(l, l + k):
                        a[i] -= 1
                    fnd = True
                    break
        if not fnd:
            f = False
    if f and all(e == 0 for e in a):
        print('YES')
    else:
        print('NO')
        """


# B
for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    ans = 0
    lst = n - 1
    lstb = 0
    for i in range(k):
        if b[i] == 1:
            ans += 0
            lst -= 1
            lstb = i

    for i in range(k - 1, lstb):
        