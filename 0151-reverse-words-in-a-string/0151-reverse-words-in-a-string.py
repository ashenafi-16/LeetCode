class Solution:
    def reverseWords(self, s: str) -> str:
        rev = s.split()
        string_conc = ""
        for i in range(len(rev)-1,-1,-1):
            string_conc += rev[i]
            if i != 0:
                string_conc += " "
        return string_conc