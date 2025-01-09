# I
a = int(input())

if a == 1:
    print(1)
    exit()


n1 = 1 % a
for n in range(1, 10**12):
    n1 = (n * n) % a
    if n1 % a == 0:
        print(n)
        break
