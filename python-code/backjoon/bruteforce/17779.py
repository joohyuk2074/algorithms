def man_count(x, y, d1, d2):
    count = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0
    }

    # 경계구역 설정
    graph = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    # 5번 경계구역 설정
    for i in range(d1 + 1):
        graph[x + i][y - i] = 5
        graph[x + d2 + i][y + d2 - i] = 5

    for i in range(d2 + 1):
        graph[x + i][y + i] = 5
        graph[x + d1 + i][y - d1 + i] = 5

    # 경계선 내부를 5번 선거구로 할당
    for i in range(x + 1, x + d1 + d2):
        flag = False
        # 행기준으로 한번 경계구역을 만나면
        for j in range(1, n + 1):
            if graph[i][j] == 5:
                flag = not flag
            if flag:
                graph[i][j] = 5

    for r in range(1, n + 1):
        for c in range(1, n + 1):
            if r < x + d1 and c <= y and graph[r][c] == 0:
                count[1] += a[r][c]  # 1번 선거구
            elif r <= x + d2 and y < c and graph[r][c] == 0:
                count[2] += a[r][c]
            elif x + d1 <= r <= n and c < y - d1 + d2 and graph[r][c] == 0:
                count[3] += a[r][c]
            elif x + d2 < r and y - d1 + d2 <= c <= n and graph[r][c] == 0:
                count[4] += a[r][c]
            elif graph[r][c] == 5:
                count[5] += a[r][c]

    return max(count) - min(count)


n = int(input())
a = [[]]
result = 1e9
for _ in range(n):
    a.append([0] + list(map(int, input().split())))

for x in range(1, n + 1):
    for y in range(1, n + 1):
        for d1 in range(1, n + 1):
            for d2 in range(1 + n + 1):
                if 1 <= x < x + d1 + d2 <= n and 1 <= y - d1 < y < y + d2 <= n:
                    result = min(result, man_count(x, y, d1, d2))

print(result)
