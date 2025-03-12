# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        memo = {}
        def pascal(row,i):
            if (row, i) in memo:
                return memo[(row, i)]

            if row == 0 and i ==0:
                return 1
            if i < 0 or row + 1 == i:
                return 0
            memo[(row, i)] = pascal(row-1,i-1) + pascal(row-1,i)
            return memo[(row, i)]

        arr = []
        for i in range(rowIndex + 1):
            arr.append(pascal(rowIndex, i))
           
        return arr