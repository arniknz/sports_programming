for _ in range(int(input())):
    s = list(input())
    if s[0] != s[0].lower():
        s = ''.join(s).lower()
        s = list(s)[::-1]
        s[0] = s[0].capitalize()
        print(''.join(s))
    else:
        #print(s, 'printed')
        s = ''.join(s).upper()
        print(s)
