"""n = int(input())
a = list(map(int, input().split()))
a.sort()
ex = 0
ans = 0
k = 1
#print(a)
for i in range(n):
    if a[i] == k:
        ans += 1
        k += 1
    elif a[i] > k:
        ex += 1
        while ex >= 2:
            ex -= 2
            ans += 1
            k += 1
        # a.insert(k, k)
    
    #print('extra:', ex, 'ans:', ans, 'k:', k)
    
while ex >= 2:
    ex -= 2
    ans += 1
    k += 1

#print(ans)
print(a)"""


"""n = int(input())
a = list(map(int, input().split()))
#a.insert(0, 0)
a.sort()
j = 0
k = 1
cnt = 0

if n > 1:
    chistyi = []
    ex = 0
    for i in range(n):
        if a[i] in chistyi or a[i] > n:
            ex += 1
        else:
            chistyi.append(a[i])
    #print(chistyi)
    #print(len(chistyi))
    #print(ex)
    if 1 not in chistyi:
        if ex == 0:
            chistyi = chistyi[:-2]
            chistyi.insert(0, 1)
        elif ex == 1:
            chistyi = chistyi[:-1]
            ex -= 1
            chistyi.insert(0, 1)
        else:
            idx = 1
            while ex >= 2:
                ex -= 2
                chistyi.insert(idx - 1, idx)
                idx += 1
    #print(chistyi)
    #print(ex, k)
    while j < len(chistyi):
        #print(ex, k)
        #print(chistyi[j])
        if chistyi[j] == k:
            cnt += 1
        else:
            #print(chistyi[j], 'in extra sec')
            ex += 1
        k += 1
        j += 1
    #print(ex)

    while ex >= 2:
        ex -= 2
        cnt += 1

    print(cnt)
else:
    if 1 in a:
        print(1)
    else:
        print(0)
#print(ex)"""


"""n = int(input())
a = list(map(int, input().split()))
if n > 1:
    if 1 in a:
        a.sort()
        st = []
        ex = 0
        k = 1
        j = 0
        cnt = 0
        for i in range(n):
            if a[i] not in st or a[i] < n:
                st.append(a[i])
            else:
                ex += 1
        while j < len(st):
            if st[j] == k:
                cnt += 1
                k += 1
            else:
                ex += 1
                while ex >= 2:
                    ex -= 2
                    cnt += 1
                    k += 1
            j += 1
        while ex >= 2:
            ex -= 2
            cnt += 1
        print(cnt)
    else:
        print(0)
else:
    if 1 in a:
        print(1)
    else:
        print(0)
"""

n = int(input())
a = list(map(int, input().split()))
a.sort()
if n > 1:
    ex = n
    k = 1
    i = 0
    cnt = 0
    while ex > 0:
        if i < n and a[i] == k:
            k += 1
            cnt += 1
            ex -= 1
            i += 1
        elif i < n and a[i] < k:
            i += 1
        else:
            if ex >= 2:
                ex -= 2
                cnt += 1
                k += 1
            else:
                break
    print(cnt)
else:
    if 1 in a:
        print(1)
    else:
        print(0)