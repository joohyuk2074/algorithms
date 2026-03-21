from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        pairs = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, 1),
            (1, 1),
            (1, 0),
            (1, -1),
            (0, -1),
        ]

        n = len(grid)
        dist = [[10000]*n for _ in range(n)]	

        def bfs(start_x, start_y):
            if(grid[start_x][start_y] == 1):
                return -1
            
            queue = deque()
            queue.append([start_x, start_y])
            grid[start_x][start_y] = 1
            dist[start_x][start_y] = 1
            
            while queue:
                cur_pair = queue.popleft()
                cur_x = cur_pair[0]
                cur_y = cur_pair[1]

                for nx, ny in pairs:
                    dx = cur_x + nx
                    dy = cur_y + ny

                    if 0 <= dx and dx < n and 0 <= dy and dy < n:
                        if grid[dx][dy] != 1 and dist[dx][dy] > dist[cur_x][cur_y] + 1:
                            grid[dx][dy] = 1
                            dist[dx][dy] = dist[cur_x][cur_y] + 1
                            queue.append([dx, dy])
        
        bfs(0, 0)
        
        if dist[n-1][n-1] == 10000:
            return -1
        else:
            return dist[n-1][n-1]
            
