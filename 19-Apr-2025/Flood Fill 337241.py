# Problem: Flood Fill - https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        val = image[sr][sc]
        dq = deque([(sr,sc)])
        direction = [(0,1),(1,0),(-1,0),(0,-1)]
        visited =set()
        def inbound(row,col):
            return 0 <= row < len(image) and 0 <= col < len(image[0])
        def solution(dq):
            while dq:
                for i in range(len(dq)):
                    a,b = dq.popleft()
                    if image[a][b] == val:
                        image[a][b] = color
                        visited.add((a,b))
                    for r,c in direction:
                        
                        row,col = r + a, c + b
                        
                        if inbound(row,col) and (row,col) not in visited and image[row][col] == val:
                            image[row][col] = color
                            visited.add((row,col))
                            dq.append((row,col))
            return image
        return solution(dq)
                
