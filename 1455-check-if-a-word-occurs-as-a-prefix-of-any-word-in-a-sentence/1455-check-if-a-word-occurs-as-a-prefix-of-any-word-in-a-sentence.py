class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        word = sentence.split()

     
        for index,value in enumerate(word):
            if value.startswith(searchWord):
                return index + 1
        return -1