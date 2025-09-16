x, y = map(int, input().split())
if x == y:
    print(0)
else:
    if x < 2 * y:
        print(3)
    else:
        a, b, c = y, y, y
        ans = 0
        while a < x or b < x or c < x:
            if a <= b and a <= c:
                a = min(b + c - 1, x)
            elif b <= a and b <= c:
                b = min(a + c - 1, x)
            else:
                c = min(a + b - 1, x)
            ans += 1
        print(ans)