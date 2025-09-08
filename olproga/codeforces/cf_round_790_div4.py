# ROUND: https://codeforces.com/contest/1676


# A
for _ in range(int(input())):
    s = list(input())
    for i in range(len(s)):
        s[i] = int(s[i])
    if sum(s[:3]) == sum(s[3:]):
        print('YES')
    else:
        print('NO')


# B
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    m = min(a)
    ans = 0
    for i in range(n):
        ans += a[i] - m
    print(ans)


# C
def count_letters(m, a, b):
    cnt = 0
    for i in range(m):
        cnt += abs(ord(a[i]) - ord(b[i]))
    return cnt

for _ in range(int(input())):
    n, m = map(int, input().split())
    a = []
    for _ in range(n):
        a.append(list(input()))
    
    cnt = count_letters(m, a[0], a[1])
    for i in range(n):
        for j in range(i + 1, n):
            cnt = min(cnt, count_letters(m, a[i], a[j]))
    print(cnt)


# D

#Взято из: https://stackoverflow.com/questions/64053727/how-to-recursively-get-diagonals-given-the-row-and-column-of-an-element-in-a-2d
class Board:
    def __init__(self, r, c):
        self.boardRows = r
        self.boardCols = c

    def getDiag(self, mt, rs, cs, direction='all'):
        mx = 0
        if not 0 <= rs < self.boardRows or not 0 <= cs < self.boardCols:
            return mx

        if direction == 'all':
            return max(mx, mt[rs][cs] + self.getDiag(mt, rs - 1, cs + 1, 'topright') + self.getDiag(mt, rs - 1, cs - 1, 'topleft') + self.getDiag(mt, rs + 1, cs + 1, 'bottomright') + self.getDiag(mt, rs + 1, cs - 1, 'bottomleft'))

        delta_r, delta_c = self.get_deltas(direction)
        return max(mx, mt[rs][cs] + self.getDiag(mt, rs + delta_r, cs + delta_c, direction=direction))

    @staticmethod
    def get_deltas(direction):
        if 'top' in direction:
            delta_r = -1
        else:
            delta_r = 1

        if 'left' in direction:
            delta_c = -1
        else:
            delta_c = 1
        return delta_r, delta_c


for _ in range(int(input())):
    n, m = map(int, input().split())
    b = Board(n, m)
    mt = []
    s = []
    for _ in range(n):
        mt.append(list(map(int, input().split())))

    for i in range(n):
        for j in range(m):
            s.append(b.getDiag(mt, i, j))
    print(max(s))

# E

"""Чтобы ускорить задачу, обратите внимание, что нам нужно найти префиксную сумму, не меньшую x. 
Поэтому, если мы вычисляем префиксные суммы обратно отсортированного массива, нам нужно найти первый элемент, 
который не меньше x.

Поскольку все элементы a положительны, массив префиксных сумм увеличивается. 
Следовательно, можно выполнить бинарный поиск первого элемента, ≥x. 
Это решает задачу за logn на запрос.

Общая временная сложность: O(qlogn+n)"""

def calculate_prefix_sum(arr):
    if not arr:
        return []

    prefix_sum = [0] * len(arr)
    prefix_sum[0] = arr[0]

    for i in range(1, len(arr)):
        prefix_sum[i] = prefix_sum[i-1] + arr[i]

    return prefix_sum


for _ in range(int(input())):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    p = calculate_prefix_sum(a)
    for _ in range(q):
        x = int(input())
        l, r = 1, n
        ans = -1
        while l <= r:
            mid = (l + r + 1) // 2
            if p[mid - 1] >= x:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        print(ans)