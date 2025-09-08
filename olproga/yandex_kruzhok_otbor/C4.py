n = int(input())
s = input()
pat = 'b'
ans = -1
if s != pat:
    for k in range(1, 100):
        if k % 3 == 1:
            pat = 'a' + pat + 'c'
            if pat == s:
                ans = k
                break
        elif k % 3 == 2:
            pat = 'c' + pat + 'a'
            if pat == s:
                ans = k
                break
        elif k % 3 == 0:
            pat = 'b' + pat + 'b'
            if pat == s:
                ans = k
                break
    #print(pat)
    print(ans)
else:
    print(0)