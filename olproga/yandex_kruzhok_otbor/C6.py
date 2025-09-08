for _ in range(int(input())):
    a, s = map(int, input().split())
    if a > s or (s - a * 2) & a != 0:
        print('No')
    else:
        print('Yes')


# Надо было заметить что если x & y = a, то эти числа должны иметь общие биты с a