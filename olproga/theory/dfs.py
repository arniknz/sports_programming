# DFS


# Рекурсивно
"""n = 5

visited = [False] * (n + 1)
def dfs(u, g, visited):
    if not visited[u]:
        visited[u] = True
    print(u)

    for h in g:
        if not visited[h]:
            dfs(h, g, visited)

graph = {1: [2, 3], 2: [4], 3: [4, 5], 4: [], 5: []}
dfs(1, graph, visited)"""


# Итеративно
"""n = 5
def dfs(u, g, visited=None):
    if visited is None:
        visited = set()
    st = []
    st.append(u)
    while st != []:
        curr = st.pop()
        print(st)
        if curr not in visited:
            visited.add(curr)
        for n in g:
            if n not in visited:
                st.append(n)

graph = {1: [2, 3], 2: [4], 3: [4, 5], 4: [], 5: []}
dfs(1, graph)"""

n = 5
visited = ['w'] * (n + 1)
def dfs(u, g, visited):
    visited[u] = 'g'
    for nb in g[u]:
        if visited[nb] == 'w':
            dfs(nb, g, visited)
        if visited[nb] == 'g':
            return True
    visited[u] = 'b'

graph = {1: [2, 3], 2: [4], 3: [4, 5], 4: [], 5: []}
if dfs(1, graph, visited):
    print('Found')
else:
    print('Not found')