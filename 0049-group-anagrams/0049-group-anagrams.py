class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict,Counter
        ana_col = defaultdict(list)
        res = []
        for item in strs:
            c = sorted(list(item))
            ana_col[tuple(c)].append(item)
        for val in ana_col.values():
            res.append(val)
        return res