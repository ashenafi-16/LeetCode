# Problem: Surrounded Regions - https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = set()
        dq = deque()
        direction = [(0,1),(1,0),(-1,0),(0,-1)]
        def inbound(row,col):
            return 0 <= row < len(board) and 0 <=  col < len(board[0])
        def rec(dq,changed_node,found):
            while dq:
                row,col = dq.popleft()
                if ((row == 0 or row == (len(board) - 1)) or (col == 0 or col ==(len(board[0])-1))) and board[row][col] == 'O':
                    found = False
                
                if (row,col) not in visited:
                    changed_node.add((row,col))
                    visited.add((row,col))
                for r,c in direction:
                    tx,ty = r+row,c + col
                
                    if inbound(tx,ty) and board[row][col] == 'O' and (tx,ty) not in visited:
                        visited.add((tx,ty))
                        changed_node.add((tx,ty))
                        dq.append((tx,ty))
            return changed_node if found else False

                
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'O' and (i,j) not in visited:
                    dq.append((i,j))
                    res = rec(dq,set(),True)

                    if res != False:
                        for a,b in res:
                            board[a][b] = "X"
        return board
