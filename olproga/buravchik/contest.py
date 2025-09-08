# A
"""with open('input.txt', 'r') as i:
    n = int(i.readline().strip())
    s = list(i.readline().strip())

if '1' in s:
    start = s.index('1')
    c = s.copy()
    #end = -c[::-1].index('1')
    zeros = []
    zeros_cnt = 0
    for i in range(start, n):
        if s[i] == '1':
            zeros.append(zeros_cnt)
            zeros_cnt = 0
        else:
            zeros_cnt += 1
    zeros = zeros[1:]
    with open('output.txt', 'w') as o:
        if len(list(set(zeros))) == 1:
            o.write('YES')
        else:
            o.write('NO')"""


"""# H
import math as m


x, y = map(int, input().split())
res = m.ceil(m.dist((0, 0), (x, y)))
if (x > 0 and y > 0):
    if res % 2 == 0:
        print('black')
    else:
        print('white')
elif (x < 0 and y < 0):
    if res % 2 == 0:
        print('black')
    else:
        print('white')
elif (x < 0 and y > 0):
    pass
elif (x > 0 and y < 0):
    pass
print(res)"""

"""x, y = map(int, input().split())
if x == 0 or y == 0:
    print('black')

if (x > 0 and y > 0):
    if max(x, y) % 2 == 0:
        print('black')
    else:
        print('white')
elif (x < 0 and y < 0):
    if max(abs(x), abs(y)) % 2 == 0:
        print('black')
    else:
        print('white')
elif (x < 0 and y > 0):
    if max(abs(x), y) % 2 == 0:
        print('white')
    else:
        print('black')
elif (x > 0 and y < 0):
    if max(x, abs(y)) % 2 == 0:
        print('white')
    else:
        print('black')"""


"""x,y = map(int,input().split())
r = ((x-0)**2 + (y-0)**2)**0.5
part = -1
if x == 0 or y == 0:
    print("black")
else:
    if x > 0:
        if y > 0:
            part = 1
        else:
            part = 4
    else:
        if y > 0:
            part = 2
        else:
            part = 3
if part == 1 or part == 3:
    if int(r)%2 == 0:
        print("black")
    elif int(r)%2 == 1 and r != int(r):
        print("white")
    else:
        print("black")
else:
    if int(r)%2 == 0:
        print("white")
    else:
        print("black")"""


x, y = map(int, input().split())
part = 0
if x == 0 or y == 0:
    print('black')
else:
    if x > 0:
        if y > 0:
            part = 1
        else:
            part = 4
    else:
        if y > 0:
            part = 2
        else:
            part = 3

x, y = abs(x), abs(y)
if part == 1 or part == 3:
    if max(x, y) % 2 == 0:
        print('black')
    else:
        print('white')
else:
    if max(x, y) % 2 == 0:
        print('white')
    else:
        print('black')