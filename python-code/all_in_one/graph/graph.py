from collections import deque

def bfs(graph, start_v):
    visited = [start_v]
    queue = deque(start_v)

    while queue:
        cur_v = queue.popleft()
        for v in graph[cur_v]:
            if v not in visited:
                visited.append(v)
                queue.append(v)

    return visited

def dfs_recursive(graph, start_v, visited):
    visited.append(start_v)

    for v in graph[start_v]:
        if v not in visited:
            dfs_recursive(graph, v, visited)
    
    return visited
    

def dfs(graph, start_v):
    visited = [start_v]
    stack = deque(start_v)

    while stack:
        cur_v = stack.pop()
        for v in graph[cur_v]:
            if v not in visited:
                visited.append(v)
                stack.appendleft(v)
    return visited
    
                

graph = {
    'A': ['B', 'D', 'E'],
    'B': ['A', 'C', 'D'],
    'C': ['B'],
    'D': ['A', 'B'],
    'E': ['A'],
}

visited = []
result = dfs_recursive(graph, 'A', visited)
print(result)