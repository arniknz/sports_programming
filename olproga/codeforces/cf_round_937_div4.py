# ROUND: https://codeforces.com/contest/1950


# A
"""for _ in range(int(input())):
    a, b, c = map(int, input().split())
    if a < b < c:
        print('STAIR')
    elif a < b > c:
        print('PEAK')
    else:
        print('NONE')"""


# B
def make_matrix(n):
    for i in range(0, 2 * n):
        for j in range(0, 2 * n):
            if (i//2 + j//2) % 2 == 0:
                print('#', end='')
            else:
                print('.', end='')
        print()


for _ in range(int(input())):
    n = int(input())
    make_matrix(n)


# C
"""import datetime


for _ in range(int(input())):
    t = input()
    d = datetime.datetime.strptime(t, '%H:%M')
    print(d.strftime('%I:%M %p'))"""


# D
"""nums = []
for i in range(1, 10**5 + 1):
    nb = set(list(str(i)))
    if nb == {'1', '0'} or nb == {'0'} or nb == {'1'}:
        nums.append(i)

#print(nums, len(nums))

def solve(n):
    if n == 1 or n in nums:
        return True
    for e in nums:
        if n % e == 0 and e != 1:
            return solve(n//e)
    return False

for _ in range(int(input())):
    n = int(input())
    if solve(n):
        print('YES')
    else:
        print('NO')"""
