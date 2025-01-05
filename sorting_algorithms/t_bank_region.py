def sum_of_dig(d):
    s = 0
    for i in range(len(d)):
        s += int(d[i])

    if len(str(s)) != 1:
        s = sum_of_dig(str(s)) 

    return s


for _ in range(int(input())):
    l, r = map(int, input().split())

    dig = []
    for i in range(l, r + 1):
        dig.append(sum_of_dig(str(i)))

    print(sum(dig))
