def dfs(x):
    for end in vector[x]:
        if check[end] == 0:
            check[end] = 1
            dfs(end)


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

vector = {}
for i in range(n):
    vector[i] = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            vector[i].append(j)

for start in range(n):
    check = [0 for _ in range(n)]
    dfs(start)
    for j in range(n):
        print(str(check[j]) + " ", end="")
    print()
