class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for word in words:
            found = True
            s = set(word)
            for i in s:
                if i not in allowed:
                    found = False
            if found:
                count += 1
        return count