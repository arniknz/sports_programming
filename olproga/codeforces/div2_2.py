# Забудь о рейтинге. Решай не на результат.


# Что дано? Что от нас хотят?
# Какие ограничения?
# Что сложно? Что сделать чтобы задача была чуть проще?


# Если WA на 2 тесте - логика либо недоработана, либо неверна.
# Если долго не получается, сноси код и пиши заново. Придумывай заново.


# Цель: ABC
# A
"""def is_possible(a, b):
    if a >= 3:
        if b < (a - 1) // 2:
            return False
    if b >= 3:
        if a < (b - 1) // 2:
            return False
    return True

for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    if c < a or d < b:
        print('NO')
        continue
    
    if not is_possible(a, b):
        print('NO')
        continue

    if is_possible(c - a, d - b):
        print('YES')
    else:
        print('NO')"""


# B
"""for _ in range(int(input())):
    n, k = map(int, input().split())
    s = list(input())
    if k > n:
        print('YES')
        print(*[i for i in range(1, n + 1)])
    else:
        if '1' * k in ''.join(s):
            print('NO')
        else:
            ones_idxs = []
            zeros_idxs = []
            for i in range(n):
                if s[i] == '1':
                    ones_idxs.append(i)
                else:
                    zeros_idxs.append(i)
            p = [0] * n
            ones_ans = [i for i in range(1, n - len(zeros_idxs) + 1)]
            zeros_ans = [i for i in range(n - len(zeros_idxs) + 1, n + 1)]
            for i in range(len(ones_idxs)):
                p[ones_idxs[i]] = ones_ans[i]
            for i in range(len(zeros_idxs)):
                p[zeros_idxs[i]] = zeros_ans[i]
            print('YES')
            print(*p)"""


# C
"""from collections import defaultdict
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    dp = [0] * (n)
    pref = [0] * (n + 1)
    pos = defaultdict(list)
    r = [0] * n
    for i in range(n):
        pos[a[i]].append(i)
        r[i] = len(pos[a[i]]) - 1
    
    for i in range(n):
        if a[i] == 1:
            dp[i] = max(1, pref[i] + 1)
        else:
            p = r[i]
            if p >= (a[i] - 1):
                idx = pos[a[i]][p - (a[i] - 1)]
                if idx > 0:
                    dp[i] = pref[idx] + a[i]
                else:
                    dp[i] = a[i]
        pref[i + 1] = max(pref[i], dp[i])
    print(pref[n])"""


# D
