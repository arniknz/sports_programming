# A
"""for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    if len(list(set(a))) < n:
        print('YES')
    else:
        print('NO')"""

# B
for _ in range(int(input())):
    n = int(input())
    g = list(map(int, input().split()))
    g.sort(reverse=True)
    cnt = 0
    for i in range(0, n - 1, 2):
        cnt += g[i]
        g[i + 1] = 0
        g[i] -= g[i + 1]
    #print(g)
    if n % 2 == 0:
        print(cnt)
    else:
        print(cnt + g[-1])