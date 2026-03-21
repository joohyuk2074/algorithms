class Solution:
    def numIslands(self, grid) -> int:
        answer = 0

        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]

        m = len(grid)
        n = len(grid[0])

        def dfs(start_x, start_y):
            grid[start_x][start_y] = "-1"
            
            for i in range(0, 4):
                cx = start_x + dx[i]
                cy = start_y + dy[i]
                if 0 <= cx and cx < m and 0 <= cy and cy < n:
                    if grid[cx][cy] == "1":
                        dfs(cx, cy)

        for x in range(0, m):
            for y in range(0, n):
                # dfs or bfs
                if grid[x][y] == "1":
                    dfs(x, y)
                    answer += 1
        
        return answer

                    
        
solution = Solution()

grid1 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print(solution.numIslands(grid1))

grid2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(solution.numIslands(grid2))