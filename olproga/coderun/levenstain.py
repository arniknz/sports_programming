s1 = input()
s2 = input()


def solve(s1, s2):
    mt = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    for i in range(len(s1) + 1):
        mt[i][0] = i
    for j in range(len(s2) + 1):
        mt[0][j] = j

    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                mt[i][j] = mt[i - 1][j - 1]
            else:
                mt[i][j] = min(
                    [mt[i - 1][j] + 1,
                    mt[i][j - 1] + 1,
                    mt[i - 1][j - 1] + 1]
                )
    """for r in mt:
        print(*r)"""
    return mt[len(s1)][len(s2)]


print(solve(list(s1), list(s2)))