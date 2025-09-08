"""def solve(n):
    if n == 0:
        return 0
    return n + solve(n - 1)


n = int(input())
print(solve(n))"""

"""
n = int(input())
def solve(n, acc=0):
    if n == 0:
        return acc
    return solve(n - 1, acc + n)
print(solve(n))
"""

"""n = int(input())

def solve(n, acc):
    if n == 0:
        return
    acc[0] += n
    solve(n - 1, acc)

acc = [0]
solve(n, acc)
print(acc[0])"""


"""n = int(input())
p = 1

def solve(p, n, turn, acc):
    if p >= n:
        return not turn
    if (p, turn) in acc:
        return acc[(p, turn)]
    for i in range(2, 10):
        np = p * i
        if not solve(np, n, not turn, acc):
            acc[(p, turn)] = True
            return True
    acc[(p, turn)] = False
    return False


acc = {}
if solve(p, n, True, acc):
    print('Stan wins.')
else:
    print('Ollie wins.')"""


"""a, b = map(int, input().split())
cnt = 0
deystvia = ''
res = f'{a}'
skobki = ''
while b > a:
    #print(b)
    if b % 2 == 0 and b // 2 >= a:
        b //= 2
        deystvia += '2'
        #res += ' * 2)'
        #skobki += '('
    else:
        b -= 1
        deystvia += '1'
        #res += ' + 1)'
        #skobki += '('
    cnt += 1
deystvia = list(deystvia)[::-1]
for e in deystvia:
    if e == '2':
        res += ' * 2)'
        skobki += '('
    else:
        res += ' + 1)'
        skobki += '('
print(f'{b} = {skobki}{res}')
#print(cnt)"""

"""def solve(p, n):
    if p >= n:
        return 0
    for i in range(2, 10):
        p1 = p * i
        return solve(p1, n) + 1


n = int(input())
print(solve(1, n))"""
#print("Ollie wins." if solve(1, n) % 2 == 0 else 'Stan wins.')

def solve(p, n):
    if p >= n:
        return False
    for i in range(2, 10):
        if not solve(p * i, n):
            return True
    return False


n = int(input())
if solve(1, n):
    print('Stan wins.')
else:
    print('Ollie wins.')

"""a, b = map(int, input().split())
cnt = 0
while b > a:
    #print(b)
    if b % 2 == 0 and b // 2 >= a:
        b //= 2
    else:
        b -= 1
    cnt += 1
print(cnt)"""

"""a, b = map(int, input().split())

def solve(a, b):
    if a == b:
        return ''
    if b % 2 == 0 and b // 2 >= a:
        return solve(a, b//2) + '2'
    return solve(a, b - 1) + '1'

print(solve(a, b))"""