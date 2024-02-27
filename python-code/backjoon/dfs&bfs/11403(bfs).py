from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

map = {}
for i in range(n):
    map[i] = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            map[i].append(j)

answer = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            answer[i][j] = 1
        else:
            check = [False for _ in range(n)]
            queue = deque()
            queue.append(i)
            check[i] = True

            while queue:
                popleft = queue.popleft()
                if graph[popleft][j] == 1:
                    answer[i][j] = 1
                    break

                for k in map[popleft]:
                    if not check[k]:
                        queue.append(k)
                        check[k] = True

for i in range(n):
    for j in range(n):
        print(str(answer[i][j]) + " ", end="")
    print()
