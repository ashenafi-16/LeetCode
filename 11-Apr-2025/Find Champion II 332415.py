# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        incoming = [0] * (n)
        for fir,sec in edges:
            incoming[sec] += 1
        if incoming.count(0) >= 2:
            return -1
        for i in range(len(incoming)):
            if incoming[i] == 0:
                return i
       