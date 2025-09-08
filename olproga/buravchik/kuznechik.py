# https://codeforces.com/group/q7pRVvtbsf/contest/584991/problem/B

n = int(input())
dp = [-1] * (n + 1)
dp[0] = 0
for i in range(1, n):
    for j in range(max(0, i - 2), i):
        dp[i] = max(dp[i], dp[j])
print(dp[n])