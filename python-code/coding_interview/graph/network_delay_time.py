import heapq

def network_delay_time(times, n, k):
    visited = set()
    graph = {}

    # 1. 인접리스트로 그래프 생성
    for start, end, length in times:
        if start in graph:
            graph[start].append((end, length))
        else:
            graph[start] = [(end, length)]
    
    visited.add(k)
    node = graph[k]
    heapq.heappush((node[1], node[0]))
    print(graph)

    # Replace this placeholder return statement with your code
    return -1




times = [[2, 1, 1], [1, 3, 1], [3, 4, 2], [5, 4, 2]]
n = 5
k = 1
print(network_delay_time(times, n, k))