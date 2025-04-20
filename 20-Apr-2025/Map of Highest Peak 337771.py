# Problem: Map of Highest Peak - https://leetcode.com/problems/map-of-highest-peak/description/

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:

        result = [[0]*len(isWater[0]) for _ in range(len(isWater))]
        iterator = 1
        queue = deque([])
        visited = set()
        for i in range(len(isWater)):
            for j in range(len(isWater[i])):
                if isWater[i][j] == 1:
                    queue.append((i,j))
                    # visited.add((i,j))
        direction = [(0,1),(1,0),(0,-1),(-1,0)]
        def inbound(row,col):
            return 0 <= row < len(isWater) and 0 <= col < len(isWater[0])
        while queue:
            for _ in range(len(queue)):
                a,b = queue.popleft()
                if isWater[a][b] == 0 and (a,b) not in visited:
                    result[a][b] = iterator
                    visited.add((a,b))
                
                for tx,ty in direction:
                    row,col = a+tx,b+ty
                    if inbound(row,col) and (row,col) not in visited:
                        if isWater[row][col] == 0:
                            result[row][col] = iterator

                        queue.append((row,col))
                        visited.add((row,col))
            iterator += 1
        return result

