n = 3

visited = [False] * (n + 1)
def dfs(u, g, visited):
    if not visited[u]:
        visited[u] = True
    else:
        return True
    print(u)

    for h in g:
        if not visited[h]:
            dfs(h, g, visited)
    return False

graph = {1: [2, 3], 2: [3], 3: [1]}
print(dfs(1, graph, visited))