# Problem: Minesweeper - https://leetcode.com/problems/minesweeper/

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        direction = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]
        def inbound(row,col):
            return 0 <= row < len(board) and 0 <= col < len(board[0])
        dq = deque()
        visited = set()
        dq.append(tuple(click))
        while dq:
            a,b  = dq.popleft()
            visited.add((a,b))
            temp = deque()
            count = 0
            if board[a][b] == 'M':
                board[a][b] = 'X'
                return board
            for tx,ty in direction:
                row,col = tx + a, ty + b
                if inbound(row,col) and (row,col) not in visited:
                    if board[row][col] == 'M':
                        count += 1
                    temp.append((row,col))
            if count == 0:
                for val in temp:
                    dq.append(val)
                    visited.add(val)
                board[a][b] = 'B'
            else:
                board[a][b] = str(count)
        return board
            



