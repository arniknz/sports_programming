"""def prefix_sum(a):
    pr = [0] * len(a)
    pr[0] = a[0]
    for i in range(1, len(a)):
        pr[i] = pr[i - 1] + a[i]

    return pr


n, q = map(int, input().split())
p = list(map(int, input().split()))
p.sort()
pr = prefix_sum(p)
for _ in range(q):
    x, y = map(int, input().split())
    if n >= x:
        print(pr)
    else:
        print(0)"""

"""import math as m


for _ in range(int(input())):
    n = int(input())
    res = m.ceil(n / 2)
    print(res)
    i, j = 0, n * 3
    while i < j:
        print(i, j)
        i += 3
        j -= 3"""


"""for _ in range(int(input())):
    words = list(map(str, input().split()))
    res = ''
    for word in words:
        res += word[0]

    print(res)
"""


"""def transform_string(s):
    if s[-1] == 's':
        return s + s[-2:]
    return s


s = input()
res = transform_string(s)
if s == 's':
    print(s * 2)
elif len(res) > 10:
    print(res * 2)
else:
    print(res)"""


"""def z_func(s):
    n = len(s)
    z = [0] * n
    left, right = 0, 0
    for i in range(1, n):
        z[i] = max(0, min(right - i, z[i - left]))
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > right:
            left = i
            right = i + z[i]
    return z


def find_substring(pat, text):
    z = z_func(pat + '#' + text)
    m = len(pat)
    res = []
    for i in range(len(z)):
        if z[i] == m:
            res.append(i - m)
    return res


p = input()
t = input()
res = find_substring(p, t)
print(len(res))
print(*res)"""


"""def prefix_func(s):
    p = [0] * len(s)
    for i in range(1, len(s)):
        k = p[i - 1]
        while k > 0 and s[i] != s[k]:
            k = p[k - 1]
        if s[i] == s[k]:
            k += 1
        p[i] = k
    return p


s = input()
print(*prefix_func(s))"""


"""def gen(n, k):
    ans = [0] * n
    direction = 'l'
    for i in range(n):
        if direction == 'l':
            ans[i // 2] = n - i
            direction = 'r'
        else:
            ans[n - i + i // 2] = n - i
            direction = 'l'
    return ans


for _ in range(int(input())):
    n, k = map(int, input().split())
    print(*gen(n, k))"""


"""def factorial(n):
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f"""


"""for i in range(int(input())):
    a, b, c = map(int, input().split())
    print(a + b + c)
    if a == 1 and b == 5 and c == 6:
        print('NO')
    elif (a + b + c) % 3 == 0:
        print('YES')
    else:
        print('NO')

# 25524 280432 419060"""


"""import math as m


for _ in range(int(input())):
    s = input()
    n = int(s)
    res = 0
    if int(n ** 0.5) == n ** 0.5:
        res = (n ** 0.5) / 2
        if int(res) == n ** 0.5:
            print(res, res)
        else:
            print(int(res), m.ceil(res))
    else:
        print(-1)"""


"""for _ in range(int(input())):
    s = input()
    n = int(s)
    res = 0
    if int(n ** 0.5) == n ** 0.5:
        print(int(n ** 0.5), 0)
    else:
        print(-1)"""


"""for _ in range(int(input())):
    n, k = map(int, input().split())
    s = list(input())
    i, j = 0, n - 1
    cnt = 0
    pairs = []
    while i < j:
        if s[i] == s[j]:
            cnt += 1
            pairs.append((s[i], s[j]))
        i += 1
        j -= 1
    if n == 2 and cnt == 0 and k != 0:
        print('NO')
    elif cnt == k:
        print('YES')
    elif cnt % 2 == 0 and (cnt + 2 == k or cnt - 2 == k) and (len(list(set(pairs))) != 1):
        print('YES')
    elif cnt % 2 != 0 and (cnt + 1 == k or cnt - 1 == k):
        print('YES')
    else:
        print('NO')"""


"""for _ in range(int(input())):
    n, k = map(int, input().split())
    s = list(input())
    zeroshki = 0
    edinichki = 0
    for i in range(n):
        if s[i] == '0':
            zeroshki += 1
        else:
            edinichki += 1

    mx_pairs = zeroshki // 2 + edinichki // 2
    if mx_pairs == 0 and k != 0:
        print('NO')
    elif k <= mx_pairs:
        print('YES')"""


"""for _ in range(int(input())):
    x, y, a = map(float, input().split())
    yama = a + 0.5
    cnt = 0
    turn = 'B'
    while True:
        if turn == 'B':
            cnt += x
            turn = 'K'
            if cnt > yama:
                print('NO')
                break
        elif turn == 'K':
            cnt += y
            turn = 'B'
            if cnt > yama:
                print('YES')
                break"""


"""for _ in range(int(input())):
    n = int(input())
    cnt = 0
    for i in range(n):
        for j in range(n):
            if i == n - j:
                cnt += 1
    print(cnt)"""


"""for _ in range(int(input())):
    a = list(input())
    b = a[::-1]
    for i in range(len(b)):
        if b[i] == 'p':
            b[i] = 'q'
        elif b[i] == 'q':
            b[i] = 'p'
    print(''.join(b))"""


"""for _ in range(int(input())):
    m, a, b, c = map(int, input().split())
    r1 = a if a <= m else m
    r2 = b if b <= m else m
    if r1 + r2 == 2 * m:
        print(r1 + r2)
    else:
        ostatki = c if c <= ((m - a if a <= m else m) + (m - b if b <= m else m)) else 2 * m - (r1 + r2)
        print(r1 + r2 + ostatki)"""


"""квас: 1 л
картофель: 1 кг
огурцы: 300 г
яйца: 5 шт
колбаса: 300 г
редис: 100 г
зелень: по вкусу"""


"""d = {
    ['квас', 'кефир']: [200, 'кг'],
    'картофель': [200, 'кг'],
    'огурцы': [60, 'г'],
    'яйца': [1, 'шт'],
    'колбаса': [300, 'г'],
    'редис': [100, 'г'],
    'зелень': 'по вкусу'
    }

spec = input().split(',')
"""


"""for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    if min(a, c) < min(b, d):
        print('Flower')
    else:
        print('Gellyfish')"""


"""def find_letter(target, arr):
    for i in arr:
        if i != target:
            return i


alphabet = 'abcdefghijklmnopqrstuvwxyz'


for _ in range(int(input())):
    s = list(input())
    found = False
    for i in range(1, len(s)):
        if s[i - 1] == s[i]:
            found = True
            s.insert(i, find_letter(s[i], alphabet))
            break

    if found:
        print(''.join(s))
    else:
        s.append(find_letter(s[-1], alphabet))
        print(''.join(s))"""


"""for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))"""


"""for _ in range(int(input())):
    print(int(input()) * 2)"""


"""for _ in range(int(input())):
    s = 0
    cnt = 0
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        s += a[i]
        if s % 2 == 0:
            cnt += 1
            while s % 2 == 0:
                s //= 2"""


"""for _ in range(int(input())):
    s = input()
    desyatka = s[:2]
    stepen = s[2:]
    if len(stepen) != 0:
        if (desyatka == '10' and stepen[0] != '0' and int(stepen) != 1):
            print('YES')
        else:
            print('NO')
    else:
        print('NO')"""


"""for _ in range(int(input())):
    nogy = int(input())
    if nogy % 4 == 0:
        print(nogy // 4)
    else:
        print(nogy // 4 + 1)"""


"""for _ in range(int(input())):
    n = int(input())
    x, y = map(int, input().split())
    f = min(x, y)
    res = n // f
    if n % f != 0:
        print(res + 1)
    else:
        print(res)
"""


"""names = []
for i in range(int(input())):
    name = input()
    if name not in names:
        print('OK')
    else:
        print(name + str(names.count(name)))

    names.append(name)"""


"""for _ in range(int(input())):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    frst = 0
    for i in range(n):
        if a[i] == 1:
            frst = i + 1
            break

    if n - frst <= x:
        print('YES')
    else:
        print('NO')"""


"""or _ in range(int(input())):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    first_idx = 0
    last_idx = 0
    for i in range(n):
        if a[i] == 1:
            #print('KKKKKKKKKK', a[i], i)
            first_idx = i
            break

    for j in range(n - 1, 0, -1):
        if a[j] == 1:
            #print('BBBBBBBBBB', a[j], j)
            last_idx = j
            break

    #print('-------->>> idxs', first_idx, last_idx)

    #print('--->>>', len(a[first_idx:last_idx + 1]), a[first_idx:last_idx + 1])

    if len(a[first_idx:last_idx + 1]) <= x:
        print('YES')
    else:
        print('NO')
"""


import sys


"""data = []

while True:
    line = sys.stdin.readline().strip()
    if not line:
        break
    data.append(line)

res = 0
for i in range(len(data)):
    if ':' in data[i]:
        idx = data[i].find(':')
        print(len(data[i][idx:]))
        res += len(data[i][idx:])

print(res)"""

"""res = 0
for line in sys.stdin:
    line = line.replace('\n', '')
    if ':' in line:
        idx = line.find(':')
        # print(len(line[idx:]))
        if line[idx + 1] == line[idx + 1].lower():
            res += len(line[idx:])
        else:
            res += len(line[idx + 1:])

print(res)"""

"""for _ in range(int(input())):
    n, k = map(int, input().split())
    res = ['0'] * n
    if n == k:
        print('1' * k)
    else:
        for i in range(k):
            res[i] = '1'

        print(''.join(res))"""


"""def find_mx_and_letter(a, b, x, y):
    if a > b:
        return 'x'
    elif a < b:
        return 'y'
    else:
        if x > y:
            return 'y'
        return 'x'


for _ in range(int(input())):
    k, a, b, x, y = map(int, input().split())
    res = k // min(x, y) + 1 - min(a, b)
    print(res if res > 0 else 0)
# 1 1 1 2 2


# 25524 280432 419060
for i in range(int(input())):
    a, b, c = map(int, input().split())
    if (a + b + c) % 3 == 0:
        if b <= (a + b + c) // 3:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
"""


"""for _ in range(int(input())):
    a, b = map(int, input().split())
    if a == 0 and b % 2 == 0 or b == 0 and a % 2 == 0:
        print('YES')
    else:
        if a != 0 and a % 2 == 0:
            print('YES')
        else:
            print('NO')"""


"""for _ in range(int(input())):
    l1, b1, l2, b2, l3, b3 = map(int, input().split())
    if l1 == l2 == l3:
        if b1 + b2 + b3 == l1:
            print('YES')
        else:
            print('NO')
    else:
        if abs(max([l1, l2, l3]) - sum([l1, l2, l3])) == max([l1, l2, l3]):
            print('YES')
        else:
            print('NO')"""

"""
for _ in range(int(input())):
    l1, b1, l2, b2, l3, b3 = map(int, input().split())
    if max([l1, l2, l3]) > max([b1, b2, b3]):
        if max([l1, l2, l3]) == sum([l1, l2, l3]) - max([l1, l2, l3]) and max([l1, l2, l3]) == sum([b1, b2, b3]):
            print('YES')
        else:
            print('NO')
    else:
        if max([b1, b2, b3]) == sum([b1, b2, b3]) - max([b1, b2, b3]) and max([b1, b2, b3]) == sum([l1, l2, l3]):
            print('YES')
        else:
            print('NO')"""


"""for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    res = -1
    ans = 'NO'
    for i in range(n):
        cnt = 0
        for j in range(n):
            if i != j:
                if abs(a[i] - a[j]) % k != 0:
                    cnt += 1
        if cnt == n - 1:
            res = i
            ans = 'YES'
            break

    if res != -1:
        print(ans + "\n" + str(res + 1))
    else:
        print(ans)"""


"""for _ in range(int(input())):
    a, x, y = map(int, input().split())
    res = -1
    st, end = 0, 0
    if x < y:
        st = x
        end = y + 1
    else:
        st = y
        end = x + 1

    for i in range(st, end):
        if abs(i - x) < abs(a - x) and abs(i - y) < abs(a - y):
            res = 1
            break

    print('YES' if res != -1 else 'NO')"""


"""for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    if n == 2:
        if abs(a[0] - a[1]) <= 1:
            print(0)
        else:
            print(-1)
    else:
        """


"""def removeDuplicates(nums):
    d = {}
    for n in nums:
        if n not in d:
            d[n] = 1
        else:
            d[n] += 1

    res = list(d.keys())
    k = len(res)

    nums[:k] = res

    return k


nums = list(map(int, input().split()))
res = removeDuplicates(nums)
print(res, nums)"""


'''n = int(input())
l, r = 0, n
while l < r:
    mid = r + (l - r) // 2
    if mid == n // mid:
        print(mid)
        break
    elif mid > n // mid:
        r = mid - 1
    else:
        l = mid + 1
print(r)'''


"""for _ in range(int(input())):
    n, a, b = map(int, input().split())
    if n == 1:
        print(a)
    else:
        if n % 2 == 0:
            print(a * n if a * n < (n // 2) * b else (n // 2) * b)
        else:
            print(a * n if a * n < ((n - 1) // 2) * b + a else ((n - 1) // 2) * b + a)"""


"""for _ in range(int(input())):
    a, b, c = map(int, input().split())
    res = a
    if b // 3 == 0:
        print(res + 1 + abs(3 - b - c) // 3 + abs(3 - b - c) % 3) if 3 - b <= c else print(-1)
    else:
        if b % 3 != 0:
            print(res + b // 3 + 1 + abs(3 - b % 3 - c) // 3 + abs(3 - b - c) % 3) if 3 - b % 3 <= c else print(-1)
        else:
            print(res + b // 3 + c // 3 + c % 3)"""

"""for _ in range(int(input())):
    x, y, a = map(int, input().split())
    if a % (x + y) + 0.5 < x:
        print('NO')
    else:
        print('YES')


for _ in range(int(input())):
    x, y, a = map(float, input().split())
    yama = a + 0.5
    cnt = 0
    turn = 'B'
    while True:
        if turn == 'B':
            cnt += x
            turn = 'K'
            if cnt > yama:
                print('NO')
                break
        elif turn == 'K':
            cnt += y
            turn = 'B'
            if cnt > yama:
                print('YES')
                break"""

"""for _ in range(int(input())):
    n = int(input())
    a = []
    for i in range(n):
        a.append(i)
    f = False
    for i in range(n):
        a.pop(i)
        for j in range(n):
            if j != i:
                if (a[i] + a[j - 1]) % 4 == 3:
                    a.pop(j)
                    f = True
                else:
                    f = False

    if f:
        print('Bob')
    else:
        print('Alice')"""


"""for _ in range(int(input())):
    n = int(input())
    print('Alice' if (n - 1) % 4 != 3 else 'Bob')"""


"""for _ in range(int(input())):
    n, j, k = map(int, input().split())
    a = list(map(int, input().split()))
    if k != 1:
        print('Yes')
    elif k == 1 and max(a) == a[j - 1]:
        print('Yes')
    else:
        print('No')"""


"""def find_mx(n, a):
    mx = 0
    for i in range(n):
        if a[i] > a[mx]:
            mx = i

    return mx


def find_mn(n, a):
    mn = 0
    for i in range(n):
        if a[i] < a[mn]:
            mn = i

    return mn


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    res = ['0'] * n
    mx = find_mx(n, a)
    mn = find_mn(n, a)
    res[mx] = '1'
    res[mn] = '1'
    res[0] = '1'
    res[-1] = '1'

    print(''.join(res))
"""


"""for _ in range(int(input())):
    n, k = map(int, input().split())
    a = input()
    if a.count('1') <= k or n < 2 * k:
        print('Alice')
    else:
        print('Bob')"""


"""n = int(input())
s = input().lower()

if len(list(set(s))) == 26:
    print('YES')
else:
    print('NO')"""


"""for _ in range(int(input())):
    n = int(input())
    s = list(input())
    a = []
    for i in range(n):
        tmp = s.copy()
        if s[i] == '1':
            tmp[i] = '0'
            a.append(''.join(tmp))
        else:
            tmp[i] = '1'
            a.append(''.join(tmp))

    a = ''.join(a)
    print(a.count('1'))"""


"""for _ in range(int(input())):
    n, k = map(int, input().split())
    res = 0
    if n % 2 != 0 and k % 2 != 0:
        res += 1
        n -= k
    elif n % 2 == 0:
        if k % 2 != 0:
            n -= (n // (k - 1)) * (k - 1)
            res += (n // (k - 1))
        else:
            n -= (n // k) * k
            res += (n // k)
    elif n % 2 != 0 and k % 2 == 0:
        res += 1
        n -= k - 1
        n -= (n // k) * k
        res += (n // k)

    print(res)"""

"""for _ in range(int(input())):
    n, k = map(int, input().split())
    res = 0
    if n % 2 != 0:
        if k % 2 != 0:
            if n % k != 0:
                n -= k
                res += 1
                n -= (n // (k - 1)) * (k - 1)
                res += (n // (k - 1))
                if n % (k - 1) != 0:
                    res += 1
                    n = 0
            else:
                res += (n // k)
        else:
            n -= (k - 1)
            res += 1
            n -= (n // k) * k
            res += (n // k)
            if n % k != 0:
                res += 1
                n = 0
    else:
        if k % 2 != 0:
            if n % k != 0:
                n -= (n // (k - 1)) * (k - 1)
                res += (n // (k - 1))
                if (n % (k - 1)) != 0:
                    n = 0
                    res += 1
            else:
                res += n // k
        else:
            if n % k != 0:
                n -= (n // k) * k
                res += n // k
                res += 1
                n = 0
            else:
                res += n // k
    print(res)"""


"""for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    mx, mn = a[-1], a[0]
    if (mx + mn) % 2 == 0:
        print(0)
    else:
        idxs = []
        for i in range(n):
            for j in range(n - 1, -1, -1):
                if (a[i] + a[j]) % 2 == 0:
                    idxs.append([i, j])

        print(a)
        print(idxs)"""


"""n, m, k = map(int, input().split())
zuby = [[0] for _ in range(m)]
for _ in range(m + 1):
    r, c = map(int, input().split())
    zuby[r - 1].append(c)

for i in range(m):
    zuby[i].sort()

if k == 0:
    print(0)
else:
    cnt = 0
    while k > 0:
        for i in range(m):
            k -= zuby[i][-1]
            cnt += zuby[i][-1]
            print(zuby[i][-1], k)
    print(cnt)"""


"""for _ in range(int(input())):
    a, b, x, y = map(int, input().split())
    cnt = 0
    if x > y:
        if (b ^ 1) != a:
            print(x * ((b ^ 1) - a)) if ((((b ^ 1) - a)) ^ 1) >= 0 else print(-1)
        else:
            print(y)
    else:
        print(x * (b - a)) if ((b - a)) >= 0 else print(-1)"""

"""for _ in range(int(input())):
    a, b, x, y = map(int, input().split())
    if a < b:
        if x > y:
            if (b - a) % 2 == 0:
                if (b - a) * x < (b - a) * x + y:
                    print((b - a) * x)
                else:
                    print((b - a) * x + y)
            else:
                print((b - a) * x)
        else:
            print((b - a) * x)
    else:
        if (a ^ 1) == b:
            print(1)
        else:
            print(-1)"""


"""for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    c = a.copy()
    c.sort()
    if a == c or n == 1:
        print('NO')
    else:
        res = []
        for i in range(n):
            if a[i] != c[i]:
                res.append(a[i])
        if len(res) != 0:
            print('YES')
            print(len(res))
            print(*res)
        else:
            print(0)"""


"""def prefix_mins(n, a):
    res = []
    curr = a[0]
    res.append(curr)
    for i in range(1, n):
        curr = min(curr, a[i])
        res.append(curr)

    return sum(res)


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    if a[0] > a[1]:
        print(a[0] + a[1])
    else:
        print(a[0] + min(a[0], a[1]))"""


"""for _ in range(int(input())):
    n, k, p = map(int, input().split())
    if k < 0:
        k *= -1

    a = k // p
    b = k % p

    res = a + 1 if b != 0 else a

    if res <= n:
        print(res)
    else:
        print(-1)"""


"""for _ in range(int(input())):
    n = int(input())
    cnt = 0
    if n >= 3:
        cnt += 3
        if n >= 15:
            cnt += 1
        print(cnt)
    else:
        print(n + 1)"""


"""for _ in range(int(input())):
    pat = 'codeforces'
    s = input()
    if s in pat:
        print('YES')
    else:
        print('NO')"""


"""for _ in range(int(input())):
    a, b, c = map(int, input().split())
    if a < b < c:
        print('STAIR')
    elif a < b > c:
        print('PEAK')
    else:
        print('NONE')"""


"""for _ in range(int(input())):
    n = int(input())
    s = list(input())
    l = 0
    r = 0
    for i in range(n):
        if s[i] == 'B':
            l = i
            break

    for j in range(n - 1, -1, -1):
        if s[j] == 'B':
            r = j + 1
            break

    print(len(s[l:r]))
"""

"""for _ in range(int(input())):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.insert(0, 0)
    a.append(x)
    res = []
    for i in range(len(a) - 1):
        res.append(abs(a[i + 1] - a[i]))

    res[-1] *= 2
    print(max(res))"""


"""for _ in range(int(input())):
    n = int(input())
    k = []
    v = []
    for _ in range(n):
        a, b = map(int, input().split())
        k.append(a)
        v.append(b)

    clean_v = []
    for i in range(len(k)):
        if k[i] <= 10:
            clean_v.append(v[i])

    mx = max(clean_v)
    res = 0
    for i in range(len(v)):
        if v[i] == mx:
            res = i + 1
            break

    print(res)"""


"""n, m = map(int, input().split())
prev = ''
cnt = 0
for _ in range(n):
    s = input()
    if s != prev and s[0] * m == s:
        cnt += 1
    prev = s

if cnt == n:
    print('YES')
else:
    print('NO')"""


"""n, m = map(int, input().split())
paper = []
mx = [0, 0]
for i in range(n):
    s = input()
    if mx[0] < s.count('*'):
        mx[0] = s.count('*')
        mx[1] = i
    paper.append(s)

res = []
l_good, r_good = paper[mx[1]].find('*'), paper[mx[1]].rfind('*')
for i in range(n):
    l = paper[i].find('*')
    r = paper[i].rfind('*')
    res.append(paper[i][l:r + 1] if len(paper[i][l:r + 1]) == mx else paper[i][l_good:r_good + 1])


for r in res:
    if r.count('*') != 0:
        print(''.join(r))"""


"""n, m = map(int, input().split())
paper = []
for i in range(n):
    paper.append(input())


min_i = 0
max_i = 0
min_j = 0
max_j = 0
for i in range(n):
    if '*' in paper[i]:
        min_i = i
        break

for i in range(n - 1, -1, -1):
    if '*' in paper[i]:
        max_i = i
        break

min_js = []
max_js = []
for i in range(n):
    for j in range(m):
        if paper[i][j] == '*':
            min_js.append(j)
    max_js.append(paper[i].rfind('*'))

min_j = min(min_js)
max_j = max(max_js)

res = []
for i in range(min_i, max_i + 1):
    res.append(paper[i][min_j:max_j + 1])
for r in res:
    print(r)"""


"""for _ in range(int(input())):
    x = int(input())
    if x % 33 == 0:
        print('YES')
    else:
        print('NO')"""


"""for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))"""


"""for _ in range(int(input())):
    n, a, b, c = map(int, input().split())
    res = (n // (a + b + c)*3)
    ost = n % (a + b + c)
    if ost != 0:
        if (ost - a) <= 0:
            res += 1
        elif (ost - (a + b)) <= 0:
            res += 2
        elif (ost - (a + b + c)) <= 0:
            res += 3
    print(res)
"""

"""for _ in range(int(input())):
    x = list(input())
    for i in range(len(x)):
        x[i] = int(x[i])

    print(min(x))"""


"""for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    cnt = 0
    i = 0
    while i < n:
        # print(i, ': index')
        if a[i] == 0:
            cnt += 1
        elif a[i] == 1:
            cnt = 0
        elif cnt == k:
            i += 2
        else:
            i += 1
        # print(cnt)

    print(cnt // k)"""


"""for _ in range(int(input())):
    s = input()
    print(s.count('1'))"""


"""for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    """


"""for _ in range(int(input())):
    n, m = map(int, input().split())
    if (n == 1 or m == 1) or (n == 2 and m == 2):
        print('NO')
    else:
        print('YES')"""


"""for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    cnt = 0
    i = 0
    while i < n:
        if a[i] == 0:
            cnt += 1
        else:
            cnt = 0
        if cnt == k:
            cnt = 0
            i += 1
            ans += 1
        i += 1
    print(ans)"""


"""for _ in range(int(input())):
    s = list(input())
    s.sort(reverse=True)
    print(''.join(s))"""

"""import math as m


for _ in range(int(input())):
    a, b, k = map(int, input().split())
    if a < k and b < k:
        print(1)
    else:
        d = m.gcd(a, b)
        if max(a // d, b // d) <= k:
            print(1)
        else:
            print(2)"""


"""def calc_pfound(labels, predictions, decay, top=None):
    if len(labels) != len(predictions):
        raise ValueError('Labels and predictions must have the same length')

    sorted_items = sorted(zip(predictions, labels), key=lambda x: x[0], reverse=True)
    if top is not None:
        sorted_items = sorted_items[:top]

    p_prev = 1.0
    pfound_score = 0.0

    for i, (pred, label) in enumerate(sorted_items):
        if i == 0:
            p_current = 1.0
        else:
            p_current = p_prev * (1 - sorted_items[i - 1][1]) * decay

        pfound_score += p_current * label
        p_prev = p_current

    return pfound_score"""


"""for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = a.copy()
    b.sort()
    if b[0] != b[1]:
        print(a.index(b[0]) + 1)
    else:
        print(a.index(b[-1]) + 1)"""

"""for _ in range(int(input())):
    a = list(map(int, input().split()))
    a.sort()
    print(a[1])"""

# a = 'abcdefghijklmnopqrstuvwxyz'

"""for _ in range(int(input())):
    n = int(input())
    s = list(set(input()))
    s.sort()
    last = a.find(s[-1])
    print(len(a[:last + 1]))"""


"""for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    res = []
    b = a.copy()
    b.sort(reverse=True)
    b = b[:2]
    for i in range(n):
        res.append(a[i] - (b[0] if a[i] != b[0] else b[1]))
    print(*res)
"""


"""for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for e in a:
        if e not in d:
            d[e] = 1
        else:
            d[e] += 1

    b = list(d.keys())
    cnt = 0
    for i in range(len(b)):
        if i == 0 or b[i] < b[i - 1]:
            cnt += 1
        elif i == n - 1 or b[i] < b[i + 1]:
            cnt += 1
        elif i > 0 and i < n and b[i] < b[i - 1] and b[i] < b[i + 1]:
            cnt += 1

    if cnt == 1:
        print('YES')
    else:
        print('NO')"""


"""import copy


def cnt(n, a):
    z = 0
    ans = 0
    for i in range(n - 1, -1, -1):
        if a[i] == 0:
            z += 1
        else:
            ans += z

    return ans


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = copy.deepcopy(a)
    c = copy.deepcopy(a)
    d = copy.deepcopy(a)
    if 0 in b:
        b[b.index(0)] = 1
    if 1 in c:
        c[len(d) - 1 - d[::-1].index(1)] = 0

    ans = cnt(n, a)
    ans = max(ans, cnt(len(b), b))
    ans = max(ans, cnt(len(c), c))

    print(ans)
"""

"""for _ in range(int(input())):
    n = int(input())
    s = list(input())
    d = {}
    for e in s:
        if e not in d:
            d[e] = 1
        else:
            d[e] += 1

    cnt = max(list(d.values()))
    ltrs = ''.join(list(d.keys()))
    if cnt == 1 and 'T' in ltrs and 'i' in ltrs and 'm' in ltrs and 'u' in ltrs and 'r' in ltrs and n == 5:
        print('YES')
    else:
        print('NO')"""


"""def solve(n, s1, s2):
    cnt = 0
    for i in range(n):
        if s1[i] == s2[i] or ((s1[i] == 'G' or s1[i] == 'B') and (s2[i] == 'G' or s2[i] == 'B')):
            cnt += 1
    if cnt == n:
        return 'YES'
    return 'NO'


for _ in range(int(input())):
    n = int(input())
    s1 = list(input())
    s2 = list(input())
    print(solve(n, s1, s2))"""


"""n, m, k = map(int, input().split())
dn = n - 1
dm = n - 1
s = max((dn + k - 1) // k, (dm + k - 1) // k)
if dn % k != 0 or dm % k != 0:
    s += 1
print(min(s, min(n, m) + max(n, m) - min(n, m)))
"""

"""for _ in range(int(input())):
    d = {}
    n = int(input())
    res = [0, 0, 0]
    for i in range(3):
        d[i + 1] = set(list(map(str, input().split())))
    if d[1] & d[2] & d[3]:
        continue
    elif d[1] & d[2]:
        l = len(list(d[1] & d[2]))
        res[0] += 1 * l
        res[1] += 1 * l
    elif d[1] & d[3]:
        l = len(list(d[1] & d[3]))
        res[0] += 1 * l
        res[2] += 1 * l
    elif d[2] & d[3]:
        l = len(list(d[2] & d[3]))
        res[1] += 1 * l
        res[2] += 1 * l
    print(res)"""


"""for _ in range(int(input())):
    n, c = map(int, input().split())
    a = list(map(int, input().split()))
    b = []

    for i in range(n):
        if a[i] <= c:
            b.append(a[i])

    b.sort(reverse=True)
    b = b[1:]
    cnt = 0
    for i in range(n):
        if a[i] > c:
            cnt += 1

    x = 2
    for i in range(len(b)):
        if b[i] * x > c:
            cnt += 1
        else:
            x *= 2
    print(cnt)"""


"""for _ in range(int(input())):
    n = int(input())
    p = list(map(int, input().split()))
    l, r = 0, n - 1
    s = ''
    while l < r:
        if p[l] < p[r]:
            s += 'LR'
        else:
            s += 'RL'
        l += 1
        r -= 1
    print(s + 'L' if n % 2 != 0 else s)"""

"""for _ in range(int(input())):
    s = input().lower()
    pat = 'yes'
    if s == pat:
        print('YES')
    else:
        print('NO')"""


"""for _ in range(int(input())):
    n = int(input())
    s = list(input())
    d = {}
    for e in s:
        if e not in d:
            d[e] = 1
        else:
            d[e] += 1

    cnt = len(list(d.values())) * 2
    for e in list(set(s)):
        d[e] -= 1
        cnt += d[e]
    print(cnt)"""

"""c = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def rotate(a, k):
    return a[k % len(a):] + a[:k % len(a)]


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    res = []
    for i in range(n):
        bi, s = map(str, input().split())
        s = list(s)
        bi = int(bi)
        f = c.index(a[i])
        for j in range(bi):
            if s[j] == 'U':
                c = rotate(c, -1)
            else:
                c = rotate(c, 1)
        res.append(c[f])
    print(*res)"""


"""def find_all_pairs(s, a):
    seq = set()
    res = []
    p = {}
    for e in a:
        p[e] = False
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            seq.append(s[i:j])

    for i in range(len(seq)):
        for j in range(len(seq)):
            if seq[i] + seq[j] == s:
                if ([seq[i], seq[j]] not in res) and (seq[i] in p and seq[j] in p):
                    print(seq[i], seq[j])
                    p[s] = True
                    res.append([seq[i], seq[j]])
    return p[s]


for _ in range(int(input())):
    n = int(input())
    a = []
    p = {}
    res = ['0'] * n
    for _ in range(n):
        s = input()
        a.append(s)
        p[s] = find_all_pairs(s, a)
    print(p)
    print(''.join(res))"""


"""def find_all_pairs(s):
    seq = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            seq.add(s[i:j])
    return seq


for _ in range(int(input())):
    n = int(input())
    a = []
    p = {}
    res = ['0'] * n
    for _ in range(n):
        s = input()
        a.append(s)
        p[s] = find_all_pairs(s)

    a_set = set(a)
    for i in range(n):
        for d in p[a[i]]:
            if d in a_set and a[i].replace(d, '', 1) in a_set:
                res[i] = '1'
                break
    print(''.join(res))"""


"""for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] < i < a[j] < a[j]:
                cnt += 1
    print(cnt)"""


"""for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    f = False
    for i in range(n - 1):
        if a[i] == a[i + 1]:
            f = True
            break
    if f:
        print('NO')
    else:
        print('YES')"""


"""import math as m


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    mx = 0
    for i in range(n):
        for j in range(i, n):
            if m.gcd(a[i], a[j]) == 1:
                mx = max(mx, i + j + 2)
    if mx != 0:
        print(mx)
    else:
        print(-1)"""

"""import math as m


def find_max_indices(a):
    max_indices = {}
    for i, num in enumerate(a):
        if num not in max_indices or i > max_indices[num]:
            max_indices[num] = i
    return max_indices


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    d = find_max_indices(a)
    mx = 0
    for i in range(1001):
        for j in d:
            if m.gcd(a[i], j) == 1:
                mx = max(mx, i + d[j] + 2)
    if mx != 0:
        print(mx)
    else:
        print(-1)"""


for _ in range(int(input())):
    a = list(map(int, input().split()))
    a.sort()
    if a[0] + a[1] == a[2]:
        print('YES')
    else:
        print('NO')
