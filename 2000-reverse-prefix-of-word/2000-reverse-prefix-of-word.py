class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        res = ""
        idx = word.find(ch)
        res += ((word[:idx+1])[::-1] + word[idx+1:])
        return res