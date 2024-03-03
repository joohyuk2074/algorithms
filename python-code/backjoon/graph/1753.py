import heapq


def dijkstra(start):
    distances[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        weight, cur_vertex = heapq.heappop(q)

        if weight > distances[cur_vertex]:
            continue

        for nv, nw in graph[cur_vertex]:
            new_distance = weight + nw

            if new_distance < distances[nv]:
                distances[nv] = new_distance
                heapq.heappush(q, (new_distance, nv))


n, m = map(int, input().split())
# 시작점
start = int(input())

q = []

graph = {node: [] for node in range(1, n + 1)}

# 가중치 테이블
distances = [1e9 for _ in range(n + 1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

dijkstra(start)

for i in range(1, n + 1):
    if distances[i] == 1e9:
        print("INF")
    else:
        print(distances[i])
