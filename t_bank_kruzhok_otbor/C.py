for _ in range(int(input())):
    n = int(input())

    if n == 1 or (n * n + 1) % 2 != 0:
        print(-1)
    else:
        print(2, (n * n + 1) // 2)