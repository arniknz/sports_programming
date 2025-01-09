k = int(input())

p = [0, 1]
res = 0
cnt = 0
for i in range(2, 10 ** 12):
    cnt += 1
    n1 = p[i - 1] * i
    n2 = n1 % k
    print(n1, n2)
    if (p[i - 1] * i) % k == 0:
        res = i
        break
    p.append(p[i - 1] * i)

print(res, cnt)