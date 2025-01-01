class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        count = 0
        vowels = set("aeiou")
        while left<= right:
            n = len(words[left]) -1
            if words[left][0] in vowels and words[left][n] in vowels:
                count += 1
            left += 1
        return count