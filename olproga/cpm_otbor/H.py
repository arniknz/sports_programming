s = input().split('.')
#print(s)
if len(s) != 4:
    print(0)
else:
    ok = True
    for i in range(len(s)):
        if s[i] != '':
            if len(s[i]) > 3 or 0 > int(s[i]) or int(s[i]) > 255:
                ok = False
                break
        else:
            ok = False
            break
    if ok:
        print(1)
    else:
        print(0)
