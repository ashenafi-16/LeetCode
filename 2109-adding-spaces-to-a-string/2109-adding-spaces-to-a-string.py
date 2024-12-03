class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        new = ""
        left = 0
        for right in spaces:
            new += s[left:right] 
            new += " "
            left = right
        new += s[spaces[len(spaces)-1]:]
        return new