import heapq

def dijkstra(graph, start, final):
    costs = {}      # 방문한 노드까지 최소 비용
    pq = []         # priority queue
    heapq.heappush(pq, (0, start)) # 힙을 사용한 priority queue 적용

    while pq:
        cur_cost, cur_v = heapq.heappop(pq)     # pq에서 pop
        if cur_v not in costs:                  # 방문 여부
            costs[cur_v] = cur_cost             # 방문 완료
            for cost, next_v in graph[cur_v]:   # 인접 노드 조회
                next_cost = cur_cost + cost     # 우선순위 큐노드 거리 + 인접 노드 거리
                heapq.heappush(pq, (next_cost, next_v)) # pq에 삽입
    
    return costs[final]

graph = {
    1: [(2, 2), (1, 4)],
    2: [(1, 3), (9, 5), (6, 6)],
    3: [(4, 6)],
    4: [(3, 3), (5, 7)],
    5: [(1, 8)],
    6: [(3, 5)],
    7: [(7, 6), (9, 8)],
    8: []
}