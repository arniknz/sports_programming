a = int(input())
b = int(input())
u = min(50 * a, 70 * b)
l = max(50 * (a - 1) + 1, 70 * (b - 1) + 1)
ans = set()
for i in range(l, u + 1):
    if 50 * (a - 1) <= i < 50 * a and 70 * (b - 1) <= i < 70 * b:
        if ((i + 59) // 60) not in ans:
            ans.add((i + 59) // 60)
print(*sorted(list(ans)) if len(ans) != 0 else [-1])