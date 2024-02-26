def dfs(r, c, d):
    global count, graph, visited

    if not visited[r][c]:
        count += 1
        visited[r][c] = True

    for i in range(4):
        d = (d + 3) % 4
        nr = r + dx[d]
        nc = c + dy[d]

        if 0 <= nr < n and 0 <= nc < m:
            if graph[nr][nc] == 0 and not visited[nr][nc]:
                dfs(nr, nc, d)
                return

    back = (d + 2) % 4
    nr = r + dx[back]
    nc = c + dy[back]

    if graph[nr][nc]:
        return

    dfs(nr, nc, d)


n, m = map(int, input().split())
r, c, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

count = 0
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)

dfs(r, c, d)

print(count)
