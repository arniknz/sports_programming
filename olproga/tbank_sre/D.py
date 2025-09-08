def order(n, dir=0, b=1):
    if n == 0:
        return [b]
    h = 2 ** (n - 1)
    if dir == 0:
        return order(n - 1, 0, b) + order(n - 1, 1, b + h)
    else:
        return order(n - 1, 0, b + h) + order(n - 1, 1, b)
    

def solve(d, k):
    o = order(d)
    v = 1
    def dfs(n, dir, b):
        nonlocal v
        if n == 0:
            if b == k:
                v += 1
                return True
            v += 1
            return False
        v += 1
        h = 2 * (n - 1)
        if dir == 0:
            if dfs(n - 1, 0, b):
                return True
            if dfs(n - 1, 1, b + h):
                return True
        else:
            if dfs(n - 1, 0, b + h):
                return True
            if dfs(n - 1, 1, b):
                return True
        return False
    dfs(d, 0, 1)
    return v


d, k = map(int, input().split())
print(solve(d, k))