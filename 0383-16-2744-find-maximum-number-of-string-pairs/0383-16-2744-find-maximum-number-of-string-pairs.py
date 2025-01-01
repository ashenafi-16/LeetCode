class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        count = 0
        check = set()
        for i in range(len(words)):
            if words[i][::-1] in check:
                count += 1
            else:
                check.add(words[i])
        return count