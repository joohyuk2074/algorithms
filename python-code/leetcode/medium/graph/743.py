import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 1. times를 통해서 가중치 그래프를 그리기
        graph = {}
        for u, v, w in times:
            if u not in graph:
                graph[u] = [(v, w)]
            else:
                graph[u].append((v, w))

        # 2. 다익스트라 알고리즘 구현
        costs = {}      # 방문 및 해당 노드까지 가중치 기록
        pq = []         # priority queue
        heapq.heapify(pq)
        heapq.heappush(pq, (0, k))  # 시작 지점 넣기

        while pq:
            cur_cost, cur_v = heapq.heappop(pq) # 현재 노드까지 최소 비용과 노드 
            if cur_v not in costs:
                costs[cur_v] = cur_cost
                for next_v, cost in graph.get(cur_v, []):
                    next_cost = cost + cur_cost
                    heapq.heappush(pq, (next_cost, next_v))
        
        
        if len(costs) != n:
            return -1
        else:
            return max(costs.values())




solution = Solution()

times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4 
k = 2
print(solution.networkDelayTime(times, n, k))

