a = list(map(int, input().split()))
f = False
for i in range(len(a) - 1):
    if a[i] >= a[i + 1]:
        f = True
        break

if f:
    print('NO')
else:
    print('YES')
