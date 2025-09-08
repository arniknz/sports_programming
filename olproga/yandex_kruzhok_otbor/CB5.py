def dfs(u, g, visited):
    st = [u]
    visited[u] = 'g'
    while st != []:
        curr = st[-1]
        unvis = False
        for nb in g[curr]:
            if visited[nb] == 'w':
                visited[nb] = 'g'
                st.append(nb)
                unvis = True
                break
            if visited[nb] == 'g':
                return True
        if not unvis:
            st.pop()
            visited[curr] = 'b'
    return False


n, m = map(int, input().split())
d = {}
ok = True
for i in range(1, m + 1):
    l = int(input())
    c = list(map(int, input().split()))
    if len(list(set(c))) < len(c):
        ok = False
    d[i] = (l, c)
if ok:
    #print(d)
    visited = ['w'] * (n + 1)
    g = {}
    for i in range(1, n + 1):
        g[i] = []
    for e in d:
        l, c = d[e]
        for i in range(l - 1):
            g[c[i]].append(c[i + 1])
    #print(g)
    visited = ['w'] * (n + 1)
    f = False
    for i in range(1, n + 1):
        if visited[i] == 'w':
            if dfs(i, g, visited):
                f = True
                break
    if f:
        print('No')
    else:
        print('Yes')
else:
    print('No')