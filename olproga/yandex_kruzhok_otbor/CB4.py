#import re


def get_all_subs(s):
    ans = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if len(s[i:j]) > 1 and list(s[i:j])[0] == '0':
                continue
            ans.add(int(s[i:j]))
    return ans


ans = []
for _ in range(int(input())):
    s, l, r = map(str, input().split())
    l = int(l)
    r = int(r)
    cnt = 0
    subs = list(get_all_subs(s))
    #print(subs)
    for n in subs:
        if l <= n <= r:
            for i in range(len(s)):
                if s[i:i + len(str(n))] == str(n):
                    cnt += 1
    ans.append(cnt)


for r in ans:
    print(r)