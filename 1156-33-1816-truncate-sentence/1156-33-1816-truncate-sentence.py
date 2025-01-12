class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        splitted_word = s.split()
        return " ".join(splitted_word[:k])