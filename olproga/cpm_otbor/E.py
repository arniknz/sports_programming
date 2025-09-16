n = int(input())
ans = [i for i in range(1, n + 1)]
while len(ans) > 1:
    l = []
    for i in range(0, len(ans), 2):
        r = int(input())
        if r == 1:
            l.append(ans[i])
        else:
            l.append(ans[i + 1])
    ans = l
print(ans[0])