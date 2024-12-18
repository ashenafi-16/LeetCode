class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        check = set()
        res = set()
        for r in range(len(s) - 9):
            ch = s[r: r+10]
            if ch in check:
                res.add(ch)
            check.add(ch)
        return list(res)
            