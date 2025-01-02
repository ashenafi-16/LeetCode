class Solution:
    def sortSentence(self, s: str) -> str:
        space = s.count(" ") + 1
        array = [0]*space
        l = 0
        for i in range(len(s)):
            if s[i].isdigit():
                array[int(s[i])-1] = s[l:i]
                l = i + 2
        return " ".join(array)
            