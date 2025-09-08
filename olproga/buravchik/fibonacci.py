# https://codeforces.com/group/q7pRVvtbsf/contest/584991/problem/A


def solve(n):
    f = [0, 1]
    for _ in range(n):
        f[0], f[1] = f[1], f[0] + f[1]
    return f[0]


n = int(input())
print(solve(n))