"""
n = int(input())
m = list(map(int, input().split()))

res = [1]
for i in m:
    if i <= n:
        res.append(i)

print(max(res))
"""

n = int(input())
m = list(map(int, input().split()))

adeq = 1
for i in m:
    if i < n and i > adeq:
        adeq = i
print(adeq)
