class Solution:
    def finalString(self, s: str) -> str:
        concat = ""
        for st in range(len(s)):
            if s[st] =='i':
                concat = concat[::-1]
            else:
                concat += s[st]
        return concat
            