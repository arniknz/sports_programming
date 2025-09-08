def mk(r):
    g = {}
    for u, v in r:
        if u not in g:
            g[u] = []
        if v not in g:
            g[v] = []
        g[u].append(v)
        g[v].append(u)
    return g


n = int(input())
e = list(map(int, input().split()))
e.insert(0, 0)
m = int(input())
r = []
for _ in range(m):
    u, v = map(int, input().split())
    r.append((u, v))
g = mk(r)

visited = [False] * (n + 1)
ans = 0
for i in range(1, n + 1):
    if not visited[i]:
        st = [i]
        mn = e[i]
        visited[i] = True
        while st != []:
            curr = st.pop()
            mn = min(e[curr], mn)
            for ng in g[curr]:
                if not visited[ng]:
                    visited[ng] = True
                    st.append(ng)
        ans += mn
print(ans)