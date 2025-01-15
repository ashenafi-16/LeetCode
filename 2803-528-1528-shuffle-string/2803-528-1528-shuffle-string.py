class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = list(s)
        for i in range(len(s)):
            res[indices[i]] = s[i]
        return "".join(res)
            