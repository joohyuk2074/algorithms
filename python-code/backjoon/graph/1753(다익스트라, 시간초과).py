import heapq

n, m = map(int, input().split())
start = int(input())
links = [[] for _ in range(n + 1)]
distance = [1e9 for _ in range(n + 1)]

for _ in range(n):
    a, b, c = map(int, input().split())
    links[a].append([b, c])

# bfs!

q = []
heapq.heappush(q, [0, start])
distance[start] = 0

while q:
    _w, node = heapq.heappop(q)

    for next, weight in links[node]:
        if distance[node] + weight < distance[next]:
            distance[next] = min(distance[next], distance[node] + weight)
            heapq.heappush(q, [distance[next], next])
