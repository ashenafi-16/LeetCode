# Problem: Minimum Number of Arrows to Burst Balloons - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        sort_val = sorted(points,key=lambda x:x[0])
        arr = [2**32,2**32]
        i = 1
        count = 0
        print(sort_val)
        for start,end in sort_val:
            if start >= arr[0] and start <= arr[1]:
                if end <= arr[1] and end >= arr[0]:
                    arr = [start,end]
            else:
                arr = [start,end]
                count += 1
        return count

