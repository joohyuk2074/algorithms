from collections import deque

def dfs_recursive(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs_recursive(graph, i, visited)

def dfs_stack(graph, start, visited):
    stack = [start]

    while stack:
        v = stack.pop()

        if visited[v]:
            continue

        visited[v] = True
        print(v, end=' ')

        for node in graph[v]:
            if not visited[node]:
                stack.append(node)
                
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    
            


# 예시 입력
graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1, 6],
    4: [2],
    5: [2],
    6: [3],
}

visited = {node: False for node in graph}
# dfs_recursive(graph, 1, visited)
# dfs_stack(graph, 1, visited)
bfs(graph, 1, visited)
# 출력: 1 2 4 5 3 6