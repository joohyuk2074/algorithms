import heapq


def dijkstra(graph, start):
    # 우선순위 큐 초기화: (거리, 정점) 형태로 저장
    priority_queue = [(0, start)]
    distance = {vertex: float('infinity') for vertex in graph}
    distance[start] = 0
    path = {}

    while priority_queue:
        # 가장 짧은 거리의 정점 선택
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # 현재 정점의 거리가 이미 계산된 거리보다 크면 무시
        if current_distance > distance[current_vertex]:
            continue

        # 현재 정점에서 인접한 정점들의 거리 업데이트
        for neighbor, weight in graph[current_vertex].items():
            new_distance = current_distance + weight

            # 더 짧은 경로를 찾았다면 거리 업데이트 및 우선순위 큐에 추가
            if new_distance < distance[neighbor]:
                distance[neighbor] = new_distance
                path[neighbor] = current_vertex
                heapq.heappush(priority_queue, (new_distance, neighbor))

    return distance, path


# 그래프 예시
graph = {
    'A': {'B': 10, 'C': 3},
    'B': {'C': 1, 'D': 2},
    'C': {'B': 4, 'D': 8, 'E': 2},
    'D': {'E': 7},
    'E': {'D': 9}
}

start = 'A'
distances, paths = dijkstra(graph, start)

print(f"Distances from {start}: {distances}")
print(f"Paths: {paths}")
