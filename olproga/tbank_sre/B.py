t = input()

c1 = {'W', 'E'}
c2 = {'N', 'S'}

if ('W' in t and 'E' in t) and ('S' in t and 'N' in t):
    print('Yes')
elif set(t) == c1 or set(t) == c2:
    print('Yes')
else:
    print('No')