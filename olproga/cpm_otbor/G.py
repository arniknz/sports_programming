def sm(a):
    cnt = 0
    while a:
        cnt += a % 10
        a //= 10
    return cnt


def prdk(a):
    cnt = a
    while len(str(a)) > 1:
        cnt += sm(a)
        a = sm(a)
    return cnt


b = int(input())
ans = -1
for i in range(b, max(1, b - 9 * len(str(b)) * 2), -1):
    if prdk(i) == b:
        ans = i
        break
print(ans)