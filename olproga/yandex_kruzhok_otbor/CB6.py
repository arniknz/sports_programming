"""def find_divs(n):
    cnt = 1
    i = 1
    while i <= int(n ** 0.5):
        if n % i == 0:
            cnt += 1
            if n // i != i:
                cnt += 1
        i += 1
    return cnt


n = int(input())
print(find_divs(n))"""

MAX = 10 ** 6

def resheto(n):
    r = [i for i in range(MAX + 10)]
    ans = []
    for i in range(2, int(n ** 0.5)//2 + 1):
        if r[i]:
            ans.append(i)
            for j in range(i ** 2, int(n ** 0.5)//2 + 1, i):
                #print(j)
                r[j] = False
    return ans

n = int(input())
resh = resheto(n)
#print(resh)
#print(len(resh))
cnt = 0

j = len(resh) - 1
for i in range(len(resh)):
    if resh[i] ** 8 <= n:
        cnt += 1
    p = resh[i] ** 2
    while j > i and p * (resh[j] ** 2) > n:
            j -= 1
    if j > i:
        cnt += (j - i)

print(cnt)