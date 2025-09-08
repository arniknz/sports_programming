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


def smpl_paths(n, g):
    cnt = 0
    vis = [False] * (n + 1)
    MAX = 10**6
    st = [1]
    while st != [] and cnt < MAX:
        curr = st.pop()
        if vis[curr]:
            vis[curr] = False
            continue
        vis[curr] = True
        cnt += 1
        if cnt >= MAX:
            return MAX
        st.append(curr)
        for nb in g.get(curr, []):
            if not vis[nb]:
                st.append(nb)
    return min(cnt, MAX)


n, m = map(int, input().split())
r = []
if m != 0:
    for _ in range(m):
        u, v = map(int, input().split())
        r.append((u, v))

    g = mk(r)
    cnt = smpl_paths(n, g)
    print(cnt)
else:
    print(1)