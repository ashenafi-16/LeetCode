class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        from collections import defaultdict
        winner = defaultdict(int)
        loser = defaultdict(int)
        res = []
        dd = []
        for win,los in matches:
            winner[win] += 1
            loser[los] += 1
        for idx,val in winner.items():
            if idx not in loser:
                res.append(idx)
        for idx,val in loser.items():
            if val == 1:
                dd.append(idx)
        return [sorted(res),sorted(dd)]
