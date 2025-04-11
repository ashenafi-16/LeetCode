# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incoming = defaultdict(int)
        outgoing = defaultdict(int)
        for out,inc in trust:
            incoming[inc] += 1
            outgoing[out] += 1
        for key,value in incoming.items():
            if value == n-1 and outgoing[key] == 0:
                return key
               
        return 1 if n == 1 and not trust else -1