from collections import deque


def bfs(r, c, d):
    global count, graph, visited

    queue = deque([(r, c, d)])

    while queue:
        r, c, d = queue.popleft()
        if not visited[r][c]:
            count += 1
            visited[r][c] = 1

        flag = 0
        for i in range(4):
            d = (d + 3) % 4
            nr = r + dx[d]
            nc = c + dy[d]

            if 0 <= nr < n and 0 <= nc < m and not graph[nr][nc]:
                if not visited[nr][nc]:
                    queue.append((nr, nc, d))
                    flag += 1
                    break

        if flag == 0:
            back = (d + 2) % 4
            nr = r + dx[back]
            nc = c + dy[back]

            if graph[nr][nc] == 0:
                queue.append((nr, nc, d))
            else:
                break


n, m = map(int, input().split())
r, c, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

count = 0
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)

bfs(r, c, d)

print(count)
