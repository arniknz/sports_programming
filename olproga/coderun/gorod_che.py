# https://coderun.yandex.ru/problem/city-of-che

n, r = map(int(input()))
d = list(map(int, input().split()))
l, r = 0, n - 1
while l < r:
    