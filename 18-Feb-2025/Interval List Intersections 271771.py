# Problem: Interval List Intersections - https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res = []
        left = 0 
        right = 0
        while left < len(firstList) and right < len(secondList):
            first = secondList[right][0]
            second = secondList[right][1]
            if firstList[left][0] > secondList[right][0]:
                first = firstList[left][0]
                if firstList[left][1] < secondList[right][1]:
                    second = firstList[left][1]
            elif firstList[left][0] < secondList[right][0]:
                first = secondList[right][0]
                if firstList[left][1] < secondList[right][1]:
                    second = firstList[left][1]
            else:
                if firstList[left][1] < secondList[right][1]:
                    second = firstList[left][1]
            if secondList[right][1] > firstList[left][1]:
                left += 1
            elif firstList[left][1] > secondList[right][1]:
                right += 1
            else:
                left += 1
                right += 1
            if first <= second:
                res.append([first,second])
        return res
            