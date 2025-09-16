"""for _ in range(int(input())):
    x, n = map(int, input().split())
    ans = []
    for i in range(n):
        if i % 2 == 0:
            ans.append(x)
        else:
            ans.append(-x)
    print(sum(ans))"""


"""for _ in range(int(input())):
    n, m, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(len(a) + len(b))"""


"""for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    g = 0
    e, o = [], []
    for i in range(n):
        if a[i] % 2 == 0:
            e.append(a[i])
        else:
            o.append(a[i])
    if len(o) == 0:
        print(0)
    else:
        o.sort(reverse=True)
        ans = []
        ans.append(o[0])
        for i in range(len(e)):
            ans.append(e[i])
        if len(o) > 2:
            l, r = 1, len(o) - 1
            while l < r:
                ans.append(o[r])
                ans.append(o[l])
                l += 1
                r -= 1
            if l == r:
                ans.append(o[l])
        elif len(o) == 2:
            ans.append(o[1])
        cnt = 0
        for i in range(len(ans)):
            if ans[i] % 2 != 0:
                if g == 0:
                    g = 1
                    cnt += ans[i]
                else:
                    g = 0
            elif g == 1:
                cnt += ans[i]
        print(cnt)"""


for _ in range(int(input())):
    n, m = map(int, input().split())
    cnt = 0
    ms = 0
    s = 0
    for _ in range(n):
        a, b = map(int, input().split())
        if s == b:
            cnt += (a - ms) - ((a - ms) % 2)
        else:
            cnt += (a - ms) - ((a - ms + 1) % 2)
        s = b
        ms = a
            
    print(cnt + (m - ms))