# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def One_D_checker(row_mid):
            low = 0
            high = len(matrix[row_mid]) - 1
            while low <= high:
                mid = (low + high) // 2
                if matrix[row_mid][mid] == target:
                    return True
                elif matrix[row_mid][mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            return False

        row_low = 0
        row_high = len(matrix) - 1
        while row_low <= row_high:
            row_mid = (row_low + row_high) // 2
            if target >= matrix[row_mid][0] and target <= matrix[row_mid][len(matrix[row_mid])-1]:
                return One_D_checker(row_mid)
            elif target > matrix[row_mid][len(matrix[row_mid])-1]:
                row_low = row_mid + 1
            else:
                row_high = row_mid - 1
        return False