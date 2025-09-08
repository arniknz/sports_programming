def resheto(n):
        r = [i for i in range(n)]
        ans = []
        for i in range(2, int(n ** 0.5) + 1):
            if r[i]:
                ans.append(i)
                for j in range(i ** 2, int(n ** 0.5) + 1, i):
                    #print(j)
                    r[j] = False
        return ans


def solve(n):
    # n = int(input())
    resh = resheto(n)
    #print(resh)
    cnt = 0
    for p in resh:
        if p ** 8 <= n:
            cnt += 1


    for i in range(len(resh)):
        p = resh[i] ** 2
        for j in range(i + 1, len(resh)):
            q = resh[j] ** 2
            if p * q <= n:
                cnt += 1

    print(cnt)


for i in range(1, 2 * 10**6):
    solve(i)
    