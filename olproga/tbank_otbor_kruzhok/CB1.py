n = int(input())
a = list(map(int, input().split()))
p = list(map(int, input().split()))
ans = {}
for i in range(n):
    cnt = 0
    for j in range(n):
        if i != j:
            cnt += abs(a[i] - a[j]) * p[j]
    ans[i + 1] = cnt
print(min(ans, key=ans.get))