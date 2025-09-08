# ROUND: https://codeforces.com/contest/1971


# A
"""for _ in range(int(input())):
    nums = list(map(int, input().split()))
    ans = sorted(nums)
    print(*ans)"""


# B
"""def rotate(a, shift):
    return a[shift:] + a[:shift]


def solve():
    n = input()
    if n != rotate(n, 1):
        print("YES")
        print(rotate(n, 1))
    else:
        print("NO")

for _ in range(int(input())):
    solve()"""


# C
"""for _ in range(int(input())):
    a, b, c, d = map(int,  input().split())
    s = ''
    for i in range(1, 13):
        if i == a or i == b:
            s +='r'
        if i == c or i == d:
            s += 'b'
    if s == 'rbrb' or s == 'brbr':
        print('YES')
    else:
        print('NO')"""


# D
for _ in range(int(input())):
    s = list(input())
    