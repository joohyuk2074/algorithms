from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [0]

        def bfs():
            queue = deque()
            queue.append(0)

            while queue:
                cur_v = queue.popleft()
                for v in rooms[cur_v]:
                    if v not in visited:
                        visited.append(v)
                        queue.append(v)
        bfs()
        
        for i in range(len(rooms)):
            if i not in visited:
                return False
        
        return True
        
            
            
        



input1 = [[1],[2],[3],[]]
input2 = [[1,3],[3,0,1],[2],[0]]

solution = Solution()
result1 = solution.canVisitAllRooms(input1)
result2 = solution.canVisitAllRooms(input2)

print(result1)
print(result2)