class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count = 0
        seen = set()
        word = "".join(set(word))
        for i in range(len(word)):
            if word[i].islower():
                if word[i].upper() in seen :
                    count += 1
                else:
                    seen.add(word[i])
            else:
                if word[i].lower() in seen :
                    count += 1
                else:
                    seen.add(word[i])
        return count
