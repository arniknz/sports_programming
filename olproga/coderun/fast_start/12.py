def bin_search(n, a, x):
    l, r = 0, n - 1
    while l < r:
        m = (r + l) // 2
        if a[m] == x:
            return m
        elif a[m] < x:
            l += 1
        else:
            r -= 1

    return l



n = int(input())
a = list(map(int, input().split()))
x = int(input())

res = bin_search(n, a, x)

print(a[res])

# WA 5 test
