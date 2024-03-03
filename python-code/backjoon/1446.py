import heapq

INF = int(1e9)


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now]:
            continue

        for next_vertex, next_dist in graph[now]:       # 간선 방문 e
            new_distance = dist + next_dist
            if new_distance < distance[next_vertex]:
                distance[next_vertex] = new_distance
                heapq.heappush(q, (new_distance, next_vertex))


n, d = map(int, input().split())
graph = [[] for _ in range(d + 1)]
distance = [INF] * (d + 1)

# 일단 거리 1로 초기화
for i in range(d):
    graph[i].append((i + 1, 1))

# 지름길 있는 경우에 업데이트
for _ in range(n):
    start, end, l = map(int, input().split())
    if end > d:
        continue
    graph[start].append([end, l])

dijkstra(0)

print(distance[d])
